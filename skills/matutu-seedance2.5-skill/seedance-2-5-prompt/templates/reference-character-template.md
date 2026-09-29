# Reference Character Template

用途：人物参考图生成身份锁与人物真实感需求的规格，不生成最终 Prompt。

```text
REFERENCE ID: <image_01>
ROLE: CHARACTER_IDENTITY

CHARACTER_LOCK
identity: CHARACTER_A
face:
  face_shape:
  facial_proportions:
  eyes:
  eyebrows:
  nose:
  lips:
  jawline:
  cheekbones:
skin:
hair:
body:
age_appearance:
wardrobe:
accessories:

REFERENCE COVERAGE
FACE: HIGH / MEDIUM / LOW / MISSING
PROFILE: ...
HAIR: ...
BODY: ...
FULL BODY: ...
HANDS: ...
CLOTHING: ...
AGE / SKIN: ...
EXPRESSION: ...
LIGHTING: ...

IDENTITY vs HUMAN REALISM
Identity 只写“是谁”；blink/呼吸/重心/布料延迟一律不进入本表。

HUMAN REALISM ROUTING DEMAND
需要 Human Realism Engine 判断：
- 人物是否出镜
- 脸是否可见
- 是否需要 body / hands / clothing / temporal modules
```

规则：

- 正脸缺失时 FACE = MISSING，身份锁只写可达上限。
- 人物参考图只提供身份与外观证据，人物动态由 Human Realism 决定。
- 多人项目每人一张独立 character table。
