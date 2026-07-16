---
navigation:
  title: 矿晶
  icon: minecraft:amethyst_cluster
  position: 2
item_ids:
  - ftb:void_crystal_catalyst
---
# <Color id="light_purple">矿晶</Color>

<Column alignItems="center" fullWidth={true}>

# <Color id="light_purple">矿晶</Color>

<ItemImage id="minecraft:amethyst_cluster" scale="2"/>

矿晶是一类会缓慢长出晶芽的晶洞方块。采下晶芽可获得晶簇，再将晶簇加工成资源碎片。所有资源都遵循同一套流程，区别只在于最初的母岩如何获得。
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
## <Color id="gold">寻找矿晶浮岛</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

部分矿晶会出现在<Color id="aqua">矿晶浮岛</Color>上。每座浮岛只会生成一种随机资源对应的矿晶母岩。

* <Color id="aqua">主世界浮岛</Color>会随机生成在高空，可产出大多数资源（铝、煤炭、铜、金、铁、青金石、铅、镍、红石、独居石、锇、银、锡、铀、锌、焦黑石英、红宝石、蓝宝石、黄玉）。
* <Color id="aqua">下界浮岛</Color>生成在下界，包含更稀有的资源（远古残骸、石英、钻石、绿宝石、铂、钨）。

找到的矿晶母岩可以用多种方式<Color id="green">搬运</Color>，最常见的是使用<Color id="yellow"><ItemLink id="mekanism:cardboard_box"/></Color>。这样就能把母岩带回基地，而不必留在原地采收。

下方每个资源页面都会注明对应矿晶出现在哪类浮岛上，并附上自行制作母岩的配方。

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
## <Color id="gold">虚无晶体催化剂</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="ftb:void_crystal_catalyst"/>
  ### <Color id="aqua">虚无晶体催化剂</Color>
</Row>

<Color id="light_purple"><ItemLink id="ftb:void_crystal_catalyst"/></Color>是几乎所有矿晶的基础方块。多数母岩配方都是将已放置的催化剂转化为指定矿晶母岩，可能需要对其使用染料、浇铸熔融金属，或在旁边引爆特定物品。具体做法请查看对应资源页面。

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
## <Color id="gold">矿晶的运作方式</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

获得矿晶母岩后，所有资源的采集流程都相同。

1. <Color id="aqua">放置母岩。</Color>它和紫水晶母岩一样，会在裸露表面缓慢长出晶芽，并依次从小型生长为中型和大型。
2. <Color id="aqua">采收大型晶芽。</Color>在<Color id="red">不使用精准采集</Color>的情况下挖掘完全成熟的大型晶芽，即可掉落对应资源的晶簇，并有小概率额外获得沙子。
3. <Color id="aqua">加工晶簇。</Color>将晶簇放入<Color id="gold">Oritech 激光设备</Color>处理，转化为可直接使用的资源碎片。

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
## <Color id="gold">矿晶自动化</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

矿晶可通过多种设备实现自动化，例如 Oritech 的<Color id="dark_purple"><ItemLink id="oritech:laser_arm_block"/></Color>、Modular Routers 的<Color id="green"><ItemLink id="modularrouters:breaker_module"/></Color>、Just Dire Things 的<Color id="aqua"><ItemLink id="justdirethings:blockbreakert2"/></Color>、Create 的<Color id="gold"><ItemLink id="create:deployer"/></Color>等。这些设备都会破坏成熟晶芽并掉落晶簇，但不会破坏矿晶母岩本身。


偏爱<Color id="light_purple">魔法路线</Color>的玩家也可以使用 GeOre Nouveau：每种矿晶都有对应的矿晶傀儡护符，可召唤傀儡自动采收晶芽并放入容器。

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
## <Color id="gold">资源</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.5"/>

<SubPages icons={true} />
