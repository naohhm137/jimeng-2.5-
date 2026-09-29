# seedance2.5-skill

Seedance 2.5 Commercial Video Director + Reference Intelligence Engine + Human Realism Engine + Prompt Compiler。

自动识别产品图、产品资料、卖点、参考图/视频、分镜、广告 Brief、已有 Prompt，先由 Reference Intelligence Engine 给每份参考素材分类、提取证据、定优先级、仲裁冲突并产出 REFERENCE SPEC，再完成导演化、分镜、人物身份锁、Human Realism 动态路由、镜头可行性检查、连续性锁、声音设计，并编译为可直接投喂 Seedance 2.5 / 即梦 / 豆包的提示词。

## 定位边界

- Strategy 决定“拍什么”。
- 本 Skill 决定“怎么拍”。
- Prompt Compiler 决定“怎么告诉模型拍出来”。

本 Skill 不承担海外市场研究、TikTok 爆款研究、用户画像、竞品营销分析、广告投放策略或 TikTok Shop 运营。

## 目录

```text
seedance2.5-skill/
├── seedance-2.5-prompt-template.md
├── docs/
│   ├── current-architecture.md
│   ├── corpus-adoptions.md
│   └── human-realism-research.md
└── seedance-2-5-prompt/
    ├── SKILL.md
    ├── QUICK-START.md
    ├── agents/openai.yaml
    ├── schemas/
    ├── reference-intelligence/
    ├── human-realism/
    ├── workflows/
    ├── references/
    ├── templates/
    ├── assets/existing-examples/
    └── tests/
        ├── fixtures/
        ├── results/
        └── run_tests.py
```

## 快速使用

最快路径：先读 `seedance-2-5-prompt/QUICK-START.md`，再复制根目录 `seedance-2.5-prompt-template.md`，按顺序填写：

```text
规格 → 导演意图 → 参考素材职责 → 产品锁 → 人物锁 → 人物真实感（可选）→ 场景锁 → 时间轴 → 摄影 → 光线 → 声音 → 连续性 → 负面约束 → 结尾状态
```

对白较多时加【口播台词表｜逐字锁定】，品牌名和生僻词附拼音。

完整导演流程为 V3 28 步（在 V2 24 步前插入 Reference Intelligence 步骤 03-06），兼容旧 V2/V1 输入，入口见 `seedance-2-5-prompt/workflows/main-pipeline.md`；Reference Intelligence 路由见 `seedance-2-5-prompt/reference-intelligence/REFERENCE-ENGINE.md`；Human Realism 路由见 `seedance-2-5-prompt/workflows/human-realism.md`。

参考素材一律先产出 `REFERENCE SPEC`，不把参考图描述直接当 Prompt 用；每张图只负责一个主 Role：人物图锁脸、产品图锁产品、场景图锁空间、动作视频锁 Motion 与 Camera Motion。

无人物项目自动跳过 Human Realism，不输出【人物真实感】。

写作时常用规则集中在一页速查表：`seedance-2-5-prompt/references/quick-reference.md`。大多数项目查这一页即可，不用先读完 Human Realism 细节模块。

第一版能稳定投喂后，学习进阶走 `seedance-2-5-prompt/references/learning-path.md`：8 轮渐进练习，每轮只练一个可观察目标；说“继续学习本 Skill”即可获得下一轮任务，不用重读全库。

同一客户重复接片走客户学习模式：首次把客户素材压缩成一张 CLIENT CARD（模板见 `seedance-2-5-prompt/templates/client-card-template.md`），后续只读客户卡，不重扫客户素材包，流程见 `seedance-2-5-prompt/workflows/client-learning.md`。

## 校验

`seedance-2.5-prompt-template.md` 是 `seedance-2-5-prompt/references/template.md` 的快速副本，以 `references/template.md` 为单一真源。

运行 `python3 seedance-2-5-prompt/tests/run_tests.py` 校验 Schema、Human Realism 知识模块、fixture（含 11 个 Human Realism 场景与 7 个 Reference Intelligence 场景）、Reference 语义断言、结果文件结构与模板同步。

从公开语料吸收的规则与来源见 `docs/corpus-adoptions.md`。

## License

Copyright (c) 2026 matutu-ai. Released under the MIT License, see `LICENSE`.
