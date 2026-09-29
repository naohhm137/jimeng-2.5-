# Body Biomechanics

机器人感来自“没有重量转移、没有启动与停止、没有骨盆/肩部代偿”。Body 模块负责把动作拆成力学过程。

## 动态要素

```text
center of mass
weight transfer
inertia
acceleration
deceleration
foot placement
heel-to-toe motion
pelvic movement
shoulder counter movement
arm swing
head stabilization
posture adjustment
```

## 走路

不要写：

```text
walks naturally
```

改为编译：

```text
natural weight transfer between feet,
physically plausible center-of-mass movement,
natural foot placement,
subtle pelvic motion,
shoulder counter-movement,
realistic arm swing
```

更具体的中文写法示例：

```text
右脚脚跟先落地，重心从前脚掌过渡到左脚；
骨盆以轻微旋转跟随步幅，左肩随右腿前摆形成反向摆动；
双臂以肘部为轴小幅摆动，起步有轻微前倾，停止时重心后收再站定。
```

## 站起 / 坐下 / 转身 / 弯腰

- 站起：先重心前移、双手或膝借力、头最后到位。
- 坐下：先视线找椅面，臀部先降，头保持稳定，衣服与头发在落座后延迟归位。
- 转身：脚先换向，骨盆跟随，肩与头延迟，视线最后固定到目标。
- 弯腰：髋关节主导，脊柱逐节弯曲，捡起物品时膝盖与髋同步下降。

## 头稳定

走路时头部在垂直轴上有微小跟随与稳定修正，但不是完全悬浮，也不是机械点头。

## 禁止

```text
robotic walk
无重量的人体滑动
骨盆与躯干锁死
四肢无启动和停止直接瞬移
左右动作完全对称
```
