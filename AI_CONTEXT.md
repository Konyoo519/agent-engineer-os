# AI Context

> 这是 ChatGPT、Codex 与未来其他 AI 工具之间的**跨 AI 上下文快照**。
> 不是完整历史记录,也不是唯一事实来源。
> 完整事实依然分布在: README / ROADMAP / PROJECT_STATE / HANDOFF / docs/knowledge/ / docs/daily/ / projects/
> 本文件只负责让一个新 AI 对话**只读这一份文件**就能快速恢复当前学习状态。
最后更新: **2026-07-20 (Day 4 完结 + 晚间 Q&A)**

---

## 1. Project

- 项目名称: **Agent Engineer OS**
- 项目目标: 120 天内成为合格的 AI Agent Engineer
- 仓库状态: Active Development
- 当前 Sprint: Sprint 4 (Agent) — tutorial 08_simple_agent
- 当前 Day: Day 4

## 2. 当前状态快照

### 主线进度
- **Phase 4 Agent — 三件套前两件完成** ✓✓○
  - ✓ 结构化输入 (Pydantic 验证参数 + 嵌套 BaseModel)
  - ✓ 结构化错误 (execute_tool 返回 dict + classify_error 查表)
  - ○ 多工具混合调用(剩余)

### 三层错误拦截设计(已完成)

```
LLM 输出 JSON 字符串
    ↓
json.loads()           ← 拦截层 1: JSON 解析错
    ↓
Pydantic BaseModel     ← 拦截层 2: 字段类型/缺字段错
    ↓
execute_tool()         ← 拦截层 3: 业务错(文件不存在)
    ↓
classify_error()       ← 把异常归类到 6 类 LLM 友好 category
```

### 6 类错误 category(用户设计)

`bad_args / not_found / wrong_type / timeout / unknown_tool / unknown_error`

### 真实能力等级 (Day 4 验证)

**L5 解释原理**:
- Agent Loop 11 步数据流(能默写 + 边界条件)
- try/except 完整机制 + 异常家族 + traceback 读法
- raise 复用 except 分支(代码整洁技巧)
- `**` 解包在函数调用和 BaseModel 实例化的复用

**L4 独立写出 + 解释**:
- dict 查表 (classify_error / TOOL_ARG_MODELS / TOOLS)
- BaseModel + 嵌套 + 字段路径错误
- 三层错误拦截设计

**L3 能跑 + 概念清楚**:
- Pydantic 在 Agent 里的应用(model_dump() 还需深化)
- 端到端 5 轮错误恢复(missing.txt + 错参数 + 空 JSON 都验证)

**L2 有印象 + 不熟细节**:
- Pydantic 高级特性(默认值 / Optional / List / Field)
- 多轮错误恢复的 token 成本
- 错误分类的边界 case(PermissionError / OSError)

### 用户当前学习最大薄弱点 (2026-07-19 复习 + 晚间 Q&A 确认)

**已通过 Q&A 解决**:
- 类 / 实例 / __init__ / self 的本质 (L4 标志: 学生自己推出 a 不是 str → 必须 model_dump())
- BaseModel 实例的 type() 与 dict 的区别
- json.loads vs model_dump 各自的应用场景
- TOOLS vs TOOL_ARG_MODELS 双字典分工

**仍然薄弱** (Day 5 优先补):
- 错误分类枚举的边界 case (PermissionError / OSError)
- Pydantic 高级特性 (Field 默认值 / Optional / List)
- 多轮错误恢复的 token 成本意识

**待补到 Day 5 单讲**:
- Q6 `validate_args` 返回 `(ok, validated)` 元组的设计哲学 — 「返回值 vs 异常表达」两种错误处理风格对比

1. **Pydantic 应用级 API** — model_dump() / Field 约束 / Optional 还没用过
2. **错误分类枚举完整性** — 6 类够不够?边界 case 未覆盖
3. **多工具混合调用** — 同一轮调多个工具的并发/顺序未涉及

## 3. 下一步 (基于 Day 4)

08_simple_agent 主线还差最后 1 件:**多工具混合调用**。

候选路径:
- **A. 多工具混合** — 同一轮连续调 print + read_file,验证 messages 顺序
- **B. 进入 09 项目** — 学完 08,开始多 turn / multi-agent 主题
- **C. 复习日** — 今天信息量大(2 Part 大改造 + Pydantic),固化一下

推荐 **C(短复习) → A(半天) → B(进入新主题)**,拉开节奏。

间隔复习:
- 3 天后 (2026-07-22) 再测 Day 4 内容(异常机制 + Pydantic 基础 + 三层拦截设计)

---

## 当前活跃文件 (2026-07-19)

- projects/tutorials/08_simple_agent/
  - agent.py — Agent 循环 + 三层错误拦截 + Pydantic 集成(已大改)
  - tools.py — tools + classify_error + TOOL_ARG_MODELS + ReadFileArgs/PrintArgs(已大改)
  - llm.py — DeepSeek 封装 OK(不动)
  - config.py — env 加载 OK(不动)
  - run_agent.py — sys.path 注入(不动)
  - test_all_errors.py — 5 轮错误恢复端到端测试(可重复运行)
  - bug_test.py / json_test.py / tools_v2.py — Day 2 训练场(不动)
- docs/daily/2026-07-19.md — **(Day 4) 新增** 4 Part 学习记录
- docs/daily/2026-07-18.md — Day 3 复习

## 4. 教学原则 (已确认)

不按"代码行数"作为掌握标准。每个知识点必须能回答:
1. 为什么不这样写
2. 需求变了改哪里
3. 报错如何定位

Agent 主线 + Python for Agent 按需补强 — 这是 Day 1 调整后的策略, **保持有效**, 不回退。

## 5. 状态

**主线** Phase 4 - 08_simple_agent 三件套 2/3 完成,剩多工具混合。
**Python 按需** Exception 基础已补, Pydantic 入门完成。
**薄弱** Pydantic 高级 API + 错误分类完整度 + 多工具并发。

## 6. 避免重讲

不要重讲这些已掌握内容:
- Tool Registry 设计
- 动态 Tool Calling + execute_tool
- **arguments 解包
- JSON.loads(str) -> dict
- f-string / 正则 / match.group / Match None / 字典 key 大小写
- Agent Loop 11 步
- messages.append 顺序语义
- try/except + raise + traceback + 异常家族(已 Day 4 确认)

如果发现新的理解错误, **针对具体问题补充**, 不要整体复习。


