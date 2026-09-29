# Clothing Dynamics

衣服没有物理感的来源是“衣服不是穿在人身上，而是贴在人身上”。Clothing 模块负责把布料当成有质量、有刚度、有摩擦的系统。

## 动态要素

```text
fabric inertia
gravity
compression
stretch
fold formation
body contact
motion response
```

人物移动时按因果链写：

```text
body motion
-> fabric reacts
-> folds shift
-> gravity restores
```

中文示例：

```text
人物从坐姿站起，外套前襟先因肩部抬起而离开身体，
下摆滞后约2-3帧再落下；转身时袖管随手臂外甩，
布料在肘弯堆出新折痕，停稳后折痕缓慢回弹但仍保留旧折方向。
```

## 面料差异

- 亚麻：折痕明显、回弹慢、下摆重量感强。
- 针织：贴身体、随动作拉伸、领口与袖口有弹性回复。
- 西装毛料：剪裁轮廓主导，肩线稳定，下摆与袖口有少量惯性。
- 丝绸/衬衫：细碎折痕多，反光随褶皱变化，不与身体完全贴合。

## 禁止

```text
rigid clothing
floating fabric
texture swimming
fabric teleportation
衣服与身体之间无受力关系
布料折痕不随动作更新
```
