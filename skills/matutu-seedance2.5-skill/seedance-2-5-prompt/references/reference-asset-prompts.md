# Reference Asset Prompts（参考素材生成提示词）

当输入只有文字 Brief、没有实际产品图或人物图，用户仍要求直接出片时，先用本文件生成“参考素材提示词”或告诉用户需要补充什么实拍图。参考素材不参与叙事，只负责锁定真实产品/人物的外观细节。

## 使用边界

- 实拍图优先级高于 AI 生成参考图。产品真实性、颜色、Logo、版型只有实拍图能作为可靠证据。
- AI 生成的参考图只算“创意占位素材”，成片不能声称等于真实货品；用户拿到实拍图后应重新复核产品锁。
- 没有品牌授权时，禁止生成真实品牌名称、Logo、刺绣图案或近似标识；“同款”只能表达版型与风格参考。
- 最终 Prompt 只引用用户真实上传的素材 ID，不能引用“生成但未上传”的图片。

## 素材职责映射

```text
@图片1  ROLE PRODUCT_APPEARANCE
         INHERIT shape / color / material / logo / logo position / proportion
         DO NOT INHERIT background / lighting / text / watermark

@图片2  ROLE PRODUCT_TEXTURE / PRODUCT_DETAIL
         INHERIT fabric weave / stitching / buttons / collar construction
         DO NOT INHERIT background / shadow / text / watermark

@图片3  ROLE CHARACTER_BODY_APPEARANCE
         INHERIT body shape / build / clothing drape / no-face policy
         DO NOT INHERIT background / lighting / face / accessories
```

## 通用生成公式

```text
{画幅}参考图。{主体}，{版型/材质/关键细节}，{构图与姿态}，{背景}，{光线}。
要求：{需要清晰呈现的真实细节}。
禁止：人物/清晰人脸（按策略）、文字、Logo、水印、与主体无关的道具。
```

补充原则：

- 产品主图必须能看到完整主体、关键结构、颜色和材质，不需要复杂场景。
- 细节图只锁一个卖点信息，例如织法、针脚、领型或纽扣，不塞入多个主体。
- 人物参考图优先背面/侧后/颈部以下，避免用 AI 生成后又被当成真实人脸身份。
- 同一套参考图之间用相同产品描述，防止颜色、版型或模特漂移。

## Polo同款风格参考图示例

### 素材1：产品主图，作为 `@图片1`

```text
竖屏9:16产品摄影图。藏青色pique针织翻领Polo衫，正面完整悬挂在浅色木衣架上，背景是米白色亚麻质感墙面。
要求：pique面料纹理清晰，翻领挺立，三粒同色纽扣门襟，袖口和下摆罗纹可见，侧缝结构真实。
光线：柔和均匀的正面自然光，色温约5500K，无强烈阴影。
禁止：人物、人脸、文字、真实品牌Logo、马球图案、水印、多余道具。
```

### 素材2：面料与门襟细节图，作为 `@图片2`

```text
商业服装细节特写图。藏青色pique针织面料，三粒同色纽扣门襟，领口内侧包边与缝合线迹清晰。
要求：织物颗粒真实，针脚密度一致，纽扣位置正确，颜色与素材1完全一致。
光线：均匀柔光，无过曝，无阴影遮挡面料。
禁止：人物、手部遮挡主要面料、文字、Logo、水印。
```

### 素材3：模特背面参考图，作为 `@图片3`

```text
竖屏9:16写实服装摄影图。同一男性模特背面朝向镜头，身穿与素材1相同的藏青色pique翻领Polo衫，站在明亮庭院拱门处。
要求：只拍背面与侧后，不露清晰正脸；领型、肩线、袖口罗纹、下摆与素材1一致；白色帆布袋搭在右肩。
光线：明亮日光，画面干净，背景为浅色墙面和拱门。
禁止：路人、第二件Polo衫、正面人脸、品牌Logo、文字、水印。
```

## 接入最终 Prompt 的写法

```text
【参考素材职责】
@图片1：ROLE PRODUCT_APPEARANCE；INHERIT shape/color/material/collar/buttons/placket；DO NOT INHERIT background/lighting/text/watermark。
@图片2：ROLE PRODUCT_TEXTURE；INHERIT pique weave/stitching/buttons；DO NOT INHERIT background/shadow/text。
@图片3：ROLE CHARACTER_BODY_APPEARANCE；INHERIT body shape/build/back view；DO NOT INHERIT background/lighting/face。
```

未上传的素材 ID 必须从最终 Prompt 删除，不能保留为“可选”。
