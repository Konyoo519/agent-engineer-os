# PROJECT_STATE

## Project Overview

- Project Name: Agent Engineer OS
- Goal: Become a qualified AI Agent Engineer within 120 days.
- Repository Status: Active Development
- Current Sprint: Sprint 4 (Agent) — tutorial 08_simple_agent
- Current Day: **Day 6** (2026-07-21)
- **当前日期: 2026-07-21**

## Current Progress

**Environment Setup**
- [x] Repository initialized
- [x] Directory structure created
- [x] Core documents completed
- [x] Python environment configured
- [x] GitHub repository pushed

**Agent 主线 (Phase 4)**

- [x] LLM API 调用 (OpenAI 兼容 / DeepSeek) — L3-L4,真跑通 2026-07-16
- [x] System Prompt 工程基础 — **L4**,2026-07-16
- [x] Tool Registry (字典式)
- [x] 单参数 Tool Calling
- [x] 多参数动态传入 Tool Calling (2026-07-15)
- [x] LLM 工具调用与 Python 工具执行职责分工 (2026-07-15)
- [x] execute_tool 升级为 (name, arguments: dict) + **arguments 解包 (2026-07-15)
- [x] agent.py 用 json.loads 解析 LLM JSON 输出 (2026-07-15)
- [x] 静态测试 test_pipeline.py 跑通端到端解析链路 (2026-07-15)
- [x] Agent Loop 与 messages.append 的"记忆"作用 — **L4**,2026-07-16
- [x] 端到端跑通真实 DeepSeek API (2026-07-16)
- [x] 调用 print 工具 (2026-07-16)
- [x] 调用 read_file 工具 (2026-07-16)
- [x] **工具结果结构化 (Pydantic + execute_tool 返回 dict)** — **L4**,2026-07-19
- [x] **错误处理与重试 (三层拦截)** — **L4**,2026-07-19
- [x] **多轮错误恢复端到端测试 (test_all_errors.py)** — **L4**,2026-07-19
- [x] **多工具混合调用 (2026-07-21, Day 6 完结, 理解不动代码)**

**晚间综合复习新增 (Day 2 晚)**
- [x] Debug 完整 4 步流程 验证通过 (2026-07-15 晚)
- [x] 独立写出 tools_v2.py (2026-07-15 晚)
- [x] 正则基础 (L3 语法细节)
- [x] Agent 全链路心智模型
- [x] 独立走完 debug 全流程 (实测)

**新增 (Day 3 跨环境调试)**
- [x] 解决 python312._pth sys.path 强制路径问题 (2026-07-16)
- [x] 安装 openai SDK (2026-07-16)
- [x] 解决 .env UTF-8 BOM 哑错误 (2026-07-16)
- [x] 修复 system prompt 与 json.loads 不一致问题 (2026-07-16)

**新增 (Day 4 错误恢复 + 结构化输出)**

- [x] **Python Exception 完整理解** (try/except/raise/traceback/异常家族) — L2 → **L4**
- [x] **异常分类设计** (raise KeyError 复用 except + dict 查表) — **L4**
- [x] **execute_tool 返回结构化 dict** (status/category/message) — **L5**
- [x] **Pydantic BaseModel + 嵌套验证** (ReadFileArgs/PrintArgs) — L3-L4
- [x] **三层错误拦截设计** (json.loads / Pydantic / execute_tool) — **L4**
- [x] **TOOLS vs TOOL_ARG_MODELS 双字典分工** — **L4**
- [x] **6 类错误 category** (bad_args/not_found/wrong_type/timeout/unknown_tool/unknown_error)

## Day 4 当日交付

| 文件 | 改动 |
|---|---|
| tools.py | + PrintArgs/ReadFileArgs + TOOL_ARG_MODELS + classify_error + execute_tool 返回 dict + validate_args |
| agent.py | + 三层错误拦截 + format_validation_error + JSON parse error 处理 + 系统 prompt 增加错误处理指引 |
| test_all_errors.py | **新文件** — 5 轮错误恢复端到端测试 |
| docs/daily/2026-07-19.md | Day 4 完整日志 |
| AI_CONTEXT.md | 已更新到 Day 4 |
| HANDOFF.md | 更新到 Day 4 handoff |

## 6 层错误拦截层次分工

| 层 | 拦什么 | 反馈给 LLM |
|---|---|---|
| 1. json.loads | JSON 语法错 | "参数解析失败：Expecting value..." |
| 2. Pydantic | 字段类型/缺字段 | "参数验证失败（read_file）：path: Input should be a valid string" |
| 3. execute_tool (KeyError) | 工具不存在 | unknown_tool |
| 4. execute_tool (**解包 TypeError) | 参数错 | wrong_type |
| 5. execute_tool (FileNotFoundError) | 文件不存在 | not_found |
| 6. execute_tool (其他) | 兜底 | unknown_error |

四层各管一段,互不替代。

## 真实能力等级 (Day 4 验证后)

**L5 解释原理:**
- Agent Loop 11 步数据流
- try/except 完整机制 + 异常家族 + traceback
- `**` 解包在函数调用 / BaseModel 实例化的复用
- raise KeyError 复用 except 分支的代码整洁技巧

**L4 独立写出 + 解释:**
- 异常分类设计 (异常类型 → LLM action category)
- 结构化错误信息 (dict + 自然语言反馈)
- Pydantic BaseModel + 嵌套 + 字段路径错误
- 三层错误拦截设计
- TOOLS vs TOOL_ARG_MODELS 双字典分工

**L3 能跑 + 概念清楚:**
- Pydantic 在 Agent 里的实际应用
- 5 轮端到端错误恢复

**L2 有印象:**
- Pydantic 高级特性 (默认值 / Optional / List / Field)
- 多轮错误恢复的 token 成本
- 错误分类边界 case (PermissionError / OSError 未测)

## 今日薄弱点（Q&A 揭示的额外）

1. Pydantic 类 / 实例 / __init__ / self 的本质概念（虽然能写代码，基础概念不熟）
2. BaseModel 实例的 type()（已通过 Q&A 解决）
3. **Q6 待补**：`validate_args` 返回元组 (ok, validated) 的设计 — 涉及「返回值表达 vs 异常表达」风格对比 — 下次单讲

## Active File List (Day 4)

projects/tutorials/08_simple_agent/
- agent.py — Agent 循环 + 三层错误拦截 + Pydantic 集成
- tools.py — tools + classify_error + TOOL_ARG_MODELS + ReadFileArgs/PrintArgs + validate_args
- llm.py — DeepSeek 封装
- config.py — env 加载
- run_agent.py — sys.path 注入
- test_all_errors.py — 5 轮错误恢复端到端测试 (新)
- bug_test.py / json_test.py / tools_v2.py — Day 2 训练场(不动)

docs/daily/2026-07-19.md — Day 4 完整日志 (新)
docs/daily/2026-07-18.md — Day 3 复习
