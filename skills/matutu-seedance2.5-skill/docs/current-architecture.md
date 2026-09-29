# Current Architecture Audit

审计日期：2026-09-07
仓库：`matutu-ai/seedance2.5-skill`
技能：`seedance-2-5-prompt`
版本：V3.0 Reference Intelligence Engine + Human Realism Engine（保留 V1/V2 全部能力）

## 1. 当前功能

- 自动识别产品图、人物图、场景图、产品资料、广告 Brief、完整分镜、参考视频、已有 Prompt 与混合输入。
- 对输入执行 V3 28 步导演流程：输入识别 → 输入规范化 → Reference Role 分类 → Reference 证据提取 → Reference 优先级 → Reference 冲突解决 → 产品/主体分析 → 人物身份锁 → Human Realism 路由 → Human Motion Engine → 视频目的 → 创意结构 → Hook 设计 → 分镜 → 景别路由 → 镜头可行性 → 逐镜 Human Realism 编译 → Camera Language → 时间连续性 → 连续性锁 → 声音设计 → Prompt 编译 → Human Realism QA → Prompt Readiness QA → Pre-Generation Risk Score → Reference QA → Repair Routing → 最终输出。
- V3 在 V2 24 步前插入 RIE 步骤 03-06；旧 V2 24 步与 V1 13 步兼容路由继续可用，V1/V2 编号不删除。
- 保留 V1/V2 兼容语义；旧输入没有 `reference_intelligence` / `human_realism` 字段时自动补默认判定：有角色进入 Human Realism Engine，无角色显式 SKIP，无参考素材不虚构覆盖度。
- 把决策结果编译为可直接投喂 Seedance 2.5 / 即梦 / 豆包的提示词。
- 支持三种输出形态：一次性投喂版（默认）、逐段独立投喂版、完整导演方案版。
- 客户学习模式：首次客户素材压缩为 CLIENT CARD，后续项目按卡复用，不重复扫客户素材包。
- 通过 JSON Schema 定义跨 Skill 项目接口，并提供 fixture 与回归校验。

## 2. Reference Intelligence Engine + Human Realism Engine

Reference Intelligence Engine（RIE）回答“参考素材负责锁什么、证据是什么、冲突归谁”，不回答“这段画面写得美不美”。RIE 执行：

```text
1. 判断参考素材职责（Role）
2. 提取视觉信息（Evidence Extraction）
3. 建立优先级（Priority）
4. 生成 Lock（Character / Product / Scene / Camera / Motion）
5. 解决冲突（Conflict Resolution）
6. 将 REFERENCE SPEC 交给 Prompt Compiler
```

核心公式是 RIF（Reference Intelligence Formula）：`RIF = Role × Identity × Subject × State × Environment × Style × Lighting × Composition × Camera × Motion × Physics × Continuity × Constraints`。每张参考图只负责一个主 Role：人物图锁脸，产品图锁产品，场景图锁空间，动作视频锁 Motion 与 Camera Motion；Reference 描述不直接进 Prompt，先落成 `derived_locks` / `rif_blocks`，再由 Prompt Compiler 消费。

### Human Realism Engine

Human Realism 是行为层，不是形容词层。核心关系：

```text
Identity != Realism
Reference != Prompt
Motion != Camera
Realism != photorealistic / 8K / masterpiece
Consistency != 重复同一句一致性咒语
```

执行顺序：

1. 有没有人物：无人物写 `enabled=false`、`skip_reason=NO_CHARACTER`，不生成【人物真实感】。
2. 脸可见吗：可见才加载 face / eye / skin / micro-expression / identity。
3. 身体动不动：动才加载 body biomechanics / weight / gait。
4. 手有没有交互：有才加载 hand dynamics / object contact。
5. 头发/衣服动不动：动才加载 inertia / delayed response。
6. 是否多镜：是才加载 temporal consistency。

景别路由只保留最小充分模块：静态胸像不加载 gait，走路镜头不加载 pores / nostril / finger tendons，产品近景出现手时加载 hand dynamics 而不是完整面部动态。

