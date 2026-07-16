import json

# 实验 1
try:
    print("1:", json.loads('hello world'))
except Exception as e:
    print("1 报错:", e)

# 实验 2
try:
    print("2:", json.loads('{"text":"hi"}'))
except Exception as e:
    print("2 报错:", e)

# 实验 3
try:
    print("3:", json.loads('123'))
except Exception as e:
    print("3 报错:", e)