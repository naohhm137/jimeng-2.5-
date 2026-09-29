# Main Pipeline

本文件是 Seedance 2.5 Commercial Video Director + Reference Intelligence Engine + Human Realism Engine + Prompt Compiler 的主编排流程。所有任务都从这里进入，按需读取子工作流。

## V3 说明

V3 在 V2 24 步基础上插入 Reference Intelligence Engine（RIE）步骤 03-06；原有 V2 24 步流程、V1 13 步兼容路由与三种输出模式全部保留。V3 不删除旧模块，只扩展参考素材理解层。

V3 步骤 03-06 输出 `REFERENCE SPEC`，后续步骤消费该规格而不是直接堆参考图描述：

```text
V2 03 REFERENCE ANALYSIS           = V3 03-06 + REFERENCE SPEC
V2 04 PRODUCT / SUBJECT ANALYSIS   = V3 07（消费 reference-derived product evidence）
V2 05 CHARACTER IDENTITY LOCK      = V3 08（消费 derived character lock）
V2 06 HUMAN REALISM ROUTING        = V3 09（先有 Identity Lock，再路由 Realism）
V2 07 HUMAN MOTION ENGINE          = V3 10（消费 motion evidence / lock）
```

RIE 的完整知识模块在 `reference-intelligence/`：核心见 `REFERENCE-ENGINE.md`，角色系统见 `reference-role.md`，优先级与冲突见 `reference-priority.md`、`reference-conflict-resolution.md`。

## V3 标准流程

```text
01 INPUT DETECTION
02 INPUT NORMALIZATION
03 REFERENCE ROLE CLASSIFICATION
04 REFERENCE ELEMENT EXTRACTION
05 REFERENCE PRIORITY
06 REFERENCE CONFLICT RESOLUTION
07 PRODUCT / SUBJECT ANALYSIS
08 CHARACTER IDENTITY LOCK
09 HUMAN REALISM ROUTING
10 HUMAN MOTION ENGINE
11 VIDEO OBJECTIVE
12 CREATIVE STRUCTURE
13 HOOK DESIGN
14 STORYBOARD
15 SHOT DISTANCE ROUTING
16 SHOT FEASIBILITY
17 SHOT HUMAN REALISM COMPILE
18 CAMERA LANGUAGE
19 TEMPORAL CONSISTENCY
20 CONTINUITY LOCK
21 SOUND DESIGN
22 SEEDANCE COMPILER
23 HUMAN REALISM QA
24 PROMPT READINESS QA
25 PRE-GENERATION RISK SCORE
26 REFERENCE QA
27 REPAIR ROUTING
28 FINAL OUTPUT
```

## V2 24 步标准流程

```text
01 INPUT DETECTION
02 INPUT NORMALIZATION
03 REFERENCE ANALYSIS
04 PRODUCT / SUBJECT ANALYSIS
05 CHARACTER IDENTITY LOCK
06 HUMAN REALISM ROUTING
07 HUMAN MOTION ENGINE
08 VIDEO OBJECTIVE
09 CREATIVE STRUCTURE
10 HOOK DESIGN
11 STORYBOARD
12 SHOT DISTANCE ROUTING
13 SHOT FEASIBILITY
14 SHOT HUMAN REALISM COMPILE
15 CAMERA LANGUAGE
16 TEMPORAL CONSISTENCY
17 CONTINUITY LOCK
18 SOUND DESIGN
19 SEEDANCE COMPILER
20 HUMAN REALISM QA
21 PROMPT READINESS QA
22 PRE-GENERATION RISK SCORE
23 REPAIR ROUTING
24 FINAL OUTPUT
```

## V1 13 步兼容路由

V1 输入与旧 13 步流程继续可用；旧输入没有 `human_realism` 字段时按 AUTO 处理：有清晰人物则自动进入 Human Realism Engine，无人物则显式 SKIP。

