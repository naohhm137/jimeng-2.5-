# Tests

测试用途：验证 Skill 升级后仍能完成核心导演流程，并保留既有能力。

## 测试列表

| 文件 | 场景 | 核心断言 |
|---|---|---|
| `product-video.md` | 运动摇摇杯，无脸、多视角、10秒 | PRODUCT LOCK、无清晰人脸、同一产品多视角 |
| `multi-view-product.md` | 耳机，产品锁、多视角、微距、无脸 | 产品不漂移、视角完整 |
| `character-product.md` | 人物使用产品 | 人物/产品一致、连续动作 |
| `dialogue-video.md` | 口播视频 | 对白逐字、品牌读音、无回声 |
| `reference-video.md` | 参考视频重构 | 原创方案、不复制内容 |
| `prompt-optimization.md` | 已有 Prompt 优化 | 保留原创意、修复时间轴/过载/连续性 |
| `industrial-product.md` | 工业产品 | 结构不变、工业场景、多视角 |

`results/` 存放每条测试执行 `workflows/main-pipeline.md` 后的最终 Prompt 与 QA 结果，作为回归基线。

## Fixtures

`fixtures/` 存放结构化样例，供自动化校验使用：

| 文件 | 用途 | 校验方式 |
|---|---|---|
| `video-project.valid.json` | 运动摇摇杯 10 秒多视角 V1/V2 基线项目，覆盖产品锁、分镜、声音、连续性、QA | 用本地 JSON Schema registry，按 `video-project.schema.json` 完整校验 |
| `video-project.human-realism-*.json` | 11 个 Human Realism 场景：说话头、行走、产品手部交互、静态肖像、特写、全身、对白、多人、远景、无人物与修复路由 | Schema 校验 + `check_human_realism_fixture` 语义断言（SKIP、最小充分动态、风险分） |
| `reference-character/video-project.reference-character.json` | 人物参考图只锁身份，输出 CHARACTER_IDENTITY Role 与 Identity Lock | Schema 校验 + `check_reference_fixture` |
| `reference-product/video-project.reference-product.json` | 产品参考图锁产品，默认 `allowed_transformations=false` | Schema 校验 + `check_reference_fixture` |
| `reference-video/video-project.reference-video.json` | 动作参考视频提取 Motion / Camera Motion / Timing 证据 | Schema 校验 + `check_reference_fixture` |
| `reference-scene/video-project.reference-scene.json` | 场景参考图只锁空间，不越权锁主体 | Schema 校验 + `check_reference_fixture` |
| `reference-multi-image/video-project.reference-multi-image.json` | 人物 + 产品 + 场景混合上传，多角色分工并生成三个 Lock | Schema 校验 + `check_reference_fixture` |
| `reference-conflict/video-project.reference-conflict.json` | 两张参考互相冲突时进入仲裁，输出 winner 与 resolved | Schema 校验 + `check_reference_fixture` |
| `reference-no-character/video-project.reference-no-character.json` | 无人物参考项目，Human Realism 显式 SKIP | Schema 校验 + `check_reference_fixture` |

`run_tests.py` 同时发现根目录扁平 fixture 与 `reference-*/` 子目录内的 fixture，因此 V3 Reference fixture 建议放在 `reference-*` 子目录中，便于语义断言按文件名分类执行。Reference Intelligence Score 必须包含六项子分（Role Accuracy / Feature Extraction / Priority Accuracy / Conflict Resolution / Lock Completeness / Prompt Mapping）且总分为 100；`reference-*` fixture 必须满足对应 Role、Lock、冲突或 SKIP 语义。

新增 fixture 时保持命名规则 `video-project.<场景>.json`，并确保能被 Schema 校验通过；需要记录“应失败”的边界样例时，在 `tests/README.md` 说明失败原因，不要放入会被 `run_tests.py` 自动要求通过的目录。

## 运行方式

1. 运行 `python3 tests/run_tests.py`。它校验：
   - 工作流、Schema、模板与测试文件是否存在；
   - `QUICK-START.md` 与 `references/quick-reference.md` 存在，且与 SKILL/模板正确互链；
   - `references/learning-path.md` 存在，SKILL 与 QUICK-START 正确路由到学习进阶模块；
   - `workflows/client-learning.md` 与 `templates/client-card-template.md` 存在且正确互链；
   - 每个 Schema 是否为合法 JSON；
   - fixture 是否满足 Schema（含跨文件 `$ref`，需已安装 `jsonschema` 与 `referencing`）；
   - Human Realism fixture 的 SKIP、最小充分动态与风险分语义；
   - Reference fixture 的 Role、Lock、冲突仲裁、无人物 SKIP 与 Reference QA/Score 语义；
   - 每条 `results/*.md` 是否包含完整段落、时间轴连续到目标时长、QA 明确 `READY`；
   - 根目录 `seedance-2.5-prompt-template.md` 与 `references/template.md` 是否仍同步。
2. 新增或修改能力后，对每个测试重新执行 `workflows/main-pipeline.md`，把 Final Prompt 放入 `results/`。
3. 用 `references/checklist.md` 逐项复查，QA 标记 `READY` 才算通过。

Seedance 实际生成质量不在本测试范围；测试只验证 Prompt 就绪度。
