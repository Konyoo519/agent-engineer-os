# PROJECT_STATE

## Project Overview

- Project Name: Agent Engineer OS
- Goal: Become a qualified AI Agent Engineer within 120 days.
- Repository Status: Active Development
- Current Sprint: Sprint 4 (Agent) — tutorial 08_simple_agent
- Current Day: Day 1（采用 Agent 主线 + Python 按需补强 策略）

---

## Current Progress

**Environment Setup**

- [x] Repository initialized
- [x] Directory structure created
- [x] Core documents completed
- [x] Python environment configured
- [x] GitHub repository pushed

**Agent 主线（Phase 4）**

- [x] LLM API 调用（OpenAI 兼容 / DeepSeek）
- [x] System Prompt 工程基础
- [x] Tool Registry（字典版）
- [x] 单参数 Tool Calling
- [ ] 多参数动态传入 Tool Calling ← **当前下一步**
- [ ] 工具结果结构化
- [ ] 错误处理与重试
- [ ] 多工具协同

**Python 按需补强（Phase 1）**

- [x] 嵌套 dict / list
- [x] 函数作为对象
- [x] Dictionary-based Tool Registry 模式
- [ ] *args / **kwargs（待补）
- [ ] 类型注解（待补）
- [ ] class 与工程化对象设计（待补）
- [ ] 装饰器（待补）
- [ ] async / await（待补）
- [ ] 模块与包（待补）
- [ ] Pydantic（待补）

---

## Current Learning Stage

**主线：AI Agent 工程化（Phase 4 - Agent）**

**辅线：Python for Agent Engineering（按需补强）**

当前活跃项目：

- `projects/tutorials/08_simple_agent`
  - `config.py`：从 .env 读取 DeepSeek 配置
  - `llm.py`：OpenAI 兼容 chat 封装
  - `tools.py`：Tool Registry（字典版，单参数）
  - `agent.py`：Think → Act → Observe 循环 + 正则解析 `[TOOL:name:arg]`

---

## Current Focus

**下一步：** 在 08_simple_agent 中把 `execute_tool(name, arg)` 升级为支持多个参数的工具调用。

引出的 Python 知识点：

- `**kwargs`（把 dict 解包成关键字参数传给函数）

---

## Portfolio Status

Projects Completed：

- None

In Progress：

- `08_simple_agent`（进行中）

---

## Next Milestone

完成 08_simple_agent：

1. 多参数工具调用
2. 工具结果结构化
3. 错误处理与重试
4. 多工具协同

完成后进入 MCP / Multi-Agent。

---

## Notes

本文件作为整个项目的仪表盘。

详细每日记录见 `docs/daily/`。

Python 知识点沉淀见 `docs/knowledge/python.md`。

## Career Target

Target Role

AI Agent Developer

Expected Timeline

120 Days

Target Companies

- DeepSeek
- MiniMax
- Moonshot AI
- ByteDance
- Zhipu AI
- Tencent
