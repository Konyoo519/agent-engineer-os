# AI Context

> 这是 ChatGPT、Codex 与未来其他 AI 工具之间的**跨 AI 上下文快照**.
> 不是完整历史记录, 也不是唯一事实来源.
> 完整事实依然分布在: README / ROADMAP / PROJECT_STATE / HANDOFF / docs/knowledge/ / docs/daily/ / projects/
> 本文件只负责让一个新 AI 对话**只读这一份文件**就能快速恢复当前学习状态.
最后更新: **2026-07-21 (Day 6 完结 —— 08_simple_agent 收尾, 多工具混合调用理论+实战, 不动代码)**

---

## 1. Project

- 项目名称: **Agent Engineer OS**
- 项目目标: 120 天内成为合格的 AI Agent Engineer
- 仓库状态: Active Development
- 当前 Sprint: Sprint 4 (Agent) —— tutorial 08_simple_agent
- 当前 Day: **Day 6**

## 2. 当前状态快照

### 主线进度
- **Phase 4 Agent —— 三件套完成** v v v
  - v 结构化输入 (Pydantic 验证参数 + 嵌套 BaseModel)
  - v 结构化错误 (execute_tool 返回 dict + classify_error 查表)
  - v 多工具混合调用 (Day 6 完结, 理解不动代码)

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

### 学生当前学习最大薄弱点 (2026-07-20 确认)

**Day 4 已通过 Q&A 解决**: 类/实例/self/json.loads vs model_dump/双字典分工.

**Day 5 已通过原理讲解补齐**: Field 二分 / model_dump() 网关 / Optional+default 二分.

**仍然薄弱 (Day 6+ 优先补)**: 错误边界 case / Pydantic 实战 / Q6 / token 成本.

**Day 5 引入的新教学规则** (Day 7 已扩展为永久规则, 强制执行):
> 进入新概念必须按 "原理 —— 字面 —— 真实代码 —— 真实输出 —— 总结规律 —— 预测 —— 练习" 节奏, 不可以在真实输出前让学生预测.

## 3. 下一步 (基于 Day 5)

08_simple_agent 主线还差最后 1 件: **多工具混合调用**.

候选路径 (Day 6):
- **A. 多工具混合调用** —— 同一轮连续调 print + read_file, 验证 messages 顺序
- **B. 进入 09 项目**
- **C. 复习日**

推荐 **A → (Day 7+) 复习 + Q6 待补**.

间隔复习 (沿用 Day 4 计划):
- 3 天后 (2026-07-22) 测 Day 4 + Day 5 内容

---

## 当前活跃文件 (2026-07-20)

- projects/tutorials/08_simple_agent/ (Day 5 未动)
  - agent.py / tools.py / llm.py / config.py / run_agent.py
  - test_all_errors.py (Day 4 新建)
  - bug_test.py / json_test.py / tools_v2.py (Day 2 训练场)

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
- **Day 7 新增永久教学规则** (强制执行):
  - 对于第一次接触的新知识, 教学必须遵循「原理 —— 字面 —— 真实代码 —— 真实运行结果 —— 总结规律 —— 预测 —— 练习」顺序
  - 禁止在学生尚未见过真实运行结果之前要求预测代码
  - 预测必须建立在真实输出基础之上
- 评估按 8 级制度
