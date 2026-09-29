# Repair Routing

用户反馈先分类，再定位到模块，只做局部 Prompt 修改。不要每次遇到问题就整段重新生成。

```text
用户反馈
-> 问题分类
-> 修复模块
-> 局部 Prompt 修改
```

## 症状路由表

| 问题 | 修复 |
|---|---|
| 脸越来越不像 | Identity + Temporal |
| 眼睛像玻璃 | Eye |
| 眼神呆 | Eye + Face |
| 脸僵 | Face |
| 表情一直一样 | Micro Expression |
| 皮肤塑料感 | Skin |
| 头发像假发 | Hair |
| 走路像机器人 | Body |
| 手指畸形 | Hand |
| 衣服飘 | Clothing |
| 镜头假 | Camera |
| 长时间变脸 | Temporal |
| 两个人变成一个人 | Multi Character Identity + Interaction Lock |
| 产品接触不真实 | Hand + Clothing |

## 修复原则

1. 症状只映射到最少模块。脸僵不把 hair / clothing / camera 全部重写。
2. 先检查现有模块是否已经写了但被冲突覆盖，再决定新增。
3. 修复文本要替换掉低价值描述，不追加“更真实”形容词。
4. 修改后更新该模块的 score 分项，而不是把总分直接抬高。
5. 涉及身份漂移时，必须复核 Reference Coverage 与同一条 Identity Block 是否被忠实复用。

## 示例

用户反馈：“人物越来越不像本人”

修复：

```text
不要增加 realistic 形容词。
1. 回到 identity.md，锁定同一条 CHARACTER_ID 身份指纹。
2. 在 Temporal 模块写入：跨镜头禁止 morphing / identity drift /
   sudden age change / facial proportion change。
3. 检查 Reference Coverage：缺少正脸视角时补参考图，
   而不是靠文字描述替代。
4. 局部替换负面约束：no identity drift / no facial morphing /
   no sudden age change，移除无信息 negative 词。
```

## 禁止

```text
“更真实一点”“更像真人一点”作为修复方案
整段重写人物锁
把失败原因归给 photorealistic 词不够多
```
