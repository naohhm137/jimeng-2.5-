# Motion Extraction

动作/视频参考提取“怎样动、何时动、多快、朝哪、身体与摄影机关系如何”，进入 Motion Lock。

## 提取字段

```text
subject_motion        主体运动类型与轨迹
body_mechanics        重心、换步、肩部、肢体链
hand_motion           手指/手腕/抓握链
head_motion           头部稳定/跟随/转头链
eye_motion            视线引导/注视
hair_motion           头发惯性、延迟、重力归位
clothing_motion       衣物惯性、褶皱变化
object_motion         道具/产品运动与受力
camera_motion         摄影机运动与主体关系
speed                 相对速度
acceleration          加速
deceleration          减速/停止
direction             运动方向与镜像风险
```

## 输出 YAML

```yaml
motion_lock:
  subject_motion:
  body_mechanics:
  hand_motion:
  head_motion:
  eye_motion:
  hair_motion:
  clothing_motion:
  object_motion:
  camera_motion:
  speed:
  acceleration:
  deceleration:
  forbidden:
    - 动作链不完整时不得直接生成
    - 不得修改人物身份
```

## 规则

- Motion 参考不锁身份：动作素材里的人脸不是身份证据。
- 动作必须拆成可执行链，禁止只写 `person walking`。
- 静态图（POSE）与动作视频（MOTION）分开：POSE 锁静态姿态，MOTION 锁时间链。
- 动作与景别冲突时返回 Shot Feasibility 拆镜，不在一个镜头硬塞多动作。
- 产品受力动作锁定接触链、受力方向与结束状态。

## 下游

Motion 结果进入 `motion_lock` / Human Motion Engine；最终由 Prompt Compiler 编译进时间轴与【人物真实感】。
