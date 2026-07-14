# HANDOFF

## 今日会话（2026-07-14）

### 学习策略调整

不再从 Python 零基础开始。

采用 **Agent 主线 + Python for Agent Engineering 按需补强**：

1. 沿 AI Agent 主线推进
2. 遇到不熟的 Python 语法 / 数据结构 / 设计模式时，暂停主线
3. 拆成最小示例讲解
4. 给我小练习
5. Review 后回到主线
6. 关键代码优先自己写
7. 样板与工程辅助由 AI 协助

---

## 当前阶段

**Phase 4 - Agent（主线）**

**活跃项目：** `projects/tutorials/08_simple_agent`

已完成：

- [x] LLM API 调用
- [x] System Prompt 工程基础
- [x] Tool Registry（字典版）
- [x] 单参数 Tool Calling

---

## 已掌握的 Python 知识

- 基础语法
- 嵌套 dict / list
- 函数作为对象（`func` 作为 value 存进 dict）
- Dictionary-based Tool Registry
- `TOOLS[name]["func"]()` 调用模式

---

## 下一步

**目标：** 在 08_simple_agent 中支持多参数动态工具调用。

引出的 Python 知识点：**`**kwargs`**（字典解包成关键字参数）

---

## 学习位置

我们站在这里：

```text
单参数:  TOOLS[name]["func"](arg)
              ↓
多参数:  TOOLS[name]["func"](**kwargs)  ← 即将学习
```

---

## 当前活跃文件

- `projects/tutorials/08_simple_agent/tools.py` — Tool Registry
- `projects/tutorials/08_simple_agent/agent.py` — Agent 循环

---

## 教学原则（再确认）

不要以"代码跑通"为掌握标准。

每个知识点要能回答：

1. 为什么这样写？
2. 需求变了改哪里？
3. 报错怎么定位？

---

## 状态

主线进行中，等待用户确认后开始 **多参数 Tool Calling** 练习。
