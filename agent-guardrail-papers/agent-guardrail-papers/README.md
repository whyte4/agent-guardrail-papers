# Agent 输出栅栏（Agent Guardrail）论文与项目收录

> 最后更新：2026-11-18 09:12 UTC · 论文 9 篇（人工精选 9 + 自动 0） · GitHub 项目 141 个

本页由脚本自动生成，**请勿手动编辑 README.md**。

- 论文：来自 arXiv 关键词检索；人工精选写在 `data/seed_papers.json`（带 ★，已核对）。
- 项目：来自 GitHub 仓库搜索，要求名称或简介同时含 agent 相关词与防护相关词，且至少 3 ⭐；按 Star 数排序。
- 修正：加入论文改 `data/seed_papers.json`；剔除论文或项目，把 arXiv ID 或 `owner/repo` 加入 `data/exclude.json`。
- 自动分类是启发式的，可能有误；未上传 arXiv 的论文和未用相关关键词命名的项目不会被收录。

## 一、人工精选论文

| 日期 | 标题 | 说明 |
|---|---|---|
| — | ★ [AGrail: A Lifelong Agent Guardrail with Effective and Adaptive Safety Detection](https://arxiv.org/abs/2502.11448) | 自适应生成安全检查，跨任务持续学习；在 Mind2Web-SC、EICU-AC、Safe-OS 上评测 |
| — | ★ [ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning](https://arxiv.org/abs/2503.22738) | 从策略文档提取概率规则并做形式化验证；提出 ShieldAgent-Bench（2K 条轨迹） |
| — | ★ [AgentSpec: Customizable Runtime Enforcement for Safe and Reliable LLM Agents](https://arxiv.org/abs/2503.18666) | 用 DSL 定义触发、条件和执行动作，在运行时拦截；开销为毫秒级 |
| — | ★ [GuardAgent: Safeguard LLM Agents via Knowledge-Enabled Reasoning](https://arxiv.org/abs/2406.09187) | 【待核对】用辅助 Agent 生成护栏代码来检查目标 Agent；ID 与标题未在搜索中核对 |
| — | ★ [Safeguarding LLM Agents from Misalignment through Provenance Analysis](https://arxiv.org/abs/2607.01236) | 分三类错位（工具、参数、理解），执行前用溯源分析判断动作是否与用户意图一致 |
| — | ★ [Towards Verifiably Safe Tool Use for LLM Agents](https://arxiv.org/abs/2601.08012) | 用 STPA 方法推导工具调用的确定性安全保证（ICSE 2026，信息来自博客，请核对） |
| — | ★ [GuardianAgentBench: Where Agents Fail and How to Guard Them](https://arxiv.org/abs/2607.20982) | 580 个场景、六个领域，基于 LangChain/LlamaIndex/Vectara；执行时结构化干预优于提示词防御（ICML 2026 研讨会） |
| — | ★ [Same Operation, Different Permission: Evaluating Whether Guardrails Honor Authorization](https://arxiv.org/abs/2610.16838) | Authorization-Pairs 基准：同一操作在不同授权证据下，护栏是否做出正确判断 |
| — | ★ [ST-WebAgentBench: A Benchmark for Evaluating Safety and Trustworthiness in Web Agents](https://arxiv.org/abs/2410.06703) | Web Agent 安全与可信度基准，只计入遵守策略的完成情况 |

## 二、自动收录论文（按方法分类）

分类结果：守护型 Agent（用另一个 Agent 审查动作） 2 篇；规则与形式化验证 3 篇；溯源 / 意图对齐 1 篇；基准与评测 3 篇

_自动收录论文暂无结果（网络原因或关键词未命中，下次运行会自动补充）。_

## 三、GitHub 相关项目（自动收录）

| 项目 | ⭐ | 语言 | 最近推送 | 简介 |
|---|---|---|---|---|
| [pipelab-org/pipelock](https://github.com/pipelab-org/pipelock) | 1002 | Go | 2026-11-18 | Open-source AI agent firewall for MCP security and agent egress. Scans mediated HTTP, MCP, A2A, and … |
| [AI45Lab/AgentDoG](https://github.com/AI45Lab/AgentDoG) | 710 | Python | 2026-06-08 | A Diagnostic Guardrail Framework for AI Agent Safety and Security |
| [DavidCarliez/trustmebro](https://github.com/DavidCarliez/trustmebro) | 607 | Go | 2026-09-01 | Bypass llm guardrails by confusing it with fabricated tool output. |
| [openguardrails/openguardrails](https://github.com/openguardrails/openguardrails) | 371 | Go | 2026-11-18 | AI agent guardrails for every builder. Local rules, a sandbox and a firewall for your agents, open s… |
| [AI45Lab/TrinityGuard](https://github.com/AI45Lab/TrinityGuard) | 221 | Python | 2026-06-25 | TrinityGuard: A Unified Framework for Safeguarding Multi-Agent Systems |
| [Graph-COM/CKA-Agent](https://github.com/Graph-COM/CKA-Agent) | 217 | Python | 2026-05-20 | [ICML 2026 & ICLR 2026 AIWILD] Official Implementation of the CKA-Agent, "The Trojan Knowledge: Bypa… |
| [luyi14-bits/jig](https://github.com/luyi14-bits/jig) | 170 | Python | 2026-09-17 | Jig — The first pre-execution Agent Firewall. Intercept before they act. |
| [SantanderAI/autoguardrails](https://github.com/SantanderAI/autoguardrails) | 129 | Python | 2026-10-01 | Alignment-research scaffold (autoresearch-style) for LLM guardrails: search over a single policy.md … |
| [LuD1161/agentjail](https://github.com/LuD1161/agentjail) | 104 | Go | 2026-09-24 | Policy guardrails for coding agents (Claude Code, Codex, Cursor) — every tool call is checked locall… |
| [rulebricks/claude-code-guardrails](https://github.com/rulebricks/claude-code-guardrails) | 79 | Python | 2026-02-04 | Real-time guardrails for Claude Code tool calls. |
| [glo26/stepshield](https://github.com/glo26/stepshield) | 78 | Python | 2026-11-16 | StepShield: When, Not Whether to Intervene on Rogue Agents — NeurIPS 2026 benchmark for temporal eva… |
| [fastino-ai/GLiGuard](https://github.com/fastino-ai/GLiGuard) | 68 | — | 2026-05-12 | Fastino's LLM guardrail |
| [killertcell428/aigis](https://github.com/killertcell428/aigis) | 53 | Python | 2026-11-14 | Get Claude Code and other AI agents approved for use at work — deterministic guardrails on every too… |
| [FareedKhan-dev/agentic-guardrails](https://github.com/FareedKhan-dev/agentic-guardrails) | 51 | Jupyter Notebook | 2025-10-05 | Layered guardrails to make agentic AI safer and more reliable. |
| [SaFo-Lab/AGrail4Agent](https://github.com/SaFo-Lab/AGrail4Agent) | 47 | Python | 2026-08-12 | [ACL 2025] The official code for "AGrail: A Lifelong Agent Guardrail with Effective and Adaptive Saf… |
| [darfaz/clawmoat](https://github.com/darfaz/clawmoat) | 45 | JavaScript | 2026-08-17 | The open-source agent firewall. Prevent AI agents from leaking data, using dangerous tools, and impo… |
| [MaxMLang/pytector](https://github.com/MaxMLang/pytector) | 45 | Python | 2026-08-10 | Easy to use LLM Prompt Injection Detection and Prompt Input Sanitization / Detector Python Package w… |
| [mayankjain0141/nixis](https://github.com/mayankjain0141/nixis) | 40 | Go | 2026-09-02 | AI agent firewall that intercepts tool calls (file, shell, network) and enforces deterministic polic… |
| [scs0209/laya-guard](https://github.com/scs0209/laya-guard) | 40 | Python | 2026-11-16 | Free local guardrail for AI coding agents: every tool_call judged on-device (regex + Laya), allow/re… |
| [tjcrims0nx/OpenMind-Jailbreak-Lab](https://github.com/tjcrims0nx/OpenMind-Jailbreak-Lab) | 39 | Python | 2026-11-18 | Open-source AI security research lab for reproducible adversarial testing, jailbreak resistance eval… |
| [unalome-ai/unalome-firewall](https://github.com/unalome-ai/unalome-firewall) | 35 | Rust | 2026-03-28 | Unalome Agent Firewall is a free, open-source desktop app that gives you complete visibility into wh… |
| [yihedeng9/DuoGuard](https://github.com/yihedeng9/DuoGuard) | 34 | Python | 2025-02-26 | DuoGuard: A Two-Player RL-Driven Framework for Multilingual LLM Guardrails |
| [aporthq/aport-agent-guardrails](https://github.com/aporthq/aport-agent-guardrails) | 30 | Shell | 2026-11-12 | Deterministic pre-action authorization for AI agents. Guardrails run before tool execution, so promp… |
| [atliq/guardex-ai](https://github.com/atliq/guardex-ai) | 29 | Python | 2026-10-13 | Python SDK for LLM guardrails with safety classification, PII detection, prompt injection defense, a… |
| [i1see1you/VirbiusAgent](https://github.com/i1see1you/VirbiusAgent) | 29 | Java | 2026-11-17 | Open-source AI Agent security platform — prompt injection defense, MCP tool-call guardrails, eBPF ru… |
| [logi-cmd/agent-guardrails](https://github.com/logi-cmd/agent-guardrails) | 28 | JavaScript | 2026-08-16 | Checks AI-generated code changes before merge: scope, validation, risk, review evidence, and optiona… |
| [manuelfussTC/PulseFramework](https://github.com/manuelfussTC/PulseFramework) | 28 | TypeScript | 2026-11-04 | PULSE Framework: CLI (pulse) + MCP Server (pulse_*) for controlled agentic development. Features 30-… |
| [doggy8088/github-copilot-coding-agent-firewall-switcher-extension](https://github.com/doggy8088/github-copilot-coding-agent-firewall-switcher-extension) | 25 | JavaScript | 2025-12-16 |  |
| [kangmintong/R-2-Guard](https://github.com/kangmintong/R-2-Guard) | 24 | Python | 2024-07-08 | [ICLR 2025] Code implementation of R^2-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-E… |
| [pranithvelar/Friday_mark2](https://github.com/pranithvelar/Friday_mark2) | 24 | Python | 2026-06-17 | Building Friday — a smarter, more advanced successor to my JARVIS project. Production-grade hybrid L… |
| [hoophq/fence](https://github.com/hoophq/fence) | 23 | Go | 2026-08-03 | Guardrails for AI coding agents — block catastrophic tool calls before they run. Semantic, agent-neu… |
| [fpytloun/intaris](https://github.com/fpytloun/intaris) | 22 | Python | 2026-11-08 | Guardrails service for AI agents. Default-deny tool call evaluation with LLM safety analysis, priori… |
| [GoldenWing-360/claude-security-skills](https://github.com/GoldenWing-360/claude-security-skills) | 21 | Python | 2026-10-27 | 25 production-tested defensive security skills for Claude Code - WordPress, VPS, Cloudflare, Next.js… |
| [Eyr3/PrivacyAsst](https://github.com/Eyr3/PrivacyAsst) | 21 | Python | 2024-03-29 | PrivacyAsst: Safeguarding User Privacy in Tool-Using Large Language Model Agents (TDSC 2024) |
| [morganwilliscloud/ai-agent-guardrails](https://github.com/morganwilliscloud/ai-agent-guardrails) | 19 | Python | 2026-11-11 |  |
| [remorses/opencode-injection-guard](https://github.com/remorses/opencode-injection-guard) | 19 | TypeScript | 2026-10-15 | Prompt injection detection plugin for OpenCode. Works with any LLM provider. Scans tool call outputs… |
| [Acacian/aegis](https://github.com/Acacian/aegis) | 18 | Python | 2026-11-14 | LLM guardrails & prompt injection detection for Python. Auto-instruments LangChain, CrewAI, OpenAI, … |
| [everafterlabs/jes](https://github.com/everafterlabs/jes) | 18 | Python | 2026-11-03 | Open-source guardrails for AI agents powered by decision models like Jev; checks prompts, retrieved … |
| [roboticforce/agent-guardrails](https://github.com/roboticforce/agent-guardrails) | 17 | Shell | 2026-07-29 | Hard policy enforcement for AI coding agents. Prevent destructive terraform, database, k8s, and clou… |
| [rock3r/atc](https://github.com/rock3r/atc) | 17 | JavaScript | 2026-11-04 | Daemonless Agent Traffic Control for Android emulators, iOS Simulators, and physical devices — lease… |
| [akasecurity/ai-tc](https://github.com/akasecurity/ai-tc) | 17 | TypeScript | 2026-11-18 | Guardrails for the agent harness. Regulated data stays on your machine, and every prompt and tool ca… |
| [MR9812/BlindGuard](https://github.com/MR9812/BlindGuard) | 16 | Python | 2026-08-24 | code for paper: BlindGuard: Safeguarding LLM-based Multi-Agent Systems under Unknown Attacks |
| [JialongZhou666/GUARDIAN](https://github.com/JialongZhou666/GUARDIAN) | 16 | Python | 2025-10-14 | [NeurIPS 2025] Official implementation of "GUARDIAN: Safeguarding LLM Multi-Agent Collaborations wit… |
| [jzOcb/agent-guardrails](https://github.com/jzOcb/agent-guardrails) | 15 | Shell | 2026-03-16 | Mechanical enforcement tools to prevent AI agents from bypassing established project standards. |
| [ljj-cyber/SafeHarbor](https://github.com/ljj-cyber/SafeHarbor) | 15 | Python | 2026-05-06 | The public repository of ICML 2026 "SafeHarbor: Defining Precise Decision Boundaries via Hierarchica… |
| [higagan/modelfuzz](https://github.com/higagan/modelfuzz) | 15 | Python | 2026-10-19 | 🛡️ Runtime guardrails for AI agents. Intercept and block unsafe tool calls caused by prompt injectio… |
| [Responsible-AI-Labs/rail-score-sdk](https://github.com/Responsible-AI-Labs/rail-score-sdk) | 15 | Python | 2026-06-12 | Official Python SDK for RAIL Score. LLM evaluation across 8 dimensions, guardrails, safe regeneratio… |
| [LegioX-Cyber-Technologies/DeceptivGuard](https://github.com/LegioX-Cyber-Technologies/DeceptivGuard) | 14 | Python | 2026-04-15 | Deception LLM Guardrail that deceives perceived adversarial queries instead of refusing them. |
| [gulbaki/jev-llm-guard](https://github.com/gulbaki/jev-llm-guard) | 14 | JavaScript | 2026-10-01 | Contextual OWASP LLM guardrail powered by Jev, with a Turkish interactive demo |
| [DebarghaG/LeanGuard](https://github.com/DebarghaG/LeanGuard) | 14 | Python | 2026-11-15 | Lean-native temporal policies and runtime guardrails for agent tool use |
| [codewithaarohi/Multi_agent_system_part_3](https://github.com/codewithaarohi/Multi_agent_system_part_3) | 13 | Python | 2026-08-02 | Production-Ready Multi-Agent AI System with LangGraph \| Supervisor Agent + Guardrails + Human-in-the… |
| [OMD-123/agent-loop-guard](https://github.com/OMD-123/agent-loop-guard) | 13 | TypeScript | 2026-11-17 | Zero-dependency guardrail framework for AI agents. Stops runaway loops, prompt injection, hallucinat… |
| [AperionAI/shield](https://github.com/AperionAI/shield) | 13 | Rust | 2026-11-13 | Local guardrails for AI coding agents. Checks each tool call from Claude Code, Cursor, Codex and MCP… |
| [AdityaBhatt3010/OWASP-Agentic-AI-CTF-FinBot-DEMO-Goal-Manipulation](https://github.com/AdityaBhatt3010/OWASP-Agentic-AI-CTF-FinBot-DEMO-Goal-Manipulation) | 13 | — | 2025-08-13 | OWASP Agentic AI CTF – FinBot Goal Manipulation challenge, showing how crafted prompts can override … |
| [kkrlstrm/cc-logger](https://github.com/kkrlstrm/cc-logger) | 12 | Python | 2026-10-19 | Observability for Claude Code: HTTP hooks record sessions, sub-agents and tool calls to Postgres, so… |
| [truss-agent/truss-harness](https://github.com/truss-agent/truss-harness) | 12 | TypeScript | 2026-11-18 | A modular coding-agent runtime for local or cloud models with a CLI, full-screen TUI, VS Code extens… |
| [SSSTAiNLESSS/AntiGravity-Launchpad](https://github.com/SSSTAiNLESSS/AntiGravity-Launchpad) | 12 | Shell | 2026-02-10 | 🚀 Production-ready multi-agent template for Google AntiGravity IDE. 7 agents, 11 skills, 9 MCP serve… |
| [Sapience-AI/openclaw-middleware-suite](https://github.com/Sapience-AI/openclaw-middleware-suite) | 11 | TypeScript | 2026-11-03 | Six in-process middlewares for OpenClaw: HITL approvals, prompt-injection guardrails, PII redaction,… |
| [yjzscode/INFA-Guard](https://github.com/yjzscode/INFA-Guard) | 11 | Python | 2026-08-21 | [EMNLP 2026] Code for Paper INFA-Guard: Mitigating Malicious Propagation via Infection-Aware Safegua… |
| [tanaikech/adk-gas](https://github.com/tanaikech/adk-gas) | 11 | JavaScript | 2026-06-24 | GASADK: Agent Development Kit for Google Apps Script. Build AI agents with Gemini API, MCP, A2A, Age… |
| [amirimi/Guardian](https://github.com/amirimi/Guardian) | 10 | Go | 2026-10-16 | Extensible Go microkernel for LLM guardrails, quota enforcement and policy plugins. |
| [aws-samples/safeguarding-travel-agent-guardrails-amazon-bedrock](https://github.com/aws-samples/safeguarding-travel-agent-guardrails-amazon-bedrock) | 9 | Jupyter Notebook | 2024-06-18 |  |
| [mcpware/IntentProbe](https://github.com/mcpware/IntentProbe) | 9 | Python | 2026-10-19 | CPU activation probes for AI-agent guardrails and classification. One frozen local model pass, many … |
| [MangroveTechnologies/mangrove-agent](https://github.com/MangroveTechnologies/mangrove-agent) | 9 | Python | 2026-11-17 | Mangrove gives trading agents guardrails. Local MCP server and plugin: built-in risk management (cir… |
| [ValentinTorassa/VT-Agent-Firewall](https://github.com/ValentinTorassa/VT-Agent-Firewall) | 9 | Python | 2026-11-10 | Local security gateway between an AI agent and its tools (fs, shell, network, MCP): default-deny pol… |
| [zitrino-oss/znyx-sdk](https://github.com/zitrino-oss/znyx-sdk) | 9 | Python | 2026-11-01 | Official client SDKs for the ZNYX Runtime guardrails API - Python, TypeScript, Java, C#, Ruby, and R… |
| [samfoy/pi-steering-hooks](https://github.com/samfoy/pi-steering-hooks) | 9 | TypeScript | 2026-09-24 | Deterministic tool-call guardrails for pi — enforce rules with before-tool hooks instead of prompts |
| [zitrino-oss/znyx-runtime](https://github.com/zitrino-oss/znyx-runtime) | 9 | Python | 2026-11-17 | Local-first guardrails evaluation server for LLM apps. Scans inputs, outputs, and tool calls against… |
| [THU-KEG/RIDAR](https://github.com/THU-KEG/RIDAR) | 9 | Python | 2026-10-25 | RIDAR: Safeguarding Research Integrity in Autonomous Research Agents via Automated Detection and Run… |
| [xkkkkkkm/e-commerce-copy-quality-inspection-agent](https://github.com/xkkkkkkm/e-commerce-copy-quality-inspection-agent) | 9 | Python | 2026-10-06 | LLM-led e-commerce content review with rule-based safeguards, tenant-isolated MySQL, Redis workers, … |
| [mverab/slashstack-skills](https://github.com/mverab/slashstack-skills) | 8 | — | 2026-09-11 | Eleven open-source, MIT-licensed skills for AI coding agents — /preflight, /audit, /ship, /remember … |
| [rayhanadev/oxray](https://github.com/rayhanadev/oxray) | 8 | TypeScript | 2026-11-09 | Opinionated agent guardrails for TypeScript projects, powered by oxlint, oxfmt, oxclippy, and a smal… |
| [kodigitaccount/LLM-Guardrails_-Enterprise-AI_-Responsible-AI](https://github.com/kodigitaccount/LLM-Guardrails_-Enterprise-AI_-Responsible-AI) | 8 | Python | 2026-08-31 |  |
| [pavanbelagatti/LLM-Guardrails-Tutorial](https://github.com/pavanbelagatti/LLM-Guardrails-Tutorial) | 8 | Python | 2025-11-03 |  |
| [mickeybeurskens/guess-the-password](https://github.com/mickeybeurskens/guess-the-password) | 8 | Python | 2024-08-13 | Testingrounds for LLM guardrail techniques |
| [vijaym2k6/SteerPlane](https://github.com/vijaym2k6/SteerPlane) | 8 | Python | 2026-11-06 | The safety layer for the AGI era. Runtime guardrails for autonomous AI agents. |
| [berkcangumusisik/repo-seatbelt](https://github.com/berkcangumusisik/repo-seatbelt) | 8 | TypeScript | 2026-05-31 | A safety layer for AI coding agents. CLAUDE.md/AGENTS.md generator, MCP runtime guardrail, pre-commi… |
| [SafellmHub/hguard-go](https://github.com/SafellmHub/hguard-go) | 8 | Go | 2025-07-18 | Guardrails for LLMs: detect and block hallucinated tool calls to improve safety and reliability. |
| [higress-group/issue-spec](https://github.com/higress-group/issue-spec) | 8 | Go | 2026-11-17 | Open-source project governance on GitHub: maintainers shape contributor agents' context before imple… |
| [CampanulaBells/XG-Guard](https://github.com/CampanulaBells/XG-Guard) | 8 | Python | 2026-05-19 | Code repo for ACL 26 Explainable and Fine-Grained Safeguarding of LLM Multi-Agent Systems via Bi-Lev… |
| [azep-ninja/ai-agent-guardrails](https://github.com/azep-ninja/ai-agent-guardrails) | 7 | TypeScript | 2026-05-03 |  |
| [massdriver-cloud/agentic-infrastructure-tutorial](https://github.com/massdriver-cloud/agentic-infrastructure-tutorial) | 7 | Dockerfile | 2026-03-20 | Making Infrastructure Safe for Agents: Guardrails, Context, and Trust in the Age of Agentic Developm… |
| [SentriusLLC/Sentrius](https://github.com/SentriusLLC/Sentrius) | 7 | Java | 2026-09-11 | Command and Control your Infra and Agents. Guardrails for agents and humans! Single pane of glass to… |
| [agentgazer/agentgazer](https://github.com/agentgazer/agentgazer) | 7 | TypeScript | 2026-02-18 | From Observability to Control - AI Agents' Firewall |
| [LeoKemp223/embedded-llm-guardrails](https://github.com/LeoKemp223/embedded-llm-guardrails) | 7 | — | 2026-05-27 | 用于在嵌入式、单片机、RTOS、驱动和板级工程中使用 LLM 辅助开发时建立安全边界的 skill。 |
| [lamhotsiagian/guardrail-system-rag](https://github.com/lamhotsiagian/guardrail-system-rag) | 7 | Python | 2026-07-30 | An interactive, chat-driven learning system and production reference architecture for recommendation… |
| [hexitlabs/vigil](https://github.com/hexitlabs/vigil) | 7 | TypeScript | 2026-02-15 | 🛡️ Open-source safety guardrail for AI agent tool calls. <2ms, zero dependencies. |
| [Cashcoin123/Cashcoin123](https://github.com/Cashcoin123/Cashcoin123) | 7 | — | 2026-10-05 | # Application card: GitHub Copilot Chat Learn how to use GitHub Copilot Chat responsibly by understa… |
| [Chandukasireddy/Agent_Guardrails_Monitoring](https://github.com/Chandukasireddy/Agent_Guardrails_Monitoring) | 6 | JavaScript | 2026-11-06 | A hands-on CTF-style workshop: break AI guardrails, learn authorization and observability with NeMo … |
| [mastepanoski/ce-ai](https://github.com/mastepanoski/ce-ai) | 6 | Rust | 2026-11-14 | Cross-host operational companion for Compound Engineering across AI coding agents. Fleet version gov… |
| [mochrzlf/aegis-forge](https://github.com/mochrzlf/aegis-forge) | 6 | Python | 2026-10-04 | Production-ready, security-first template for Web, Mobile & Trading systems — with AI agent guardrai… |
| [shivanagendrakore/agent-firewall](https://github.com/shivanagendrakore/agent-firewall) | 6 | TypeScript | 2026-10-21 | Deterministic firewall for AI coding agents: fixed rules, outside the model, check each tool call be… |
| [aatakansalar/yaml-opa-llm-guardrails](https://github.com/aatakansalar/yaml-opa-llm-guardrails) | 6 | Python | 2025-06-27 | A YAML to OPA Rego compiler that enables defining LLM output guardrails using familiar YAML syntax a… |
| [saranyan/llm_guardrail_testing](https://github.com/saranyan/llm_guardrail_testing) | 6 | Python | 2025-05-23 |  |
| [Jaycubic/toolboundary](https://github.com/Jaycubic/toolboundary) | 6 | Python | 2026-11-17 | Local runtime security and policy enforcement for AI agents and LLM tool calls, with permissions, gu… |
| [sazid/bitcode](https://github.com/sazid/bitcode) | 6 | Go | 2026-05-19 | An AI coding assistant - agentic loop, tool calls, guardrails, reminders, terminal TUI. |
| [kkrlstrm/agent-guard](https://github.com/kkrlstrm/agent-guard) | 6 | Python | 2026-09-29 | Tool-call guardrails for Claude Code derived from cc-logger telemetry: nudge recoverable mistakes, b… |
| [williamw99/SafeGuard](https://github.com/williamw99/SafeGuard) | 6 | — | 2026-07-02 | [ECCV 2026] SafeGuard: A Multi-Agent Perception-Reasoning Framework for Social-Risk AI-Generated Vid… |
| [Bl4ckk01/agent-guardrail](https://github.com/Bl4ckk01/agent-guardrail) | 5 | Python | 2026-11-15 | Ultra-fast, zero-cost safety guardrail for Claude Code & OpenAI Codex. Deterministic & neural protec… |
| [lmy-1219/agent-guardrails](https://github.com/lmy-1219/agent-guardrails) | 5 | Python | 2026-08-21 | AI工作流插件，包含Claude Code版（调用codex）、Claude Code独立版、Codex版。用于及时制止AI偷懒行为，提醒AI多思考一层、及时落盘。让AI窗口之间像人类部门协作一样沟通… |
| [kallolchakraborty/ABAP-guardian](https://github.com/kallolchakraborty/ABAP-guardian) | 5 | Python | 2026-08-04 | Enterprise-grade SAP ABAP code review skill & AI agent guardrails enforcing Clean ABAP, ATC quality … |
| [use-ash/ash](https://github.com/use-ash/ash) | 5 | Python | 2026-04-02 | ASH — Agent Safety Harness: how to build a production AI agent system with persistent memory, multi-… |
| [onestardao/WFGY-Agent-Firewall](https://github.com/onestardao/WFGY-Agent-Firewall) | 5 | TypeScript | 2026-04-06 | WFGY-Agent-Firewall |
| [SudeshRPatil20/MCP-MathMind-Intelligent-math-solver-powered-by-MCP](https://github.com/SudeshRPatil20/MCP-MathMind-Intelligent-math-solver-powered-by-MCP) | 5 | TypeScript | 2025-08-22 | MCP-MathMind – An AI-powered, human-in-the-loop math tutor built with MCP (Model Context Protocol) f… |
| [R1ngZer0/LLM-Guardrails](https://github.com/R1ngZer0/LLM-Guardrails) | 5 | CSS | 2024-04-16 |  |
| [siddhant-0707/llm-guardrails](https://github.com/siddhant-0707/llm-guardrails) | 5 | Python | 2025-11-24 |  |
| [Carlosmarroquin20/llm-guardrail-proxy](https://github.com/Carlosmarroquin20/llm-guardrail-proxy) | 5 | Python | 2026-11-03 | A lightweight, zero-cost Python proxy designed to intercept, audit, and sanitize developer prompts b… |
| [MGASALUCAS/askari_llm](https://github.com/MGASALUCAS/askari_llm) | 5 | Python | 2024-09-05 | Open Source Version of Askari LLM , Guardrails implementation for Large Language Model |
| [kkrlstrm/callusguard](https://github.com/kkrlstrm/callusguard) | 5 | Python | 2026-09-29 | Guardrails for Claude Code and Codex written from telemetry: record tool calls, derive rules from re… |
| [dungnotnull/craft-village-heritage-tourism-agent-skill](https://github.com/dungnotnull/craft-village-heritage-tourism-agent-skill) | 5 | Python | 2026-07-30 | 🏺 Multi-agent AI framework for sustainable craft heritage & creative tourism planning. Balances arti… |
| [Lasyasriyerramsetty/CrewHire](https://github.com/Lasyasriyerramsetty/CrewHire) | 5 | Python | 2026-07-15 | An elegant multi-agent AI recruitment pipeline (CrewAI) that screens, scores, audits and schedules c… |
| [dkneeland/agentic-guardrails](https://github.com/dkneeland/agentic-guardrails) | 4 | — | 2026-04-12 | Modular markdown workflow templates to keep AI coding agents from shipping sloppy code. Catch defens… |
| [DennisFaucher/hermes-agent-guardrails](https://github.com/DennisFaucher/hermes-agent-guardrails) | 4 | Python | 2026-05-13 |  |
| [DzKriMo/Aegis](https://github.com/DzKriMo/Aegis) | 4 | Python | 2026-03-26 | AI Agents Guardrail |
| [architsharm/agentfox](https://github.com/architsharm/agentfox) | 4 | Python | 2026-11-16 | AgentFox: open-source control plane for AI agents. Guardrails on model traffic, tool calls bounded b… |
| [shouryasingh2311/bouncer-on-board](https://github.com/shouryasingh2311/bouncer-on-board) | 4 | Python | 2026-10-25 | Zero-Trust IDE Agent Firewall & Pre-Deploy Security Gatekeeper |
| [pipelab-org/pipelock-rules](https://github.com/pipelab-org/pipelock-rules) | 4 | Python | 2026-11-17 | Official community detection rules for Pipelock - the open-source agent firewall |
| [limithit/llm_router_guard](https://github.com/limithit/llm_router_guard) | 4 | Go | 2026-09-24 | A self-hosted LLM gateway with built-in input/output guardrails — multi-protocol routing, quotas, au… |
| [shivadharmi/AI_DS_Technical_Eval](https://github.com/shivadharmi/AI_DS_Technical_Eval) | 4 | Jupyter Notebook | 2026-08-21 | EV fleet analytics: a next-day revenue prediction pipeline (Ridge / Random Forest / XGBoost over lea… |
| [gabrielchua/llm-guardrails-workshop](https://github.com/gabrielchua/llm-guardrails-workshop) | 4 | Python | 2024-11-20 |  |
| [vli31/llm-guardrail-sensitivity](https://github.com/vli31/llm-guardrail-sensitivity) | 4 | Jupyter Notebook | 2024-07-17 | GPT Guardrail Sensitivity in Context |
| [atharvakanchan25/LLM-Guardrails-Gateway](https://github.com/atharvakanchan25/LLM-Guardrails-Gateway) | 4 | — | 2026-06-26 |  |
| [CentreSecuriteIA/BELLS-O](https://github.com/CentreSecuriteIA/BELLS-O) | 4 | Python | 2026-07-25 | A framework to assess operational cost of LLM guardrails. https://centresecuriteia.github.io/BELLS-O… |
| [InnerWarden/inner-warden](https://github.com/InnerWarden/inner-warden) | 4 | Rust | 2026-11-16 | Open-source runtime guardrail for AI agents: screens shell commands and MCP/tool calls before they r… |
| [arijeetganguli/Agentra](https://github.com/arijeetganguli/Agentra) | 4 | Python | 2026-06-12 | Secure AI coding governance, runtime guardrails, token optimization, and enterprise DevSecOps orches… |
| [cirbuk/safeguards](https://github.com/cirbuk/safeguards) | 4 | Python | 2025-04-23 | Agentic Safety Framework |
| [VamsiSudhakaran1/release-gate](https://github.com/VamsiSudhakaran1/release-gate) | 4 | Python | 2026-10-12 | 🚪 Governance gate for AI agents. Enforce policies before deployment: request contracts, operational … |
| [cmu-soda/ProvenanceGuard](https://github.com/cmu-soda/ProvenanceGuard) | 3 | Python | 2026-08-08 | [ASE 2026] ProvenanceGuard is a provenance-based runtime guardrail for LLM agent safety that detects… |
| [DSCmatter/Agentic_Firewall](https://github.com/DSCmatter/Agentic_Firewall) | 3 | Python | 2026-10-28 | Agentic Firewall sits between an AI agent or MCP client and an MCP server. It can enforce runtime po… |
| [hakomicat/Agent-Firewall](https://github.com/hakomicat/Agent-Firewall) | 3 | Go | 2026-05-11 |  |
| [jingwora/LLM-Guardrails](https://github.com/jingwora/LLM-Guardrails) | 3 | — | 2024-06-06 | LLM-Guardrails |
| [royapakzad/multilingual_llm_guardrails](https://github.com/royapakzad/multilingual_llm_guardrails) | 3 | Python | 2026-05-11 | Evaluating Multilingual Discrepancies in LLM Guardrails |
| [KryptosAI/mcp-seatbelt](https://github.com/KryptosAI/mcp-seatbelt) | 3 | TypeScript | 2026-08-04 | Runtime guardrails for AI agent MCP tools. Blocks dangerous tool calls at runtime with a default-den… |
| [KeelStack-me/guard](https://github.com/KeelStack-me/guard) | 3 | TypeScript | 2026-08-07 | Runtime guardrails for TypeScript AI agents. Prevents duplicate tool calls, enforces per-user cost b… |
| [awesome-pro/guardloop](https://github.com/awesome-pro/guardloop) | 3 | Python | 2026-09-23 | Production runtime guardrails for AI agents: budget caps, circuit breakers, and OpenTelemetry traces… |
| [repoforge-dev/authority-layer](https://github.com/repoforge-dev/authority-layer) | 3 | TypeScript | 2026-03-11 | Runtime guardrails for AI agents that enforce token budgets, loop limits, and tool rate limits local… |
| [PathlayerLabs/pathlayer](https://github.com/PathlayerLabs/pathlayer) | 3 | Python | 2026-11-08 | Runtime guardrail layer for AI agents: detect loops, retries, cost explosions and lack of progress, … |
| [liuhe37186/agent-harness-health-check](https://github.com/liuhe37186/agent-harness-health-check) | 3 | Python | 2026-06-01 | 对用户的 Agent 系统做 Harness 体检，检查 workflow 与 agent 边界、执行回路、工具契约、权限审批、状态恢复、上下文治理、trace/replay、HITL、eval 与发… |
| [safetycard/safetycard](https://github.com/safetycard/safetycard) | 3 | Python | 2026-10-18 | Agent plugin that scores internal safeguards of MCP servers and AI agents and suggests the safest se… |
| [SpaceMatterDeep/AGPI-Constitution-And-Demos](https://github.com/SpaceMatterDeep/AGPI-Constitution-And-Demos) | 3 | Python | 2026-03-24 | Prototype constitutions, attestation loops, and demos for multi-agent systems with value drift check… |
| [JeremyZ-ctrl/NeoArcClaw](https://github.com/JeremyZ-ctrl/NeoArcClaw) | 3 | Python | 2026-07-22 | An experimental multi-agent coding assistant for local workspaces, featuring LangGraph orchestration… |
