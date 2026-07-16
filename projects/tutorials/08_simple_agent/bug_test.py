def add(a, b):
    return a + b

def greet(name):
    return f"Hello, {name}"

def now():
    return "2026-07-15"

TOOLS = {
    "add": {"func": add},
    "greet": {"func": greet},
    "now": {"func": now}
}

def execute_tool(name, arguments: dict) -> str:
    return TOOLS[name]["func"](**arguments)

print(execute_tool("add", {"a": 1, "b": 2}))
print(execute_tool("greet", {"name": "Tom"}))
print(execute_tool("now", {}))