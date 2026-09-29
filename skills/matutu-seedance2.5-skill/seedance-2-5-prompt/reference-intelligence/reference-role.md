# Reference Role System

每个参考素材都必须先判断 Role，再进入提取。Role 回答“这张素材负责锁什么”，不回答“这张素材拍得像不像”。

## Canonical Roles

```text
CHARACTER_IDENTITY    锁人物身份：同一张脸、同一身体、同一年龄感
CHARACTER_APPEARANCE  锁人物可辨识外观，但不单独承担完整身份（例如背面/半身）
WARDROBE              锁服装/版型/面料/颜色/穿搭结构
POSE                  锁静态姿态、身体朝向、重心
ACTION                锁动作内容与动作链
PRODUCT_IDENTITY      锁产品身份：同一产品、同一型号、同一视觉主体
PRODUCT_DETAIL        锁产品局部细节：结构、Logo、文字、按钮、接口
PRODUCT_MATERIAL      锁材质、纹理、表面处理
PRODUCT_USAGE         锁使用方式与受力状态
SCENE                 锁空间、地点、建筑与背景主体
ENVIRONMENT           锁环境气氛、天气、自然/城市环境
ARCHITECTURE          锁建筑结构、空间关系
COMPOSITION           锁构图、取景、画面元素分布
CAMERA                锁景别、机位、焦段、运镜、景深、焦点
LIGHTING              锁光线方向、强度、色温、对比、阴影
COLOR_PALETTE         锁画面主色、色调与色彩关系
VISUAL_STYLE          锁视觉风格、质感、情绪调性
MOTION                锁动作模式、速度、方向、节奏
CAMERA_MOTION         锁摄影机运动模式与人物/产品的摄影关系
TIMING                锁节奏、节拍、时间分布
AUDIO                 锁声音设计参考（环境声/音效/对白气质）
OVERALL_STYLE         锁成片整体气质，仅作为顶层风格参考
```

## 与 V2 角色名映射

V3 canonical role 统一后，旧角色名继续可读，映射如下：

```text
IDENTITY_REFERENCE        -> CHARACTER_IDENTITY
HAIR_REFERENCE            -> CHARACTER_APPEARANCE（只锁发）或 WARDROBE（如果同时锁发色外的服装）
OUTFIT_REFERENCE          -> WARDROBE
POSE_REFERENCE            -> POSE
PRODUCT_REFERENCE         -> PRODUCT_IDENTITY
PRODUCT_APPEARANCE        -> PRODUCT_IDENTITY
PRODUCT_TEXTURE           -> PRODUCT_MATERIAL / PRODUCT_DETAIL
SCENE_REFERENCE           -> SCENE
STYLE_REFERENCE           -> VISUAL_STYLE / OVERALL_STYLE
MOTION_REFERENCE          -> MOTION
CAMERA_REFERENCE          -> CAMERA / CAMERA_MOTION
```

## 每个 Reference 必须输出

```yaml
reference_id: image_01
role: CHARACTER_IDENTITY
secondary_roles:
  - CHARACTER_APPEARANCE
  - WARDROBE
priority: 100
confidence: 0.97
lock_level: HARD_LOCK
```

- `role` 只有一个；`secondary_roles` 只写该素材确实能提供的辅助证据。
- `priority` 使用 Reference Priority System，不直接写入 `subject-lock.priority`（后者是 1-10 的锁优先级）。
- `confidence` 表示该素材作为证据的可靠程度：清晰正面实拍 > 侧面实拍 > 低清/遮挡/生成图。
- `lock_level` 取 `HARD_LOCK / SOFT_LOCK / STYLE_REFERENCE / INSPIRATION`。

## Role 判定规则

```text
1. 主体是什么：人物、产品、场景、摄影语言、声音
2. 素材能提供什么证据：身份/外观/材质/姿态/动作/空间/光线/风格
3. 素材不能提供什么证据：遮挡的部分、低清的部分、非主体的部分
4. 同一素材多个能力时，按最高价值职责定主 role，其余进 secondary_roles
```

禁止让参考素材承担自己无法提供证据的 Role。

## Role 冲突护栏

- Camera Reference 不能误当成 Subject Reference：画面中出现人物/产品，不代表该素材锁定人物/产品。
- Style Reference 不能覆盖 Identity Lock：风格只决定调色/质感，不改脸、改五官。
- Motion Reference 不能修改人物 Identity：动作证据只进入 Motion Lock。
- HUMAN REALISM 永远不能改写身份：Human Realism 属于行为层，不进入 Identity Lock。
