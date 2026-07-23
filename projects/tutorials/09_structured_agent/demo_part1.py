"""运行 Tutorial 09 Part 1 的确定性示例。"""

from part1_protocol import describe_action, parse_action


RAW_RESPONSE = """
{
  "kind": "tool_calls",
  "tool_calls": [
    {"name": "read_file", "arguments": {"path": "tools.py"}},
    {"name": "print", "arguments": {"text": "读取完成"}}
  ]
}
"""


if __name__ == "__main__":
    action = parse_action(RAW_RESPONSE)
    print("=== STRUCTURED ACTION ===")
    for line in describe_action(action):
        print(line)
