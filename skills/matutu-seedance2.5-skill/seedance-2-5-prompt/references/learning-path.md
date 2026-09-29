# Learning Path（学习进阶模块）

本文件是“学习本 Skill”与“练习下一步”的唯一真源。用户表达学习意图时，不要进入 V2 24 步 / V3 28 步生成 Pipeline，先命中下方触发词，再执行对应轮次。

## 触发词

```text
继续学习本 Skill
本轮练习：第 X 轮 / <轮次名>
学完之后下一步学什么
我已跑完学习轮次表
我的第 X 版又出现了 <症状>
```

没有明确说明已完成多少时，只回一个问题：`当前你做到第几轮？` 不要问专业术语，也不要一次发整张轮次表。

## 会话输出模板

每次学习会话只输出下面五块，不输出完整 Prompt、不输出 V2 24 步 / V3 28 步流程：

```text
当前轮次：第 X 轮 <轮次名>
本轮目标：<一条可观察目标>
本轮锁：只练 <Y>；其他模块出现小瑕疵也先记录不修
可观察变化：完成标准是 <1 个回放可确认现象>
练习口令：<一段可直接粘贴给 Seedance / 即梦 的最小练习 Prompt>
```

练习口令必须是该轮最小样例，例如只练产品锁时只输出产品图 + 5 秒产品使用镜头，不夹带人物、对白与复杂分镜。

## 轮次表

| 轮次 | 名字 | 只练什么 | 完成标准（回放可确认） | 本轮查 |
|---|---|---|---|---|
| 1 | 回放诊断 | 找出自己视频里 1 个最假的位置 | 能写清“哪一秒、什么现象、怀疑哪个模块” | `references/checklist.md` |
| 2 | 参考职责 | Role + Priority + INHERIT + DO NOT INHERIT（V3 可读 RIE 模块） | 每张参考图职责不重叠，正脸缺失时写 `MISSING`，冲突时写明 winner | `reference-intelligence/reference-role.md`、`reference-priority.md`、`references/reference-asset-prompts.md`、`human-realism/reference-analysis.md` |
| 3 | 产品锁 | 产品全程不变形、不变 Logo、不变结构 | 同一产品跨 3 个机位形状一致 | `references/product-lock-rules.md`、`workflows/product-multi-view.md` |
| 4 | 人物锁 | 同一人跨所有镜头不换脸 | 每个时间轴段沿用同一条 `CHARACTER_ID`，不重写长相 | `human-realism/identity.md`、`human-realism/temporal-consistency.md` |
| 5 | 动作动态链 | 只练一个动作：走路 / 坐下 / 拿杯 | 动作有准备 → 发力 → 接触 → 反应 → 恢复，衣摆或头发有延迟 | `human-realism/body-biomechanics.md`、`references/quick-reference.md` |
| 6 | 景别最小动态 | 只练一个景别的人体模块 | 特写不出现步态；全景不出现毛孔与眼神细节 | `human-realism/HUMAN-REALISM.md` |
| 7 | 时间连续性 | 上一镜结束状态 = 下一镜开始状态 | 切镜后位置、朝向、服装、光线无跳变 | `workflows/continuity.md`、`references/continuity-rules.md` |
| 8 | QA 门禁 | 低于 70 分不投喂 | 每版都能给出完整 Risk Score，未达标先回模块补齐 | `human-realism/realism-qa.md`、`human-realism/repair-routing.md` |

## 症状路由（练习中遇到问题时）

只根据用户说的症状读取一个模块；不要一次读完整批 Human Realism 文件。

| 用户说 | 只读 |
|---|---|
| 脸越来越不像 | `human-realism/identity.md` + `temporal-consistency.md` |
| 眼睛像玻璃 / 眼神呆 | `human-realism/eye-dynamics.md` |
| 表情一直一样 / 脸僵 | `human-realism/face-dynamics.md` + `micro-expression.md` |
| 走路像机器人 | `human-realism/body-biomechanics.md` |
| 手指畸形 / 拿东西假 | `human-realism/hand-dynamics.md` |
| 衣服飘 / 像贴纸 | `human-realism/clothing-dynamics.md` |
| 头发像假发 | `human-realism/hair-dynamics.md` |
| 皮肤塑料感 | `human-realism/skin-dynamics.md` |
| 说不清哪里假 | `human-realism/repair-routing.md` |

## 综合 QA 练习

用户完成第 8 轮并说“我已跑满学习轮次表”时，不要自动进入第 9 轮；改为让用户投喂一个新项目，对生成结果执行 10 项一次性检查：

```text
IDENTITY / EYES / SKIN / HAIR / BODY / HANDS / CLOTHING
/ CONTINUITY / REFERENCE COVERAGE / QA GATE
```

每项只给 `PASS` 或 `FAIL`。8 项以上 `PASS` 视为毕业；否则只把失败项作为下一轮练习内容，不重跑已通过部分。
