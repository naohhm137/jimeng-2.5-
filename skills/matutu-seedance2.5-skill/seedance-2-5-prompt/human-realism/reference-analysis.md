# Reference Analysis

人物参考图不是一句话“character reference”。它是一份需要拆出职责、覆盖度与可信边界的证据清单。

## Reference Coverage

建立覆盖度表，只写参考图里实际能看到的内容：

```text
FACE        HIGH / MEDIUM / LOW / MISSING
PROFILE     HIGH / MEDIUM / LOW / MISSING
HAIR        HIGH / MEDIUM / LOW / MISSING
BODY        HIGH / MEDIUM / LOW / MISSING
FULL BODY   HIGH / MEDIUM / LOW / MISSING
HANDS       HIGH / MEDIUM / LOW / MISSING
CLOTHING    HIGH / MEDIUM / LOW / MISSING
AGE / SKIN  HIGH / MEDIUM / LOW / MISSING
EXPRESSION  HIGH / MEDIUM / LOW / MISSING
LIGHTING    HIGH / MEDIUM / LOW / MISSING
```

规则：

- MISSING 就是 MISSING。Reference 没有正脸时，Identity Block 只能写“以参考图半侧脸为上限”，不能伪造正面脸锚点。
- FULL BODY MISSING 时，Full Body 镜头需要用户补参考或接受可辨识的体型风险。
- HANDS MISSING 时，手部特写优先拆成独立镜头，并写清“参考图未覆盖手指结构”。

## Reference Role

一个参考素材只承担明确职责：

```text
IDENTITY_REFERENCE    锁脸、五官、年龄、身份锚点
HAIR_REFERENCE        锁发色、发量、发型结构
OUTFIT_REFERENCE      锁版型、材质、颜色、服装结构
POSE_REFERENCE        锁静态姿态与身体朝向
PRODUCT_REFERENCE     锁产品外观与受力状态
SCENE_REFERENCE       锁空间、背景、道具
STYLE_REFERENCE       锁视觉风格、调色、情绪
MOTION_REFERENCE      锁动作节奏、运动状态，不锁身份
```

不要让一张图同时承担 identity / pose / camera / lighting / outfit / environment，职责越杂越容易控制冲突。

## 素材声明写法

```text
@图片1：ROLE CHARACTER_IDENTITY
        INHERIT face structure / facial proportions / eye shape /
                nose / lips / jaw / skin tone / age / hair
        DO NOT INHERIT background / lighting / expression / outfit
```

## Reference Priority

参考素材与文字冲突时，按以下优先级裁定：

```text
IDENTITY_REFERENCE  > OUTFIT_REFERENCE
OUTFIT_REFERENCE    > POSE_REFERENCE
PRODUCT_REFERENCE   > SCENE_REFERENCE
SCENE_REFERENCE     > STYLE_REFERENCE
```

同一优先级内，`subject-lock.schema.json` 的 `priority` 决定胜负。

## Reference ≠ Prompt

- Reference 是上限：成片不能超出参考图提供的外观证据。
- Prompt 是下限：没有 Reference 时，不得用一段漂亮的文字假装身份已被锁定。
- 最终 Prompt 只引用真实上传且仍在场的素材 ID，不引用“生成后未上传”的图片。
