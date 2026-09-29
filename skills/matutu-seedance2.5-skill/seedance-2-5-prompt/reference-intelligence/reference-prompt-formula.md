# Seedance Reference Prompt Formula

不要直接复制 Midjourney 参数公式。Seedance 2.5 是视频模型，需要时间、物理、连续性、约束。

# RIF — Reference Intelligence Formula

```text
RIF =
Role
×
Identity
×
Subject
×
State
×
Environment
×
Style
×
Lighting
×
Composition
×
Camera
×
Motion
×
Physics
×
Continuity
×
Constraints
```

## RIF 全字段对照

```text
REFERENCE ROLE     该素材的 canonical role
SUBJECT            画面主体是谁/是什么
IDENTITY           人物/产品身份锚点
STATE / POSE       静态状态与姿态
ACTION             动作链
ENVIRONMENT        空间与背景
STYLE              视觉风格与氛围
LIGHTING           光线证据
COMPOSITION        构图/取景
CAMERA             景别/机位/焦段/运镜/景深/焦点
MOTION             主体运动与摄影机运动
PHYSICAL RESPONSE  头发/衣服/液体/道具/环境的物理响应
TEMPORAL BEHAVIOR  时间、节拍、加减速、转场
CONTINUITY         跨镜一致性
CONSTRAINTS        默认锁、禁止变更项
```

## 动态路由

不是所有字段都强制输出。字段是否进入 RIF 由 Role 决定：

```text
CHARACTER_IDENTITY  -> Identity + Subject + State + Constraints
WARDROBE            -> Subject + 服装 Identity + 面料细节 + Constraints
PRODUCT_IDENTITY    -> Subject + Identity + Detail + Constraints
PRODUCT_MATERIAL    -> Subject + Texture/Surface + Lighting（材质可见性）+ Constraints
SCENE               -> Environment + Composition + Lighting + Continuity
CAMERA              -> Camera + Composition
LIGHTING            -> Lighting + Continuity
MOTION / ACTION     -> Motion + Physics + Temporal + Camera
AUDIO               -> Audio（不进入画面主体锁）
OVERALL_STYLE       -> Style + Color Palette + Constraints
```

## RIF 块输出格式

RIE 输出的是供 Prompt Compiler 消费的规格块，不是成片文字：

```yaml
rif_blocks:
  - block: ROLE
    role: CHARACTER_IDENTITY
    source_refs: [image_01]
    content: |
      同一张自然亚洲男性脸：偏长方脸...
    lock: HARD_LOCK
    constraints:
      - 只继承面部证据
      - 不继承背景与光线
```

## RIF 规则

- Role 优先：相同字段冲突时，role 优先级高的素材赢。
- 只写可见证据：Reference 没有的信息不得用想象力补足。
- 动态路由：人物特写不加载 gait，产品细节不加载面部微表情，动作视频不锁身份。
- 每个 RIF 块都标注 `source_refs`，Prompt Compiler 可追溯来源。
- 最终 Prompt 只引用真实上传且仍在场的素材 ID。
