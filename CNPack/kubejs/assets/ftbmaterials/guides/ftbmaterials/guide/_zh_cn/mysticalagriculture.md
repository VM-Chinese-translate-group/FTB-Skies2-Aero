---
navigation:
  title: 神秘农业
  icon: minecraft:wheat_seeds
  position: 3
item_ids:
  - mysticalagriculture:prosperity_shard
  - mysticalagriculture:prosperity_seed_base
  - mysticalagriculture:awakening_altar
  - mysticalagriculture:awakening_pedestal
  - mysticalagriculture:essence_vessel
  - mysticalagriculture:cognizant_dust
  - mysticalagriculture:awakened_supremium_block
  - mysticalagriculture:awakened_supremium_essence
---
# <Color id="green">神秘农业</Color>

<Column alignItems="center" fullWidth={true}>

# <Color id="green">神秘农业</Color>

<ItemImage id="minecraft:wheat_seeds" scale="2"/>

神秘农业可以把资源当作作物种植。每种资源都有对应层级的作物，收获后获得精华，再将精华转化为材料。本节按作物层级整理。
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
## <Color id="gold">运作方式</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

1. 在耕地上<Color id="aqua">种下种子</Color>。资源作物在对应层级的精华耕地上生长最快；手持精华右击普通耕地即可将其转化。
2. <Color id="aqua">收获作物</Color>，获得对应资源精华。
3. <Color id="aqua">将精华转化为材料。</Color>将种子送入<Color id="gold">种子再处理器</Color>内可得到对应的精华。可将八份精华围成一圈合成。在本整合包中，金属精华产出的是<Color id="green">粗矿</Color>，而非锭。

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
## <Color id="gold">种子与层级</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

种子不能在工作台上制作。请为<ItemLink id="mysticalagriculture:prosperity_seed_base"/>注入四份目标资源和四份对应层级精华，并在<Color id="gold">注魔祭坛</Color>上完成仪式。使用的精华层级决定作物层级与制作难度。

精华按以下顺序逐级提升，每一级都由前一级合成：

<Row>
  <ItemImage id="mysticalagriculture:inferium_essence" scale="0.75"/>
  <ItemImage id="mysticalagriculture:prudentium_essence" scale="0.75"/>
  <ItemImage id="mysticalagriculture:tertium_essence" scale="0.75"/>
  <ItemImage id="mysticalagriculture:imperium_essence" scale="0.75"/>
  <ItemImage id="mysticalagriculture:supremium_essence" scale="0.75"/>
  <ItemImage id="mysticalagradditions:insanium_essence" scale="0.75"/>
</Row>

<Color id="green">下级精华</Color>可通过击杀生物、开采下级精华矿或收获低层级作物获得。<Color id="green">活化水晶</Color>来自活化水晶矿石（富集后制成碎片）或筛矿。最高层级材料需要在<Color id="gold">觉醒祭坛</Color>上锻造，而不是使用普通注魔。

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
## <Color id="gold">觉醒祭坛</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="mysticalagriculture:awakening_altar"/>
  <ItemImage id="mysticalagriculture:awakening_pedestal"/>
  <ItemImage id="mysticalagriculture:essence_vessel"/>
</Row>

普通注魔最高只能达到终极精华层级。想继续提升，就要搭建<Color id="gold">觉醒祭坛</Color>：这是一套多方块仪式，会将基础元素精华注入终极精华物品，使其<Color id="green">觉醒</Color>。觉醒终极精华是制作本整合包顶级神秘农业工具、盔甲和盔甲升级的核心材料。

以一座<ItemLink id="mysticalagriculture:awakening_altar"/>为中心，周围摆放八座<ItemLink id="mysticalagriculture:awakening_pedestal"/>和四个<ItemLink id="mysticalagriculture:essence_vessel"/>即可组成结构。

<ItemImage id="minecraft:air" scale="0.25"/>

仪式操作步骤：

1. 向四个容器<Color id="aqua">注入基础元素精华</Color>：<ItemLink id="mysticalagriculture:air_essence"/>、<ItemLink id="mysticalagriculture:earth_essence"/>、<ItemLink id="mysticalagriculture:water_essence"/>和<ItemLink id="mysticalagriculture:fire_essence"/>。
2. 将材料<Color id="aqua">摆放在基座上</Color>，并把基础物品放到祭坛中央。
3. 右击祭坛<Color id="aqua">启动仪式</Color>。仪式会逐步抽取容器中的精华，完成后留下觉醒产物。

<ItemImage id="minecraft:air" scale="0.25"/>

> <Color id="yellow">核心配方：</Color>以<ItemLink id="mysticalagriculture:supremium_block"/>为基础，周围放置四份<ItemLink id="mysticalagriculture:cognizant_dust"/>，并分别注入 10 份四种元素精华，可觉醒为一个<ItemLink id="mysticalagriculture:awakened_supremium_block"/>和九份<ItemLink id="mysticalagriculture:awakened_supremium_essence"/>。

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
## <Color id="gold">作物层级</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.5"/>

<SubPages icons={true} />
