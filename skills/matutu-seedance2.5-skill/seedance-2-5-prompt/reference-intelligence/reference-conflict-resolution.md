# Reference Conflict Resolution

多参考素材冲突时不能直接混合。必须按顺序完成检测、Role 比较、优先级比较、Hard Lock 保护与解决。

## 冲突检测

两个或多个 Reference 在同一锁定维度给出不一致证据时视为冲突。冲突维度至少包括：

```text
facial identity
hairstyle / hair color
body proportion
wardrobe / fabric / color
product identity / logo / structure
product material
scene / architecture
lighting
camera / composition
motion / action
```

## 解决流程

```text
Conflict Detection
↓
Role Comparison
↓
Priority Comparison
↓
Hard Lock Protection
↓
Conflict Resolution
```

## 输出格式

```text
REFERENCE CONFLICT

image_01 vs image_02

Conflict:
facial identity

Winner:
image_01

Reason:
CHARACTER_IDENTITY > STYLE_REFERENCE

Action:
preserve image_01 identity
ignore conflicting facial structure from image_02
```

## 裁定规则

```text
1. HARD_LOCK 永远高于 SOFT_LOCK / STYLE_REFERENCE / INSPIRATION
2. 同维度不同 Role 时，优先级高者赢
3. 同 Role 同优先级时，confidence 高者赢
4. confidence 也相同但覆盖度不同，覆盖度高者赢
5. 仍无法区分时，保留用户明确指令或较早声明的素材，并输出 REPAIR 提示
6. 输家只失去冲突维度；与冲突无关的可继承特征保留
```

## 关键防错

- Style Reference 不能覆盖 Identity Lock。
- Camera Reference 不能覆盖主体锁。
- Motion Reference 不能修改人物身份。
- Human Realism 不能修改人物身份。
- Product 默认 `PRODUCT_TRANSFORMATION_ALLOWED=false`，产品参考之间冲突时锁原产品设计。
- 无明确冲突证据时不要制造冲突；覆盖度 MISSING 不等于冲突。

## 冲突解决后

冲突结果写入 REFERENCE SPEC：

```yaml
conflicts:
  - dimension: facial identity
    refs: [image_01, image_02]
    winner: image_01
    loser: image_02
    reason: CHARACTER_IDENTITY > STYLE_REFERENCE
    action: preserve image_01 identity; ignore conflicting facial structure from image_02
    resolved: true
```
