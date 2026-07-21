# ROADMAP

## 学习策略

**Agent 主线 + Python for Agent Engineering 按需补强**

- 沿 AI Agent 工程化主线学习
- 遇到不熟的 Python 语法 / 数据结构 / 设计模式时, 按需插入最小化补强
- 关键代码优先自己敲; 模板 / 工程脚手架由 AI 协助
- 掌握标准: 能回答 "为什么这样写 / 需求变了改哪里 / 报错怎么定位"

---

## Phase 0 —— 环境

- [x] 仓库初始化
- [x] 目录结构
- [x] 核心文档

## Phase 1 —— Python for Agent Engineering

按需补强模式.

已掌握:

- [x] 基础语法 (变量、字符串、循环、if)
- [x] 嵌套 dict / list
- [x] 函数作为对象
- [x] Dictionary-based Tool Registry
- [x] TOOLS[name]["func"]() 调用模式
- [x] parameter / argument 语义区分 (2026-07-15)
- [x] arguments = {...} 作为命名参数字典 (2026-07-15)
- [x] **arguments 字典解包成命名参数 (2026-07-15)
- [x] Pydantic (Day 4 入门 + Day 5 强化, 理论层 L4-L5, 实战待补 Day 6+)

待补 (遇到时再补):

- [ ] *args
- [ ] 类型注解
- [ ] class 与工程化对象设计
- [ ] 装饰器
- [ ] async / await
- [ ] 模块与包
- [ ] Pydantic 自定义验证器

## Phase 2 —— FastAPI

待主线推进.

## Phase 3 —— LLM Fundamentals

- [x] LLM API 调用 (OpenAI 兼容)
- [x] System Prompt 工程基础
- [x] Think → Act → Observe 循环

## Phase 4 —— Agent (当前主线)

当前项目: projects/tutorials/08_simple_agent

进度:

- [x] Tool Registry (字典版)
- [x] 单参数 Tool Calling
- [x] 多参数动态传入 Tool Calling (2026-07-15)
- [x] LLM 工具调用与 Python 工具执行职责区分 (2026-07-15, 纯概念)
- [x] 工具结果结构化 (Pydantic + execute_tool dict) (2026-07-19)
- [x] 错误处理与重试 (三层拦截 + 6 类 category) (2026-07-19)
- [x] Pydantic 强化 (Field 高级 / model_dump / Optional / List 理论层) (2026-07-20, Day 5)
- [x] **多工具混合调用** (2026-07-21, Day 6 完结, 理解不动代码)

## Phase 5 —— MCP

待主线推进.

## Phase 6 —— Multi-Agent

待主线推进.

## Phase 7 —— Production

待主线推进.

---

## Day 5 → Day 6 衔接 (2026-07-21 更新)

**Day 5 完成内容** (全部理论, 未动代码):
- Field 必填/约束 二分本质
- model_dump() 是 "对象 → dict 网关"
- Optional + default 是两件事
- List[X] + None + Field 高级约束理论层
- 新教学规则: 原理 → 字面 → 代码 → 输出 → 预测

**Day 6 完成内容** (全部验证 + 理论, 未动业务代码):
- 多工具混合调用机制 (08_simple_agent 最后 1 件完成)
- 真实运行 read_file → print → read_file → 自然语言答复
- 验证 messages 长度 = 2 + 2N 规律
- 验证 re.search 只匹配第一个 [TOOL:...] 限制
- 能力验收: 画流程图 + 用自己话解释 (L4-L5)

**Day 7+ 主线 (Tutorial 09 准备)**:
- 复杂工具设计 (嵌套 args)
- 多工具并行可能性 (OpenAI 标准 tool_calls 字段, 与 re.search 的对比)
- Pydantic List[str] 实战 (MultiPrintArgs)
- Q6 待补讲: validate_args 返回 (ok, validated) 元组风格对比
