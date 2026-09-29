# Composition Extraction

构图参考提取取景与画面元素分布，不把画面里出现的人物/产品当作身份或产品证据。

## 提取字段

```text
frame_balance         主体在画面中的位置与留白关系
foreground_layer      前景遮挡/引导线
midground_layer       中景主体关系
background_layer      背景信息密度
subject_placement     中心/三分/边角/对称
lead_room / head_room 视线与头部空间
depth_layers          画面层次数
negative_space        留白用途
graphic_lines         线条/几何结构
```

## 规则

- 构图是“怎么放”，不锁“放的是什么”。同一构图可用于不同人物/产品。
- 参考构图中出现的人物脸、产品 Logo 不被继承，除非该图同时承担对应 Role。
- 构图参考通常作为 secondary role 附在 CAMERA / VISUAL_STYLE 素材上，不单独成为主体锁。
- 动态构图必须写清运动后构图如何变化，不允许只锁第一帧。

## 下游

构图结果进入 `camera_lock.composition` 或 Storyboard 的取景字段，不直接成为画面描述。
