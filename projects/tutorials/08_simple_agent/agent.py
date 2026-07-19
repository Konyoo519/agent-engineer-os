"""Agent 核心：Think → Act → Observe 循环。"""

import re
import json
from pydantic import ValidationError
import llm
from tools import (
    get_tool_descriptions,
    execute_tool,
    validate_args,
)

MAX_ROUNDS = 10
TOOL_PATTERN = re.compile(r"\[TOOL:([^:]+):(.*?)\]")


def build_system_prompt() -> str:
    return f"""你是一个 AI 助手。用户会给你一个目标，你需要一步步完成它。

你可以使用以下工具：

{get_tool_descriptions()}

调用工具的格式：在回复中写 [TOOL:工具名:参数]
参数必须是合法 JSON，例如：
[TOOL:print:{{"text":"hello world"}}]
[TOOL:read_file:{{"path":"./data.txt"}}]

只有在需要执行操作时才写 [TOOL:...]；
如果不需要执行任何操作，就直接给出最终答案，不要包含任何 [TOOL:...]。

如果工具执行失败，你会收到反馈信息，例如：
工具 read_file 执行失败（not_found）：文件不存在
或参数验证失败的信息，例如：
参数验证失败（path）：Field required 或 Input should be a valid string

请根据反馈调整下一步：
- bad_args / wrong_type / 参数验证失败：调整参数后重试
- not_found：换路径或告诉用户文件不存在
- unknown_tool：使用正确的工具名
- timeout：稍后重试
- unknown_error：停止并告诉用户出错了
"""


def format_result(result: dict) -> str:
    """把 execute_tool 返回的 dict 翻译成给 LLM 的字符串。"""
    if result["status"] == "success":
        return f"工具 {result['tool']} 执行成功：{result['content']}"
    return (
        f"工具 {result['tool']} 执行失败（{result['category']}）：{result['message']}"
    )


def format_validation_error(tool_name: str, e: ValidationError) -> str:
    """把 Pydantic ValidationError 翻译成给 LLM 的字符串。"""
    errors = e.errors()
    parts = []
    for err in errors:
        loc = ".".join(str(x) for x in err["loc"])
        msg = err["msg"]
        parts.append(f"{loc}: {msg}")
    detail = "; ".join(parts)
    return f"参数验证失败（{tool_name}）：{detail}"


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

        try:
            arguments = json.loads(tool_arg)
        except json.JSONDecodeError as e:
            feedback = f"参数解析失败：{e}。请输出合法 JSON。"
            print(f"[参数错误] {feedback}")
            messages.append({"role": "assistant", "content": response})
            messages.append({"role": "user", "content": feedback})
            continue

        print(f"[调用工具] {tool_name}({tool_arg!r})")

        # Pydantic 验证
        ok, validated = validate_args(tool_name, arguments)
        if not ok:
            feedback = format_validation_error(tool_name, validated)
            print(f"[参数验证失败] {feedback}")
            messages.append({"role": "assistant", "content": response})
            messages.append({"role": "user", "content": feedback})
            continue

        # 执行工具
        result = execute_tool(tool_name, validated)
        print(f"[工具结果] {result}")

        feedback = format_result(result)
        messages.append({"role": "assistant", "content": response})
        messages.append({"role": "user", "content": feedback})

    return f"已达到最大轮数 {MAX_ROUNDS}，强制结束。"
