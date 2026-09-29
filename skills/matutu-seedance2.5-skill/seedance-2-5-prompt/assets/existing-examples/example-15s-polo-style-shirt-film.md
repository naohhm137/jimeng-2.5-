# Pipeline Run 02｜Polo同款风格翻领Polo衫宣传片（15秒）

## Pipeline Trace

- Input Type: `AD_BRIEF + PRODUCT_DATA`（本次无实拍图）
- Task: `GENERATE`
- Objective: `BRAND_AD`
- Creative: 美式学院风：pique面料细节 → 模特上身姿态 → 明亮庭院行走 → 正面packshot
- Hook: `ACTION_HOOK`，第一帧已在把叠好的Polo衫拎起并翻正的中间动作
- Defaults: 15秒，9:16竖屏，30fps，无字幕，无旁白，无BGM，无清晰人脸，不生成品牌Logo
- Output Mode: `ONE_SHOT_PROMPT`

## Run Notes

本次没有实拍图，先按“同款风格文字占位版”跑通整条流程。真实货品的颜色、面料、领型、刺绣或织唛以实拍图为准；三张参考素材提示词见下节。生成并上传素材后，按 `references/reference-asset-prompts.md` 接入实际 `@图片` ID，并复核 Product Lock。

## 01 Reference Asset Prompts

### @图片1｜产品主图（ROLE PRODUCT_APPEARANCE）

```text
竖屏9:16产品摄影图。藏青色pique针织翻领Polo衫，正面完整悬挂在浅色木衣架上，背景是米白色亚麻质感墙面。
要求：pique面料纹理清晰，翻领挺立，三粒同色纽扣门襟，袖口和下摆罗纹可见，侧缝结构真实。
光线：柔和均匀的正面自然光，色温约5500K，无强烈阴影。
禁止：人物、人脸、文字、真实品牌Logo、马球图案、水印、多余道具。
```

### @图片2｜面料与门襟细节（ROLE PRODUCT_TEXTURE）

```text
商业服装细节特写图。藏青色pique针织面料，三粒同色纽扣门襟，领口内侧包边与缝合线迹清晰。
要求：织物颗粒真实，针脚密度一致，纽扣位置正确，颜色与素材1完全一致。
光线：均匀柔光，无过曝，无阴影遮挡面料。
禁止：人物、手部遮挡主要面料、文字、Logo、水印。
```

### @图片3｜模特背面参考（ROLE CHARACTER_BODY_APPEARANCE）

```text
竖屏9:16写实服装摄影图。同一男性模特背面朝向镜头，身穿与素材1相同的藏青色pique翻领Polo衫，站在明亮庭院拱门处。
要求：只拍背面与侧后，不露清晰正脸；领型、肩线、袖口罗纹、下摆与素材1一致；白色帆布袋搭在右肩。
光线：明亮日光，画面干净，背景为浅色墙面和拱门。
禁止：路人、第二件Polo衫、正面人脸、品牌Logo、文字、水印。
```

## Final Prompt

【规格】
15秒，9:16竖屏，30fps，无字幕，无旁白，无背景音乐。

【导演意图】
美式学院风藏青Polo衫宣传片：从面料与版型细节进入，经过模特上身姿态和明亮庭院场景，收在正面悬挂packshot；画面干净高级、真实可执行，不出现清晰人脸与品牌字样。

【参考素材职责】
本次无已上传素材，当前不引用任何未上传图片；Polo衫外观由文字产品锁驱动。接入实拍图后，本段替换为实际 `@图片` ROLE 与 INHERIT / DO NOT INHERIT 映射。

【产品锁】
藏青Polo同款翻领针织衫：pique织面纹理、翻领、三粒同色纽扣门襟、袖口与下摆罗纹、侧缝结构、领口包边与针脚全程一致；不变色、不变版型、不新增文字、不出现第二件同款。

【人物锁】
无清晰人脸；只允许同一男性模特背面、侧后、手部与颈部以下入镜；全片只有一位模特，不换人、不出现路人脸。

【场景锁】
三个场景因果相连：浅色亚麻桌面细节区 → 明亮庭院拱门与走道 → 米白墙面studio packshot区；光线均为自然明亮，方向稳定，空间干净无杂物。

