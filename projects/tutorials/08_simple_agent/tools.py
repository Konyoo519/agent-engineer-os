"""工具定义 + 执行器。"""

from pathlib import Path


def print_tool(text: str) -> str:
    """在屏幕上打印文本。"""
    print(text)
    return "打印成功"


def read_file_tool(path: str) -> str:
    """读取文件内容。"""
    try:
        return Path(path).read_text(encoding="utf-8")
    except Exception as e:
        return f"读取失败: {e}"


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


def get_tool_descriptions() -> str:
    """生成给 LLM 看的工具说明。"""
    lines = []
    for tool in TOOLS.values():
        lines.append(f"- {tool['name']}({tool['name']}_args): {tool['description']}")
    return "\n".join(lines)


def execute_tool(name: str, arg: str) -> str:
    """根据名字执行工具，返回结果字符串。"""
    if name not in TOOLS:
        return f"未知工具: {name}"
    return TOOLS[name]["func"](arg)
