---
navigation:
  title: 材料
  icon: compactcrafting:projector_dish
  parent: index.md
  position: 3
item_ids:
  - compactcrafting:projector_dish
  - compactcrafting:base
---
# <Color id="light_purple">材料</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="light_purple">材料</Color>
  <ItemImage id="projector_dish" scale="2"/>
  用于制作<ItemLink id="field_projector"/>的合成材料。你不会直接使用它们；它们是搭建微缩装配装置时的中间产物。
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>
***

<Row>
  <ItemImage id="projector_dish"/>
  ### <Color id="aqua">微缩力场投影盘</Color>
</Row>

这是<ItemLink id="field_projector"/>的发射元件。该盘负责实际的力场投影几何结构；若没有它，投影仪就无法标记出属于自己那一侧的力场边界。

<RecipeFor id="projector_dish"/>

<ItemImage id="minecraft:air" scale="0.5"/>

<Row>
  <ItemImage id="base"/>
  ### <Color id="aqua">基座</Color>
</Row>

承载<ItemLink id="projector_dish"/>的安装底板。将其与盘（以及其他材料）组合，即可制作一台完整的<ItemLink id="field_projector"/>。

<RecipeFor id="base"/>
