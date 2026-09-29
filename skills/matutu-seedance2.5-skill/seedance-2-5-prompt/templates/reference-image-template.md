# Reference Image Extraction Template

用途：把一张参考图转成 REFERENCE SPEC 条目。Role 必须先于描述，继承边界先于画面文字。

```text
REFERENCE ID: <image_01 / image_02 / video_01>

SUBJECT
subject_type: <CHARACTER / PRODUCT / SCENE / CAMERA / STYLE / AUDIO>
subject_label: <CHARACTER_A / PRODUCT_01 / SCENE_01>

ROLE
primary_role: <canonical role>
secondary_roles: <只写该素材确实能提供的辅助证据>
priority: <按 Reference Priority System>
confidence: <0-1>
lock_level: <HARD_LOCK / SOFT_LOCK / STYLE_REFERENCE / INSPIRATION>

COVERAGE
FACE: HIGH / MEDIUM / LOW / MISSING / N/A
FULL BODY: ...
PRODUCT STRUCTURE: ...
MATERIAL: ...
LIGHTING: ...

KEY FEATURES
<只写实际可见、可继承的特征，逐维度列出>

DO NOT INHERIT
<背景/文字/水印/非主体道具/镜头畸变/情绪化光线>

CONFLICT CANDIDATES
<与其他素材在同一维度可能冲突的字段，无则写 NONE>
```

规则：

- Role 是主键；一张图只承担一个 primary role。
- confidence < 0.5 的素材默认降为 INSPIRATION，除非用户明确要求硬锁。
- MISSING 就是 MISSING，不写“参考图未显示但应该如此”。
