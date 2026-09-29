# Reference Product Template

用途：产品参考图生成 Product Lock 规格。默认禁止产品设计变更。

```text
REFERENCE ID: <image_02>
ROLE: PRODUCT_IDENTITY / PRODUCT_DETAIL / PRODUCT_MATERIAL

PRODUCT_LOCK
identity:
silhouette:
dimensions:
materials:
colors:
textures:
logo:
typography:
controls:
ports:
accessories:
packaging:
allowed_transformations: false

SOURCE REFS
<生成该锁依据的 asset_id 列表>

EVIDENCE GAPS
<未覆盖的结构/材质/Logo 面，标记 MISSING>
```

规则：

- `PRODUCT_TRANSFORMATION_ALLOWED` 默认 false，除非用户明确开启。
- 多视角产品图必须来自同一真实产品；各视角不得漂移。
- 产品运动/变形状态锁“变化前 + 变化后”，禁止中间态漂移。
- AI 生成产品图只能作为创意占位素材，锁真实货品前必须复核。
