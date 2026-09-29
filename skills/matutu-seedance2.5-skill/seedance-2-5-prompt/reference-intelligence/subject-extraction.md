# Subject Extraction

Subject Extraction 回答“这张参考的主体是谁/是什么”，是提取的第一步，也是 Role 判定的前置条件。

## 主体分类

```text
CHARACTER   人物主体（是否露脸、是否背影、是否只有手）
PRODUCT     产品主体（完整/局部/使用中/拆解状态）
SCENE       环境/空间主体（无明确中心人物的背景）
ANIMAL      动物主体
VEHICLE     车辆/机械主体
NATURE      自然主体（山川/水面/植物/天气）
OBJECT      道具/非产品物件
CAMERA      主体其实是摄影语言（人物+景别都只是演示，不作为证据）
MIXED       多主体，必须拆分处理
```

## 提取字段

```text
subject_type
subject_label         给该主体一个稳定 ID，例如 CHARACTER_A / PRODUCT_01 / SCENE_01
count                 主体数量；多主体图必须逐主体登记
visible_parts         该主体可见的结构部分
occluded_parts        被遮挡、切出画外、低清不可辨的部分
evidence_limit        该素材证据的上限
```

## 规则

- 主体有多个时，每个主体单独提取；不允许“一张图包含三个人”就当作一个 Identity。
- 主体没有明确可见特征时，不编造。
- 产品主体 + 人物使用时，人物是否成为 Identity 由人物脸部/身体证据决定，产品与人物分两个 subject。
- Camera/Composition 参考里的主体只是演示者，默认不属于本项目要锁的人物/产品。

## 输出

主体提取结果进入 REFERENCE SPEC 的 `references[].subject` 与 `extracted_features[].subject`。
