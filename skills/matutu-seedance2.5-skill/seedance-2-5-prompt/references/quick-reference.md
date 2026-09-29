# Quick Reference（速查表）

写 Prompt 时默认查本表。本表未覆盖的规则才进入 `human-realism/`、`workflows/` 与 `references/` 的细节模块，避免每次把全库读一遍。

## 1. 输出顺序

```text
【规格】→【导演意图】→【参考素材职责】→【产品锁】→【人物锁】
→【人物真实感】（可选）→【场景锁】→【时间轴】→【摄影】→【光线】
→【声音】→【连续性】→【负面约束】→【结尾状态】
```

无产品省略产品锁；无人物省略人物锁与人物真实感。人物真实感一旦出现，必须在人物锁之后、场景锁之前。

## 1.1 有参考素材先走 RIE

```text
上传图/视频
→ 每个素材判定一个主 Role
→ 提取可继承特征与 MISSING 覆盖度
→ 写 priority / confidence / lock_level
→ 同维度冲突写 winner + reason
→ 生成 derived locks + rif_blocks（REFERENCE SPEC）
→ Prompt Compiler 只消费 locks，不把参考图描述直接写进 Prompt
```

人物图锁身份，产品图锁产品，场景图锁空间，动作视频只学 Motion / Camera Motion / Timing。

## 2. 默认值

```text
画幅未指定 -> 9:16
BGM 未指定 -> 无
字幕未指定 -> 无
时长未指定 -> 10-15 秒
帧率未指定 -> 24fps 或 30fps，按平台习惯
0-3 秒     -> 第一帧已在动作中间
```

## 3. 参考素材职责句

```text
@图片1：ROLE PRODUCT_APPEARANCE
        INHERIT shape/color/material/collar/buttons/logo position
        DO NOT INHERIT background/lighting/text/watermark/camera angle

@图片2：ROLE PRODUCT_TEXTURE
        INHERIT fabric weave/stitching/buttons/collar construction
        DO NOT INHERIT background/shadow/text/watermark

@图片3：ROLE CHARACTER_IDENTITY + OUTFIT_WORN
        INHERIT original face/age/hair/body scale/outfit fit
        DO NOT INHERIT chair pose/background/lighting/accessories
```

原则：一个素材只承担明确职责；Reference 没有正脸或手部时写 `MISSING`，不假装已经锁住。

完整版输出必须追加在【参考素材职责】内部：

```text
REFERENCE DECISION：@图片N 的主体、证据、覆盖度、priority、confidence、lock_level。
PROMPT USAGE MAP：@图片N → 具体 Lock / 模块 / 时间段或镜头；DO NOT APPLY → 不得影响的模块。
```

使用判定：参考图未绑定具体输出位置 = `Prompt Mapping: MISSING`；参考图看不清的字段 = `MISSING`；无参考素材 = `REFERENCE INTELLIGENCE: SKIP`，不写任何 `@` token。

## 4. 锁的句式

```text
【产品锁】
<产品名>：不可改变 <形状/比例/颜色/材质/Logo/结构>；
允许变化：<无，或用户明确要求的变形状态>。

【人物锁】
CHARACTER_ID = CHARACTER_A。
同一张脸：<脸型/五官/发色/发型/年龄感/体型>；
服装：<上衣/下装/鞋/配饰>；全片只出现一次身份描述，时间轴只写增量。
```

## 5. 景别 -> 模块

| 景别 | 加载重点 | 不加载 |
|---|---|---|
| EXTREME_CLOSE_UP | eye / skin / lip / face / micro-expression | body gait / clothing |
| CLOSE_UP / MEDIUM_CLOSE_UP | face / eyes / skin / hair / micro-expression | foot / pelvic gait |
| MEDIUM | face / body / hands / clothing | skin pores / nostril |
| FULL | body / weight / feet / gait / hair / clothing | facial pore / micro-expression |
| WIDE / EXTREME_WIDE | body trajectory / environment / camera | 面部细节 |
| MACRO | product / material / hands | 人脸模块 |

