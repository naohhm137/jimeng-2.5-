# Client Learning（AI 学习客户的提速协议）

同一客户只学一次：第一次把客户素材压缩成一张可复用的 CLIENT CARD；之后生成新视频只读 CLIENT CARD，不重扫客户原始素材包。

## 触发词

用户说出下列任一意图时进入本流程：

```text
学习这个客户 / 认识这个客户 / 客户是什么风格
新客户 / 客户首次素材 / 客户资料包
老客户：<客户名>，再做一条
同品牌 / 同客户继续用之前定的规则
客户资料有更新 / 客户改了产品或方向
```

只学习时输出 CLIENT CARD，不输出视频 Prompt；学习并生成时先出卡，再按 `main-pipeline.md` 继续。

## AI Read Budget（读卡预算）

```text
首次学习  只读：本文件 + templates/client-card-template.md + 客户素材索引
复用      只读：已有 CLIENT CARD + SKILL.md + 本次模板
更新      只读：CLIENT CARD + 用户指出的新增素材，不重扫旧素材
禁止      开局扫 references/、human-realism/、reference-intelligence/ 全目录
```

同一客户第二次生成时，若没有出现 `客户资料有更新`，任何新素材都不能静默推翻 CLIENT CARD 已确认锁；冲突先输出 `CLIENT CONFLICT`（Winner / Reason / Action），再决定是否升级卡片版本。

## 流程

```text
C1 CLIENT DETECTION       判断是全新客户、老客户复用还是客户资料更新
C2 SINGLE-PASS EXTRACTION 只提取 CLIENT CARD 需要的字段，一次完成
C3 CLIENT CARD COMPILE    输出一页卡，超长素材合并成可复用锁，不留整包描述
C4 CLIENT CARD LOCK       区分稳定锁与本次增量，避免下次重复问
C5 REUSE ROUTE            后续项目只消费卡片，不再重读客户素材
```

字段必须来自客户实际素材或用户明确确认；没有证据时写 `UNKNOWN / NEEDS_INPUT`，不编造。

## 客户卡存放

- CLIENT CARD 保存到用户指定目录或当前任务客户文件夹，如 `<客户工作区>/client-cards/<client-id>.md`；客户素材与业务事实不进本 Skill 库。
- 找卡顺序：用户指定路径 → 本会话已引用卡片 → 上述 `client-cards/` 约定路径；找不到再问，不扫客户原始素材目录找风格。
- 同一客户始终维护同一张卡：更新在原卡上做，升 `CARD_VERSION` 并在“变更记录”追加一行，不另存 `<client-id>_v2.md`。
- 卡内只写素材路径/编号作为证据，不复制整包图片或原文。

## 输出形态

```text
CLIENT ID：
CARD VERSION：
本次模式：CREATE / REUSE / UPDATE
已确认锁：<稳定可跨项目复用的内容>
本次新增或变更：<delta，无则 NO CHANGE>
待确认：<不超过 3 条，不逐条盘问>
下次生成入口：<直接给本次产品/卖点/动作即可>
```
