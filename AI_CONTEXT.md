# AI Context

> 这是 ChatGPT、Codex 与未来其他 AI 工具之间的**跨 AI 上下文快照**.
> 不是完整历史记录, 也不是唯一事实来源.
> 完整事实依然分布在: README / ROADMAP / PROJECT_STATE / HANDOFF / docs/knowledge/ / docs/daily/ / projects/
> 本文件只负责让一个新 AI 对话**只读这一份文件**就能快速恢复当前学习状态.
最后更新: **2026-07-23 (Day 7 —— Tutorial 09 Part 1 已完成)**

---

## 1. Project

- 项目名称: **Agent Engineer OS**
- 项目目标: 120 天内成为合格的 AI Agent Engineer
- 仓库状态: Active Development
- 当前 Sprint: Sprint 4 (Agent) —— tutorial 09_structured_agent
- 当前 Day: **Day 7**

## 2. 当前状态快照

### 主线进度
- **Phase 4 Agent —— 三件套完成** v v v
  - v 结构化输入 (Pydantic 验证参数 + 嵌套 BaseModel)
  - v 结构化错误 (execute_tool 返回 dict + classify_error 查表)
  - v 多工具混合调用 (Day 6 完结, 理解不动代码)
- **Tutorial 09 已完成课程设计，Part 1 已完成**
  - [x] Part 1：结构化 Agent action 与多工具调用解析（2026-07-23 完成）
  - [ ] Part 2：参数模型与嵌套参数验证
  - [ ] Part 3：结构化动作的工具执行
  - [ ] Part 4：多工具调度与结果回传
  - 说明：Part 1 已完成 Why / Principle / Terminology / Real Code / Real Output / Pattern / Prediction / Practice，且学生已明确表示“本 Part 学习完成。”

### 三层错误拦截设计 (Day 4 已完成)

LLM 输出 JSON 字符串 →  json.loads() ← 拦截层 1: JSON 解析错 → Pydantic BaseModel ← 拦截层 2: 字段类型/缺字段错 (两种 error type: missing vs value) → execute_tool() ← 拦截层 3: 业务错 (文件不存在/无权限/...) → classify_error() ← 把异常归类到 6 类 LLM 友好 category

### 6 类错误 category (Day 4 用户设计)

`bad_args / not_found / wrong_type / timeout / unknown_tool / unknown_error`

### 真实能力等级 (Day 5 验证)

**L5 解释原理**:
- Pydantic Field 的两件事 (必填标记 / 值约束)
- 类型错 vs 值越界 的区分 (int_parsing / greater_than_equal / less_than_equal / int_from_float)
- Agent Loop 11 步数据流 (能默写 + 边界条件)
- try/except 完整机制 + 异常家族 + traceback 读法
- raise 复用 except 分支 (代码整洁技巧)
- `**` 解包在函数调用和 BaseModel 实例化的复用

**L4 独立写出 + 解释**:
- Pydantic 4 行口头自测 (必填 / 默认 / 上下限 三维度)
- `model_dump()` 是 "对象 —— dict 网关" 概念
- dict 查表 (classify_error / TOOL_ARG_MODELS / TOOLS)
- BaseModel + 嵌套 + 字段路径错误
- 三层错误拦截设计
- TOOLS vs TOOL_ARG_MODELS 双字典分工 (Day 5 复习确认)
- 异常分类设计 + 结构化错误信息

**L3 听过原理 + 概念清楚 (未在项目里实际写过)**:
- `Optional[T] = Field(default=...)` 写法
- `List[X]` 字段 + `min_length/max_length`
- `None` 在 Agent 工具中的角色
- Pydantic 在 Agent 里的实际应用
- 5 轮端到端错误恢复

**L2 仍然薄弱**:
- Pydantic 实战 (Day 6 自然补齐)
- Q6 (Day 7+ 单讲)
- 错误分类边界 case
- 多轮错误恢复的 token 成本意识
- Tutorial 09 Part 1 已完成课堂学习流程、练习和最终确认

### 学生当前学习最大薄弱点 (2026-07-20 确认)

**Day 4 已通过 Q&A 解决**: 类/实例/self/json.loads vs model_dump/双字典分工.

**Day 5 已通过原理讲解补齐**: Field 二分 / model_dump() 网关 / Optional+default 二分.

