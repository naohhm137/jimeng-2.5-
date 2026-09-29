# Character Identity Lock

Identity Layer 只回答一个问题：

> 这个人是谁？

不回答“怎么说话、怎么走路、手怎么放”。那些属于 Human Realism Layer 与 Human Motion Engine。

## Identity Fingerprint

为每个有清晰脸或可辨身体的人物建立 `IDENTITY FINGERPRINT`。字段如下：

```text
CHARACTER_ID      CHARACTER_A / CHARACTER_B
FACE SHAPE        face structure
FACIAL PROPORTIONS
EYE SHAPE
EYEBROW SHAPE
NOSE SHAPE
LIP SHAPE
JAWLINE
CHEEKBONE STRUCTURE
SKIN TONE
AGE
HAIR STYLE
HAIR COLOR
BODY PROPORTIONS
OUTFIT
SIGNATURE FEATURES
```

示例：

```text
CHARACTER_ID = CHARACTER_A
同一张自然亚洲男性脸：偏长方脸、下颌线清晰、眉眼间距适中、
鼻梁直、唇形薄、年龄感约35岁、浅褐色短发、
176cm偏瘦身材、白色亚麻两件套、无明显疤痕或纹身。
```

## Identity 规则

1. Identity Block 全片只写一次，跨 Shot 原样复用，不换措辞。
2. 时间轴只写“这一镜新增的动作与状态”，不重述整段身份。
3. 身份锚点来自 Reference Coverage。Reference 没有正脸时，不能假装“参考图已锁脸”。
4. 年龄感、脸型、五官比例属于 Identity；皱纹的“动态形变”属于 Skin / Face Dynamics。
5. 人物越近，身份字段越需要精确；FULL / WIDE 镜头只保留头身比、发色、服装这些远程可辨识锚点。
6. 同一身份可以用不同景别描述，但必须引用同一个 `CHARACTER_ID`。

## 禁止把 Realism 写进 Identity

不要把以下内容写进 Identity Block：

```text
natural blinking
subtle breathing
weight transfer
fabric inertia
natural expression
photorealistic
```

这些由 `facial_dynamics`、`body`、`clothing` 等模块负责。

## Multi Character

- 每个人物独立 `CHARACTER_A` / `CHARACTER_B`，各自维护 Identity Fingerprint。
- `INTERACTION LOCK` 单独保存人物之间的相对位置、视线、距离、身体朝向、手部接触和物体归属，不并入任何一个人的 Identity。
- 禁止出现 face merge、identity swap、clothing swap、body swap。
