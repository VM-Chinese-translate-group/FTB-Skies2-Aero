---
navigation:
  title: 除以零
  icon: excessive_utilities:division_sigil
  position: 0
item_ids:
  - excessive_utilities:division_sigil
  - excessive_utilities:unstable_ingot
  - excessive_utilities:cursed_earth
---
# <Color id="gold">除以零</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="gold">除以零</Color>

  <ItemImage id="excessive_utilities:division_sigil" scale="2"/>

  **分割徽章**是<Color id="yellow">Excessive Utilities</Color>模组添加的道具。在探索世界时，极难在战利品箱中发现它。你也可以从游戏中期商店购买，或通过击杀末影龙Boss获取。该徽章在投入使用前必须先进行激活。
</Column>

激活后，可以使用<Color id="gold"><ItemLink id="division_sigil"/></Color>来制作<Color id="light_purple"><ItemLink id="unstable_ingot"/></Color>。不稳定金属锭可用于合成部分中后期的道具。需要注意的是，不稳定金属锭<Color id="red">在合成10秒后便会发生爆炸</Color>并瞬间秒杀玩家，因此请务必随用随合。

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">激活仪式</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

若要激活徽章，需搭建以下祭坛：

* 在能直面天空的泥土或草地平台上放置一个<Color id="light_purple"><ItemLink id="minecraft:enchanting_table"/></Color>。
* 用8个<Color id="red"><ItemLink id="minecraft:redstone"/></Color>将其环绕。
* 半径8格范围内必须至少有20个能直面天空的草方块或泥土方块。
* 祭坛必须处于完全黑暗中（光照强度为0）。

> 随时手持分割徽章右击附魔台，即可查看祭坛的搭建进度。

等到午夜时分（23:30至00:30之间）。时间一到，击杀一只站在祭坛附近的生物，即可激活背包内的所有分割徽章。每个激活的徽章均可使用**256次**。

<GameScene zoom="1.25" background="#333333" interactive={true}>
  <ImportStructure src="assets/division_sigil.nbt"/>

</GameScene>

<ItemImage id="minecraft:air" scale="0.25"/>

> <Color id="yellow">击杀生物会引发落雷轰击祭坛。</Color>祭坛周围的草方块（约6x6范围）会转化为<Color id="gold"><ItemLink id="excessive_utilities:cursed_earth"/></Color>，并在玩家周围快速生成大量怪物。诅咒之土一旦接触阳光便会起火，并退化为普通泥土。

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">伪逆徽章</Color> <Color id="red">(暂未实现)</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

激活后的分割徽章可以再次进行激活仪式，从而转化为**伪逆徽章**。该仪式只能在末地维度中进行。强烈建议在仪式前先击败末影龙，但并非硬性要求。

在一片面积至少为11x11的平坦区域搭建仪式：

1. 在中心放置一个<Color id="gold"><ItemLink id="minecraft:beacon"/></Color>。
2. 用<ItemLink id="minecraft:redstone"/>与<ItemLink id="minecraft:string"/>在信标周围铺设螺旋形图案。
3. 在东、南、西、北四个方向上各放置一个箱子，箱子与信标之间需间隔4格。
4. 往每个箱子中放入指定的祭品（详见下文）。

> 随时按住Shift键并手持激活的分割徽章右击信标，即可查看仪式的搭建进度。

击杀一只站在仪式区域内的铁傀儡以触发仪式。若操作成功，会发生一场爆炸并摧毁信标与箱子，同时末地里的所有末影人都会瞬间消失。随后，周围会开始生成成群结队且拥有急迫效果的敌对怪物。击杀其中**100**只即可完成仪式。注意，若玩家在此期间死亡或离开了该维度，仪式便会宣告失败，必须从头开始。

仪式完成后，背包中第一个激活的徽章会稳定成**伪逆徽章**。它拥有无限的使用次数。在合成栏中用它将<ItemLink id="minecraft:iron_ingot"/>“除以”<ItemLink id="minecraft:diamond"/>，即可制作出**莫比乌斯（稳定/不稳定）金属锭**。这种锭不会爆炸，可以在任何合成界面中进行合成，且最大堆叠上限为64。

<ItemImage id="minecraft:air" scale="0.25"/>

<GameScene zoom="1.5" background="#333333" interactive={true}>
  <ImportStructure src="assets/pseudo_inversion.nbt"/>
</GameScene>

<Row>
  <Column>
    ## <Color id="green">箱子内容物</Color>
  </Column>
</Row>

下方展示的物品仅供参考。由于部分其他模组也对此仪式进行了兼容，你可以通过JEI的标签搜索功能来查找更多可用物品。例如，搜索'#gifts_of_earth'即可显示所有满足“大地的馈赠”要求的物品。

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="minecraft:furnace" scale="0.75"/>
  ### 北侧：<Color id="red">烈火之子</Color>
</Row>

14种由熔炉烧炼产出的物品。

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="minecraft:grass_block" scale="0.75"/>
  ### 南侧：<Color id="green">大地的馈赠</Color>
</Row>

13种在主世界自然生成的地形方块或矿石。

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="minecraft:potion" scale="0.75"/>
  ### 东侧：<Color id="blue">流水之裔</Color>
</Row>

在原版62种具有实际效果的药水中，选择其中的12种。

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="minecraft:music_disc_13" scale="0.75"/>
  ### 西侧：<Color id="yellow">空气之香</Color>
</Row>

12张原版音乐唱片。

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">祛除附魔</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

祛除工具或武器上的附魔等级有两种方法，但这两种方法均会消耗所使用的书。

<Row>
  <ItemImage id="minecraft:book"/>
  ### <Color id="aqua">书</Color>
</Row>

在合成栏中用<ItemLink id="minecraft:book"/>“除以”任何已附魔的工具或武器，会使所有的附魔效果降低1级，并扣除该装备约25%的耐久度。

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="minecraft:enchanted_book"/>
  ### <Color id="aqua">附魔书</Color>
</Row>

在合成栏中用<ItemLink id="minecraft:enchanted_book"/>“除以”任何已附魔的工具或武器，会扣减该书上所指定的特定附魔和等级，且不会对装备造成任何耐久度损伤。例如：一把附有节肢杀手IV与火焰附加II的钻石剑，若用一本附有节肢杀手I的附魔书进行“相除”，则会得到一把附有节肢杀手III和火焰附加I的钻石剑。
