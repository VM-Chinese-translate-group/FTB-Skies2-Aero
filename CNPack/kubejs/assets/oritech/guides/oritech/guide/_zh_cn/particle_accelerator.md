---
navigation:
  title: 粒子加速器
  position: 3
  icon: "oritech:accelerator_controller"
item_ids:
  - oritech:accelerator_controller
  - oritech:accelerator_ring
  - oritech:accelerator_motor
  - oritechthings:accelerator_magnetic_field
---
# <Color id="aqua">粒子加速器</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="aqua">粒子加速器</Color>

  <GameScene zoom="2.5" interactive={true}>
    <ImportStructure src="oritech:assets/basic_accelerator.nbt"/>
    <IsometricCamera yaw="225" pitch="30"/>
    <DiamondAnnotation pos="0.5 0.5 1.5" color="#ff6d6d">
    每套配置都需要2个粒子加速器，用于放入待加速的物品。
    </DiamondAnnotation>
    <DiamondAnnotation pos="3.5 0.5 2.5" color="#ff6d6d">
    加速器磁场应放置在中心，并使用高级目标标识器与粒子加速器主结构进行绑定。此外它也支持安装插件！
    </DiamondAnnotation>
    <DiamondAnnotation pos="5.5 0.5 2.5" color="#ff6d6d">
    直线型马达需安装在导向环内部。通电后即可为粒子加速。
    </DiamondAnnotation>
    <DiamondAnnotation pos="2.5 0.5 4.5" color="#ff6d6d">
    导向环用于引导粒子沿环路运转。放置后，可通过右击改变其射入角度。
    </DiamondAnnotation>
  </GameScene>
  #### *基础粒子加速器配置*
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">组件</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="oritech:accelerator_controller"/>
  ### <Color id="aqua">粒子加速器</Color>
</Row>

<Color id="aqua">粒子加速器</Color>是任何加速器结构中的主体设备。在此处可将物品放入粒子加速环路中。一套基础配置至少需要2个<Color id="aqua">粒子加速器</Color>，且均需与<Color id="green">粒子加速器导向环</Color>相连。

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="oritech:accelerator_ring"/>
  ### <Color id="aqua">加速器导向环</Color>
</Row>

<Color id="green">粒子加速器导向环</Color>用于引导粒子进行环状循环。放置后，右击即可改变射入角度。在规划粒子在环路中的运动路径时必须使用导向环，也可以根据实际搭建需要增加其使用数量。

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="oritech:accelerator_motor"/>
  ### <Color id="aqua">直线型马达</Color>
</Row>

<Color id="green">粒子加速器直线型马达</Color>用于为环路中的粒子提供加速度。这些马达必须通电运行。虽然最少只需1个即可运转，但增加马达数量能让粒子加速得更快。

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="oritechthings:accelerator_magnetic_field"/>
  ### <Color id="aqua">加速器磁场</Color>
</Row>

<Color id="gold">加速器磁场</Color>需放置在结构的中心。要进行绑定，可先手持<Color id="dark_green"><ItemLink id="oritechthings:advanced_target_designator"/></Color>潜行+右击主粒子加速器，随后潜行+右击该磁场方块。

该磁场设备的耗电量极大。可以为其安装插件，或使用机器扩展坞——对于较小的环路，必须使用扩展坞才能达到15kJ的能量门槛。

<Column>
  #### <Color id="green">推荐的磁场插件</Color>
</Column>

* 储能扩展坞：提升磁场的能量容量，并允许安装更多插件。
* 机器容量插件：提升磁场的能量容量。
* 机器适配器插件：提升磁场可以接收的能量上限。
* 效率升级插件：提升磁场在单次运转中的能量利用效率。
  * 效率速度升级插件也是不错的选择，因为它们在9级时具有更高的效率上限。

<ItemImage id="minecraft:air" scale="0.5"/>

<Column alignItems="center" fullWidth={true}>
  <Color id="yellow">下方所示的简单示例配置通过使用机器扩展坞以及上述几种插件，即可轻松达到15kJ的能量。</Color>
  <GameScene zoom="2.5" interactive={true}>
    <ImportStructure src="oritech:assets/particle_accelerator.nbt"/>
    <RemoveBlocks id="minecraft:stone"/>
    <IsometricCamera yaw="135" pitch="30"/>
  </GameScene>
</Column>