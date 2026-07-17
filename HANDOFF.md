# HANDOFF

## 最近会话: 2026-07-16 (Day 3)

### 主题

**真实跑通 DeepSeek API** — 08_simple_agent 端到端端到端 Agent Loop 第一次真跑通 print + read_file 两个工具。

### 今天 (全天) 已掌握 (经过练习验证)

**上午 (Day 3 上):**
- llm.py 5 个核心问题 (请求时机 / 请求内容 / messages 传入 / 返回结构 / 为什么是 str)
- 4 个用户主动提出的不解 (类型注解 / SDK 调用 / 关键字参数 / 点号链)
- response.choices[0].message.content 4 层剥洋葱
- json.loads 三种输入的合法/非法判定 (实验验证)

**下午 (Day 3 下):**
- 真实跑通 DeepSeek (Phase 2) — 解决了 3 个意外 bug:
  - python312._pth 强制 sys.path 导致 import 失败 -> 写 run_agent.py sys.path.insert
  - openai 没装 -> pip install
  - .env 文件 UTF-8 BOM 导致 key 找不到 -> 重写无 BOM
  - 系统 prompt 示例与 json.loads 要求不一致 -> 改 prompt 要求 JSON 格式
- Phase 3: 调用 print 工具成功 (单轮结束)
- Phase 4: 调用 read_file 工具成功,LLM 自主总结出 tools.py 内容 (验证 messages.append 记忆)
- Phase 5: 观察 Agent Loop 自然完成 (看到了 2 轮循环)
- Phase 6: 能力验证 - 完整 11 步数据流用户能复述

### 真实能力等级 (Day 3 验证后)

L4 (独立写出 + 解释):
- JSON 合法格式判定 (双引号字符串 / 数组 / 对象)
- 正则 (.*?) + match.group(N) 捕获组用法
- ** 字典解包命名参数
- Agent 数据流心智模型 (完整 11 步)
- 字符串/字典/工具对象/函数/返回值的类型轨迹

L3 (能跑,概念清但未压力测试):
- 真实 Agent Loop (看了 2 轮,没 10 轮)
- 环境调试流程 (修过 3 个坑,流程独立但还欠系统)

L2 (有印象,不熟练):
- Python 错误类型术语 (JSONDecodeError / ModuleNotFoundError 见到了,其他类比)
- 正则非贪婪 + 回溯 (用了但不知其所以然)
- Match 对象其他方法 (只用过 group)

### 下一步

**主线 Phase 4 Agent 推进 (08_simple_agent 收尾):**

1. 工具结果结构化 (JSON schema 或 Pydantic,让 LLM 返回结构化数据而不是只能打印字符串)
2. 错误处理与重试 (工具执行失败时怎么告诉 LLM,LLM 怎么重试)
3. 多工具混合 (同一轮里同时用 read_file + print)

下次引入的 Python 知识点 (如果遇到卡点):
- Pydantic (参数 schema 时用到)
- try / except (工具执行报错时)

间隔复习:
- 3 天后再测一次 Debug 4 步流程 (防止退化)

### 今天不展开的选修

- 一个工具多参数 / 不同工具不同参数 / 工具不存在 / 参数缺失 (现在只有 print text + read_file path 两个)
- LLM 概念深入 (暂时从代码驱动学习就够)
- OpenAI SDK 内部细节

### 教学规则 (再确认)

不按"代码行数"作为掌握标准。每段知识必须能回答:
1. 为什么这样写
2. 需求变更时改哪里
3. 报错如何定位

---

## 上一会话: 2026-07-15 (Day 2)

### 学习策略调整

不再以 Python 脚手架开始。
采用 **Agent 主线 + Python for Agent Engineering 按需补强**:

1. 顺 AI Agent 主线推进
2. 遇到不熟的 Python 语法 / 数据结构 / 设计模式时 - 暂停主线
3. 拆成最小示例讲解
4. 给我小练习自己完成
5. Review 后回到主线
6. 关键代码优先自己抄

## 当前阶段

**Phase 4 - Agent (主线)**

**活跃项目:** projects/tutorials/08_simple_agent

已完成:
- [x] LLM API 调用 (Day 3 校准: L3-L4)
- [x] System Prompt 工程基础 (Day 3 升级: L4,亲自修过 prompt 的 JSON bug)
- [x] Tool Registry (字典式)
- [x] 单参数 Tool Calling
- [x] 多参数动态传入 Tool Calling (2026-07-15)
- [x] **kwargs 基础用法 (2026-07-15)
- [x] LLM 与 Python 工具执行职责分工 (2026-07-15,纯概念)
- [x] execute_tool(name, arguments) 升级 (2026-07-15)
- [x] agent.py 解析 LLM JSON 输出 + json.loads (2026-07-15)
- [x] 静态测试 test_pipeline.py 跑通端到端解析链路 (2026-07-15)
- [x] Agent Loop 与 messages.append 的"记忆"作用 (Day 3 升级: L4, 真实看到 2 轮效果)
- [x] **端到端跑通真实 DeepSeek API** (2026-07-16,Day 3 主要成就)
- [x] 调用 print 工具成功 (2026-07-16)
- [x] 调用 read_file 工具成功, LLM 自主总结文件内容 (2026-07-16)

