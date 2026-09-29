# Reference Video Analysis

视频参考比图片多出时间维度。不能只输出 `person walking`；必须拆出动作如何发生、何时发生、在哪里发生、多快、朝哪个方向、身体如何换重心、摄影机与动作的关系。

## 视频参考提取顺序

```text
时长与节奏
→ 主体与动作链
→ 运动方向 / 速度 / 加减速
→ 身体力学
→ 摄影机与运镜
→ 时间节拍与转场
→ 物理响应（头发/衣服/道具/环境）
→ 声音参考（如果视频有音轨）
```

## 提取字段

```text
subject                人物/产品/车辆/自然物/其他
action                 动作名（walk / turn / reach / pour / ...）
motion_pattern         动作链，不是单一动词
motion_direction       左右/前后/朝向
speed                  慢/中/快，尽量给相对速度
acceleration           起始加速、中途变速、结束减速
deceleration
body_mechanics         重心、换步、肩部反方向、肢体延迟
weight_shift           体重转移位置
camera_relationship    摄影机跟随/固定/环绕时与主体距离变化
camera_movement        推/拉/摇/移/手持/轨道
shot_size              景别变化
timing                 动作起止秒、节拍、停顿
beat / transition      节奏点、硬切/叠化/匹配剪辑
physical_response      头发、衣物、液体、灰尘、道具的物理响应
audio_reference        只记录声音设计气质，不复制原音轨
```

## 动作证据写法

不要：

```text
person walking
```

要写成可执行链：

```text
MEDIUM FULL SHOT：人物从画面右侧向左走，左脚先着地，
重心交替转移到前脚；肩部小幅度反向摆动；
头发与亚麻衣摆滞后一拍；摄影机侧向平移保持相同距离。
```

## 时间与节拍

- 动作参考视频拆出节拍结构，但只保留“何时发生什么”，不复制原片叙事。
- 产品出现时间、人物动作、转场、情绪、结尾都只作为节奏参考。
- 结构、节奏、镜头语言、内容机制可学；产品、人物、场景、台词、具体动作必须换成本项目真实素材。

## 输出

拆解结果进入 `motion_lock` / `camera_lock` / `timing` 等字段，不直接作为最终 Prompt 画面。
