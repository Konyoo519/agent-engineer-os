# HANDOFF

## 最近会话: 2026-07-23 (Day 7)

### 主题

**Tutorial 09 课程设计** —— 从 Tutorial 08 的文本工具协议设计结构化 Agent action 协议. **Tutorial 08 已完成，Tutorial 09 Part 1 尚未开始教学**.

Part 1 的代码只是教学材料草稿，不代表学生已学习或掌握.

---

## 今天 (全天) 已掌握 (理论层面, 未动手)

### Part 1 - Field 原理
- `Field()` 三件事: 必填标记 / 值约束 / 元数据
- 4 行口头自测
- 学生口头解释全部自洽

### Part 2 - model_dump() 的本质
- BaseModel 实例不是 dict —— `model_dump()` 是对象 —— dict 网关
- 在 `validate_args` 里存在的目的: 给下游 `execute_tool(**arguments)` 喂 dict-friendly 数据

### Part 3 - TOOL_ARG_MODELS 复习
- 它不是函数, 是**全局字典**, 跟 `TOOLS` 对称
- 加新工具时, 两个字典各加一行 (2 处改动)

### Part 4 - Optional + default 是两件事
- `Optional[X]` —— 类型上接受 `None`
- `default=Y` —— 漏传时用 Y 兜底
- 4 种组合的真实行为表已建立

### Part 5 - List[X] 与 None 是什么类型
- `List[X]` 字面 = X 的列表, 逐元素校验 (报错带索引)
- `None` 是 Python 的 "空" 标记, 等价 JSON `null`

### Part 6 - Field 高级约束 + 教学风格更新
- `pattern` 慎用, 约束按需加
- **教学风格新规则**: 进入新概念必须先讲原理 —— 字面 —— 真实代码 —— 真实输出, 再让学生预测

---

## 当前能力等级 (Day 5 验证后)

### L5 解释原理
- Pydantic Field 的两件事 (必填标记 / 值约束)
- 类型错 vs 值越界 的区分 (int_parsing / greater_than_equal / less_than_equal / int_from_float)
- `**` 解包在函数调用和 BaseModel 实例化的复用

### L4 独立写出 + 解释
- Pydantic 4 行口头自测 (必填 / 默认 / 上下限 三维度)
- `model_dump()` 是 "对象 —— dict 网关" 概念
- `Optional[T]` 跟 `default=Y` 是两件事
- `TOOLS` vs `TOOL_ARG_MODELS` 双字典分工 (复习确认)

### L3 听过原理 + 概念清楚 (未在项目里实际写过)
- `Optional[T] = Field(default=...)` 写法
- `List[X]` 字段 + `min_length/max_length`
- `None` 在 Agent 工具中的角色

### L2 仍然薄弱
- Pydantic `Optional` / `List` / `Field(default=...)` 在 `tools.py` 里实际写过 (Day 6 自然补齐)
- 错误分类边界 case (PermissionError / IsADirectoryError / UnicodeDecodeError)
- 多轮错误恢复的 token 成本意识
- `validate_args` 返回元组 `(ok, validated)` 的设计哲学 (Day 4 Q6, 待 Day 7 单讲)

---

## 当前文件状态 (Day 7)

projects/tutorials/08_simple_agent/
- agent.py —— Agent 循环 + 三层错误拦截 + Pydantic 集成 (未改)
- tools.py —— tools + classify_error + TOOL_ARG_MODELS + ReadFileArgs/PrintArgs (未改)
- llm.py —— DeepSeek 封装 (未改)
- config.py —— env 加载 (未改)
- run_agent.py —— sys.path 注入 (未改)
- test_all_errors.py —— 5 轮错误恢复端到端测试 (未改)
- bug_test.py / json_test.py / tools_v2.py —— Day 2 训练场 (未改)

docs/daily/2026-07-20.md —— **Day 5 完成日志** (新)
docs/daily/2026-07-19.md —— Day 4 完成日志 (未改)
docs/daily/2026-07-23.md —— Day 7 Tutorial 09 Part 1 日志
projects/tutorials/09_structured_agent/ —— Tutorial 09 Part 1
AI_CONTEXT.md —— 更新到 Day 7
PROJECT_STATE.md —— 更新到 Day 7
ROADMAP.md —— 更新到 Tutorial 09 Part 1

---

## 下次 Session 起点 (Day 7 Part 1 练习)

### 主线进度
08_simple_agent 三件套完成度: **3 / 3** 完成
- v 结构化输入 (Pydantic)
- v 结构化错误 (execute_tool + classify_error)
- v 多工具混合调用 (Day 6 完结, 验证机制不动代码)

### 今日 5 阶段教学节奏 (沿用)
原理 —— 字面 —— 真实代码 —— 真实输出 —— 学生预测.

### 今日代码草稿验证 (不计入学习完成)
- JSON action 响应解析为 `AgentAction`
- 一个响应解析出 2 个 `ToolCall`
- 解析阶段不执行任何工具

### Tutorial 09 当前状态
- Part 1 教学材料已搭建
- Part 1 尚未正式教学
- Part 1 尚未完成练习与能力确认

### 正式教学顺序
- Part 1：Why → Principle → Terminology → Real Code → Real Output → Pattern → Prediction → Practice
- Part 2：参数模型与嵌套参数验证
- Part 3：结构化动作的工具执行
- Part 4：多工具调度与结果回传
- 复杂工具设计 (`@dataclass` + 嵌套 args)
- Pydantic List[str] 实战 (MultiPrintArgs)
- Q6 `validate_args` 返回 `(ok, validated)` 元组的设计风格对比
- 错误分类边界 case (PermissionError / IsADirectoryError / UnicodeDecodeError)

### 环境注意事项 (沿用 Day 4)
- PowerShell `Set-Content -Encoding UTF8` 加 BOM —— 今天用 Node `fs.writeFileSync` 写文件避免
- Windows console 报 UnicodeEncodeError —— 跑前 `$env:PYTHONIOENCODING='utf-8'`

---

## 避免重开 (下次 Session 不要重新教学这些)

- Tool Registry / 动态 Tool Calling / execute_tool(name, arguments)
- **arguments 解包 / f-string / 正则 / match.group / Match None
- JSON.loads(str) -> dict / 字典 key 大小写敏感
- Agent Loop 11 步 / messages.append 顺序语义
- try/except + raise + traceback + 异常家族 (Day 4 确认)
- Pydantic 4 行口头自测 (Day 5 确认)
- model_dump() 网关 (Day 5 确认)
- Optional + default 二分 (Day 5 确认)
- TOOLS vs TOOL_ARG_MODELS 双字典分工 (Day 5 复习确认)
- **多工具连续调用机制 (Day 6 确认)**: re.search 只取第一个 TOOL, 下一轮基于上一轮 result 重新决策, messages 长度 = 2 + 2N

如果发现新的理解错误, 针对具体问题补充, 不整体复习.

---

## 核心学习风格备注

- 学生喜欢完整代码块 (反馈过: 不要碎片化代码)
- 学生喜欢真实项目例子 (不用假设类)
- 学生喜欢从具体反推抽象 (已展示 L4 推理能力)
- **新规则** (Day 5 起强制): 教学用「原理 —— 字面 —— 代码 —— 输出 —— 预测」节奏, 不要在没讲清楚前让学生预测
- 评估按 8 级制度