## 已掌握的 Python 知识

- 基础语法
- 嵌套 dict / list
- 函数作为对象 ("func" 作为 value 存进 dict)
- Dictionary-based Tool Registry
- TOOLS[name]["func"]() 调用模式
- parameter / argument 区分 (2026-07-15)
- *arguments = {...} 作为命名参数字典 (2026-07-15)
- **arguments 字典解包成命名参数 (2026-07-15)
- print(...) 的"先取值再打印"机制 (2026-07-15)
- 类型注解 : str 和 -> str (2026-07-15)
- list.append(item) 列表末尾添加 (2026-07-15)
- json.loads(s) 字符串 -> dict (2026-07-15)
- set vs dict 的字面量区分: {a, b} vs {key: value} (2026-07-15)
- **(Day 3 新增)** f-string 占位符 {} 必须有 f 前缀才生效
- **(Day 3 新增)** 正则 (.*?) 配合 match.group(N) 拿捕获组
- **(Day 3 新增)** Match 对象 truthy/falsy 特性 (None 为 falsy)
- **(Day 3 新增)** Python SDK 调用模式 (client.method().sub_method().create(...))
- **(Day 3 新增)** JSON 合法格式判定 (双引号字符串必须是 "...")

## 当前活跃文件

- projects/tutorials/08_simple_agent/agent.py — Agent 循环 + LLM JSON 解析 + JSON-格式 prompt
- projects/tutorials/08_simple_agent/tools.py — Tool Registry + 升级后的 execute_tool
- projects/tutorials/08_simple_agent/llm.py — DeepSeek 封装 (OpenAI 兼容 API)
- projects/tutorials/08_simple_agent/config.py — env 配置 (修复了 BOM 问题)
- projects/tutorials/08_simple_agent/run_agent.py — **(Day 3 新增)** sys.path 注入的启动器
- projects/tutorials/08_simple_agent/json_test.py — **(Day 3 新增)** JSON 解析实验

## 教学规则 (再确认)

不按"代码行数"作为掌握标准。
每个知识点必须能回答:
1. 为什么这样写
2. 需求变更时改哪里
3. 报错如何定位

---

## 最新会话: 2026-07-18 (Day 3 复习日)

### 主题

**Day 3 全面复习** — 不学新知识,验证 Day 3 真实掌握程度。

### 5 个 Part 的复习结果

**Part 1 知识回顾**: 5 个概念用自己的话解释。整体方向对,Q3/Q4 需要追问才答到点。

**Part 2 代码阅读**: 逐文件回答"为什么存在 / 删了会怎样 / 在流程哪一步"。T3 try-except 原理只到结论级(明白结论,未懂原理)。

**Part 3 Debug 复盘**: 6 道典型报错诊断。JSONDecodeError 方向对根因修一半 / ModuleNotFoundError 答不出 / KeyError 答不出(我点破字典大小写) / TypeError 答对 try-except 让 LLM 重试 / 哑错误(env / BOM)答不出。

**Part 4 数据流默写**: 11 步顺序全对,但漏了"正则提取"独立一步 + 把 append 目的说成"防止 system_prompt 丢失"(实际是给 LLM 看完整对话历史)。修正后通过。

**Part 5 综合练习**: 判断题 3/3 / 填空题 3/4 / 预测题漏 [OUT] / 代码修改对 / Debug 方向对一半 / 应用题漏写工具函数本身。

### 8 级能力评估

| 维度 | 等级 | 理由 |
|---|---|---|
| Agent Loop | L5 解释原理 | 11 步数据流能完整默写,边界条件清晰 |
| Tool Calling | L4 独立写出 | 理解 str→dict→函数调用全链 |
| execute_tool | L4-L5 之间 | 动态性懂,字段语义模糊 |
| JSON | L5 解释原理 | 能区分 str vs dict 本质差异 |
| Debug | L3-L4 | 能定位报错行,哑错误意识有 |
| Git 工作流 | 未评估 | 今天未涉及 |

### 今日真正掌握

1. 数据流 11 步完整闭环
2. 字典注册模式的动态性(加工具不改 execute_tool)
3. append 顺序的语义(assistant 决策 + user 工具结果)
4. 错误处理方向(LLM 输出不稳定 → try/except 让 LLM 重试)
5. 哑错误意识(env 静默返回 None / BOM 导致 key 找不到)

### 薄弱点

1. try/except 原理只到结论级(明日补 Python 异常基础)
2. openai SDK 内部细节完全黑盒(Choice / Message 类型)
3. Python 错误类型语义不熟
4. lambda / 装饰器 / 闭包等高阶函数空白

### 明日路径建议

可以进入 Pydantic / 结构化输出,但建议先补 try/except 基础(30 min)。

主线 Phase 4 还有 3 项没收尾:
1. 工具结果结构化(Pydantic / JSON schema)
2. 错误处理与重试(try/except)
3. 多工具混合调用

不建议直接上 LangGraph / MCP。
