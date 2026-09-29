# Reference Image Analysis

图片参考先判定单张职责，再做覆盖度与可继承证据提取。图片参考的读取顺序固定为：

```text
主体识别
→ Role 判定
→ 可继承证据提取
→ 不可继承边界
→ confidence / lock_level
```

## 通用提取字段

```text
subject_type          CHARACTER / PRODUCT / SCENE / CAMERA / STYLE / AUDIO
subject_identity      能唯一指向真实主体的证据描述
coverage              该证据的可见程度 HIGH / MEDIUM / LOW / MISSING
key_features          只写实际可见且可继承的特征
do_not_inherit        背景、灯光情绪、文字、水印、非主体道具、镜头畸变
confidence            0-1，衡量证据可靠度
```

## 图片类型与提取重点

```text
人物参考图
  Identity / Face / Hair / Skin / Age Appearance / Body Proportion /
  Wardrobe / Pose / Expression / Lighting / Composition / Camera
  -> 自动进入 Human Realism Engine + Identity Lock

产品参考图
  Product Identity / Shape / Silhouette / Color / Material / Texture /
  Surface / Logo / Text / Buttons / Ports / Packaging / Accessories /
  Proportion / Reflection
  -> 自动进入 Product Lock，默认禁止产品设计变更

场景参考图
  Location / Architecture / Objects / Materials / Depth /
  Foreground / Midground / Background / Color Palette / Lighting /
  Atmosphere / Composition / Camera
  -> 进入 Scene Lock 与摄影/光线层

摄影/构图参考图
  Shot Size / Focal Length Estimate / Camera Height / Camera Angle /
  Perspective / Depth of Field / Focus Plane / Lens Character /
  Camera Movement / Composition
  -> 进入 Camera Lock / Composition，不锁定画面主体

服装/风格参考图
  Wardrobe / Fabric / Color / Cut / Texture / Fits / Overall Mood
  -> 进入 WARDROBE 或 VISUAL_STYLE
```

## 继承边界

实拍图只继承它真实呈现的内容。以下情况必须降 confidence 或标记 MISSING：

```text
没有正面 -> FACE 不写正面锚点
背光/逆光 -> 肤色、材质细节不写死
低清 -> 纹理、Logo、文字不写死
多人物图 -> 不默认等于“可继承身份”
AI 生成图 -> 只能当创意占位，不能当真实身份/产品证据
文字/Logo/水印 -> 一律 DO NOT INHERIT，除非该素材本身就是品牌资产图
```

## 输出

每张图写入 REFERENCE SPEC 的 `references[]`，提取结果写入 `extracted_features[]`。图片参考本身不生成 Prompt。
