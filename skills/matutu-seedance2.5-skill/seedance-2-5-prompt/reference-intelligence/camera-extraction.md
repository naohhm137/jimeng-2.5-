# Camera Extraction

摄影参考提取“摄影机如何看”，不提取“摄影机看到谁”。

## 提取字段

```text
shot_size             景别
camera_height         机位高度
camera_angle          平视/仰/俯/过肩/视线齐平
lens                  焦段感（估计值写 estimate）
perspective           透视关系
depth_of_field        景深
focus_plane           焦点平面
lens_character        镜头性格：压缩/畸变/呼吸感
camera_movement       固定/推/拉/摇/移/跟/环绕/手持
camera_motion_pattern 运动方向、速度、启停
composition           构图关系（见 composition-extraction.md）
```

## 输出 YAML

```yaml
camera_lock:
  shot_size:
  camera_height:
  camera_angle:
  lens:
  perspective:
  depth_of_field:
  focus:
  camera_motion:
  composition:
```

## 规则

- 景别与运镜不能偷换成人物的 Identity；人物脸只是镜头演示内容。
- 画面里出现脸部特写不代表本项目人物被锁定，除非素材同时声明 CHARACTER role。
- 多个摄影参考冲突时，按用户指令 > 项目镜头语言 > 默认推断裁定。
- Camera Reference 永远不修改人物外观与产品设计。

## 下游

Camera Extraction 结果进入 `camera_lock` 与 `workflows/camera.md`；最终由 Prompt Compiler 写成【摄影】。
