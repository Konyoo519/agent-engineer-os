# Tutorial 09：Structured Agent

## 项目定位

Tutorial 08 的 Agent 使用普通文本承载工具调用：

```text
[TOOL:read_file:{"path":"tools.py"}]
```

Tutorial 09 将把 Agent 的动作表示为结构化数据，使“最终回答”和“工具调用”成为明确的数据类型，后续再逐步加入参数验证、工具执行和多工具调度。

## 学习目标

- 理解文本协议在复杂 Agent 中的边界
- 理解 Agent 动作为什么需要结构化表示
- 使用 `@dataclass` 表示工具调用和 Agent 动作
- 从 JSON 响应解析出多个结构化工具调用
- 区分“解析动作”和“执行工具”两个职责

## 课程边界

本 Tutorial 不追求一次完成完整 Agent。每个 Part 只增加一个能力，并在真实输出后再进入预测和练习。

## 目录

- `part1_protocol.py`：Part 1，结构化动作协议与解析
- `demo_part1.py`：Part 1 可重复运行的真实示例
- `test_part1.py`：Part 1 基础行为测试

后续 Part（待学习后设计）可能包括：

- 参数模型与嵌套参数验证
- 结构化动作的工具执行
- 多工具调度与结果回传
- Agent Loop 的新数据流
