---
navigation:
  title: 量子采石场
  icon: excessive_utilities:quantum_quarry
  parent: ftbmaterials:oregenerators.md
  position: 5
item_ids:
  - excessive_utilities:quantum_quarry
  - excessive_utilities:quantum_quarry_actuator
---
# <Color id="gold">量子采石场</Color>

<Column alignItems="center" fullWidth={true}>

# <Color id="gold">量子采石场</Color>

<ItemImage id="excessive_utilities:quantum_quarry" scale="2"/>

Excessive Utilities 的一种机器，会从口袋维度中开采矿石，因此不会在你的世界里留下矿坑。
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
## <Color id="gold">运作方式</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="excessive_utilities:quantum_quarry"/>
  ### <Color id="aqua">量子采石场</Color>
</Row>

<ItemLink id="excessive_utilities:quantum_quarry"/>会从模拟的量子维度中开采方块和矿石，而不是破坏周围世界。制作时需要一个已激活的魔法雪景球。建成后，它能持续产出矿石且不会损坏地形。

**搭建：**放置量子采石场后，在其六个面（上、下及四个水平方向）分别放置<Color id="aqua"><ItemLink id="excessive_utilities:quantum_quarry_actuator"/></Color>，结构类似 IC2 核反应堆。具现设备可从任意方向接收能源，并作为多方块结构的交互接口。

采石场支持红石信号控制。可在界面中、生物群系标记槽位下方设置红石模式，使其根据输入信号暂停或继续开采，便于限制产量或与其他系统联动。

<Color id="red">警告：</Color>量子采石场附近绝对不要使用方块加速类物品，例如急迫光束、速度升级或其他刻加速装置。采石场检测到加速后会**爆炸**。请确保周围不存在任何刻加速效果。

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
## <Color id="gold">供能</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

量子采石场是终局矿石来源，耗能也非常惊人。内部可缓存<Color id="red">200,000 RF</Color>，每瞬间开采一个方块消耗<Color id="red">20,000 RF</Color>；满功率时每刻最多开采一个方块。供能不足时，采石场会暂停并等待能源恢复。

* 每开采一个方块消耗<Color id="red">20,000 RF</Color>（瞬间完成，每刻最多一个）
* 内部缓存： <Color id="red">200,000 RF</Color>
* 开采顺序：从地表开始垂直向下

启动前，请确保拥有稳定而充足的持续供能，以及足够大的产物存储空间。

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
## <Color id="gold">界面与升级</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

右击任意<ItemLink id="excessive_utilities:quantum_quarry_actuator"/>即可打开界面。界面提供三个升级槽位，并显示当前开采状态：

**升级槽位：**
* **附魔书：**可应用时运 III（提高掉落）、精准采集（以方块形式获取）或效率 V（加快开采）等升级，强烈建议使用。
* **过滤器：**限制允许保留的开采产物。未列入过滤器的物品都会被销毁；留空则开采并保留全部物品。

**状态显示：**
* 当前开采的生物群系
* 当前 Y 坐标（深度）
* 放置后累计开采方块数（采石场方块被破坏后重置）

<ItemImage id="minecraft:air" scale="0.25"/>

> <Color id="yellow">查看[矿物生成](ftbmaterials:oregenerators.md)</Color>，了解其他无需采矿即可产出矿石的方法。
