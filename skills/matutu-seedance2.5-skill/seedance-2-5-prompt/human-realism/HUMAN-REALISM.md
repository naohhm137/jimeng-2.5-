# Human Realism Engine

本目录把 Seedance 2.5 Skill 从“Prompt Generator”升级为“Human Video Director”。

## 核心关系

```text
Identity ≠ Realism
Identity = 这个人是谁
Realism = 这个人如何像真人一样活着

Reference ≠ Prompt
Reference = 真实外观证据
Prompt = 可执行导演指令

Motion ≠ Camera
Motion = 人体动作
Camera = 观察动作的摄影机

Realism ≠ Quality Adjectives
Realism = 动态、惯性、物理响应、时间连续性
Quality Adjectives = photorealistic / 8K / highly detailed 等描述

Consistency ≠ Repeating The Same Sentence
Consistency = 同一条 Identity Block 复用 + 状态机连续
```

质量形容词只能作为外观层补充，不能替代 Human Realism Engine。

## 分层架构

```text
REFERENCE INTELLIGENCE ENGINE (V3)
  -> Role + Evidence + Priority + Conflict -> REFERENCE SPEC
REFERENCE ANALYSIS
  -> 素材职责 + 覆盖度
CHARACTER IDENTITY LOCK
  -> CHARACTER_A 是谁，跨 Shot 永远不变
HUMAN REALISM ENGINE
  -> 脸、眼、皮肤、头发、身体、手、衣服如何活起来
HUMAN MOTION ENGINE
  -> ACTION 编译为最少必要动态
SHOT DISTANCE ROUTING
  -> 景别决定加载哪些模块
TEMPORAL CONSISTENCY
  -> Shot 内 / 跨 Shot / Sequence State
PROMPT COMPILER
  -> 身份与真实感分别写入，不混成一个长段落
REALISM QA
  -> PRE-GENERATION RISK SCORE
REPAIR ROUTING
  -> 症状定位到模块，做局部修复
```

V3 有参考素材时，RIE 先于 Identity Lock 与 Human Realism 执行；Human Realism 只接收 RIE 给出的 Identity Lock 与可见性/动作需求。

## 模块文件

- 身份锁：`identity.md`
- 参考素材职责与覆盖度：`reference-analysis.md`
- 脸：`face-dynamics.md`
- 眼：`eye-dynamics.md`
- 皮肤：`skin-dynamics.md`
- 头发：`hair-dynamics.md`
- 身体：`body-biomechanics.md`
- 手：`hand-dynamics.md`
- 衣服：`clothing-dynamics.md`
- 微表情：`micro-expression.md`
- 摄影机真实感：`camera-realism.md`
- 环境真实感：`environmental-realism.md`
- 时间连续性：`temporal-consistency.md`
- QA：`realism-qa.md`
- 修复路由：`repair-routing.md`

## 自动路由

```text
CHARACTER?
├── NO
│   └── SKIP HUMAN REALISM
└── YES
    ├── FACE VISIBLE?
    │     YES -> face_dynamics + eye_dynamics + skin + identity
    ├── BODY MOVEMENT?
    │     YES -> body_biomechanics
    ├── HAND INTERACTION?
    │     YES -> hand_dynamics
    ├── HAIR MOVEMENT?
    │     YES -> hair_dynamics
    ├── CLOTHING MOVEMENT?
    │     YES -> clothing_dynamics
    └── MULTI-SHOT?
          YES -> temporal_consistency
```

判断顺序不可反过来：先问有没有人物、人物可不可见、人物动不动，再决定加载哪些模块。

## 最小充分原则

- 静态胸像不加载 gait / foot placement / pelvic motion。
- 走路镜头不加载 nostril movement / pores / finger tendons。
- 产品近景出现手时加载 hand_dynamics，不加载完整面部动态。
- 没有人物时 `enabled=false` 并写明 `skip_reason`，不产生任何 Human Realism 段落。

## 使用入口

工作流入口在 `workflows/human-realism.md`。执行顺序由 `workflows/main-pipeline.md` 控制，最终由 `workflows/prompt-compiler.md` 写入 Prompt。
