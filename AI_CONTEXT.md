# AI Context

> 这是 ChatGPT、Codex 与未来其他 AI 工具之间的 **跨 AI 上下文快照**。
> 不是完整历史记录, 也不是唯一事实来源。
> 完整事实仍然分布在: README / ROADMAP / PROJECT_STATE / HANDOFF / docs/knowledge/ / docs/daily/ / projects/
> 本文件只负责让一个新 AI 对话 **只读这一份文件** 就能快速恢复当前学习状态。

最后更新: **2026-07-16 晚 (Day 3 全天: 真实 DeepSeek API 跑通)**

---

## 1. Project

- 项目名称: **Agent Engineer OS**
- 项目目标: 120 天内成为合格的 AI Agent Engineer
- 仓库状态: Active Development
- 当前 Sprint: Sprint 4 (Agent) — tutorial 08_simple_agent
- 当前 Day: Day 3
- **当前日期: 2026-07-16**

## 2. 当前状态快照

### 主线进度
- **Phase 4 Agent 主线 — 端到端跑通了** 
  - 08_simple_agent 现在能真与 DeepSeek 通信, 调用 print + read_file 两个工具均成功
  - Round 1 -> Round 2 完整 agent loop 验证成功
  - Day 3 解决了 3 个不期而遇的 bug (见 HANDOFF)
  
### 真实能力等级 (Day 3 校准)
- **L4** (独立写出 + 解释): JSON 合法格式判定 / 正则捕获组 / ** 解包 / Agent 11 步数据流 / 字符串-字典-函数-返回值的类型轨迹
- **L3** (能跑 + 概念清): 真实 Agent Loop / DeepSeek v4-pro 模型 / 环境调试流程
- **L2** (有印象, 不熟练): Python 错误类型术语 / 正则非贪婪 / Match 对象其他方法

### 用户当前学习最大薄弱点
1. **Python 错误类型术语** (TypeError / KeyError / ValueError / JSONDecodeError - 见过但分类不熟)
2. **正则语法细节** (\w \d \s 字符类 + 贪婪/非贪婪 + 回溯)
3. **SDK 内部细节** (只用过 chat.completions.create, 其他方法不知道)

## 3. 下一步 (基于 Day 3 真实测试)

**主线 Phase 4 Agent 收尾:**

1. 工具结果结构化 (Pydantic / JSON schema, 让 LLM 返回结构化数据, 不是只打印字符串)
2. 错误处理与重试 (execute_tool 加 try/except, 工具错误作为 user 消息反馈给 LLM 让其重试)
3. 多工具混合 (同一轮里同时调 print + read_file)

之后按需引入的 Python 知识点:
- Pydantic (结构化输出)
- try / except (工具错误反馈)

间隔复习:
- 3 天后 (2026-07-19) 再测一次 Debug 4 步流程 (防止退化)

---

## 当前活跃文件 (Day 3 状态)

- projects/tutorials/08_simple_agent/
  - agent.py — Agent 循环 + JSON prompt
  - tools.py — Tool Registry + execute_tool
  - llm.py — DeepSeek 封装
  - config.py — env 加载
  - .env — **(Day 3 修复)** 移除 UTF-8 BOM, base_url = https://api.deepseek.com, model = deepseek-v4-pro
  - **run_agent.py** — **(Day 3 新增)** sys.path 注入启动器
  - **json_test.py** — **(Day 3 新增)** JSON 解析实验
  - tools_v2.py — (Day 2 晚) 独立写的测试工具集
  - bug_test.py — (Day 2 晚) debug 训练场

## 4. 教学原则 (已确认)

不按"代码行数"作为掌握标准。
每个知识点必须能回答:
1. 为什么这样写
2. 需求变更时改哪里
3. 报错如何定位

Agent 主线 + Python for Agent 按需补强 — 这是 Day 1 调整后的策略, **保持有效**, 不回退。

## 5. 状态

**主线** Phase 4 - Agent 真跑通, Phase 4 还剩 3 项收尾任务 (结构化输出 / 错误重试 / 多工具混合) 才能算 08_simple_agent 完成。

**辅线** Python 按需补强, 核心已通, 后续只需针对性补强 (正则 + 错误类型术语 + Pydantic 按需 + try/except 按需)。

## 6. 避免重开

不要重新讲这些已掌握内容:
- Tool Registry 设计
- 动态 Tool Calling
- execute_tool(name, arguments) 4 步
- ** arguments 解包
- JSON.loads(str) -> dict
- f-string 基础用法
- 正则 (.*?) 与 match.group(N)
- Match 对象 None 判定

如果发现新的理解错误, **针对具体问题补充**, 不要整体复习。