# Python

Python 语言基础知识,为 Agent 开发常用技术。

> 学习策略:**按需补强**。沿 Agent 主线推进,遇到不熟的语法 / 数据结构 / 设计模式时再补。

---

## 已掌握

### 字典的 key 与 value

字典是一组 **key → value** 的映射。

- **key**:用于检索的"名字",通常是字符串或数字
- **value**:key 对应的"内容",可以是任何对象,包括函数、字典、列表

`python
user = {"name": "Alice", "age": 30}

# key  → value
# "name" → "Alice"
# "age"  → 30

print(user["name"])  # 用 key 取出 value → Alice
`

**读取报错的两种常见情况**:

- KeyError: 'xxx' → 字典里没有这个 key
- 属性语法混淆 → 比如 list 用 user.name(属性语法)而不是 user["name"]

### 函数作为一等公民(First-Class Function)

Python 中函数是对象,可以:

- 赋值给变量
- 存进 dict / list
- 作为参数传递
- 作为返回值

`python
def greet(name):
    return f"Hello, {name}"

# 赋值给变量
f = greet
print(f("Alice"))  # Hello, Alice
`

**关键区分**:

- greet → 函数对象(可以传递、存储、但还没执行)
- greet("Alice") → 函数**调用**的结果

**应用场景:** Tool Registry 把函数作为 value 存进字典。

### 固定调用 vs 动态调用

**固定调用:** key 写死在代码里。

`python
TOOLS["print"]["func"]()
`

**动态调用:** key 用变量传入。

`python
tool_name = "print"        # 可能是 LLM 决定的,可能是用户决定的
TOOLS[tool_name]["func"]()
`

**为什么需要动态调用**:

- Agent 场景下,"调用哪个工具"是运行时决定的
- 当前由用户(写死的变量)决定;未来由 LLM 决定
- 把 key 变成变量,是 Agent Tool Calling 的关键一步

### Dictionary-based Tool Registry

将工具用 dict 组织,key 是工具名,value 包含元数据和函数本身。

`python
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
`

动态调用模式:

`python
TOOLS[name]["func"]()
# 等价于
tool_function = TOOLS[name]["func"]  # 取出函数对象
tool_function()                        # 调用它
`

**工程意义**:

- 不需要写 if/elif 链
- 加新工具只需往 TOOLS 加一项
- LLM 可以通过名称动态选择

### 参数区分:parameter vs argument

- **parameter(形参)**:def greet(name): 中的 
ame,是函数定义里的"占位格"
- **argument(实参)**:greet("Alice") 中的 "Alice",是调用时实际填进去的值

**为什么需要参数**:函数是模板,参数让同一个模板能处理不同的具体值。

### 命名参数字典 rguments

为多参数工具调用准备一个字典容器:

`python
arguments = {"name": "Alice", "city": "Hangzhou"}
`

- key 对应**函数参数名**
- value 对应**实际传入的值**
- Agent 系统喜欢这种形态,因为它**结构化**,可以直接由 LLM 输出

### **kwargs:字典解包成命名参数(2026-07-15)

`python
arguments = {"name": "Alice", "city": "Hangzhou"}

greet(**arguments)
# 等价于
greet(name="Alice", city="Hangzhou")
`

**机制**:Python 把 ${dbstar}arguments 里的字典"展开"成命名参数,key 对应形参名,value 对应形参值。

**限制**:

- 字典的 **key 必须和函数形参名完全一致**
- key 多了 / 少了 / 拼错都会 TypeError

**与 *args 的对比**:

| 写法 | 展开的是什么 | 喂给函数的形态 |
|---|---|---|
| greet(**arguments) | 字典 | 命名参数 
ame='Alice' |
| greet(**args_list)(待补) | 列表/元组 | 位置参数 'Alice' |

**Agent 价值**:

- LLM 输出 {"name": "greet", "arguments": {"name": "Alice", ...}}
- Agent 程序 TOOLS[name]["func"](**arguments) 一行完成"取函数 + 解包 + 调用"
- 这就是动态工具调用 + 多参数的**完整一行**

### 完整调用:TOOLS[name]["func"](**arguments)

Python 真的做的 4 步(从外往内展开):

`python
print(TOOLS['greet']['func'](**arguments))
`

1. TOOLS['greet'] → 取出内嵌字典 {"func": greet}
2. ['func'] → 取出 greet 函数对象
3. (**arguments) → 把字典展开成命名参数并真正启动 greet,得到返回字符串
4. print(...) → 打印 greet 的返回值

**位置参数 vs 关键字参数的对比**:

`python
# 位置参数(匿名,从左到右填)
greet("Alice", "Hangzhou")

# 关键字参数(有名字,按名字对应形参)
greet(name="Alice", city="Hangzhou")

# **arguments 把字典展开成第二种
greet(**arguments)
`

---

## 待补(遇到时再补)

- \*args(列表/元组解包成位置参数)
- 类型注解
- class 与工程化对象设计
- 装饰器
- async / await
- 模块与包
- Pydantic
- 第三方库工程代码

---

## f-string(2026-07-15,补一句)

`python
name = "Alice"
print(f"Hello, {name}")  # Hello, Alice
`

把 {} 里的变量就地替换成字符串。其余 Python 部分该是什么样就还是什么样。