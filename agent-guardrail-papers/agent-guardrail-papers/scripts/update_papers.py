#!/usr/bin/env python3
"""自动收集 Agent 输出栅栏（Agent Guardrail）相关论文与开源项目，生成 README.md。
只依赖 Python 标准库。数据源：arXiv API + GitHub 仓库搜索 API。

流程：检索 -> 相关性过滤 -> 与已有数据合并 -> 套用人工精选/排除 -> 分类 -> 生成页面
"""
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEED = os.path.join(ROOT, 'data', 'seed_papers.json')      # 人工精选论文（已核对）
EXCLUDE = os.path.join(ROOT, 'data', 'exclude.json')       # 排除列表：arXiv ID 或 owner/repo
STORE = os.path.join(ROOT, 'data', 'papers.json')          # 论文累积存储，只增不减
GH_STORE = os.path.join(ROOT, 'data', 'github_repos.json') # 仓库累积存储
OUT_MD = os.path.join(ROOT, 'README.md')

ARXIV_API = 'http://export.arxiv.org/api/query'
GITHUB_API = 'https://api.github.com/search/repositories'
NS = {'a': 'http://www.w3.org/2005/Atom'}

# ---------- arXiv 检索 ----------
ARXIV_QUERIES = [
    'abs:"agent" AND abs:guardrail',
    'abs:"agent" AND abs:safeguard',
    'abs:"agent" AND abs:"runtime enforcement"',
    'abs:"agent" AND abs:"output" AND abs:"filter"',
    'abs:"agent" AND abs:"action" AND (abs:verification OR abs:monitor)',
    'abs:"tool" AND abs:"agent" AND abs:defense',
    'ti:"guard agent" OR ti:"guardagent" OR ti:"shieldagent"',
    'ti:guardrail AND (ti:agent OR ti:agentic)',
]

# ---------- GitHub 检索 ----------
GITHUB_QUERIES = [
    '"agent guardrail" in:name,description',
    '"agent guardrails" in:name,description',
    '"agent safety" guardrail in:name,description',
    '"agent firewall" in:name,description',
    '"output guardrail" in:name,description',
    '"llm guardrail" in:name,description',
    '"runtime guardrail" in:name,description',
    '"tool call" guardrail in:name,description',
    'safeguard agent in:name,description',
    'awesome guardrail agent in:name',
]
GITHUB_FILTERS = 'pushed:>2024-01-01 fork:false archived:false'
GH_MIN_STARS = 3

# ---------- 相关性过滤 ----------
AGENT_RE = re.compile(r'\bagent|agentic|\bllm|tool[- ]call|\bmcp\b', re.I)
GUARD_RE = re.compile(r'guard|safeguard|shield|firewall|runtime enforcement|output filter|'
                      r'moderat|sanitiz|护栏|防火墙', re.I)
PAPER_GUARD_RE = re.compile(r'guard|safeguard|shield|firewall|runtime enforcement|output filter|'
                            r'moderat|sanitiz|defen[cs]e|defend|enforc|verif|monitor', re.I)

# ---------- 论文自动分类（启发式，可由人工精选覆盖） ----------
CATEGORIES = [
    ('守护型 Agent（用另一个 Agent 审查动作）', r'guard ?agent|shield ?agent|monitor(ing)? agent|supervisor agent'),
    ('溯源 / 意图对齐', r'provenance|intent|misalign'),
    ('规则与形式化验证', r'formal|\bsmt\b|temporal logic|\bdsl\b|verifiab|provabl|specification|'
                        r'rule-based|runtime enforcement|policy enforcement'),
    ('LLM 裁判', r'as-a-judge|as a judge|llm judge|\bjudge'),
    ('分类器与检测', r'classifier|detector|detection|moderation|filter'),
    ('基准与评测', r'benchmark|dataset|evaluat'),
]
OTHER = '其他 / 综合防御'


def log(msg):
    print(msg, file=sys.stderr)


def load_json(path, default):
    if not os.path.exists(path):
        return default
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def sleep_between(i, n, seconds):
    if i < n - 1:
        time.sleep(seconds)


# ================= arXiv =================
def parse_feed(data):
    root = ET.fromstring(data)
    out = []
    for e in root.findall('a:entry', NS):
        raw_id = e.findtext('a:id', default='', namespaces=NS)
        aid = re.sub(r'v\d+$', '', raw_id.split('/abs/')[-1])
        title = ' '.join(e.findtext('a:title', default='', namespaces=NS).split())
        summary = ' '.join(e.findtext('a:summary', default='', namespaces=NS).split())
        date = (e.findtext('a:published', default='', namespaces=NS) or '')[:10]
        authors = [a.findtext('a:name', default='', namespaces=NS) for a in e.findall('a:author', NS)]
        out.append({'id': aid, 'title': title, 'summary': summary, 'date': date,
                    'authors': authors[:3] + (['et al.'] if len(authors) > 3 else [])})
    return out


