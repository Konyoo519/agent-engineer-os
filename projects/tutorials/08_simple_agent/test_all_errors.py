import sys
sys.path.insert(0, '.')
import llm

# Mock LLM 模拟 5 轮：依次触发各种错误 + 最后成功
scripted = [
    "[TOOL:read_file:{\"path\": 123}]",                        # 1. Pydantic 类型错
    "[TOOL:read_file:{\"path\": \"missing_file.txt\"}]",        # 2. 文件不存在
    "[TOOL:read_file:]",                                        # 3. JSON 解析错
    "[TOOL:read_file:{\"path\": \"tools.py\"}]",                # 4. 成功
    "全部任务完成。",                                            # 5. 最终回答
]
llm.chat = lambda messages: scripted.pop(0)

import agent
final = agent.run("读 tools.py 告诉我有什么")
print()
print("=== FINAL ===")
print(final)
