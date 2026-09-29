# Seedance 2.5 Prompt QA Checklist

## 基础

- [ ] 规格完整：时长、画幅、帧率、字幕、BGM、旁白均已写明。
- [ ] 未指定画幅时默认为 9:16；未指定 BGM 时明确无 BGM。
- [ ] 时长在 4-30 秒范围内。

## 结构

- [ ] 0-3秒第一帧已在动作中间，不是空镜或“人物慢慢走进房间”。
- [ ] 每个参考素材都声明“负责什么+不负责什么”。
- [ ] 每个时间段都有 SHOT / ACTION / CAMERA / AUDIO 四要素。
- [ ] 结尾有明确收束状态，避免硬切。

## Reference Intelligence（有参考素材时）

- [ ] 每个素材只承担一个主 Role：人物锁身份，产品锁产品，场景锁空间，视频锁 Motion / Camera Motion / Timing。
- [ ] 素材已提取可继承特征与覆盖度，MISSING 未假装存在。
- [ ] 每个素材有 priority、confidence、lock_level，未把低置信素材直接硬锁。
- [ ] 【参考素材职责】内部有 `REFERENCE DECISION`，写明主体、证据、覆盖度与 MISSING。
- [ ] 【参考素材职责】内部有 `PROMPT USAGE MAP`，每个 `@图片N` 都绑定到具体 Lock、模块和时间轴/镜头，并列出不得影响的模块。
- [ ] 同维度冲突已写 `REFERENCE CONFLICT`（refs / winner / reason / action / resolved）。
- [ ] `derived_locks` 覆盖人物/产品/场景/摄影机/动作锁，编译只消费 locks 与 `rif_blocks`，不读参考图画面散文。
- [ ] `reference_qa.status` 为 PASS，`Reference Intelligence Score` 六项齐全且不与生成质量分数混淆。
- [ ] 未绑定实际使用位置的参考素材不能标记 READY；无参考素材时显式写 `REFERENCE INTELLIGENCE: SKIP`。

## 锁

- [ ] 人物固定特征只写一次，时间轴只写本镜增量。
- [ ] 有产品时建立产品锁，禁止默认改产品设计。
- [ ] 场景空间关系明确（门/吧台/窗等相对位置）。
- [ ] 道具数量与消失/复制/悬浮规则已写。

## 对白与声音

- [ ] 对白有逐字台词表、起止时间、repeat_count=1、不回声。
- [ ] 品牌名、生僻词附拼音或明确读音，禁止同音替换。
- [ ] AMBIENCE / SFX / VOICE / DIALOGUE / BGM 分层清晰。

## 摄影与光线

- [ ] 运镜是单一主运动，无复合运镜过载。
- [ ] 镜头描述可执行，无“电影感高级镜头”这类空词。
- [ ] 光线有明确演变或保持一致，无时间线冲突。

## 连续性

- [ ] 人物不换脸、不换装、不换鞋。
- [ ] 产品不变色、不消失、不复制、不穿模。
- [ ] 左右方向、运动轨迹、镜像正确。
- [ ] No-Face 策略已传递到人物锁、镜头、画面与负面约束。

## Human Realism（有角色时）

- [ ] 人物身份锁与真实感动态分开成段，Identity 不混入 blink / breathing / weight transfer。
- [ ] 参考素材职责与覆盖度明确，正脸缺失时未假装“参考图已锁脸”。
- [ ] 按景别只加载最小动态：静态胸像无 gait / foot placement / pelvic motion。
- [ ] 走路镜头未加载 nostril / pores / finger tendons，产品近景手部镜头未加载完整面部动态。
- [ ] 无人物项目未输出【人物真实感】，并写明 `HUMAN_REALISM: SKIP`。
- [ ] 动态由可执行动作链组成，没有用 photorealistic / 8K / masterpiece 冒充真实感。
- [ ] 多人项目有独立 `CHARACTER_ID` 与 `INTERACTION LOCK`，禁止 face merge / identity swap / clothing swap / body swap。
- [ ] Camera Language 明确且无理由不默认 handheld。
- [ ] 无真实视频时只输出 Pre-Generation Risk Score，不表述为实际画质成绩。

## QA

- [ ] SPEC / PRODUCT / CHARACTER / SCENE / ACTION / CAMERA / LIGHTING / SOUND / DIALOGUE / HUMAN_REALISM / CONTINUITY / NEGATIVE / ENDING 全部 PASS（无人物时 HUMAN_REALISM 为 SKIP）。
- [ ] 任一模块缺失标记 INCOMPLETE，不假装完整。
- [ ] Prompt Readiness Score 已给出，且不被误读为实际生成质量评分。
- [ ] 有角色项目已给出 100 分 Pre-Generation Risk Score，低于 70 未直接投喂。
- [ ] Motion Conflict QA 通过，无 `SHOT FEASIBILITY WARNING`。
