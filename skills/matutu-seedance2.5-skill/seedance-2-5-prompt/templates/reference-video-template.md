# Reference Video Extraction Template

用途：动作参考视频拆成 Motion Lock / Camera Lock / Timing，不直接复制原片。

```text
REFERENCE ID: <video_01>
ROLE: MOTION / ACTION / CAMERA_MOTION / TIMING

MOTION_LOCK
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

CAMERA_LOCK
shot_size:
camera_height:
camera_angle:
lens:
perspective:
depth_of_field:
focus:
camera_motion:
composition:

TIMING
<动作起止、节拍、停顿、转场节奏>

DO NOT INHERIT
<原片人物身份、产品、台词、场景、品牌>
```

规则：

- 动作链必须可执行：方向、速度、换重心、摄影机关系都要写。
- Motion 参考不锁身份；素材里的人脸不是本项目人物的身份证据。
- 结构、节奏、镜头语言、内容机制可学；人物/产品/场景/台词必须替换。
