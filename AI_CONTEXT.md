# AI Context

> 这是 ChatGPT、Codex 与未来其他 AI 工具之间的**跨 AI 上下文快照**。
> 不是完整历史记录,也不是唯一事实来源。
> 完整事实仍然分布在:README / ROADMAP / PROJECT_STATE / HANDOFF / docs/knowledge/ / docs/daily/ / projects/
> 本文件只负责让一个新 AI 对话**只读这一份文件**就能快速恢复当前学习状态。

最后更新:2026-07-15 晚(Day 2 全天 + 综合复习)

---

## 1. Project

- 项目名称:**Agent Engineer OS**
- 项目目标:120 天内成为合格的 AI Agent Engineer
- 仓库状态:Active Development
- 当前 Sprint:Sprint 4(Agent)— tutorial 08_simple_agent
- 当前 Day:Day 2(Agent 主线 + 晚间综合复习)
- **当前日期:2026-07-15**

## 2. 当前主线进展(Phase 4 - Agent)

最近进展(2026-07-15):

### 上午 / 下午(已通过测试)
- [x] Tool Registry(字典版)
- [x] 单参数 Tool Calling
- [x] 多参数动态传入 Tool Calling
- [x] **kwargs 字典解包基础
- [x] LLM 与 Python 工具执行职责分工(纯概念)
- [x] execute_tool 升级为 (name, arguments: dict) + **arguments 解包
- [x] agent.py 用 json.loads 解析 LLM JSON 输出
- [x] 静态测试 test_pipeline.py 跑通端到端解析链路
- [x] Agent Loop 中 messages.append 的"记忆"作用(纯概念,真实未跑通)
- [x] **Debug 完整 4 步流程**(2026-07-15 晚 — 真实跑报错 + 推断 + 修复 + 解释)
- [x] **独立写出 tools_v2.py**(2026-07-15 晚 — 3 工具 + execute_tool + 测试通过)
- [x] **Agent 全链路心智模型**(2026-07-15 晚 — 完整串讲)
- [x] **正则基础**(2026-07-15 晚 — 运行级理解,语法细节 L3)
- [ ] **跑真实 DeepSeek API 端到端** → **当前下一步**
- [ ] 工具结果结构化
- [ ] 错误处理与重试
- [ ] 多工具混合

辅助进展(Phase 1 - Python):
- [x] **kwargs 字典解包基础
- [x] 类型注解(基础:`text: str`、`-> str`)
- [x] list.append(item)
- [x] json.loads(s)(字符串 → dict)
- [ ] *args(按需)
- [ ] Pydantic(工具结构化时再补)
- [ ] try / except(工具报错时再补)
- [x] **正则基础(运行级理解,L3)**(2026-07-15 晚新增)

## 3. 真实能力等级(经测试验证,2026-07-15 晚重新校准)

### 已真正掌握(L4 = 测试验证)
- Tool Registry 设计模式 + 嵌套字典 + 动态函数调用
- **arguments 解包成命名参数(独立写出 + 解释)
- Agent 全链路心智模型(完整串讲)
- 独立 debug 流程(跑代码 → 读报错 → 推断 → 修复 → 解释)
- 独立写出 tools_v2.py(测试通过)

### 基本理解但不稳定(L3)
- 正则 `+` `*` `?` 区别(能跟着实验得出,无法复述)
- 贪婪 vs 非贪婪(能跑对比,不懂机制)
- 字面字符 vs 转义字符(懂 `\[` `\]` 概念,但最初说不出 `TOOL:` 是字面字符)
- 整体匹配 + 回溯(概念懂,具体回溯机制不熟)

### 明显薄弱点(L1-L2)
- **Python 错误类型术语**(TypeError / KeyError / ValueError)— 不知道是什么
- **正则基础语法**(每天在用但说不出符号含义)
- **主动读报错** — 倾向直接给答案
- **LLM 概念** — 用户自己承认"没详细学"

### 尚未接触(L0)
- async/await、class、装饰器、Pydantic、try/except、*args、第三方框架

### 工程化(L4)
- Git commit / push / GitHub
- AI_CONTEXT / HANDOFF / PROJECT_STATE / ROADMAP 维护
- 跨 AI 上下文管理(ChatGPT ↔ Codex)

## 4. 最近一次会话:2026-07-15(Day 2 全天 + 晚间复习)

### 上午主题
从 `TOOLS[name]["func"]()` 推进到 `TOOLS[name]["func"](**arguments)`,6 阶段跑通。

### 下午主题
把上午学的内容接入 08_simple_agent 真实项目,完成"LLM 决策 → Python 工具执行"的端到端链路。

### 晚间主题(2026-07-15)
全阶段综合复习与能力诊断。测试方法:主动回忆 + 代码预测 + 独立编程 + Debug 全流程。

**核心成果**:
- 暴露 [x] 标记的虚高,真实等级重新校准
- Debug 能力 L4 验证通过
- 独立写出 tools_v2.py
- Agent 心智模型 L4
- 正则基础 L3(运行级)

**关键发现**:仓库里大量 `[x]` 标记是"能跑通"标记,不是"真正理解"标记。LLM 概念 / Tool Calling 概念其实是薄弱点。

### 关键洞察

- LLM 自己**看不到**工具返回结果,所以 Agent Loop 用 `messages.append(...)` 把工具结果"喂回"下一轮 messages,这就是"记忆"
- 删除 messages.append 两行,LLM 会无限循环重复调用同一工具
- 用户坦诚承认"LLM 没详细学,Tool Calling 不太理解" → 启发了复习重新校准

## 5. 下次起点

主线 Phase 4 Agent 下一步:

1. `cd projects/tutorials/08_simple_agent; python agent.py` 跑真实 DeepSeek API,完成端到端
2. 调试 `print` 工具至少一次
3. 调试 `read_file` 工具至少一次
4. 端到端跑通一个 user goal

之后引入的 Python 知识点(如果主线遇到卡点):

- Pydantic 模型(用于参数 schema 时会用到)
- 异常处理 try / except(用于工具执行报错时)
- 正则 `\w` `\d` `\s` 等字符类深入(本次复习未深入)

## 6. 详细维护规则

见 `AGENTS.md` 的 "AI Context Synchronization" 章节。

## 7. 状态一致性

本文件与以下文件保持同步(最近一次核对:2026-07-15 晚):

- ROADMAP.md(Phase 4 当前步:端到端真实 LLM)
- PROJECT_STATE.md(Sprint 4 / Day 2 / 当前下一步:跑真实 DeepSeek API)
- HANDOFF.md(下一步:python agent.py 跑真实 LLM)
- docs/daily/2026-07-15.md(白天下午 + 晚间复习记录)
- docs/knowledge/python.md(新增正则基础章节)

---

## 8. 重要注意事项(2026-07-15 复习发现)

**不要假设用户已经掌握**:
- LLM API 详细概念(用户承认未深入)
- 正则语法细节(运行级 L3,细节不足)
- Python 错误类型术语

**应该直接假设用户已经掌握**:
- Tool Registry 设计模式(独立写出验证)
- 动态函数调用 `TOOLS[name]["func"](**arguments)`
- Agent 全链路心智模型

如果新 AI 接手本仓库,**请优先**:
1. 读本 AI_CONTEXT.md
2. 读 docs/daily/2026-07-15.md
3. 读 PROJECT_STATE.md
4. 再开始教学