```text
V1 01 INPUT DETECTION      -> V2 01
V1 02 INPUT NORMALIZATION  -> V2 02
V1 03 PRODUCT / SUBJECT    -> V2 04 + 05
V1 04 VIDEO OBJECTIVE      -> V2 08
V1 05 CREATIVE STRUCTURE   -> V2 09
V1 06 HOOK DESIGN          -> V2 10
V1 07 STORYBOARD           -> V2 11 + 12
V1 08 SHOT FEASIBILITY     -> V2 13
V1 09 CONTINUITY LOCK      -> V2 16 + 17
V1 10 SOUND DESIGN         -> V2 18
V1 11 SEEDANCE COMPILER    -> V2 19
V1 12 PROMPT QA            -> V2 20 + 21 + 22
V1 13 FINAL OUTPUT         -> V2 23 + 24
```

V2 流程与 V3 流程都可用于输入；V3 是可升级入口，V2 编号保留给老用户、外部接线与旧回归结果。进入 V3 时按上文映射消费既有 V2 产物。

## 步骤路由

1. 输入识别：读取 `input-analysis.md`。
2. 输入规范化：统一输入到 `video-project.schema.json` 项目对象。
3. Reference Role Classification：读取 `reference-intelligence/REFERENCE-ENGINE.md`、`reference-role.md`、`reference-image-analysis.md`、`reference-video-analysis.md`；给每个素材判定唯一 primary role、secondary roles、coverage、confidence、lock_level。无参考素材时跳过 03-06，直接按文字 Brief 继续。
4. Reference Element Extraction：按 role 读取 `character-extraction.md` / `product-extraction.md` / `scene-extraction.md` / `composition-extraction.md` / `camera-extraction.md` / `lighting-extraction.md` / `motion-extraction.md`，只提取素材真实可见的可继承证据。
5. Reference Priority：读取 `reference-priority.md`；写入每个素材的 evidence priority。默认值允许项目覆盖，覆盖需写明原因。
6. Reference Conflict Resolution：读取 `reference-conflict-resolution.md`；同一锁定维度证据不一致时输出 `REFERENCE CONFLICT`（冲突对 / Winner / Reason / Action），再进入锁阶段。无冲突时状态为 `NO CONFLICT`。
7. 产品/主体理解：读取 `product-analysis.md`；消费 RIE 的 product-derived evidence 建立 Product Lock。无产品时跳过产品锁，但仍识别人物、手、道具等主体。
8. Character Identity Lock：读取 `reference-intelligence/character-extraction.md` 与 `human-realism/identity.md`；有清晰脸或可辨身体时建立 `CHARACTER_ID` 与 Identity Fingerprint，写入 `characters[].identity_lock`。无人物时跳过本步。Identity Lock 与 Human Realism 严格分离。
9. Human Realism Routing：读取 `workflows/human-realism.md` 与 `human-realism/HUMAN-REALISM.md`；先问人物是否存在，再按可见性与动作加载最小模块。无人物时写 `enabled=false`、`skip_reason=NO_CHARACTER`，后续 Human Realism 步骤全部跳过，不生成【人物真实感】段落。
10. Human Motion Engine：按 Action 词表与 RIE motion evidence 把动作编译为动态链（如 `WALK -> weight transfer -> gait -> arm swing -> clothing delay`），写入 `motion_lock`；静态胸像不加载 gait / foot placement / pelvic motion。
11. 视频目的：读取 `video-objective.md`。
12. 创意结构：读取 `creative-structure.md`；用户已给创意时直接执行，未给时生成 3 个概念并推荐 BEST CONCEPT。
13. Hook 设计：读取 `hook-engine.md`。
14. 分镜：读取 `storyboard.md`，为每镜确定 `shot_size`、`first_frame_state`、`subject_action` 与结束状态。
15. Shot Distance Routing：按每镜景别做 Human Realism 景别修正，生成 `shot_distance_routing`；EXTREME_CLOSE_UP 不加载 gait，FULL/WIDE 不加载 nostril / pores。
16. 镜头可行性：读取 `shot-feasibility.md`；动作过载、人物运动与相机方向冲突、手与物体接触链不完整时自动拆镜或返回步骤 14。
17. Shot Human Realism Compile：把本镜动作增量编译为最小动态，写进时间轴；人物身份锁全片只写一次，时间轴只写状态增量。
18. Camera Language：读取 `camera.md` 与 `human-realism/camera-realism.md`；每个项目选择 TRIPOD / HANDHELD / PHONE / DOCUMENTARY / COMMERCIAL / CINEMATIC 之一，无理由不默认 handheld。
19. Temporal Consistency：读取 `human-realism/temporal-consistency.md`；维护 WITHIN SHOT / CROSS SHOT / SEQUENCE STATE 三层规则。
20. Continuity Lock：读取 `continuity.md`；多人项目同时维护 `INTERACTION LOCK`（相对位置、视线、距离、身体朝向、手部接触、物体归属）。
21. 声音设计：读取 `sound-design.md`；人物说话时启用 dialogue 专用动态，但台词只由 Dialogue Lock 控制，Human Realism 不改写台词。
22. 编译 Prompt：读取 `prompt-compiler.md` 与 `reference-intelligence/reference-prompt-formula.md`；按固定段落顺序输出，人物真实感只写入【人物真实感】，不混入人物锁或时间轴。
23. Human Realism QA：读取 `human-realism/realism-qa.md`；无人物时状态为 `SKIP`，不当作缺失。
24. Prompt Readiness QA：读取 `prompt-qa.md`；任何关键模块缺失标记 `INCOMPLETE`，回到对应步骤修复，不假装完整。
25. Pre-Generation Risk Score：输出 100 分生成前风险评估与等级；没有真实生成视频时，不能把该分数表述为实际画质成绩。
26. Reference QA：按 `reference-intelligence/REFERENCE-ENGINE.md` 的 REFERENCE QA 逐项复核；输出 `Reference Intelligence Score`（Role Accuracy 20 / Feature Extraction 20 / Priority Accuracy 15 / Conflict Resolution 15 / Lock Completeness 15 / Prompt Mapping 15，共 100）。该分数与 Prompt Readiness Score、Pre-Generation Risk Score 独立，不互相混淆。
27. Repair Routing：读取 `human-realism/repair-routing.md` 与 `reference-intelligence/reference-conflict-resolution.md`；有症状时定位到模块做局部修复，再返回步骤 22-26。
28. 输出：按输出模式交付 FINAL READY-TO-FEED PROMPT。

