# Seedance 2.5 QUICK-START（30 秒上手）

本文件只解决一个问题：让新用户尽快从“不知道文件有什么用”进入“能生成第一条 Prompt”。详细导演学、Human Realism 模块与 V2 24 步 / V3 28 步流程不要在这里学，遇到具体问题时再按需读取。

## 最短文件路径

```text
1. QUICK-START.md               本文件：决定怎么做
2. ../seedance-2.5-prompt-template.md  输出骨架：直接填空
3. references/quick-reference.md 写作速查：景别/动作/修复查表
4. references/checklist.md      投喂前 10 秒检查
```

不要为了写一条 Prompt 读完整个库。默认只打开上面 4 个文件；只有 QA 不通过或用户反馈具体症状时，才进入 `workflows/`、`human-realism/` 与 `references/` 的细节文件。

## 上传素材一句话出片（V3 自动流）

最简单用法：用户不需要填写复杂 Prompt。

```text
用户上传：人物图 / 产品图 / 场景图 / 动作参考视频
用户只说：做一个15秒商业广告，产品卖点是 XXX。
```

Skill 自动执行：

```text
识别素材
→ 分配 Role
→ 提取证据
→ 建立优先级
→ 解决冲突
→ 生成 Character / Product / Scene / Camera / Motion Lock
→ 生成导演方案
→ 分镜
→ Human Realism
→ Seedance Prompt
```

Reference Intelligence 会先产出 `REFERENCE SPEC`（每个素材的 role / priority / confidence / derived locks），再编译 Prompt；它不会把参考图描述直接当 Prompt 用。每张上传图只负责一个主 Role：人物图锁脸，产品图锁产品，场景图锁空间，动作视频锁 Motion 与 Camera Motion。

完整版 Prompt 必须在【参考素材职责】中给出 `REFERENCE DECISION` 与 `PROMPT USAGE MAP`：写清每个 `@图片N` 的判断依据、可继承内容、MISSING、作用模块和具体镜头/时间段；没有实际使用位置的参考素材不能进入 READY。

## 同一客户第二次更快（客户学习模式）

第一次遇到新客户或品牌素材时，先说一句“学习这个客户”。AI 只做一张 CLIENT CARD（品牌、产品、风格基线、稳定锁、待确认问题），不生成视频 Prompt。之后同客户再要新片，说“老客户：<客户名>，本次产品/卖点是...”，AI 会先调 CLIENT CARD 再生成，不重扫客户原始素材包。

客户方向或产品变了，说“客户资料有更新”并附新素材，只补差异，不复述已确认内容。规则见 `workflows/client-learning.md`，卡片模板见 `templates/client-card-template.md`。

## 三步开始

1. 复制根目录 `seedance-2.5-prompt-template.md`。
2. 用下面的项目速填卡收集信息，把已知字段直接填进模板。
3. 按模板顺序输出，投喂前用 `references/checklist.md` 检查。

模板输出顺序不可乱：

```text
规格 → 导演意图 → 参考素材职责 → 产品锁 → 人物锁
→ 人物真实感（可选）→ 场景锁 → 时间轴
→ 摄影 → 光线 → 声音 → 连续性 → 负面约束 → 结尾状态
```

## 项目速填卡

没有完整 Brief 时，只向用户收集这一张卡，不要逐条问专业术语：

```text
时长与画幅：
产品与参考图：
人物与参考图：
核心动作或剧情：
对白：
场景与风格：
镜头要求：
必须保留/禁止出现：
```

缺省值由 Skill 自动补齐，不必让用户回答：

```text
画幅未指定 -> 9:16
BGM 未指定 -> 无
字幕未指定 -> 无
时长未指定 -> 10-15 秒，按内容复杂度选择
```

## 输入速判

| 输入 | 你只需关注 | 不要读 |
|---|---|---|
| 产品图/资料，无清晰人物 | 产品锁、多视角、packshot | Human Realism 15 个模块 |
| 人物照/人物使用产品 | 人物锁、人物真实感最小模块 | 无关的 gait / pores / hand 细节 |
| 参考视频 | 原创重构、镜头结构 | 逐条复制原视频内容 |
| 已有 Prompt | 诊断、局部修复 | 整段重写 |
| 广告 Brief / 分镜 | 导演方案 + 分镜 | 过早读 QA 与修复路由 |

## 生成后只查四件事

```text
1. 每个时间轴段是否都有 SHOT / ACTION / CAMERA / AUDIO
2. 每张参考图是否写了 ROLE + INHERIT + DO NOT INHERIT + `PROMPT USAGE MAP`
3. 无人物时没有【人物真实感】；有角色时没写 gait 到静态胸像
4. QA 明确 READY，低于 70 的 Risk Score 没有直接投喂
```

## 出问题再看哪个文件

| 反馈 | 读 |
|---|---|
| 脸越来越不像 | `human-realism/identity.md` + `temporal-consistency.md` |
| 眼睛像玻璃/眼神呆 | `human-realism/eye-dynamics.md` |
| 走路像机器人 | `human-realism/body-biomechanics.md` |
| 衣服飘/折痕假 | `human-realism/clothing-dynamics.md` |
| 手畸形 | `human-realism/hand-dynamics.md` |
| 其他症状 | `human-realism/repair-routing.md` 先定位，再局部修 |

完整路由表见 `SKILL.md` 的“按需路由”；每类动作怎么写见 `references/quick-reference.md`。

## 想先学习再动手

1. 打开一个成品示例，例如 `assets/existing-examples/example-15s-old-money-linen-shirt-film.md`。
2. 对照模板看它如何填空：规格、参考素材职责、产品锁、人物锁、人物真实感、时间轴。
3. 把示例换成自己的产品，先只改“产品锁 + 时间轴”，其余段落沿用模板，跑通后再学景别与动作细节。

## 跑通后：学习进阶

第一版已能投喂并产出可用视频后，进入 8 轮渐进练习。完整轮次表、会话模板与综合 QA 见 `references/learning-path.md`，本文件不再重复维护：

```text
第 1 轮 回放诊断 → 第 2 轮 参考职责 → 第 3 轮 产品锁
→ 第 4 轮 人物锁 → 第 5 轮 动作动态链 → 第 6 轮 景别最小动态
→ 第 7 轮 时间连续性 → 第 8 轮 QA 门禁
```

每轮开始时把下面这段发给支持本 Skill 的对话，它会按轮次表给出 3 个检查点、1 个对照示例和可观察变化：

```text
继续学习本 Skill。
当前已完成：<示例名或自己第几版 Prompt>。
本轮练习：<第几轮 / 轮次名>。
```

练满 8 轮后发送“我已跑满学习轮次表”，按 `references/learning-path.md` 执行综合 QA 练习。
