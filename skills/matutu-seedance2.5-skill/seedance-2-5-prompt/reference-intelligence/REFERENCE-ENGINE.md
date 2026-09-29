# Reference Intelligence Engine（V3 核心）

本目录是 V3 的核心升级：把“识别参考素材”升级为“自动理解参考素材 → 判断素材职责 → 提取视觉信息 → 建立优先级 → 解决多素材冲突 → 生成 Lock → 交给 Prompt Compiler”。

Reference Intelligence Engine 不直接生成最终 Prompt。它先输出 `REFERENCE SPEC`，再由后续管线消费。

## 核心原则

```text
Reference ≠ Prompt Description
Reference 是外观证据，不是一句漂亮的画面描述。

Reference
→ Role
→ Information Extraction
→ Priority
→ Lock
→ Conflict Resolution
→ Prompt Compilation
```

## 与 V1/V2 的关系

- V1 13 步输入兼容能力保留。
- V2 24 步 Human Realism / Product Lock / Identity Lock / Continuity / Sound / QA / Risk Score 全部保留。
- V3 只做 ADD / EXTEND / ROUTE / REFACTOR。V3 不删除旧模块，不改写旧语义。
- V2 的 `reference_analysis` 是角色与覆盖度层；V3 RIE 在其之前执行并产出结构化 `REFERENCE SPEC`，二者通过 asset_id 关联。

## 主流程

```text
INPUT DETECTION
↓
INPUT NORMALIZATION
↓
REFERENCE ROLE CLASSIFICATION
↓
REFERENCE ELEMENT EXTRACTION
↓
REFERENCE PRIORITY
↓
REFERENCE CONFLICT RESOLUTION
↓
REFERENCE SPEC
↓
PRODUCT / SUBJECT ANALYSIS
↓
CHARACTER IDENTITY LOCK
↓
HUMAN REALISM ROUTING
↓
... 后续 V2 步骤保持
↓
PROMPT COMPILER
```

## 阶段任务

```text
Phase 1  Reference Intelligence Core      本目录
Phase 2  Role + Extraction                reference-role.md / *-extraction.md
Phase 3  Priority + Conflict Resolution   reference-priority.md / reference-conflict-resolution.md
Phase 4  Lock System Integration          REFERENCE SPEC 中写入 derived locks
Phase 5  Human Realism Integration        人物路由只传 Identity Lock 与最小动态需求
Phase 6  Prompt Compiler Integration      编译器只消费 REFERENCE SPEC
Phase 7  Schema + Templates               schemas/reference-*.schema.json + templates/reference-*.md
Phase 8  Tests + Fixtures                 tests/fixtures/reference-*/
Phase 9  Documentation                    SKILL.md / QUICK-START.md / README.md / main-pipeline.md
Phase 10 Full Regression QA               tests/run_tests.py
```

## 文件路由

```text
人物参考图 -> reference-image-analysis.md + character-extraction.md
产品参考图 -> reference-image-analysis.md + product-extraction.md
场景参考图 -> reference-image-analysis.md + scene-extraction.md
摄影/构图参考 -> reference-image-analysis.md + composition-extraction.md + camera-extraction.md + lighting-extraction.md
动作参考视频 -> reference-video-analysis.md + motion-extraction.md + camera-extraction.md
混合参考素材 -> 先逐个分类，再统一做 Priority + Conflict Resolution
```

## REFERENCE SPEC 契约

RIE 的最终产物是 `REFERENCE SPEC`，包含：

```text
reference_summary     每个素材一句话职责结论
references            reference_id / role / secondary_roles / priority / confidence / lock_level
extracted_features    按素材类型提取的可继承视觉信息
conflicts             冲突对、胜负、原因、动作
derived_locks         由证据直接推导的 character/product/scene/camera/motion lock 需求
reference_qa          本模块 QA 结论
reference_score       Reference Intelligence Score
rif_blocks            按 RIF 动态路由生成的规格块，供 Prompt Compiler 消费
```

`REFERENCE SPEC` 不是最终 Prompt，不允许把提取结果直接堆成画面描述。提取结果必须经过 Lock 与 Compiler 的职责转换。

## 输出模式

三种输出模式都保留，且都先完成 `REFERENCE SPEC`：

```text
MODE A  ONE-SHOT          REFERENCE SUMMARY + LOCKS + FINAL PROMPT
MODE B  SHOT-BY-SHOT      每个 SHOT 自带 Reference Role / Identity / Action / Camera / Motion / Human Realism
MODE C  DIRECTOR PACKAGE  REFERENCE MAP + 全部 LOCKS + STORYBOARD + HUMAN REALISM PLAN + FINAL PROMPTS + QA + RISK SCORE
```

## REFERENCE QA

RIE 完成后逐项检查，任一关键项不通过就标记 `INCOMPLETE` 或 `REPAIR`：

```text
[ ] 每个素材都有 Role
[ ] Role 有 confidence
[ ] 关键素材有 priority
[ ] 人物项目有 Identity Lock
[ ] 产品项目有 Product Lock
[ ] 多素材项目完成 conflict detection
[ ] Camera Reference 没有误当成 Subject Reference
[ ] Style Reference 没有覆盖 Identity Lock
[ ] Motion Reference 没有误修改人物 Identity
[ ] Human Realism 没有修改人物身份
[ ] Product 默认没有发生设计变更
```

## Reference Intelligence Score

100 分制，只衡量参考智能层：

```text
Role Accuracy       20
Feature Extraction  20
Priority Accuracy   15
Conflict Resolution 15
Lock Completeness   15
Prompt Mapping      15
TOTAL              100
```

该分数与 `Prompt Readiness Score`、`PRE-GENERATION RISK SCORE` 独立，三者不互相混淆，也不能代替真实生成视频质量评分。

## 禁止

- 不把参考素材描述当作创作方案：只能继承可见事实。
- 不让一张参考图同时承担互相冲突的职责；无法拆分时降低 confidence 并标记。
- 不把 Camera / Lighting / Style 素材当成 Subject 素材，锁会因此错误。
- 不让 Motion Reference 修改人物身份，不让 Style Reference 覆盖 Identity Lock。
- 不让 Human Realism 修改人物身份。
- 产品默认 `PRODUCT_TRANSFORMATION_ALLOWED = false`，不得由模型擅自改设计。
