# Face Dynamics

脸僵的本质是“只有表情结果，没有表情过程”。Face Dynamics 只输出可执行的肌肉与状态变化。

## 动态要素

```text
micro facial movement
eyelid movement
jaw relaxation
lip compression
lip release
cheek movement
brow movement
forehead movement
nostril movement
facial asymmetry
expression transition
expression recovery
```

## 表情过程模板

不要写“从第一帧笑到最后一帧”。默认使用：

```text
neutral
-> subtle response
-> expression peak
-> natural relaxation
```

写法示例：

```text
0-1秒保持中性，嘴角有极轻微准备动作；
1-3秒表情达到峰值：两侧颧肌不完全对称地上提，幅度约为全笑的60%；
3-5秒缓缓放松回中性，嘴角与眼轮匝肌延迟收束，不瞬间复位。
```

## 眼睑与眉

- 眼睑随眨眼自然覆盖虹膜边缘，不是整个眼皮开关。
- 说话、微笑、惊讶时，眉、眼睑、额头不是同步联动；至少保留一个非对称时间差。
- 长时间中性表情必须有微小呼吸级前额张力变化，不能完全冻结。

## 禁止

```text
全片一个表情
表情瞬间跳变
两侧脸完全镜像
表情与台词时间无关
“面部表情自然”这种不可执行描述
```