商业 TVC、30 秒长片、旁白片、多人围桌或复杂产品动作输入，在 V3 步骤 12-14 建立分镜前先读取 `references/commercial-directing-rules.md`；普通 10-15 秒产品短片不强制读取。

## 架构边界

本 Skill 只负责“怎么拍”和“怎么告诉模型拍出来”。不承担海外市场研究、TikTok 爆款研究、用户画像、国家市场分析、竞品营销分析、广告投放策略或 TikTok Shop 运营。这些输入应来自上游 Creative Strategy Skill。

## 标准输出

用户只说“帮我生成 Seedance 视频”时，默认输出：

1. 创意方向
2. 核心 Hook
3. 分镜
4. Human Realism 分层（有角色时）
5. Seedance 一次性投喂 Prompt
6. QA 与 Pre-Generation Risk Score

用户只要 Final Prompt 时，只输出 Final Prompt。

## 数据结构

整个流程维护一个 `video-project.schema.json` 对象，子工作流只填充自己的字段。`reference_intelligence` 由 V3 RIE 填充并符合 `schemas/reference-intelligence.schema.json`；`reference_analysis`、`characters[].identity_lock` 与顶层 `human_realism` 由 V2 模块填充；该 Schema 是未来被其他 Skill 调用的核心接口。
