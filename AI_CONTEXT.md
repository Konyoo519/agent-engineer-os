# AI Context

> 这是 ChatGPT、Codex 与未来其他 AI 工具之间的**跨 AI 上下文快照**。
> 不是完整历史记录,也不是唯一事实来源。
> 完整事实依然分布在: README / ROADMAP / PROJECT_STATE / HANDOFF / docs/knowledge/ / docs/daily/ / projects/
> 本文件只负责让一个新 AI 对话**只读这一份文件**就能快速恢复当前学习状态。
最后更新: **2026-07-18 (Day 3 复习日完成)**

---

## 1. Project

- 项目名称: **Agent Engineer OS**
- 项目目标: 120 天内成为合格的 AI Agent Engineer
- 仓库状态: Active Development
- 当前 Sprint: Sprint 4 (Agent) — tutorial 08_simple_agent
- 当前 Day: Day 3 (含 2026-07-16 实战 + 2026-07-18 复习)

## 2. 当前状态快照

### 主线进度
- **Phase 4 Agent 主线 — 端到端跑通了** ✓
  - 08_simple_agent 真实 DeepSeek API,print + read_file 两个工具均成功
  - Round 1 → Round 2 完整 agent loop 验证成功
  - Day 3 解决了 3 个不期而遇的 bug (utf-8 BOM / sys.path / prompt JSON 不一致)
  - Day 3 复习(2026-07-18)完成 5 部分评估,验证 L4-L5 掌握度

### 真实能力等级 (Day 3 + 复习日验证)

**L5 解释原理**:
- Agent Loop 11 步数据流(能默写 + 边界条件)
- JSON str vs dict 本质差异 + json.loads 三种输入合法性

**L4 独立写出 + 解释**:
- 字典注册模式 + execute_tool 动态调用
- Tool Calling 全链(str → 正则 → dict → 函数调用)
- messages.append 顺序语义

**L3 能跑 + 概念清楚**:
- 真实 Agent Loop(已跑 2 轮)
- DeepSeek v4-pro 模型
- 环境调试流程

**L2 有印象 + 不熟细节**:
- Python 错误类型语义(TypeError / KeyError / JSONDecodeError / ModuleNotFoundError)
- 正则非贪婪 + 回溯
- openai SDK Choice / ChatCompletionMessage 类型

### 用户当前学习最大薄弱点 (2026-07-18 复习确认)

1. **try/except 原理只到结论级** — 知道"让 LLM 自救",不知道 Python 异常机制如何工作
2. **Python 错误类型分类不熟** — 见过的错能识别,新错难分类
3. **OpenAI SDK 内部细节** — 只用了 chat.completions.create 一条路径

## 3. 下一步 (基于 Day 3 复习评估)

**主线 Phase 4 Agent 收尾 (08_simple_agent):**

1. 工具结果结构化 (Pydantic / JSON schema, 让 LLM 返回结构化数据而不是只能打印字符串)
2. 错误处理与重试 (execute_tool 包 try/except, 工具错误作为 user 消息反馈给 LLM 让其重试)
3. 多工具混合 (同一轮里同时调 print + read_file)

**Day 4 推荐路径**:
- 上午 (30 min): 补 Python try/except 基础(3-5 个小例子) — Day 4 错误处理的地基
- 下午: 进入 Pydantic 结构化输出(约束 LLM 返回 schema) — 解决 Day 3 残留的 JSON 不稳定问题

不建议直接上 LangGraph / MCP。

间隔复习:
- 3 天后 (2026-07-21) 再测一次 Debug 4 步流程(防止遗忘)

---

## 当前活跃文件 (2026-07-18)

- projects/tutorials/08_simple_agent/
  - agent.py — Agent 循环 + JSON prompt
  - tools.py — Tool Registry + execute_tool
  - llm.py — DeepSeek 封装
  - config.py — env 加载(已修复 BOM 问题)
  - .env — base_url = https://api.deepseek.com/v1, model = deepseek-chat
  - run_agent.py — sys.path 注入启动器
  - json_test.py — JSON 解析实验
  - tools_v2.py — (Day 2 晚) 独立写的测试工具层
  - bug_test.py — (Day 2 晚) debug 训练场
- docs/daily/2026-07-18.md — **(Day 3 复习日) 新增** 5 部分复习评估记录

## 4. 教学原则 (已确认)

不按"代码行数"作为掌握标准。每个知识点必须能回答:
1. 为什么不这样写
2. 需求变了改哪里
3. 报错如何定位

Agent 主线 + Python for Agent 按需补强 — 这是 Day 1 调整后的策略, **保持有效**, 不回退。

## 5. 状态

**主线** Phase 4 - Agent 真实跑通 + 复习评估完成, 还剩 3 项收尾任务(结构化输出 / 错误重试 / 多工具混合)才能算 08_simple_agent 完成。
**侧线** Python 按需补强, 核心已齐, 后续只需针对性补漏(正则 + 错误类型语义 + Pydantic 按需 + try/except 按需)。

## 6. 避免重开

不要重讲这些已掌握内容:
- Tool Registry 设计
- 动态 Tool Calling
- execute_tool(name, arguments) 4 步
- ** arguments 解包
- JSON.loads(str) -> dict
- f-string 基础用法
- 正则 (.*?) 与 match.group(N)
- Match 对象 None 判定
- 字典 key 大小写敏感

如果发现新的理解错误, **针对具体问题补充**, 不要整体复习。
