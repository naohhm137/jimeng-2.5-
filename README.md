# Seedance Skills

此仓库收录两套 Seedance / 即梦 Agent Skills，分别保留上游目录结构、配套参考资料和原始说明文档。

## 收录内容

| Skill | 入口文件 | 内容 |
|---|---|---|
| Seedance 2.5 Director | [`skills/seedance2.5-skills/seedance-25/SKILL.md`](skills/seedance2.5-skills/seedance-25/SKILL.md) | 面向 Seedance 2.5 的导演式提示词工作流、参考资料、提示词检查器。 |
| Seedance Prompt Skill | [`skills/seedance2.5-prompt-skill/SKILL.md`](skills/seedance2.5-prompt-skill/SKILL.md) | Seedance 2.0 / 2.5 中文提示词技能，以及 references、实验案例和项目文档。 |

## 使用

将目标 skill 的目录复制到所用 Agent 的 Skills 搜索路径，并以 `SKILL.md` 所在目录作为 skill 根目录：

- Seedance 2.5 Director：`skills/seedance2.5-skills/seedance-25/`
- Seedance Prompt Skill：`skills/seedance2.5-prompt-skill/`

例如，可复制到 Claude Code 的 `~/.claude/skills/` 或项目级 `.claude/skills/`。其他 Agent 的安装路径请按其文档调整。

## 上游来源与版本

- [sjinn-ai/seedance2.5-skills](https://github.com/sjinn-ai/seedance2.5-skills) — 导入上游提交 `6db1b37e51b3d64ead12722faf5d71f0666d3f93`；skill 主目录位于 `seedance-25/`。
- [ye4wzp/seedance2.5-prompt-skill](https://github.com/ye4wzp/seedance2.5-prompt-skill) — 导入上游提交 `b093438a133ebc3fe81cd1be214271a222516919`。

导入日期：2026-09-29。更新上游内容时请保留来源、许可证和作者署名信息，并检查上游差异。

## 许可与署名

- `skills/seedance2.5-prompt-skill/` 保留上游 `LICENSE`、README 和其中关于 [MapleShaw](https://github.com/MapleShaw/seedance2.0-prompt-skill) 等原作者的署名说明。请以该目录内的许可证与署名文件为准。
- `skills/seedance2.5-skills/` 的上游仓库未声明公开许可证。此处文件的导入基于仓库维护者对复制权限的确认；本仓库不对这些上游文件额外授予再分发或改编许可。使用或再分发时请遵循权利人的授权范围。
