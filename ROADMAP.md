# ROADMAP

## 学习策略

**Agent 主线 + Python for Agent Engineering 按需补强**

- 沿 AI Agent 工程化主线学习
- 遇到不熟的 Python 语法 / 数据结构 / 设计模式时,按需插入最小化补强
- 关键代码优先自己敲;模板 / 工程脚手架由 AI 协助
- 掌握标准:能回答"为什么这样写 / 需求变了改哪里 / 报错怎么定位"

---

## Phase 0 — 环境

- [x] 仓库初始化
- [x] 目录结构
- [x] 核心文档(README / AGENTS / ROADMAP / PROJECT_STATE / HANDOFF)

## Phase 1 — Python for Agent Engineering

按需补强模式。

已掌握:

- [x] 基础语法(变量、字符串、循环、if)
- [x] 嵌套 dict / list
- [x] 函数作为对象
- [x] Dictionary-based Tool Registry
- [x] TOOLS[name]["func"]() 调用模式
- [x] parameter / argument 语义区分(2026-07-15)
- [x] rguments = {...} 作为命名参数字典(2026-07-15)
- [x] **arguments 字典解包成命名参数(2026-07-15)

待补(遇到时再补):

- [ ] *args(列表解包成位置参数)
- [ ] 类型注解
- [ ] class 与工程化对象设计
- [ ] 装饰器
- [ ] async / await
- [ ] 模块与包
- [ ] Pydantic
- [ ] 第三方库工程代码

## Phase 2 — FastAPI

待主线推进。

## Phase 3 — LLM Fundamentals

- [x] LLM API 调用(OpenAI 兼容)
- [x] System Prompt 工程基础
- [x] Think → Act → Observe 循环

## Phase 4 — Agent(当前主线)

当前项目:projects/tutorials/08_simple_agent

进度:

- [x] Tool Registry(字典版)
- [x] 单参数 Tool Calling
- [x] 多参数动态传入 Tool Calling(2026-07-15)
- [x] LLM 工具调用与 Python 工具执行职责区分(2026-07-15,纯概念)
- [ ] 工具结果结构化 → **当前下一步**
- [ ] 错误处理与重试
- [ ] 多工具混合

## Phase 5 — MCP

待主线推进。

## Phase 6 — Multi-Agent

待主线推进。

## Phase 7 — Production

待主线推进。