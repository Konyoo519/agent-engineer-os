# Python

Python 语言基础知识与 Agent 开发常用技巧。

> 学习策略：**按需补强**。沿 Agent 主线推进，遇到不熟的语法 / 数据结构 / 设计模式时再补。

---

## 已掌握

### 字典的 key 与 value

字典是一组 **key → value** 的映射。

- **key**：用于查找的"名字"，通常是字符串或数字
- **value**：key 对应的"内容"，可以是任何对象，包括函数、字典、列表

```python
user = {"name": "Alice", "age": 30}

# key  → value
# "name" → "Alice"
# "age"  → 30

print(user["name"])  # 用 key 取出 value → Alice
```

**读取报错的两种常见情况：**

- `KeyError: 'xxx'` → 字典里没有这个 key
- 类型错 → 比如 list 用 `user.name`（属性语法）而不是 `user["name"]`

### 函数作为一等公民（First-Class Function）

Python 中函数是对象，可以：

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

**关键区分：**

- `greet` → 函数对象（可以传递、存储、但还没执行）
- `greet("Alice")` → 函数**调用**的结果

**应用场景：** Tool Registry 把函数作为 value 存进字典。

### 固定调用 vs 动态调用

**固定调用：** key 写死在代码里。

```python
TOOLS["print"]["func"]()
```

**动态调用：** key 用变量传入。

```python
tool_name = "print"        # 可能是 LLM 决定的，可能是用户决定的
TOOLS[tool_name]["func"]()
```

**为什么需要动态调用？**

- Agent 场景下，"调用哪个工具"是运行时决定的
- 当前由用户（写死的变量）决定；未来由 LLM 决定
- 把 key 变成变量，是 Agent Tool Calling 的关键一步

### Dictionary-based Tool Registry

将工具用 dict 组织，key 是工具名，value 包含元数据和函数本身。

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

动态调用模式：

```python
TOOLS[name]["func"]()
# 等价于
tool_function = TOOLS[name]["func"]  # 取出函数对象
tool_function()                        # 调用它
```

**工程意义：**

- 不需要写 `if/elif` 链
- 加新工具只需往 TOOLS 加一项
- LLM 可以通过名称动态选择

---

## 待补（遇到时再补）

- *args / **kwargs
- 类型注解
- class 与工程化对象设计
- 装饰器
- async / await
- 模块与包
- Pydantic
- 第三方库工程代码
