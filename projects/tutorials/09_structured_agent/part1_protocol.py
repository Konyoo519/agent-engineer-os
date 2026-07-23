"""Tutorial 09 Part 1：把 Agent 响应表示为结构化动作。"""

from dataclasses import dataclass, field
import json
from typing import Any


@dataclass
class ToolCall:
    """一个待执行的工具调用，只描述动作，不执行工具。"""

    name: str
    arguments: dict[str, Any]


@dataclass
class AgentAction:
    """Agent 对当前响应的结构化表示。"""

    kind: str
    tool_calls: list[ToolCall] = field(default_factory=list)
    final_text: str | None = None


def parse_action(raw_response: str) -> AgentAction:
    """解析 Agent 的 JSON 响应，生成动作对象。"""
    payload = json.loads(raw_response)
    kind = payload["kind"]

    if kind == "tool_calls":
        calls = [
            ToolCall(name=item["name"], arguments=item["arguments"])
            for item in payload["tool_calls"]
        ]
        return AgentAction(kind=kind, tool_calls=calls)

    if kind == "final":
        return AgentAction(kind=kind, final_text=payload["text"])

    raise ValueError(f"不支持的 action kind: {kind}")


def describe_action(action: AgentAction) -> list[str]:
    """把结构化动作转换成适合观察的输出，不执行任何工具。"""
    lines = [f"ACTION KIND: {action.kind}"]

    if action.kind == "tool_calls":
        lines.append(f"TOOL CALL COUNT: {len(action.tool_calls)}")
        for index, call in enumerate(action.tool_calls, start=1):
            lines.append(f"CALL {index}: {call.name}({call.arguments})")
    else:
        lines.append(f"FINAL TEXT: {action.final_text}")

    return lines
