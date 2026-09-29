# Realism QA

Human Realism QA 是最终 Prompt 的生成前检查。没有真实生成视频时，只能输出 `PRE-GENERATION RISK SCORE`，不能假装完成视频视觉质量检测。

## 100 分制

```text
IDENTITY              20
EYES                  15
FACIAL DYNAMICS       15
SKIN                  10
HAIR                  10
BODY BIOMECHANICS     15
HANDS                  5
CLOTHING               5
TEMPORAL CONSISTENCY   5
-------------------------
TOTAL                100
```

## 等级

```text
90-100  CINEMA REALISM
80-89   COMMERCIAL REALISM
70-79   ACCEPTABLE
60-69   AI ARTIFACT RISK
<60     REGENERATE
```

低于 70 时必须回到对应模块补齐，不能直接投喂。

## 模块检查

```text
[ ] Identity Lock
[ ] Reference Coverage
[ ] Face Dynamics
[ ] Eye Dynamics
[ ] Skin Dynamics
[ ] Hair Dynamics
[ ] Body Biomechanics
[ ] Hand Dynamics
[ ] Clothing Dynamics
[ ] Camera Realism
[ ] Temporal Consistency
[ ] Anti-AI
```

## 过载与冲突检查

```text
[ ] 是否模块过载（不需要 body gait 的镜头没有加载 gait）
[ ] 是否重复（同一动态没有写两遍）
[ ] 是否存在冲突（gaze 方向与 body turn 冲突、相机方向与走位冲突）
[ ] 是否存在不必要的形容词
[ ] 是否符合镜头距离
[ ] 是否符合动作
```

## Motion Conflict QA

发现以下组合时输出 `SHOT FEASIBILITY WARNING`，而不是强行生成：

```text
camera 与 character 的运动方向互相矛盾
character 与 environment 的位置关系不成立
hand 与 object 的接触链不完整
body 超出 frame 的可容纳范围
action 无法在给定 duration 内完成
```

## 输出

把结果写入 `human_realism.score`：`total`、九个分项、`level`，并在 `qa` 字段标注 `HUMAN_REALISM_QA: PASS/WARNING`。
