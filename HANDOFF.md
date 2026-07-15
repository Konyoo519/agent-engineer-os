# HANDOFF

## 最新会话：2026-07-15

### 今日主题

从「无参数动态工具调用」推进到「带参数动态工具调用」。
完整跑通六个阶段，每一步都经过「先解释 → 自己写 → Review → 跑通」四件套验证。

### 今日已掌握（经过练习验证）

- parameter（形参）/ argument（实参）的语义区分
- arguments = {"key": "value", ...} 作为命名参数字典的形态
- ** arguments 的解包语义：把字典展开成命名参数 name="Alice", city="Hangzhou"
- print(...) 的求值顺序：Python 先把括号里「算」出一个值，再交给 print
- TOOLS[tool_name]["func"](** arguments) 这整行的 4 步执行过程（能用大白话讲）
- 为什么 Tool Registry 选嵌套字典而不是扁平 key→函数：为了给 description / 参数 schema 等元数据留扩展空间
- LLM 与 Python 的职责分工：
  - LLM 决定 name（调哪个工具） + arguments（参数是什么）
  - Python 拿到这两个值，真正执行 TOOLS[name]["func"](** arguments)
  - LLM 不直接执行 Python 函数

### 下一步

主线 Phase 4 Agent 推进：

1. 把 08_simple_agent/tools.py 的 execute_tool(name, arg) 升级，真正接收 arguments: dict，内部用 ** arguments 解包
2. 让 LLM 输出的 name + arguments 真正驱动工具调用（接 DeepSeek / OpenAI API）
3. 引入工具结果结构化（JSON schema / Pydantic）
4. 引入错误处理与重试

下一步引入的 Python 知识点（如果遇到卡点）：

- 类型注解（def greet(name: str, city: str) -> str）— 视情况补
- Pydantic 模型 — 用于参数 schema 时会用到

### 旁支：今日不展开的选修

- 一个工具多参数 / 不同工具不同参数 / 工具不存在 / 参数缺失 / try-except

如果推进主线时需要，直接补；不强行单开课时。

### 教学规则再确认

不按「代码行数」作掌握标准。每段知识必须能回答：

1. 为什么这样写
2. 需求变更改哪里
3. 报错如何定位

---

## 上一会话：2026-07-14

### 学习策略调整

不再从 Python 零基础开始。

采用 **Agent 主线 + Python for Agent Engineering 按需补强**：

1. 沿 AI Agent 主线推进
2. 遇到不熟的 Python 语法 / 数据结构 / 设计模式时，暂停主线
3. 拆成最小示例讲解
4. 给我小练习自己完成
5. Review 后回到主线
6. 关键代码优先自己敲；模板与工程脚手架由 AI 协助

## 当前阶段

**Phase 4 - Agent（主线）**

**活跃项目：** projects/tutorials/08_simple_agent

已完成：

- [x] LLM API 调用
- [x] System Prompt 工程基础
- [x] Tool Registry（字典版）
- [x] 单参数 Tool Calling
- [x] 多参数动态传入 Tool Calling（2026-07-15）
- [x] **kwargs 基础用法（2026-07-15）
- [x] LLM 与 Python 工具执行职责区分（2026-07-15，纯概念）

## 已掌握的 Python 知识

- 基础语法
- 嵌套 dict / list
- 函数作为对象（"func" 作为 value 存进 dict）
- Dictionary-based Tool Registry
- TOOLS[name]["func"]() 调用模式
- parameter / argument 区分（2026-07-15）
- rguments = {...} 作为命名参数字典（2026-07-15）
- **arguments 字典解包成命名参数（2026-07-15）
- print(...) 的「先求值再打印」机制（2026-07-15）

## 当前活跃文件

- projects/tutorials/08_simple_agent/tools.py — Tool Registry
- projects/tutorials/08_simple_agent/agent.py — Agent 循环

## 教学原则（再确认）

不要按「代码行数」作为掌握标准。

每个知识点要能回答：

1. 为什么这样写
2. 需求变更改哪里
3. 报错怎么定位

## 状态

主线进行中，多参数动态工具调用已跑通。下次开始：把 08_simple_agent/tools.py 中的 execute_tool(name, arg) 真正升级为支持多参数 + 接入 LLM API 驱动。