## 6. 动作 -> 动态

| 动作 | 最少动态链 |
|---|---|
| WALK | 脚跟先落 -> 重心转移 -> 骨盆跟随 -> 肩部反向 -> 手臂摆动 -> 衣摆延迟 |
| RUN | 重心前移 -> 步频提高 -> 手臂屈曲 -> 头发/衣服更强惯性 |
| TURN | 眼先移 -> 脚换向 -> 骨盆 -> 肩 -> 头延迟 -> 头发延迟 |
| SIT | 视线找椅面 -> 臀部先降 -> 头稳定 -> 衣料落座后延迟归位 |
| STAND | 重心前移 -> 借力起身 -> 头最后到位 |
| TALK | 口型先于首字 -> 下颌随台词 -> 自然呼吸停顿 -> 头微小非周期移动 |
| SMILE | neutral -> 眼轮匝肌/颧肌启动 -> 峰值 -> 自然放松，两侧保留 10-30% 差 |
| REACH / PICK_UP | 肩先出 -> 手张开 -> 指腹接触 -> 拇指反向压力 -> 随重心提起 |
| HOLD | 腕部中立 -> 握力随物体运动微调 -> 不做整手僵硬造型 |
| DRINK | 视线落杯 -> 手抬杯到唇 -> 头微仰 -> 放杯不回跳 |

## 7. 常见症状 -> 修复

| 用户反馈 | 先修 |
|---|---|
| 脸越来越不像 | Identity + Temporal（跨镜复用同一条 CHARACTER_ID） |
| 眼睛像玻璃 | Eye（角膜反光、泪膜、不规则眨眼） |
| 眼神呆 | Eye + Face（注视对象 + 视线先于转头） |
| 脸僵/表情一直一样 | Face + Micro Expression（表情要有过程） |
| 皮肤塑料感 | Skin（分区高光、肤色色差、肌肉形变） |
| 头发像假发 | Hair（发丝分层、不同延迟、重力归位） |
| 走路像机器人 | Body（重心、重量转移、启动/停止） |
| 手指畸形 | Hand（五指独立、腕部中立、接触链） |
| 衣服飘/像贴纸 | Clothing（折痕生成、惯性、回弹） |
| 镜头不真实 | Camera（对焦/曝光/抖动绑定动作） |
| 两人变一人 | Multi Character + INTERACTION LOCK |

修复规则：先定位到最少模块，再局部替换低价值描述；不要追加“更真实”“更自然”这类空词。

## 8. Camera Language

每个项目只选一种：

```text
TRIPOD / HANDHELD / PHONE / DOCUMENTARY / COMMERCIAL / CINEMATIC
```

无理由不默认 handheld。对焦转移要写“从哪里到哪里、何时开始”；运动模糊只出现在主体或相机实际运动时。

## 9. QA 与风险分

```text
IDENTITY 20 / EYES 15 / FACIAL DYNAMICS 15 / SKIN 10 / HAIR 10
BODY BIOMECHANICS 15 / HANDS 5 / CLOTHING 5 / TEMPORAL CONSISTENCY 5
总分 100
```

```text
90-100  CINEMA REALISM
80-89   COMMERCIAL REALISM
70-79   ACCEPTABLE
60-69   AI ARTIFACT RISK
<60     REGENERATE
```

低于 70 回到对应模块补齐再投喂；没有真实视频时只叫生成前风险分，不叫实际画质成绩。

## 10. 负面约束候选

只写本项目高风险项，不无脑堆词：

```text
no face change / no identity drift / no product redesign
no duplicated objects / no floating objects / no extra fingers
no mirrored direction / no fabric teleportation / no synchronized hair
no unwanted subtitles / no watermark / no UI
```

## 反模式

不要用以下词替代动态细节：

```text
photorealistic / 8K / masterpiece / 自然走路 / 高级镜头 / 更像真人
```

它们应改写为可执行的景别、动作链、延迟帧与物理响应。