def fetch_arxiv(query, max_results=100):
    params = urllib.parse.urlencode({
        'search_query': query, 'start': 0, 'max_results': max_results,
        'sortBy': 'submittedDate', 'sortOrder': 'descending'})
    req = urllib.request.Request(f'{ARXIV_API}?{params}', headers={'User-Agent': 'agent-guardrail-papers/1.0'})
    with urllib.request.urlopen(req, timeout=30) as r:
        return parse_feed(r.read())


def is_relevant_paper(p):
    text = p['title'] + ' ' + p['summary']
    return bool(AGENT_RE.search(text)) and bool(PAPER_GUARD_RE.search(text))


def categorize(p):
    text = (p['title'] + ' ' + p['summary']).lower()
    for name, pattern in CATEGORIES:
        if re.search(pattern, text):
            return name
    return OTHER


def collect_arxiv():
    found = {}
    n = len(ARXIV_QUERIES)
    for i, q in enumerate(ARXIV_QUERIES):
        try:
            entries = fetch_arxiv(q)
        except Exception as e:
            log(f'[warn] arXiv 检索失败：{q[:50]}… {e}')
            entries = []
        for p in entries:
            if is_relevant_paper(p):
                found[p['id']] = p
        sleep_between(i, n, 3)  # arXiv 要求请求间隔
    return found


# ================= GitHub =================
def fetch_github(query, per_page=30):
    params = urllib.parse.urlencode({
        'q': f'{query} {GITHUB_FILTERS}', 'sort': 'stars', 'order': 'desc', 'per_page': per_page})
    headers = {'Accept': 'application/vnd.github+json', 'User-Agent': 'agent-guardrail-papers/1.0'}
    token = os.environ.get('GITHUB_TOKEN')  # Actions 中由 secrets.GITHUB_TOKEN 提供，可提高限流额度
    if token:
        headers['Authorization'] = f'Bearer {token}'
    req = urllib.request.Request(f'{GITHUB_API}?{params}', headers=headers)
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    out = []
    for it in data.get('items', []):
        out.append({
            'full_name': it['full_name'],
            'url': it['html_url'],
            'description': ' '.join((it.get('description') or '').split()),
            'stars': it.get('stargazers_count', 0),
            'language': it.get('language') or '',
            'updated': (it.get('pushed_at') or '')[:10],
            'topics': (it.get('topics') or [])[:5],
        })
    return out


# 仓库相关性：必须出现明确的防护术语（不接受单独的 guard / moderation 等泛词）
REPO_AGENT_RE = re.compile(r'\bagent|agentic|tool[- ]call|\bmcp\b', re.I)
REPO_LLM_RE = re.compile(r'\bllm|language model', re.I)
REPO_STRONG_RE = re.compile(r'guardrail|firewall|safeguard|shield|护栏|防火墙|runtime enforcement|'
                            r'output filter|prompt injection|jailbreak|policy enforcement', re.I)


def is_relevant_repo(r):
    text = f"{r['full_name']} {r['description']}"
    if r['stars'] < GH_MIN_STARS:
        return False
    if REPO_AGENT_RE.search(text) and REPO_STRONG_RE.search(text):
        return True
    return bool(REPO_LLM_RE.search(text)) and bool(re.search(r'guardrail', text, re.I))


def collect_github():
    found = {}
    n = len(GITHUB_QUERIES)
    for i, q in enumerate(GITHUB_QUERIES):
        try:
            items = fetch_github(q)
        except Exception as e:
            log(f'[warn] GitHub 检索失败：{q[:50]}… {e}')
            items = []
        for r in items:
            if is_relevant_repo(r):
                found[r['full_name']] = r
        sleep_between(i, n, 7)  # 未认证时搜索接口约 10 次/分钟
    return found


# ================= 合并与人工数据 =================
def merge(store, fresh, today, key):
    for k, v in fresh.items():
        if k in store:
            for field, val in v.items():
                if val not in (None, '', []):
                    store[k][field] = val
            store[k]['last_seen'] = today
        else:
            v['first_seen'] = today
            store[k] = v


def apply_seeds(store, seeds, today):
    for s in seeds:
        p = store.setdefault(s['id'], {'id': s['id'], 'title': '', 'date': '', 'summary': '',
                                       'authors': [], 'first_seen': today})
        if s.get('title'):
            p['title'] = s['title']
        p['starred'] = True
        p['category_manual'] = s.get('category')
        p['note'] = s.get('note', '')
        p['verify'] = bool(s.get('verify'))


# ================= 渲染 =================
def md(s):
    return (s or '').replace('|', '\\|').replace('\n', ' ')


def short(s, n=110):
    return s if len(s) <= n else s[:n] + '…'


