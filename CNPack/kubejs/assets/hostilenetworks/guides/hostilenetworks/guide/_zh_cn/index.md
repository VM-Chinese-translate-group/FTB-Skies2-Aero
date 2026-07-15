---
navigation:
  title: 数据中心
  icon: hostilenetworks:data_center
  position: 0
item_ids:
  - hostilenetworks:data_center
  - hostilenetworks:data_center_io_port
---
# <Color id="aqua">数据中心</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="aqua">数据中心</Color>

  <ItemImage id="hostilenetworks:data_center" scale="2"/>

  <Color id="gold">数据中心</Color>是一个7×7×7的多方块结构，能够同时运行多达25个<Color id="light_purple">自我意识</Color>数据模型，每个模型都将依照其独立的周期产出掉落物。
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">结构</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Column alignItems="center" fullWidth={true}>
  <GameScene zoom="2" interactive={true} background="#333333">
    <ImportStructure src="hostilenetworks:hnn_data_center.nbt"/>
    <IsometricCamera yaw="-45" pitch="30"/>
    <BoxAnnotation min="1 1 1" max="6 6 6" color="#ff0000">
      内部必须留空。
    </BoxAnnotation>
    <BlockAnnotation x="5" y="1" z="6" color="#55ffff">
      可选。若未实现数据模型的自动化输入，可将其替换为**黑色染色玻璃**。
    </BlockAnnotation>
  </GameScene>
  #### *数据中心多方块结构*
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

先铺设7×7的实心<ItemLink id="minecraft:obsidian"/>底座。随后用<ItemLink id="minecraft:black_stained_glass"/>搭建墙壁和顶部，确保内部完全中空。

在最底层的外墙上，放置一个<ItemLink id="hostilenetworks:data_center"/>控制器，以及至少三个<ItemLink id="hostilenetworks:data_center_io_port"/>。这些端口必须分别配置为以下三种模式：<Color id="aqua">能量</Color>、<Color id="aqua">输入</Color>和<Color id="aqua">输出</Color>。此外，还可以额外配置第四个端口，将其设置为<Color id="aqua">模型</Color>模式。

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">IO端口</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="hostilenetworks:data_center_io_port"/>
  ### <Color id="aqua">数据中心IO端口</Color>
</Row>

IO端口可以用于替代外壳最底层的任意墙体。右击可以循环切换模式。这四种模式必须全部存在，多方块结构才能正常运转。

| 模式 | 作用 |
|---|---|
| <Color id="aqua">能量</Color> | 接收能量输入 |
| <Color id="aqua">输入</Color> | 输入各模型所需的原料物品 |
| <Color id="aqua">输出</Color> | 提取产出的掉落物 |
| <Color id="aqua">模型</Color> | 向数据中心输入数据模型（可选） |