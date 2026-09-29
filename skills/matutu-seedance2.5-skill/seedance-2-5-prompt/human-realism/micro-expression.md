# Micro Expression Engine

情绪词（confident / happy / sad / sexy / professional）是给导演看的意图，不是给模型执行的动作。

转换公式：

```text
emotion
-> facial muscle behavior
-> intensity
-> transition
-> recovery
```

## 情绪编译表

| 情绪 | 可执行动态 |
|---|---|
| Confidence | 下颌放松、眉峰极轻微回落、颧肌低强度上提、眼神注视时间延长、嘴角出现受控微笑后自然收回 |
| Warm / Friendly | 眼轮匝肌先于嘴角启动、笑容峰值约50-70%、眉毛轻微上扬、说话间隙保持自然嘴角弧线 |
| Professional | 上眼睑抬起稳定、口型提前于首字形成、表情峰值低、眨眼节奏均匀但非机械 |
| Amused | 鼻翼轻微扩张、眼角挤压、嘴角先压后抬、头有极轻后仰、笑容峰值后自然收束 |
| Concerned | 眉间肌轻微收缩、下唇内压、视线短暂下移再抬起、呼吸变浅 |
| Calm / Relaxed | 肩线下沉、眼睑覆盖度增加、咀嚼肌放松、眨眼变慢 |

## 微表情规则

- 每个表情块都要给强度区间与恢复路径，避免全片停在峰值。
- 真表情不是左右脸完全一致；两侧肌肉存在 10-30% 的幅度差。
- 情绪跟随剧情：状态 A -> 触发 -> 峰值 -> 恢复，不在相邻镜头间无理由重置。
- 只有特写 / Close-up 才写眉、眼睑、鼻翼等细节；Medium 只写整体表情轨迹。
