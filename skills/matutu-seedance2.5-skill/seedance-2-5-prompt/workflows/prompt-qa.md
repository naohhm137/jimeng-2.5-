# Prompt QA

最终 Prompt 必须逐模块检查。任何关键模块缺失，标记 `INCOMPLETE`，不假装完整。

## 检查模块

```text
SPEC
PRODUCT
CHARACTER
SCENE
ACTION
CAMERA
LIGHTING
SOUND
DIALOGUE
HUMAN_REALISM
CONTINUITY
NEGATIVE
ENDING
```

每个模块状态：`PASS` / `MISSING` / `WEAK` / `SKIP` / `N/A`。
`HUMAN_REALISM` 只在有角色且人物参与画面时检查；无人物项目标记 `SKIP`，不算缺失。

## Human Realism QA

有角色项目必须运行 `human-realism/realism-qa.md`：

```text
Identity Lock
Reference Coverage
Face / Eye / Skin / Hair / Body / Hand / Clothing Dynamics
Camera Realism
Temporal Consistency
Anti-AI
```

- Identity 是“同一张脸”，Realism 是“动态像真人”，两者缺一不可且不能互相替代。
- 静态胸像加载 gait / foot placement / pelvic motion 时标记 `WEAK`。
- 用 photorealistic / 8K / masterpiece 充当真实感时标记 `WEAK`，改写为可执行动态。
- 人物说话但 Dialogue 专用动态缺失时标记 `MISSING`。
- 多人项目缺少 `INTERACTION LOCK` 时标记 `MISSING`。

## Reference QA and Reference Intelligence Score

有参考素材项目必须按 `reference-intelligence/REFERENCE-ENGINE.md` 的 REFERENCE QA 复核：

```text
Role Accuracy          每个素材一个主 Role，不越界
Feature Extraction     证据可执行、不虚构 MISSING 项
Priority Accuracy      证据优先级与产品/人物意图一致
Conflict Resolution    同一锁定维度冲突已裁决并写 winner
Lock Completeness      derived locks 覆盖全部锁定主体
Prompt Mapping         编译只消费 derived locks / rif_blocks
```

输出 100 分制 `Reference Intelligence Score`：

```text
ROLE ACCURACY          20
FEATURE EXTRACTION     20
PRIORITY ACCURACY      15
CONFLICT RESOLUTION    15
LOCK COMPLETENESS      15
PROMPT MAPPING         15
TOTAL                 100
```

该分数与 Prompt Readiness Score、Pre-Generation Risk Score 独立，只衡量参考智能，不代表实际生成质量。

## Motion Conflict QA

发现以下组合时输出 `SHOT FEASIBILITY WARNING`，回到 `shot-feasibility.md`，不强行生成：

```text
camera 与 character 的运动方向互相矛盾
character 与 environment 的位置关系不成立
hand 与 object 的接触链不完整
body 超出 frame 的可容纳范围
action 无法在给定 duration 内完成
```

## Pre-Generation Risk Score

有角色项目输出 100 分制 Human Realism 生成前风险评估：

```text
IDENTITY              20
EYES                  15
FACIAL DYNAMICS       15
SKIN                  10
HAIR                  10
BODY BIOMECHANICS     15
HANDS                  5
CLOTHING               5
TEMPORAL CONSISTENCY   5
TOTAL                100
```

等级：

```text
90-100  CINEMA REALISM
80-89   COMMERCIAL REALISM
70-79   ACCEPTABLE
60-69   AI ARTIFACT RISK
<60     REGENERATE
```

低于 70 必须回到对应 Human Realism 模块补齐。无角色项目标记 `SKIPPED`。

## Prompt Readiness Score

评分维度：

```text
Clarity
Actionability
Continuity
Product Fidelity
Character Fidelity
Camera Executability
Audio Completeness
Temporal Coherence
```

每项 0-100。

注意：这是 `Prompt Readiness Score`，不是 Seedance 实际生成质量评分，不得混淆。
`Pre-Generation Risk Score` 同样是生成前风险评分，没有真实视频时不能表述为实际画质检测结果。

## 修复规则

- `MISSING`：回到对应 workflow 补齐。
- `WEAK`：改为可执行描述。
- 动作过载：回到 `shot-feasibility.md` 拆镜。
- 光线冲突：回到 `camera.md` 修正。
- 连续性冲突：回到 `continuity.md` 修复。
- Human Realism 症状：读取 `human-realism/repair-routing.md`，定位到对应动态模块做局部修复。
- Human Realism 分数低于 70：回到 `workflows/human-realism.md` 补齐后重新编译。

## 输出

填充 `qa` 字段：`status`、`checks`（含 `HUMAN_REALISM`）、`missing_modules`、`score`、`notes`；Human Realism 分数写入 `human_realism.score`。
