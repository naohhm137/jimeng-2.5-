# Product Extraction

产品参考图提取真实产品证据并交给 Product Lock。产品默认禁止 AI 自行修改设计。

## 提取字段

```text
product_identity     产品名称/型号/视觉身份
shape                整体造型
silhouette           轮廓线
dimensions           比例关系（没有真实尺寸时写比例，不编造 mm/cm）
colors
materials
textures
surface
logo
typography / text
buttons
ports / interfaces
packaging
accessories
proportion
reflection
```

## 输出 YAML

```yaml
product_lock:
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
```

## 规则

- `PRODUCT_TRANSFORMATION_ALLOWED` 默认 false。
- 只锁该产品真实可见的证据；UNKNOWN 就写 UNKNOWN。
- Logo、文字、数量、包装、配件都是锁内容，不能因为“看起来好看”而改。
- 多视角产品必须来自同一真实产品；视角之间不得设计漂移。
- 产品在运动中：锁定受力、接触链与变形前后两个状态，不产生中间态漂移。
- AI 生成的产品图只是创意占位，不能作为真实货品证据。

## 下游

Product Extraction 结果进入 `product.lock`，再由 Prompt Compiler 写成【产品锁】。
