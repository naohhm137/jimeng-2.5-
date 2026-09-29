# Reference Priority System

多个参考素材不能平均融合。先定每个素材的优先级，再进入冲突解决。

## 四级 Lock Level

```text
HARD_LOCK        不可覆盖，作为项目硬约束
SOFT_LOCK        默认保留，用户明确指令可覆盖
STYLE_REFERENCE  只进入风格/质感/氛围层
INSPIRATION      只作为灵感，不进入锁
```

## 默认优先级

```text
IDENTITY = 100
PRODUCT IDENTITY = 100
PRODUCT DESIGN = 100
WARDROBE = 90
POSE = 80
ACTION = 80
SCENE = 70
CAMERA = 70
LIGHTING = 60
STYLE = 50
COLOR = 40
INSPIRATION = 20
```

数值越大越不可被低优先级素材覆盖。允许项目覆盖默认值；覆盖必须写明原因。

## Canonical Role → 默认优先级

```text
CHARACTER_IDENTITY    100  HARD_LOCK
PRODUCT_IDENTITY      100  HARD_LOCK
PRODUCT_DETAIL        100  HARD_LOCK（产品设计硬约束）
PRODUCT_MATERIAL       90  HARD_LOCK
PRODUCT_USAGE          80  SOFT_LOCK
CHARACTER_APPEARANCE   90  HARD_LOCK（人物外观锚点）
WARDROBE               90  HARD_LOCK
POSE                   80  SOFT_LOCK
ACTION                 80  SOFT_LOCK
SCENE                  70  SOFT_LOCK
ENVIRONMENT            70  SOFT_LOCK
ARCHITECTURE           70  SOFT_LOCK
CAMERA                 70  SOFT_LOCK
CAMERA_MOTION          70  SOFT_LOCK
LIGHTING               60  SOFT_LOCK
COMPOSITION            60  SOFT_LOCK
VISUAL_STYLE           50  STYLE_REFERENCE
COLOR_PALETTE          40  STYLE_REFERENCE
OVERALL_STYLE          40  STYLE_REFERENCE
TIMING                 50  STYLE_REFERENCE
MOTION                 80  SOFT_LOCK
AUDIO                  40  STYLE_REFERENCE
```

## 覆盖顺序

```text
用户明确指令
> HARD LOCK
> 默认 Reference Priority
> 同优先级 confidence
> 覆盖度更高者
> 模型默认推断
```

## 优先级与 subject-lock 的关系

V3 Reference Priority 是“素材证据层”优先级；`subject-lock.priority` 的 1-10 是“最终锁”优先级。二者不混用：

```text
reference_priority 决定哪张参考素材是证据赢家
subject_lock.priority 决定锁在 Prompt 中的不可覆盖级别
```

Reference 冲突在步骤 06 解决后，赢家证据才进入 Lock；Lock 之间仍有冲突时按 1-10 的 subject-lock priority 裁定。

## 单素材也要输出 priority

只有一个参考素材时同样输出 priority、confidence、lock_level；默认值不等于可以跳过。
