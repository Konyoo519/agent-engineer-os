"""工具定义 + 执行器。"""

from pathlib import Path
from pydantic import BaseModel, ValidationError


def print_tool(text: str) -> str:
    """在屏幕上打印文本。"""
    print(text)
    return "打印成功"


def read_file_tool(path: str) -> str:
    """读取文件内容。"""
    return Path(path).read_text(encoding="utf-8")


TOOLS = {
    "print": {
        "name": "print",
        "description": "在屏幕上打印文本",
        "func": print_tool,
    },
    "read_file": {
        "name": "read_file",
        "description": "读取文件内容，参数是文件路径",
        "func": read_file_tool,
    },
}


class PrintArgs(BaseModel):
    text: str


class ReadFileArgs(BaseModel):
    path: str


TOOL_ARG_MODELS = {
    "print": PrintArgs,
    "read_file": ReadFileArgs,
}


def get_tool_descriptions() -> str:
    """生成给 LLM 看的工具说明。"""
    lines = []
    for tool in TOOLS.values():
        lines.append(f"- {tool['name']}({tool['name']}_args): {tool['description']}")
    return "\n".join(lines)


def classify_error(e: Exception) -> str:
    """把 Python 异常归类成 LLM 友好的 category。"""
    error_map = {
        FileNotFoundError: "not_found",
        TimeoutError: "timeout",
        TypeError: "wrong_type",
        ValueError: "bad_args",
    }
    return error_map.get(type(e), "unknown_error")


def execute_tool(name: str, arguments: dict) -> dict:
    """执行工具，返回结构化结果（成功/失败）。"""
    try:
        if name not in TOOLS:
            raise KeyError(f"未知工具: {name}")
        result = TOOLS[name]["func"](**arguments)
        return {"tool": name, "status": "success", "content": result}
    except Exception as e:
        return {
            "tool": name,
            "status": "error",
            "category": classify_error(e),
            "message": str(e),
        }


def validate_args(tool_name: str, arguments: dict):
    """用 Pydantic 验证参数。返回 (ok, validated_dict_or_error_message)。"""
    if tool_name not in TOOL_ARG_MODELS:
        return True, arguments
    Model = TOOL_ARG_MODELS[tool_name]
    try:
        validated = Model(**arguments)
        return True, validated.model_dump()
    except ValidationError as e:
        return False, e
