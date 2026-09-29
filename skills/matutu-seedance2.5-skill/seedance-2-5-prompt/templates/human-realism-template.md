# Human Realism 可投喂模板

用途：人物出镜的商业视频进入 V2 后按本模板分层编译。无人物项目不读取本文件。

## Layer 1: Director Layer（WHAT）

```text
人物：CHARACTER_A（引用 Identity Block）
动作：<action>，<起止时间>
状态链：<第一帧状态> -> <动作完成态> -> <结尾状态>
```

## Layer 2: Human Realism Layer（HOW A REAL HUMAN BEHAVES）

先按 Shot Distance Routing 选模块，再写最小动态。

```text
FACE
Subtle facial muscle movement.
Natural expression transitions.
Small asymmetries remain visible.
Expression gradually develops and naturally relaxes.

EYES
Natural irregular blinking.
Subtle saccadic eye movement.
Natural focus shifts.
Moist realistic eyes.
Natural eyelid deformation.

SKIN
Natural skin texture.
Subtle tonal variation.
Realistic skin deformation during facial movement.
Natural highlights rather than plastic skin.

HAIR
Individual strands respond naturally to movement.
Loose strands and flyaways move independently.
Hair follows head movement with slight inertia.

BODY
Natural center-of-mass movement.
Physically plausible weight transfer.
Natural posture adjustment.
Realistic acceleration and deceleration.

HANDS
Anatomically plausible fingers.
Independent finger movement.
Natural wrist rotation.
Realistic grip and object contact.

CLOTHING
Fabric responds naturally to body movement,
gravity and inertia.
Folds shift according to body movement.

CAMERA
Realistic camera behavior appropriate to the selected capture style.
Natural focus and exposure response.
```

只保留当前镜需要的高亮模块，其余删除。

## Layer 3: Prompt Layer（FINAL SEEDANCE PROMPT）

最终 Prompt 继续使用现有中文模板段落，身份与真实感分层写入：

```text
【规格】
...

【导演意图】
...

【参考素材职责】
@图片1：ROLE CHARACTER_IDENTITY；INHERIT face structure/facial proportions/eye shape/nose/lips/jaw/skin tone/age/hair；DO NOT INHERIT background/lighting/outfit。
@图片2：ROLE OUTFIT_REFERENCE；INHERIT cut/fabric/color/fit；DO NOT INHERIT background/lighting/face。

【人物锁】
CHARACTER_ID = CHARACTER_A。
同一张自然亚洲男性脸：<固定身份锚点，只写一次>。
发型、发色、体型、服装、配饰全程不变。

【人物真实感】
身份锁定后只加载最小动态：
<FACE / EYES / SKIN / HAIR / BODY / HANDS / CLOTHING 中与景别匹配的模块>
<包含动作编译后的因果链：转头 -> 发丝延迟 -> 重力归位>

【时间轴】
0-3秒｜钩子
第一帧已在动作中间：<动作中间帧>。
<人物动态增量，只写本镜新增>

【摄影】
<capture language>，<单一主运镜>，<对焦/曝光响应>。

【连续性】
人物一致性：CHARACTER_A 身份、发型、服装、鞋、配饰全程不变。
Sequence State：上一镜<结束状态>延续到本镜第一帧<开始状态>。

【负面约束】
只写本项目高风险项：no identity drift / no facial morphing / no frozen gaze /
no robotic blinking / no plastic skin / no synchronized hair movement /
no stiff fingers / no floating clothing。

【结尾状态】
...
```

## 三张参考图职责建议

需要三张参考图时，不要把它合成一张多人图；每张图独立生成、承担单一职责：

```text
参考图1：人物正面身份参考图
同一 40-50 岁美国白人男性，偏长方脸，下颌清晰，
自然灰棕短发，年龄感 45 岁，肤色自然带真实色差，
正面平视，眼神有自然注视方向；只负责脸与身份。

参考图2：服装版型参考图
同一人物，暖米白色天然亚麻两件套，上衣与长裤同色同料，
肩线、领型、袖长、裤长、松量可见；只负责服装结构。

参考图3：老钱松弛感姿态参考图
同一人物坐在帆布椅上，身体重心后靠，双腿自然伸展，
双手松弛放在扶手上；只负责姿态与服装自然垂坠。
```

三张参考图的服装描述必须完全一致，避免分开生成后出现颜色或版型漂移。

## 禁止

```text
把三个 Reference Role 合成一张图
人物锁里混入 blink / breathing / weight transfer
无人物仍输出【人物真实感】
静态胸像加载 gait / foot placement / pelvic motion
把 photorealistic / 8K / masterpiece 当作真实感来源
```