**仍然薄弱 (Day 6+ 优先补)**: 错误边界 case / Pydantic 实战 / Q6 / token 成本.

**Day 5 引入的新教学规则** (Day 7 已扩展为永久规则, 强制执行):
> 进入新概念必须按 "原理 —— 字面 —— 真实代码 —— 真实输出 —— 总结规律 —— 预测 —— 练习" 节奏, 不可以在真实输出前让学生预测.

## 3. 下一步 (Day 7 结束)

Tutorial 09 `09_structured_agent` 下一步是进入 Part 2。

Part 1 已完成课堂学习流程与练习。学生已理解 `AgentAction` 用于表示 LLM 这一轮想做什么，`ToolCall` 表示一个具体工具调用，`parse_action()` 负责把 LLM JSON 文本解析为 `AgentAction`。

Part 1 已获得学生最终确认。下一次学习可以进入 Part 2：参数模型与嵌套参数验证。

间隔复习 (沿用 Day 4 计划):
- 3 天后 (2026-07-22) 测 Day 4 + Day 5 内容

---

## 当前活跃文件 (2026-07-23)

- projects/tutorials/08_simple_agent/ (Day 5 未动)
  - agent.py / tools.py / llm.py / config.py / run_agent.py
  - test_all_errors.py (Day 4 新建)
  - bug_test.py / json_test.py / tools_v2.py (Day 2 训练场)
- projects/tutorials/09_structured_agent/
  - README.md
  - part1_protocol.py
  - demo_part1.py
  - test_part1.py

- docs/daily/2026-07-23.md — Day 7 Tutorial 09 Part 1 完成日志
- docs/daily/2026-07-19.md — Day 4 完成日志
- docs/daily/2026-07-20.md —— **Day 5 完成日志** (新)

---

## 避免重开

下次 Session 不要重新教学这些已掌握内容:
- Tool Registry / 动态 Tool Calling / execute_tool(name, arguments)
- **arguments 解包 / f-string / 正则 / match.group / Match None
- JSON.loads(str) -> dict / 字典 key 大小写敏感
- Agent Loop 11 步 / messages.append 顺序语义
- try/except + raise + traceback + 异常家族 (Day 4 确认)
- Pydantic 4 行口头自测 (Day 5 确认)
- model_dump() 网关概念 (Day 5 确认)
- Optional + default 二分 (Day 5 确认)
- TOOLS vs TOOL_ARG_MODELS 双字典分工 (Day 5 复习确认)

如果发现新的理解错误, 针对具体问题补充, 不整体复习.

---

## 核心学习风格备注

- 学生喜欢完整代码块 (反馈过: 不要碎片化代码)
- 学生喜欢真实项目例子 (不用假设类)
- 学生喜欢从具体反推抽象 (已展示 L4 推理能力)
- **学习进度判定规则（永久，最高优先级）**:
  - 学习进度只能根据学生的实际学习情况更新
  - 创建 Tutorial、编写示例代码、编写测试、编写 README、更新文档、运行示例，都不能视为学生完成学习
  - 只有同时满足以下全部条件，才能将某个 Part 标记为完成：
    1. 已完成 Why、Principle、Terminology 教学
    2. 学生阅读并理解真实代码
    3. 学生观察真实运行结果
    4. 学生完成练习
    5. 学生确认已经理解
    6. 学生明确表示：“本 Part 学习完成。”
  - 在全部条件满足之前，只能标记为“教学材料已准备”或“待学习”
- **Day 7 新增永久教学规则** (强制执行):
  - 对于第一次接触的新知识, 教学必须遵循「原理 —— 字面 —— 真实代码 —— 真实运行结果 —— 总结规律 —— 预测 —— 练习」顺序
  - 禁止在学生尚未见过真实运行结果之前要求预测代码
  - 预测必须建立在真实输出基础之上
- **课程结束与仓库操作权限规则（永久）**:
  - 课程结束时，Codex 不得自动更新 Git、Commit 或 Push
  - 必须先向学生请求明确选择：
    - A. 今天只学习，不更新仓库
    - B. 更新学习文档，但不 Git Commit
    - C. 更新文档并 Git Commit
    - D. 更新文档、Commit 并 Push GitHub
  - 在学生明确选择之前，不得执行 Commit 或 Push
- 评估按 8 级制度
