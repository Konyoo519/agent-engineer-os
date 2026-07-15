# Python

Python 语言基础知识,为 Agent 开发常用技术。

> 学习策略:**按需补强**。沿 Agent 主线推进,遇到不熟的语法 / 数据结构 / 设计模式时再补。

---

## 已掌握

### 字典的 key 与 value

字典是一组 **key → value** 的映射。

- **key**:用于检索的"名字",通常是字符串或数字
- **value**:key 对应的"内容",可以是任何对象,包括函数、字典、列表

```python
user = {"name": "Alice", "age": 30}

# key  → value
# "name" → "Alice"
# "age"  → 30

print(user["name"])  # 用 key 取出 value → Alice
```

**读取报错的两种常见情况**:

- `KeyError: 'xxx'` → 字典里没有这个 key
- 属性语法混淆 → 比如 list 用 `user.name`(属性语法)而不是 `user["name"]`

### 函数作为一等公民(First-Class Function)

Python 中函数是对象,可以:

- 赋值给变量
- 存进 dict / list
- 作为参数传递
- 作为返回值

```python
def greet(name):
    return f"Hello, {name}"

# 赋值给变量
f = greet
print(f("Alice"))  # Hello, Alice
```

**关键区分**:

- `greet` → 函数对象(可以传递、存储、但还没执行)
- `greet("Alice")` → 函数**调用**的结果

**应用场景:** Tool Registry 把函数作为 value 存进字典。

### 固定调用 vs 动态调用

**固定调用:** key 写死在代码里。

```python
TOOLS["print"]["func"]()
```

**动态调用:** key 用变量传入。

```python
tool_name = "print"        # 可能是 LLM 决定的,可能是用户决定的
TOOLS[tool_name]["func"]()
```

**为什么需要动态调用**:

- Agent 场景下,"调用哪个工具"是运行时决定的
- 当前由用户(写死的变量)决定;未来由 LLM 决定
- 把 key 变成变量,是 Agent Tool Calling 的关键一步

### Dictionary-based Tool Registry

将工具用 dict 组织,key 是工具名,value 包含元数据和函数本身。

```python
TOOLS = {
    "print": {
        "name": "print",
        "description": "在屏幕上打印文本",
        "func": print_tool,
    },
    "read_file": {
        "name": "read_file",
        "description": "读取文件内容",
        "func": read_file_tool,
    },
}
```

动态调用模式:

```python
TOOLS[name]["func"]()
# 等价于
tool_function = TOOLS[name]["func"]  # 取出函数对象
tool_function()                        # 调用它
```

**工程意义**:

- 不需要写 if/elif 链
- 加新工具只需往 TOOLS 加一项
- LLM 可以通过名称动态选择

### 参数区分:parameter vs argument

- **parameter(形参)**:`def greet(name):` 中的 `name`,是函数定义里的"占位格"
- **argument(实参)**:`greet("Alice")` 中的 `"Alice"`,是调用时实际填进去的值

**为什么需要参数**:函数是模板,参数让同一个模板能处理不同的具体值。

### 命名参数字典 `arguments`

为多参数工具调用准备一个字典容器:

```python
arguments = {"name": "Alice", "city": "Hangzhou"}
```

- key 对应**函数参数名**
- value 对应**实际传入的值**
- Agent 系统喜欢这种形态,因为它**结构化**,可以直接由 LLM 输出

### **kwargs:字典解包成命名参数(2026-07-15)

```python
arguments = {"name": "Alice", "city": "Hangzhou"}

greet(**arguments)
# 等价于
greet(name="Alice", city="Hangzhou")
```

**机制**:Python 把 `**arguments` 里的字典"展开"成命名参数,key 对应形参名,value 对应形参值。

**限制**:

- 字典的 **key 必须和函数形参名完全一致**
- key 多了 / 少了 / 拼错都会 `TypeError`

**与 `*args` 的对比**:

| 写法 | 展开的是什么 | 喂给函数的形态 |
|---|---|---|
| `greet(**arguments)` | 字典 | 命名参数 `name='Alice'` |
| `greet(*args_list)`(待补) | 列表/元组 | 位置参数 `'Alice'` |

**Agent 价值**:

- LLM 输出 `{"name": "greet", "arguments": {"name": "Alice", ...}}`
- Agent 程序 `TOOLS[name]["func"](**arguments)` 一行完成"取函数 + 解包 + 调用"
- 这就是动态工具调用 + 多参数的**完整一行**

### 完整调用:`TOOLS[name]["func"](**arguments)`

Python 真的做的 4 步(从外往内展开):