【时间轴】

0-1.8秒｜钩子
第一帧已是双手从浅色亚麻布面把叠好的藏青Polo衫拎起并翻正的中间动作；衣领抖开，pique织面自然垂落。
镜头：MEDIUM，45度桌面俯拍，轻微前推。声音：布料舒展声、桌面轻微摩擦。

1.8-3.6秒｜面料与门襟
镜头贴至pique织面与门襟，手从画面下方入画，食指轻按织面一次后抬起，三粒纽扣保持原位。
镜头：EXTREME_CLOSE_UP，固定。声音：织物摩擦、指腹轻触。

3.6-6.2秒｜上身调整
模特已穿好Polo衫，镜头从背侧进入；右手把后领翻正，左手拉平下摆，领口与肩线保持挺拔。
镜头：MEDIUM，侧后视角，轻微横移。声音：领口调整、面料摩擦。

6.2-9.5秒｜行走场景
模特背对镜头穿过明亮庭院拱门，白色帆布袋搭在右肩，Polo衫随步伐自然摆动，画面继续跟拍。
镜头：FULL，正后方跟拍。声音：轻脚步、风吹布料、庭院低频环境音。

9.5-12秒｜袖口收束
模特在拱门阴影与阳光交界处停步，右手整理右袖口，下摆被自然拉直；画面以侧后中景收住，不切正脸。
镜头：MEDIUM_CLOSE_UP，固定或极轻微前推。声音：袖口整理、环境音保持。

12-14秒｜Packshot
藏青Polo衫正面悬挂在浅色木衣架上，背景为米白墙面，纽扣全部扣好，领型挺立，衣身自然垂落，画面中心稳定。
镜头：CLOSE_UP，固定，浅景深。声音：环境音渐弱。

14-15秒｜收束
Polo衫保持正面packshot，画面固定约1秒自然收尾，无文字出现。
镜头：CLOSE_UP，固定。声音：环境音降至静默。

【摄影】
35-50mm写实时尚片质感，以固定与极轻微运镜为主；浅景深只用于细节镜，packshot保持主体全部清晰；不做甩镜、不做环绕。

【光线】
自然明亮日光为主：细节区为柔和侧光，庭院区为高光与拱门阴影的明确过渡，packshot区为均匀正面柔光；三区色温一致约5500K，无冷蓝或暖橙滤镜。

【声音】
AMBIENCE：庭院微风、室内低频。SFX：布料舒展、指腹轻触、领口调整、脚步、帆布袋摩擦。VOICE：无。DIALOGUE：无。BGM：无。

【连续性】
同一件藏青Polo衫：pique纹理、领型、门襟、纽扣、罗纹与侧缝结构全程一致；模特同身型、同服装、始终不露清晰正脸；场景光线方向明确，产品不漂移、不复制、不穿模。

【负面约束】
不要清晰人脸、不要换模特、不要路人入镜；不要真实品牌Logo、马球图案、Polo Ralph Lauren等文字或近似标识；不要字幕、标题、水印、UI；不要产品变色、变形、消失、复制、穿模；不要手指异常或左右镜像错误。

【结尾状态】
Polo衫正面packshot固定约1秒，画面干净收束。

## QA

- SPEC: PASS（15秒连续覆盖）
- PRODUCT: PASS（文字占位版结构通过；上传实拍图后复核颜色/领型/织唛）
- CHARACTER: PASS（无清晰人脸，唯一模特）
- SCENE: PASS（三场景有明确光线轨迹）
- ACTION: PASS（每镜单一主动作，含完成态）
- CAMERA: PASS（无环绕，packshot稳定）
- LIGHTING: PASS
- SOUND: PASS（无BGM、无旁白）
- DIALOGUE: N/A
- CONTINUITY: PASS
- NEGATIVE: PASS
- ENDING: PASS
- Prompt Readiness Score: Clarity 96 / Actionability 94 / Continuity 96 / Product Fidelity 90（无实拍图需复核）/ Character Fidelity 95 / Camera Executability 95 / Audio Completeness 96 / Temporal Coherence 97
- Status: `READY`（文字占位版可投喂；参考素材生成并上传后按 `reference-asset-prompts.md` 更新【参考素材职责】并复核 Product Lock）
