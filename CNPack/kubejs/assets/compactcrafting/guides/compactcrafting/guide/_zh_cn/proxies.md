---
navigation:
  title: 微缩力场代理器
  icon: compactcrafting:rescan_proxy
  parent: index.md
  position: 2
item_ids:
  - compactcrafting:rescan_proxy
  - compactcrafting:match_proxy
---
# <Color id="light_purple">Field Proxies</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="light_purple">微缩力场代理器</Color>
  <ItemImage id="rescan_proxy" scale="2"/>
  代理器能让你在不靠近投影仪的情况下，将力场接入红石自动化系统。每个代理器都会绑定一个特定的力场，并将其作为可读取红石信号的方块暴露出来。
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>
***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">绑定代理器</Color>
</Column>

两种类型的代理器均使用相同的绑定流程：

1. 在你想要连接红石的位置放置代理器。
2. <Color id="aqua">Shift+使用</Color>属于该力场的任意一台<ItemLink id="field_projector"/>，即可将代理器绑定到该力场。
3. <Color id="aqua">右键点击代理器</Color>可短暂高亮显示其绑定力场的所有投影仪。这非常适用于确认代理器连接的是哪个力场。
4. 对空进行<Color id="aqua">Shift+使用代理器</Color>以解除绑定。

<ItemImage id="minecraft:air" scale="0.25"/>
***

<Row>
  <ItemImage id="match_proxy"/>
  ### <Color id="aqua">微缩力场代理器（匹配）</Color>
</Row>

**输出**红石信号。每当绑定的力场中包含有效且被识别的配方结构（即玩家或管道系统完成正确方块摆放的瞬间）时，就会发出红石信号。可以配合对准力场的漏斗/投掷器使用，从而实现自动丢入催化剂。

<RecipeFor id="match_proxy"/>

<ItemImage id="minecraft:air" scale="0.5"/>

<Row>
  <ItemImage id="rescan_proxy"/>
  ### <Color id="aqua">微缩力场代理器（重扫描）</Color>
</Row>

**接收**红石信号。红石上升沿信号会强制绑定的力场立即重新扫描其内容并重新评估配方，而无需等待下一次周期性检查。这非常适用于高频率的时钟自动化系统，可以让力场在方块放置的瞬间立刻做出反应。

<RecipeFor id="rescan_proxy"/>