## 3. 当前输入

- 产品图片 / 人物图片 / 场景图片
- 产品资料 / 卖点 / 参数
- 参考视频 / 参考图片
- 完整分镜 / 广告 Brief / 已有 Prompt
- 视频创意 / 规格（时长、画幅、帧率、字幕、BGM）

## 4. 当前输出

- 默认：精简一次性投喂版，可直接粘贴 Seedance / 即梦。
- 拆段需求：逐段独立投喂版，注明拼接顺序与转场要求。
- 完整方案需求：先输出叙事框架与导演决策，再附一次性投喂版。
- 分析需求：仅输出结构拆解，不生成 Prompt。
- 有参考素材项目：先产出 `REFERENCE SPEC`（role / priority / confidence / derived locks / conflicts），再编译 Prompt；Reference Intelligence Score 只衡量参考智能。
- 有角色项目：附 `PRE-GENERATION RISK SCORE`（100 分制）与等级。

## 5. 当前目录结构

```text
seedance2.5-skill/
├── README.md
├── seedance-2.5-prompt-template.md   # 可复用模板快速副本（单一真源见 references/template.md）
├── docs/
│   ├── current-architecture.md
│   ├── corpus-adoptions.md           # 网络语料采用记录与来源
│   └── human-realism-research.md     # Human Realism 研究资料与采用原则
└── seedance-2-5-prompt/
    ├── SKILL.md                      # Skill 入口与模块路由
    ├── QUICK-START.md                # 用户 30 秒最短路径
    ├── agents/openai.yaml
    ├── schemas/
    │   ├── video-project.schema.json # 顶层项目接口（含可选 reference_intelligence）
    │   ├── reference-intelligence.schema.json # RIE Spec
    │   ├── reference-role.schema.json # Reference 角色定义
    │   ├── reference-lock.schema.json # Reference 派生锁
    │   ├── reference-conflict.schema.json # 冲突与仲裁结果
    │   ├── subject-lock.schema.json  # 锁系统 + identity/motion/temporal lock
    │   ├── human-realism.schema.json # Human Realism Engine
    │   ├── storyboard.schema.json    # 分镜镜头
    │   └── dialogue.schema.json      # 对白锁
    ├── reference-intelligence/       # 15 个 Reference Intelligence 知识模块
    ├── workflows/
    │   ├── main-pipeline.md          # V3 28 步 + V2 24 步 + V1 13 步兼容路由
    │   ├── client-learning.md        # 客户学习模式：CLIENT CARD 复用与读卡预算
    │   ├── human-realism.md          # Human Realism 工作流入口
    │   └── ...
    ├── human-realism/                # 15 个 Human Realism 知识模块
    ├── references/                   # 速查表、学习进阶、模板、QA、规则与连续性约束
    ├── templates/                    # 按用途细分的可投喂模板（含 Reference 模板）
    ├── assets/existing-examples/     # 示例与 Pipeline Run 记录
    └── tests/
        ├── README.md
        ├── run_tests.py
        ├── fixtures/                 # 1 个 V1 fixture + 11 个 Human Realism fixture + 7 个 RIE fixture
        │   ├── reference-character/  # Character Identity Lock
        │   ├── reference-product/    # Product Lock + allowed_transformations=false
        │   ├── reference-video/      # Motion / Camera Motion Lock
        │   ├── reference-scene/      # Scene Lock
        │   ├── reference-multi-image/ # 多角色多 Lock（人物 + 产品 + 场景）
        │   ├── reference-conflict/   # 冲突仲裁
        │   └── reference-no-character/ # 无人物 SKIP
        ├── *.md                      # 场景测试输入
        └── results/*.md              # V1/V2/V3 回归基线（Final Prompt + QA）
```

## 6. 模板与一致性