```python
print(TOOLS['greet']['func'](**arguments))
```

1. `TOOLS['greet']` → 取出内嵌字典 `{"func": greet}`
2. `['func']` → 取出 greet 函数对象
3. `(**arguments)` → 把字典展开成命名参数并真正启动 greet,得到返回字符串
4. `print(...)` → 打印 greet 的返回值

**位置参数 vs 关键字参数的对比**:

```python
# 位置参数(匿名,从左到右填)
greet("Alice", "Hangzhou")

# 关键字参数(有名字,按名字对应形参)
greet(name="Alice", city="Hangzhou")

# **arguments 把字典展开成第二种
greet(**arguments)
```

### 类型注解(2026-07-15)

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

- `name: str` —— 标注参数 `name` 期望是字符串
- `-> str` —— 标注函数返回字符串
- **运行时完全不影响行为**,只是"声明/注释"

```python
# 有类型注解
def greet(name: str) -> str: ...

# 没有类型注解(也合法)
def greet(name): ...
```

**Agent 价值**:Tool Registry 中 `def print_tool(text: str) -> str` 这种风格让 LLM / 工程师一眼看出"这个工具接收什么、返回什么"。

### `list.append(item)`:列表末尾追加(2026-07-15)

```python
messages = []                                # 空列表
messages.append({"role": "user", "content": "hi"})
messages.append({"role": "assistant", "content": "hello"})
# messages: [{'role': 'user', 'content': 'hi'}, {'role': 'assistant', 'content': 'hello'}]
```

- `messages.append(...)` = "**往盒子里塞纸条**"
- `messages` 是盒子(列表)
- 一张纸条就是一个 dict

**Agent 价值**:Agent Loop 中 `messages.append(...)` 把"工具结果"塞回下一轮 messages,LLM 在新一轮"看到"自己刚才调的工具返回了什么,才能决定下一步。

### `json.loads(s)`:字符串 → dict(2026-07-15)

```python
import json

text = '{"text": "hello world"}'
arguments = json.loads(text)
print(arguments)        # {'text': 'hello world'}
print(type(arguments))  # <class 'dict'>
```

- `json` 是 Python 标准库,`import json` 直接用,**不用 pip install**
- `json.loads(s)` 把"长得像 JSON 的字符串"反序列化成 Python 字典
- `json.dumps(d)` 把 dict 序列化成 JSON 字符串(今天用不到,以后会)

**与上午 `**arguments` 的关系**:

| 操作 | 写法 | 方向 |
|---|---|---|
| dict → 命名参数 | `greet(**arguments)` | Python 函数调用 |
| 字符串 → dict | `json.loads(s)` | JSON 反序列化 |

**Agent 价值**:

- LLM 输出 JSON 字符串(系统 prompt 约束的格式)
- agent.py 用 `json.loads()` 转成 dict
- 再走 `execute_tool(name, arguments)` → `**arguments` 解包调用

完整链:

```python
text = '[TOOL:print:{"text":"hello"}]'
match = re.search(...)                         # 正则挑出中间 JSON
arg_str = match.group(2).strip()              # 拿到字符串
arguments = json.loads(arg_str)                # 字符串 → dict
result = execute_tool("print", arguments)     # dict → 命名参数 → 真执行
```

### 字面量区分:`{a, b}`(set)vs `{key: value}`(dict)(2026-07-15)

```python
{"a", "b"}                # ← set 字面量(没有冒号)
{"key_a": "a", "key_b": "b"}  # ← dict 字面量(必须带冒号)
```

**常见错误**:

```python
{'tool_arg', tool_arg}    # ← 这是 set,Python 会报错说"unhashable"
{'text': tool_arg}        # ← 这才是 dict
```

**Agent 价值**:`json.loads` 反序列化出来的对象**总是 dict**,但写 JSON 字面量时,稍不留神会写成 set。

### f-string 里的引号(2026-07-15,补一句)

```python
name = "Alice"
print(f"Hello, {name}")  # Hello, Alice
```

- `{}` 里的变量就地替换成字符串
- **在 f-string 三引号 `f"""..."""` 里嵌 JSON 示例时,内层双引号是合法的**(因为外层是三引号)

```python
prompt = f"""请用 JSON 格式,例如:
  [TOOL:print:{{"text":"hello"}}]"""
```

---

## 待补(遇到时再补)

- *args(列表/元组解包成位置参数)
- 类型注解的高级用法(typing 模块、Optional、Union)
- class 与工程化对象设计
- 装饰器
- async / await
- 模块与包
- Pydantic
- 异常处理 try / except
- 第三方库工程代码