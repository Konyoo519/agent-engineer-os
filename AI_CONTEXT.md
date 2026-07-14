# AI Context

> 这是 ChatGPT、Codex 与未来其他 AI 工具之间的**跨 AI 上下文快照**。
>
> 它**不是**完整历史，也**不是**唯一事实来源。
> 完整事实分布在：README / ROADMAP / PROJECT_STATE / HANDOFF / docs/knowledge/ / docs/daily/ / projects/。
> 本文件只负责让一个新的 AI 对话只读这一份文件就能快速恢复当前学习状态。

最后更新：2026-07-14

---

## 1. Project

- 项目名称：**Agent Engineer OS**
- 项目目标：120 天内具备 AI Agent Developer 岗位的工程能力
- 目标岗位：AI Agent Developer
- 目标公司：DeepSeek / MiniMax / Moonshot AI / ByteDance / Zhipu AI / Tencent

---

## 2. AI Collaboration Model

| 角色         | 职责 |
| -------------- | ------------------------------------------------------- |
| **ChatGPT**    | 学习路线规划 / 原理解释 / 知识体系建立 / 复习 / 职业规划 / 面试指导 |
| **Codex**      | 编码实践 / 练习 / Code Review / Debug / 项目执行 / 仓库维护 / 学习进度跟踪 |
| **Git**        | 版本控制与历史记录                                          |
| **GitHub**     | 远程同步 / 备份 / 作品展示                                  |
| **Markdown**   | 持久化学习状态（README / ROADMAP / PROJECT_STATE / HANDOFF / AI_CONTEXT / docs/） |

---

## 3. Current Stage

- **当前 Sprint**：Sprint 4 — Agent
- **当前学习阶段**：AI Agent 工程化（主线）
- **当前学习主题**：Tool Calling 基础
- **当前活跃项目**：`projects/tutorials/08_simple_agent`
- **当前 Day**：Day 1（采用 Agent 主线 + Python 按需补强 策略）

活跃项目结构：

- `config.py`：从 `.env` 读取 DeepSeek 配置
- `llm.py`：OpenAI 兼容 chat 封装
- `tools.py`：Tool Registry（字典版，单参数 `execute_tool(name, arg)`）
- `agent.py`：Think → Act → Observe 循环 + 正则解析 `[TOOL:name:arg]`

---

## 4. Learning Strategy

**主线：** AI Agent 工程化开发
**辅线：** Python for Agent Engineering（**按需补强**）

用户**不是** Python 零基础。能理解基础语法，但在阅读 AI Agent 工程代码时可能需要补强：

- 嵌套 dict / list
- 函数作为对象
- Tool Registry
- *args / **kwargs
- 类型注解
- class 与工程化对象设计
- 装饰器
- async / await
- 模块与包
- Pydantic
- 第三方库工程代码

**教学循环：**

```text
遇到不理解的 Python 语法 / 数据结构 / 设计模式
        ↓
暂停 Agent 主线
        ↓
使用最小示例解释
        ↓
用户自己完成小练习
        ↓
Review
        ↓
确认理解
        ↓
返回 Agent 主线
```

**规则：**

- 不要让用户从 Python 零基础重新学习
- 不要因为使用 AI 编程而跳过关键 Python 能力

**目标能力：**

1. 能阅读 Agent 工程代码
2. 能独立编写小型 Python 逻辑
3. 能修改 AI 生成的代码
4. 能 Debug
5. 能解释自己的项目和关键代码

---

## 5. Completed Learning

> 只有经过实际学习、练习或明确确认的内容才能进入此清单。

### 项目协作

- Agent Engineer OS 的基本协作模式
- ChatGPT / Codex / Git / GitHub 的职责分工
- Git 基础工作流（init / commit / log）

### Agent 概念

- ChatBot / Workflow / Agent 的初步区别
- Tool Calling 的基础概念
- Think → Act → Observe 循环

### Python for Agent

- Python 嵌套字典
- 字典 key 和 value 的区别
- 字典的基本读取（`TOOLS[name]`）
- 函数本身与函数调用的区别
- 函数可以作为字典的 value
- 函数可以赋值给变量、可以取出再调用
- Tool Registry 的基本思想
- **固定工具调用**：`TOOLS["print"]["func"]()`
- **动态工具选择**：使用变量 `tool_name` 选工具
- Dictionary-based Tool Registry
- 动态函数调用模式：`TOOLS[tool_name]["func"]()`

---

## 6. Key Understanding

当前已经理解并能写出：

```python
TOOLS[tool_name]["func"]()
```

**拆解：**

| 部分              | 含义                              |
| ----------------- | ------------------------------- |
| `TOOLS`          | 整个工具注册表（dict）                  |
| `[tool_name]`    | 用名字动态选工具                       |
| `["func"]`       | 嵌套字典中的 key（指向函数对象）             |
| `()`             | 真正执行函数                         |

**核心认知：**

```text
现在：用户决定 tool_name
未来：LLM 可以决定 tool_name
```

当前练习是 Agent Tool Calling 机制的**简化雏形**。

---

## 7. Current Learning Position

**已完成：** 无参数工具的动态选择和动态调用。

**暂停位置：**

```python
TOOLS[tool_name]["func"]()
```

**下一步准备学习：** 带参数的工具调用，包括但不限于：

- 函数参数
- arguments
- 参数字典
- *args
- **kwargs
- 如何将参数动态传入工具函数
- 这些机制如何逐步对应到 LLM Tool Calling

**注意：** 不要一次性全部教学。继续使用「小步练习 → 用户作答 → Review → 下一步」的方式。

---

## 8. User Learning Profile

只记录对未来 AI 恢复教学状态有帮助的信息：

- 用户具备基础 Python 阅读能力，**不是零基础**
- 用户更适合通过**真实 Agent 场景**理解 Python
- 用户对抽象工程代码需要逐层拆解
- 手写小练习有助于确认真实理解
- 不应以"代码成功运行"作为掌握标准

**掌握标准（必须三者都能回答）：**

1. 这段代码为什么这样写？
2. 需求改变时改哪里？
3. 报错时从哪里定位？

---

## 9. Next Step

从无参数动态工具调用：

```python
TOOLS[tool_name]["func"]()
```

继续学习：**如何向动态选择的工具传递参数**。

引出的 Python 知识点：**`**kwargs`**（把字典解包成关键字参数）。

---

## 状态一致性

本文档与以下文件保持同步（最后核对：2026-07-14）：

- ROADMAP.md（Phase 4 下一步：多参数动态传入）
- PROJECT_STATE.md（Sprint 4 / Day 1 / 当前下一步：多参数动态传入 Tool Calling）
- HANDOFF.md（下一步：在 08_simple_agent 中支持多参数动态工具调用）

详细维护规则见 `AGENTS.md` 的 "AI Context Synchronization" 章节。