- 用户快速路径：`QUICK-START.md`，只读最短 4 文件即可开始；细节按需读取。
- 写作速查：`references/quick-reference.md`，集中输出顺序、景别路由、动作动态、修复路由与 QA 分数。
- Reference 速查：`reference-intelligence/reference-role.md`、`reference-priority.md`、`reference-conflict-resolution.md`。
- 学习进阶：`references/learning-path.md`，8 轮渐进练习 + 会话输出模板 + 综合 QA 检查；SKILL.md 与 QUICK-START 都路由到此模块。
- 客户学习：`workflows/client-learning.md` 为唯一入口，客户卡模板见 `templates/client-card-template.md`。
- 可复用提示词模板的单一真源是 `seedance-2-5-prompt/references/template.md`。
- 根目录 `seedance-2.5-prompt-template.md` 是面向复制使用的快速副本，内容必须与真源一致；`tests/run_tests.py` 会校验两者同步。
- 编译顺序不可乱：规格 → 导演意图 → 参考素材职责 → 产品/人物锁 → 人物真实感（可选）→ 时间轴 → 摄影 → 光线 → 声音 → 连续性 → 负面约束 → 结尾状态。
- 对白较多时在规格后加【口播台词表｜逐字锁定】。
- Human Realism 分层模板见 `templates/human-realism-template.md`。
- 客户卡模板见 `templates/client-card-template.md`，只做一页式跨项目复用卡。

## 7. 核心规则

- 0-3 秒第一帧必须在动作中间，不是空镜或慢速入场。
- 每个参考素材声明“负责什么 + 不负责什么”；覆盖度缺失时记录为 MISSING，不假装存在。
- Identity Lock 全片只写一次，时间轴只写本镜增量。
- 产品默认禁止改设计；变形必须由用户明确开启并锁定前后状态。
- 对白逐字锁定，标注起止时间与 `repeat_count=1`，不回声不重复；Human Realism 不改写用户台词。
- 每个项目只选一种 Camera Language：TRIPOD / HANDHELD / PHONE / DOCUMENTARY / COMMERCIAL / CINEMATIC；无理由不默认 handheld。
- 多人项目每人独立 `CHARACTER_ID`，并维护 `INTERACTION LOCK`。
- 商业 TVC、30 秒长片、旁白片、多人围桌与复杂产品动作进入分镜前，先读取 `references/commercial-directing-rules.md`。
- 负面约束只写高风险项，不使用无信息的大词堆叠。
- 结尾必须有明确收束状态，避免模型硬切。

## 8. 质量保障

- `tests/run_tests.py` 校验文件存在性、Schema JSON 合法性、Human Realism 知识模块存在性、fixture 的 Schema 符合性、SKIP 语义、最小充分动态、Reference 语义规则、Reference QA 键与总分、结果文件结构、时间轴连续性与模板同步。
- 客户学习模式由同一测试入口校验：`client-learning.md` 与客户卡模板存在，SKILL/QUICK-START 正确路由，模板保持固定分段。
- 11 个 Human Realism fixture 覆盖：说话头、行走、产品手部交互、静态肖像、特写、全身、对白、多人、远景、无人物与修复路由。
- 7 个 Reference Intelligence fixture 覆盖：人物、产品、场景、动作视频、多角色、冲突仲裁与无人物 SKIP；每个 fixture 同时满足 `video-project.schema.json` 与 Reference 语义断言。
- 结果文件必须包含全部提示词段落、时间轴连续覆盖到目标时长、QA 明确 `READY`。
- 旧 V1/V2 回归结果保留为既有能力基线，不因 V3 新增字段而重写。

## 9. 架构边界

- 本 Skill 只负责“怎么拍”与“怎么告诉模型拍出来”。
- 不做海外市场研究、TikTok 爆款研究、用户画像、竞品营销分析、广告投放策略或 TikTok Shop 运营。
- 保留既有能力：4-30 秒、9:16 默认、无字幕、无 BGM、时间码、锁系统、连续性、负面约束、结尾状态、10/15/30 秒常用结构与既有示例。
