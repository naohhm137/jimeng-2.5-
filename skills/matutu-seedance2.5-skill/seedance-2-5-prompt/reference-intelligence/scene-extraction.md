# Scene Extraction

场景参考图提取空间与背景证据，交给 Scene Lock。

## 提取字段

```text
location             地点与功能
architecture         建筑结构
environment          自然/城市/室内/室外环境
objects              固定道具与移动道具
materials            表面材质
depth                空间层次
foreground           前景元素
midground            中景元素
background           背景元素
color_palette        主色与色彩关系
lighting             光源/方向/色温/对比
atmosphere           气氛
composition          空间取景关系
camera               该场景允许的景别/机位（不是产品锁）
```

## 输出 YAML

```yaml
scene_lock:
  location:
  architecture:
  environment:
  objects:
  materials:
  depth:
  foreground:
  midground:
  background:
  lighting:
  atmosphere:
  color_palette:
  composition:
```

## 规则

- 场景参考中的固定空间关系（门/窗/柜台相对位置）必须写清，方便跨镜保持一致。
- 道具数量、位置、消失/复制/悬浮规则进入 Continuity，不只写“有椅子”。
- 光线随时间变化必须合理，不在同一场景内无理由跳变。
- 人物场景图以人物为主体时，背景证据只继承该图真正覆盖的空间范围。

## 下游

Scene Extraction 结果进入 `scene` 与 `scene_lock`，Prompt Compiler 写成【场景锁】。
