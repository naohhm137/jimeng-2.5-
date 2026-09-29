# Prompt Compiler

把导演决策编译为 Seedance 2.5 可执行 Prompt。

## 输入

```text
REFERENCE SPEC
Product
Character
Identity Lock
Human Realism
Motion Lock
Scene Lock
Scene
Creative
Storyboard
Camera
Lighting
Sound
Continuity
Negative
```

REFERENCE SPEC 来自 `reference-intelligence/` 的 RIE 输出。编译时只消费其中的 derived locks 与 `rif_blocks`，不读取参考图画面散文；参考素材职责句由 RIF 结论生成。

有参考素材时，编译器必须在【参考素材职责】内部输出 `REFERENCE DECISION` 与 `PROMPT USAGE MAP`：每个 `@图片N` 都要绑定到具体锁、模块和时间轴/镜头，并列出不得继承的内容。未绑定到实际输出位置的参考素材视为 `Prompt Mapping = MISSING`，不得标记 READY。无参考素材时显式输出 `REFERENCE INTELLIGENCE: SKIP`，不得虚构 `@` 引用。

## 输出模式

### MODE A：ONE-SHOT PROMPT

一次性投喂版，默认输出。

### MODE B：SHOT-BY-SHOT PROMPT

逐镜头生成版，每镜可独立生成，注明拼接顺序与转场要求。

### MODE C：DIRECTOR PACKAGE

导演方案 + 分镜 + Prompt 完整包。

## 输出顺序

默认顺序不可乱：

```text
【规格】
【导演意图】
【参考素材职责】
【产品锁】
【人物锁】
【人物真实感】
【场景锁】
【时间轴】
【摄影】
【光线】
【声音】
【连续性】
【负面约束】
【结尾状态】
```

无产品时省略【产品锁】；无人物时省略【人物锁】与【人物真实感】。
有人物但 Human Realism 被跳过时（例如只有 No-Face 产品操作手部），仍只省略【人物真实感】；该段落一旦出现，必须位于【人物锁】之后、【场景锁】之前。

## 编译规则

- 身份与真实感分段落：身份锁回答“这个人是谁”，人物真实感回答“这个人如何像真人一样活着”，两个段落内容不混写。
- 【人物真实感】只保留 Shot Distance Routing 选中的最小模块，删除本片不需要的动态；走路不写 nostril / pores，静态胸像不写 gait / foot placement / pelvic motion。
- Human Realism 是动态与物理响应，不是 `photorealistic`、`8K`、`masterpiece` 等外观形容词的替代品。
- 人物固定特征只写一次，时间轴只写本镜增量。
- 参考图必须经过 Role、证据、覆盖度、优先级与冲突判断后再编译；`@图片N` 的实际使用位置必须在参考素材职责块中列出，并在对应锁或时间轴镜头中再次绑定。
- 参考图只影响被授权的锁定维度；人物图不自动改变场景，场景图不自动改变人物，Camera / Lighting / Style / Motion 参考不得越权覆盖身份锁。
- 对白按 Dialogue Lock 逐字输出，品牌名附拼音或明确读音。
- 人物说话时启用 dialogue 专用动态（口型、下颌、呼吸、视线、微表情、头部微小非周期运动），但台词内容只由 Dialogue Lock 控制。
- 多人项目在【人物真实感】中引用同一条 `INTERACTION LOCK`，禁止出现 face merge、identity swap、clothing swap、body swap。
- 负面约束只写本项目的高风险项。
- 用户只要 Final Prompt 时，不输出分析过程。

## 人物真实感写法

```text
【人物真实感】
身份锁定后只加载最小动态：
FACE / EYES / SKIN / HAIR / BODY / HANDS / CLOTHING 中与景别匹配的模块
动作因果链：<触发 -> 身体响应 -> 惯性/织物/头发的延迟与归位>
```

没有真实视频可复核时，不要把段落写成“视频整体很真实”。该段落只描述本镜可见的动态。