def paper_row(p):
    star = '★ ' if p.get('starred') else ''
    title = f"{star}[{p.get('title') or p['id']}](https://arxiv.org/abs/{p['id']})"
    note = p.get('note') or ''
    if not note and p.get('summary'):
        note = short(p['summary'])
    if p.get('verify'):
        note = '【待核对】' + note
    return f"| {p.get('date') or '—'} | {md(title)} | {md(note)} |"


PAPER_HEAD = '| 日期 | 标题 | 说明 |\n|---|---|---|'


def render(papers, repos, now):
    starred = [p for p in papers if p.get('starred')]
    rest = [p for p in papers if not p.get('starred')]
    counts = {}
    for p in papers:
        cat = p.get('category_manual') or p['category_auto']
        counts[cat] = counts.get(cat, 0) + 1

    L = ['# Agent 输出栅栏（Agent Guardrail）论文与项目收录', '',
         f'> 最后更新：{now:%Y-%m-%d %H:%M} UTC · 论文 {len(papers)} 篇（人工精选 {len(starred)} + 自动 {len(rest)}）'
         f' · GitHub 项目 {len(repos)} 个', '',
         '本页由脚本自动生成，**请勿手动编辑 README.md**。', '',
         '- 论文：来自 arXiv 关键词检索；人工精选写在 `data/seed_papers.json`（带 ★，已核对）。',
         '- 项目：来自 GitHub 仓库搜索，要求名称或简介同时含 agent 相关词与防护相关词，且至少 '
         f'{GH_MIN_STARS} ⭐；按 Star 数排序。',
         '- 修正：加入论文改 `data/seed_papers.json`；剔除论文或项目，把 arXiv ID 或 `owner/repo` 加入 `data/exclude.json`。',
         '- 自动分类是启发式的，可能有误；未上传 arXiv 的论文和未用相关关键词命名的项目不会被收录。', '']

    if starred:
        L += ['## 一、人工精选论文', '', PAPER_HEAD]
        L += [paper_row(p) for p in sorted(starred, key=lambda p: p.get('date') or '', reverse=True)]
        L.append('')

    L += ['## 二、自动收录论文（按方法分类）', '']
    L += ['分类结果：' + ('；'.join(f'{k} {v} 篇' for k, v in counts.items()) or '无'), '']
    for cat in [name for name, _ in CATEGORIES] + [OTHER]:
        items = [p for p in rest if (p.get('category_manual') or p['category_auto']) == cat]
        if not items:
            continue
        L += [f'### {cat}（{len(items)}）', '', PAPER_HEAD]
        L += [paper_row(p) for p in sorted(items, key=lambda p: p.get('date') or '', reverse=True)]
        L.append('')
    if not rest:
        L += ['_自动收录论文暂无结果（网络原因或关键词未命中，下次运行会自动补充）。_', '']

    L += ['## 三、GitHub 相关项目（自动收录）', '']
    if repos:
        L += ['| 项目 | ⭐ | 语言 | 最近推送 | 简介 |', '|---|---|---|---|---|']
        for r in sorted(repos, key=lambda r: r['stars'], reverse=True):
            name = f"[{r['full_name']}]({r['url']})"
            L.append(f"| {md(name)} | {r['stars']} | {md(r['language'] or '—')} | {r['updated'] or '—'} "
                     f"| {md(short(r['description'], 100))} |")
        L.append('')
    else:
        L += ['_GitHub 项目暂无结果（可能是限流或网络原因，下次运行会自动补充）。_', '']
    return '\n'.join(L)


# ================= 主流程 =================
def main():
    os.makedirs(os.path.dirname(STORE), exist_ok=True)
    now = datetime.now(timezone.utc)
    today = now.strftime('%Y-%m-%d')
    excl = set(load_json(EXCLUDE, []))

    # 论文
    store = {p['id']: p for p in load_json(STORE, [])}
    merge(store, collect_arxiv(), today, 'id')
    apply_seeds(store, load_json(SEED, []), today)
    for pid in excl:
        store.pop(pid, None)
    for p in store.values():
        p['category_auto'] = categorize(p)
    papers = sorted(store.values(), key=lambda p: p.get('date') or '', reverse=True)

    # GitHub 项目
    repo_store = {r['full_name']: r for r in load_json(GH_STORE, [])}
    merge(repo_store, collect_github(), today, 'full_name')
    for name in excl:
        repo_store.pop(name, None)
    repos = sorted(repo_store.values(), key=lambda r: r['stars'], reverse=True)

    with open(STORE, 'w', encoding='utf-8') as f:
        json.dump(papers, f, ensure_ascii=False, indent=2)
    with open(GH_STORE, 'w', encoding='utf-8') as f:
        json.dump(repos, f, ensure_ascii=False, indent=2)
    with open(OUT_MD, 'w', encoding='utf-8') as f:
        f.write(render(papers, repos, now))
    print(f'论文 {len(papers)} 篇，GitHub 项目 {len(repos)} 个，已写入 {OUT_MD}')


if __name__ == '__main__':
    main()
