# PROJECT_STATE

## Project Overview

- Project Name: Agent Engineer OS
- Goal: Become a qualified AI Agent Engineer within 120 days.
- Repository Status: Active Development
- Current Sprint: Sprint 4 (Agent) — tutorial 08_simple_agent
- Current Day: **Day 3** (2026-07-16)
- **当前日期: 2026-07-16**

## Current Progress

**Environment Setup**

- [x] Repository initialized
- [x] Directory structure created
- [x] Core documents completed
- [x] Python environment configured
- [x] GitHub repository pushed

**Agent 主线 (Phase 4)**

- [x] LLM API 调用 (OpenAI 兼容 / DeepSeek) — L3-L4,真跑通 2026-07-16
- [x] System Prompt 工程基础 — **L4**,2026-07-16 亲自修过 prompt 与 json.loads 不一致的 bug
- [x] Tool Registry (字典式)
- [x] 单参数 Tool Calling
- [x] 多参数动态传入 Tool Calling (2026-07-15)
- [x] LLM 工具调用与 Python 工具执行职责分工 (2026-07-15,纯概念)
- [x] execute_tool 升级为 (name, arguments: dict) + **arguments 解包 (2026-07-15)
- [x] agent.py 用 json.loads 解析 LLM JSON 输出 (2026-07-15)
- [x] 静态测试 test_pipeline.py 跑通端到端解析链路 (2026-07-15)
- [x] Agent Loop 与 messages.append 的"记忆"作用 — **L4**,2026-07-16 真跑 2 轮验证
- [x] **端到端跑通真实 DeepSeek API** (2026-07-16,Day 3 主要成就)
- [x] 调用 print 工具 (2026-07-16)
- [x] 调用 read_file 工具 (2026-07-16)
- [ ] 工具结果结构化 -> **当前下一步**
- [ ] 错误处理与重试
- [ ] 多工具混合

**晚间综合复习新增 (Day 2 晚)**

- [x] **Debug 完整 4 步流程** 验证通过 (2026-07-15 晚)
- [x] **独立写出 tools_v2.py** (2026-07-15 晚)
- [x] **正则基础** (运行级理解,语法细节 L3)
- [x] **Agent 全链路心智模型** (完整串讲)
- [x] **独立走完 debug 全流程** (实测)

**新增 (Day 3 跨环境调试)**

- [x] python312._pth 强制 sys.path 问题诊断
- [x] sys.path.insert(0, ...) 启动器模式
- [x] UTF-8 BOM 导致 env var key 名带不可见字符问题
- [x] 显式 ASCII vs UTF-8 编码选择

**Python 按需补强 (Phase 1)**

- [x] 嵌套 dict / list
- [x] 函数作为对象
- [x] Dictionary-based Tool Registry 模式
- [x] parameter / argument 区分 (2026-07-15)
- [x] **arguments 字典解包成命名参数 (2026-07-15)
- [x] 类型注解基础 (2026-07-15)
- [x] list.append(item) (2026-07-15)
- [x] json.loads(s) 字符串 -> dict (2026-07-15)
- [x] **(Day 3 新增)** f-string 占位符
- [x] **(Day 3 新增)** 正则 match.group(N) 捕获组
- [x] **(Day 3 新增)** Match 对象 None 判定
- [x] **(Day 3 新增)** 真实 OpenAI 兼容 API 调用
- [ ] *args
- [ ] class 与工程化对象设计 (待补)
- [ ] 装饰器 (待补)
- [ ] async / await (待补)
- [ ] 模块与包 (待补)
- [ ] Pydantic (按需,结构化输出时再补)
- [ ] try / except (按需,工具错误处理时再补)

---

## Current Learning Stage

**主线:** AI Agent 工程化 (Phase 4 - Agent)
**辅线:** Python for Agent Engineering (按需补强)

当前活跃项目:
- projects/tutorials/08_simple_agent
  - config.py: 从 .env 读取 DeepSeek 配置 (已修复 BOM 问题)
  - llm.py: OpenAI 兼容 chat 封装
  - tools.py: Tool Registry (嵌套字典) + 升级后的 execute_tool
  - agent.py: Think -> Act -> Observe 循环 + JSON-格式 prompt
  - run_agent.py: **(新增)** sys.path 注入启动器
  - json_test.py: **(新增)** JSON 解析实验

---

## Current Focus

**下一步:**

1. tools.py / agent.py 引入 Pydantic 或 JSON schema 约束 LLM 返回结构
2. 引入 try/except 包装 execute_tool,捕获工具执行错误并把错误信息反馈给 LLM 让其重试
3. 多工具混合测试 (同一轮里调用 print + read_file)

之后引入的 Python 知识点 (如果遇到卡点):
- Pydantic (参数 schema 时)
- try / except (工具错误反馈时)

---

## Portfolio Status

Projects Completed: 0
In Progress: 08_simple_agent (Day 3 已端到端跑通,等收尾 3 项后算完成)

---

## Next Milestone

完成 08_simple_agent:
1. 多参数工具调用 ✓ (2026-07-15)
2. LLM 端到端驱动 ✓ **(2026-07-16 完成)**
3. 工具结果结构化 -> 下一步
4. 错误处理与重试
5. 多工具混合

完成后进入 MCP / Multi-Agent。

---

## Notes

本文档作为整个项目的仪表板。
详细每日记录见 docs/daily/。
Python 知识点索引见 docs/knowledge/python.md。

## Career Target

Target Role: AI Agent Developer
Expected Timeline: 120 Days
Target Companies:
- DeepSeek
- MiniMax
- Moonshot AI
- ByteDance
- Tencent

---

## 2026-07-18 更新 (Day 3 复习日)

**复习评估结果**:
- Agent Loop: L5
- Tool Calling: L4
- execute_tool: L4-L5 之间
- JSON: L5
- Debug: L3-L4
- Git 工作流: 未评估

**新增薄弱点**:
- try/except 原理只到结论级
- Python 错误类型语义分类不熟
- OpenAI SDK 内部细节黑盒

**Phase 4 Agent 主线剩余 3 项**:
- 工具结果结构化(Pydantic / JSON schema)
- 错误处理与重试(try/except)
- 多工具混合调用

**Phase 1 Python 按需补强**:核心已齐,后续针对性补漏。
