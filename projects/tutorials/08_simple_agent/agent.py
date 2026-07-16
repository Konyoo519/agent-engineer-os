"""Agent 核心：Think → Act → Observe 循环。"""

import re
import json
import llm
from tools import get_tool_descriptions, execute_tool

MAX_ROUNDS = 10
TOOL_PATTERN = re.compile(r"\[TOOL:([^:]+):(.*?)\]")


def build_system_prompt() -> str:
    return f"""你是一个 AI 助手。用户会给你一个目标，你需要一步步完成它。

你可以使用以下工具：

{get_tool_descriptions()}

调用工具的格式：在回复中写 [TOOL:工具名:参数]
例如：
[TOOL:print:{{"text":"hello world"}}]
[TOOL:read_file:{{"path":"./data.txt"}}]

只有在需要执行操作时才写 [TOOL:...]；
如果不需要执行任何操作，就直接给出最终答案，不要包含任何 [TOOL:...]。"""


def run(goal: str) -> str:
    """启动 Agent，返回最终结果。"""
    messages = [
        {"role": "system", "content": build_system_prompt()},
        {"role": "user", "content": goal},
    ]

    for round_num in range(1, MAX_ROUNDS + 1):
        response = llm.chat(messages)
        print(f"\n[Round {round_num}] LLM 回复：\n{response}")

        match = TOOL_PATTERN.search(response)
        if not match:
            return response

        tool_name = match.group(1).strip()
        tool_arg = match.group(2).strip()
        arguments = json.loads(tool_arg)
        print(f"[调用工具] {tool_name}({tool_arg!r})")

        
        result = execute_tool(tool_name, arguments)
        print(f"[工具结果] {result}")

        messages.append({"role": "assistant", "content": response})
        messages.append({"role": "user", "content": f"工具执行结果：{result}"})

    return f"已达到最大轮数 {MAX_ROUNDS}，强制结束。"
