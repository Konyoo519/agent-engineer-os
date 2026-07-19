# Changelog

记录 Agent Engineer OS 的关键里程碑。

---

## 2026-07-19 / 2026-07-20 — Day 4：错误恢复 + 结构化输出

### 项目

- **08_simple_agent**：完成三件套中的前两件
  - ✓ 结构化输入：Pydantic BaseModel 验证参数 + 嵌套验证
  - ✓ 结构化错误：execute_tool 返回 dict + classify_error 6 类 category
  - ○ 多工具混合调用（剩余）

### 核心交付

- `tools.py` — 大改：新增 `ReadFileArgs` / `PrintArgs` / `TOOL_ARG_MODELS` / `validate_args` / `classify_error`，`execute_tool` 改返回 dict
- `agent.py` — 大改：三层错误拦截（json.loads / Pydantic / execute_tool）+ 系统 prompt 错误处理指引
- `test_all_errors.py` — 新增：5 轮端到端错误恢复测试

### 能力跃迁

| 维度 | Day 3 | Day 4 |
|---|---|---|
| Python Exception | L2 | **L4** |
| Pydantic | 未接触 | **L3-L4** |
| execute_tool | L4-L5 | **L5** |
| 错误恢复设计 | L2 | **L4** |

### 学习风格修订

- 学生反馈：「代码碎片化，跳来跳去看很累」 → 改为「代码块自包含所有上下文」

---

## 2026-07-18 — Day 3 复习日

- 5 个 Part 复习评估完成
- 真实掌握度验证：L3-L5 主体

## 2026-07-16 — Day 3 实战

- 08_simple_agent 真实跑通 DeepSeek API
- Round 1 → Round 2 完整 agent loop 验证
- 解决 3 个意外 bug：utf-8 BOM / sys.path / prompt JSON 不一致

## 2026-07-15 — Day 2

- Python 按需补强
- Tool Calling 全链路打通
- tools_v2.py 独立写出

## 2026-07-14 — Day 1

- 项目启动 + 仓库初始化
- 方向调整：Agent 主线 + Python 按需补强

## 2026-07-03 — 项目初始化

- README / AGENTS.md / 模板搭建
- 主目录结构
