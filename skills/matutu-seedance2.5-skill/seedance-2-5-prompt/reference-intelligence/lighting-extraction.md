# Lighting Extraction

光线参考提取可复现的光照方案，不能把“氛围很高级”当成光源证据。

## 提取字段

```text
source              主光源：太阳/窗光/灯/霓虹/反射光
direction           方向：顺/侧/逆/顶/底
intensity           强度相对关系
color_temperature   色温估计（写 estimate 或冷暖描述）
contrast            对比度
shadows             阴影软硬、方向、扩散
ambient             环境光/补光
modifiers           柔光/硬光/反光板/格栅等可判断的控光线索
light_progression   运动物体经过光线时的明暗变化（视频参考）
```

## 规则

- 只写参考中真实可见的光线证据，不编造光源位置。
- 一张“氛围图”没有光源细节时，降级为 STYLE 参考，不锁光线。
- 场景锁与光线锁分离：场景决定“在哪”，光线决定“怎么被照”。
- 逆光人物参考只锁轮廓，不锁皮肤/面料细纹理。

## 下游

光线结果进入 `lighting` 字段与 `scene_lock.lighting`，Prompt Compiler 写成【光线】。
