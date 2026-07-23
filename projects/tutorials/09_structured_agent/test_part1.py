"""Tutorial 09 Part 1 的基础测试。"""

import unittest

from part1_protocol import parse_action


class Part1ProtocolTests(unittest.TestCase):
    def test_parse_multiple_tool_calls(self):
        raw = (
            '{"kind":"tool_calls","tool_calls":'
            '[{"name":"print","arguments":{"text":"hi"}}]}'
        )

        action = parse_action(raw)

        self.assertEqual(action.kind, "tool_calls")
        self.assertEqual(len(action.tool_calls), 1)
        self.assertEqual(action.tool_calls[0].name, "print")
        self.assertEqual(action.tool_calls[0].arguments, {"text": "hi"})

    def test_parse_final_response(self):
        action = parse_action('{"kind":"final","text":"完成"}')

        self.assertEqual(action.kind, "final")
        self.assertEqual(action.final_text, "完成")


if __name__ == "__main__":
    unittest.main()
