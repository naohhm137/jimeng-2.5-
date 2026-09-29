# Character Extraction

人物参考图把人物拆成两个不同层：

```text
IDENTITY LOCK      这个人是“谁”：脸、发型、体型、年龄感、可辨外观
HUMAN REALISM      这个人“如何像真人一样活着”：blink、呼吸、重心、布料延迟
```

绝不允许合并成一个笼统段落。

## 提取字段

```text
character_id        CHARACTER_A / CHARACTER_B
identity
  face_structure / face_shape
  facial_proportions
  eyes / eyebrows / nose / lips / jawline / cheekbones
  skin_tone
  age_appearance
  hair_style / hair_color
  body_proportion / build
  signature_features
wardrobe           服装结构证据（只写可见）
accessories
pose               姿态证据
expression         表情证据（可作为状态参考，不写进身份锁）
lighting           仅影响人物证据可靠度，不直接锁身份
composition/camera 仅用于判断可取景角度，不锁脸
```

## 输出 YAML

```yaml
character_lock:
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
```

## 规则

- 正脸缺失时只能写“半侧脸/背影可见的上限”，不伪造正面锚点。
- 身份锚点只在 Identity Lock 出现一次；时间轴与各镜不重述整段身份。
- Realism 动态永远不属于 identity 字段。
- 人物越近身份字段越精确；FULL/WIDE 只保留头身比、发色、服装等远程锚点。
- 多人项目逐人维护 CHARACTER_ID 与 interaction 拓扑，禁止 face merge / identity swap。

## 下游

提取完成后进入 Human Realism Routing。RIE 只决定人物需要哪些身份证据；人物是否存在、是否加载动作动态由 Human Realism Engine 裁决。
