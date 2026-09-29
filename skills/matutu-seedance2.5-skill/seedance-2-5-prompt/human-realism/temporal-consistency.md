# Temporal Consistency

一致性不是“每句 Prompt 重复同一句话”，而是让身份、状态与物理量在时间轴上一层层锁定。

## Level 1: Within Shot

同一个 Shot 内不允许：

```text
identity change
face structure morph
hair cut/color jump
outfit change
body proportion change
expression reset
lighting direction jump
```

允许：

```text
表情从 neutral 自然过渡到峰值再恢复
衣物折痕随动作缓慢更新
镜头内曝光/对焦按物理原因微调
```

## Level 2: Cross Shot

不同 Shot 之间，以下内容必须来自同一条 Identity Block：

```text
face
age
body
hair
outfit
identity
```

做法：

- 每个 Shot 的 Prompt 都引用同一 `CHARACTER_ID`，正文只写增量。
- 同一人物不得在每个 Shot 换一种“发型描述”。
- Reference 覆盖度不足的方向不参与跨 Shot 身份承诺。

## Level 3: Sequence State

前一个 Shot 的结束状态成为后一个 Shot 的开始状态：

```text
emotion
posture
hair state
clothing state
object state
physical position
```

例子：

```text
Shot 1 人物右手拿手机
-> Shot 2 手机必须仍在同一只手上，除非画面明确发生放手机动作
Shot 1 外套下摆被风吹起
-> Shot 2 开头外套下摆仍带上一镜残余折痕，再自然落下
```

## 禁止

```text
Shot 1 holding phone -> Shot 2 phone disappears
表情无理由每镜从零开始
头发/衣服状态跳变
人物随镜头数量增加逐渐年轻/变老
```
