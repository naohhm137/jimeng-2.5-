# Human Realism Workflow

本工作流把人物输入升级为两层控制：

```text
Identity Layer = 这个人是谁
Realism Layer  = 这个人如何像真人一样活着
```

主流程在 V2 步骤 05-07 调用本工作流做全局路由，步骤 12-14 再按景别做逐镜修正，最终把结果写入项目对象的 `reference_analysis`、`characters[].identity_lock` 与顶层 `human_realism`。输入含参考素材时，V3 RIE（步骤 03-06）先产出 `REFERENCE SPEC`，Human Realism 只消费其中的 Identity Lock 与最小动态需求，不读取参考图描述。

## 自动路由

先判断人物是否存在，再判断加载什么。

```text
1. CHARACTER?
    NO
      -> human_realism.enabled = false
      -> skip_reason = "NO_CHARACTER"
      -> 停止，不生成 Human Realism 段落
    YES -> 继续

2. FACE VISIBLE?
    YES -> identity + face_dynamics + eye_dynamics + skin + micro_expression

3. BODY MOVEMENT?
    YES -> body_biomechanics

4. HAND INTERACTION?
    YES -> hand_dynamics

5. HAIR MOVEMENT?
    YES -> hair_dynamics

6. CLOTHING MOVEMENT?
    YES -> clothing_dynamics

7. MULTI-SHOT?
    YES -> temporal_consistency
```

`modules` 最终只保留这一步得到的最小充分列表，不把 15 个知识模块全部塞进 Prompt。

## Shot Distance Routing

| Shot Size | 加载重点 | 降低 |
|---|---|---|
| EXTREME_CLOSE_UP | eye / skin / lip / face / micro-expression / identity | body gait / clothing |
| CLOSE_UP / MEDIUM_CLOSE_UP | face / eyes / skin / hair / micro-expression / identity | 不写脚部与骨盆步态 |
| MEDIUM | face / body / hands / clothing | skin pores / nostril |
| FULL | body biomechanics / weight / feet / gait / hair / clothing / hands | facial pore 与微表情 |
| WIDE / EXTREME_WIDE | body trajectory / environment / camera | 面部细节，只保留头身比/发色/服装 |
| MACRO | product / material / hands | 人脸模块关闭 |

## Action 到 Dynamics

把动作词编译成可执行动态，至少支持以下动作：

| Action | Dynamics |
|---|---|
| STAND | posture adjustment / center of mass / micro balance / breathing |
| SIT | gaze to seat / weight lowers / head stabilizes / fabric delay |
| WALK | weight transfer / foot placement / gait / pelvic movement / arm swing / shoulder counter-movement / head stabilization / hair / clothing |
| RUN | higher stride frequency / center of mass forward / arm flexion / heel-to-toe / hair and clothing stronger inertia |
| TURN | eye lead / foot redirect / pelvis / shoulder / head delay / hair delay |
| LOOK | saccade / head turn follows / gaze hold target |
| TALK | lip / jaw / breathing / eye behavior / micro-expression / head micro-movement |
| SMILE | neutral -> subtle cheek -> peak -> relaxation |
| LAUGH | breathing rhythm / chest movement / eye squeeze / head shake small amplitude |
| CRY | brow / lid tension / breathing / tear film / jaw restraint |
| REACH | shoulder leads / arm extends / wrist rotates / hand opens before contact |
| PICK_UP | reach / finger wrap / thumb opposition / lift follows center of mass |
| PUT_DOWN | elbow lowers / fingers open gradually / object leaves hand without drop jump |
| HOLD | wrist neutral / grip pressure adjusts / small repositioning |
| TOUCH | fingertip contact / slight skin deformation / object responds |
| DRINK | eyes lower / hand lifts cup to lips / head tilts slightly / cup returns |
| EAT | jaw opens / lip contact / cheek movement / swallow |
| OPEN | hand contacts edge / wrist rotation / fingers spread / lid/fabric responds |
| CLOSE | same contact chain reversed, final state locked |
| LEAN | pelvis remains anchor / torso tilts / support hand optional / head stable |
| DANCE | rhythm drives weight transfer / limbs overshoot less / hair-clothing inertia stronger |

## 对话专用

人物说话时自动启用：

```text
lip movement
jaw movement
breathing
eye movement
micro-expression
head micro-movement
```

规则：

- 用户台词逐字写入 Dialogue Lock，Human Realism 不得改写台词。
- 口型先于首字出现，尾音结束后嘴唇闭合延迟 1-2 帧。
- 长句中间有自然呼吸停顿，句中轻微停顿不闭眼。
- 说话时头部有微小非周期性移动，禁止像提线木偶一样固定。

## Multi Character

- 每个角色独立 `CHARACTER_A` / `CHARACTER_B` Identity Fingerprint。
- `INTERACTION LOCK` 固定：

```text
relative position
gaze
distance
body orientation
hand interaction
object ownership
```

- 禁止 face merge / identity swap / clothing swap / body swap。
- 两人转身或靠近时，每个人分别完成自己的重心、视线和延迟，禁止复制镜像动作。

## Camera Language

为每个项目选择一种 capture language：

```text
TRIPOD / HANDHELD / PHONE / DOCUMENTARY / COMMERCIAL / CINEMATIC
```

规则：

- 无理由不默认 handheld。
- 运镜方向、对焦转移、曝光变化必须与人物动作绑定。
- 镜头语言与人物运动冲突时输出 `SHOT FEASIBILITY WARNING`。

## Temporal 编译

```text
WITHIN SHOT    身份/表情/衣服/灯光不跳变
CROSS SHOT     复用同一条 CHARACTER_ID
SEQUENCE STATE 上一镜结束状态 = 下一镜开始状态
```

每镜结束状态写入 Storyboard 的 `first_frame_state` / `subject_action` 增量，不做独立“一致性咒语”。

## 输出

把 `human_realism` 写入 `human-realism.schema.json` 结构：

```text
enabled
character_present
character_ids
shot_distance_routing
routing
reference_coverage
identity
facial_dynamics / skin / hair / body / hands / clothing
camera / environment / temporal
dialogue
interaction_lock
anti_ai_rules
score
```

没有人物时只写：

```json
{
  "enabled": false,
  "character_present": false,
  "skip_reason": "NO_CHARACTER"
}
```

## 返回 QA

完成后运行 `human-realism/realism-qa.md` 的检查。分数低于 70 时回到对应模块修复，再由 `prompt-compiler.md` 编译。
