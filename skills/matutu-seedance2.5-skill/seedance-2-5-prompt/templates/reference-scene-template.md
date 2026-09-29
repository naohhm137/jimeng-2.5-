# Reference Scene Template

用途：场景参考图生成 Scene Lock 与摄影/光线规格。

```text
REFERENCE ID: <image_03>
ROLE: SCENE

SCENE_LOCK
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

SPATIAL RELATIONS
<门/窗/柜台/树等固定物体的相对位置>

LIGHTING EVIDENCE
<只写可见光源证据；氛围图没有光源细节时降为 STYLE>
```

规则：

- 固定空间关系必须写清，跨镜才能保持一致。
- 场景锁与光线锁分离：场景决定“在哪”，光线决定“怎么被照”。
- 人物场景图中的背景只继承该图真正覆盖的范围。
