---
navigation:
  title: Compact Crafting
  icon: compactcrafting:field_projector
  position: 0
---
# <Color id="light_purple">Compact Crafting</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="light_purple">Compact Crafting</Color>

  <ItemImage id="field_projector" scale="2"/>

  通过**搭建微缩结构**来合成物品。放置投影仪以标记出一个立方体力场，在其内的空中搭建配方所需的方块结构，然后丢入催化剂。方块随后将融合成合成产物。
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>
***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">快速入门</Color>
</Column>

一次完整的合成流程：

1. **制作一个<ItemLink id="base"/>与一个<ItemLink id="projector_dish"/>**，然后将它们组合成一台<ItemLink id="field_projector"/>。每个力场需要**四台投影仪**，分别放置在立方体的四个水平侧面上。
2. **将四台投影仪全部朝内放置**在一片开阔的空气立方体周围，每台投影仪需居中并对准其对面的投影仪。四台投影仪必须全部就位，力场才能形成。
3. **等待力场激活。**投影仪之间会出现一个发光的立方体边框，这便是你的建造区域。如果未看到边框，说明要么缺少投影仪，要么间距错误（仅限“3、5、7、9、11、13、15”个空白方块），或者某台投影仪未能正确对准对面的投影仪。
4. **打开JEI**并搜索“微缩合成”分类，找到你想制作的配方。每个配方都会显示精确的方块布局（配有逐层滑块）以及催化剂物品。
5. **在力场内的空中搭建结构。**可以站在方块上垫高、跳起放置方块，或使用建筑小帮手。建造顺序无关紧要，只有最终的排列结构才关键。
6. **确认配方已被检测到。**使用JADE看向任意一台投影仪，其应当会显示<Color id="green">已找到有效配方</Color>。如果未显示，请仔细对照JEI核对方块布局。
7. **向力场丢入催化剂。**手持催化剂物品并按下<Color id="aqua">Q</Color>键将其丢入立方体中。随后方块将被消耗，合成产物会以物品形式掉落。

<ItemImage id="minecraft:air" scale="0.25"/>
***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">力场大小</Color>
</Column>

立方体的边长取决于**两台相对的投影仪之间的空白距离**。有效大小（单位：方块）：

<Color id="aqua">**3, 5, 7, 9, 11, 13, 15**</Color>

例如，5×5×5的力场需要每对相对的投影仪表面之间有**5个空白方块**。任何其他的间距都完全无法产生力场，投影仪也会保持静止状态。

正常运行的力场需要**四台投影仪**，分别放置在立方体的四个水平侧面上。顶部和底部敞开，以便从上方投入方块和催化剂，并让合成产物从下方掉落。

<ItemImage id="minecraft:air" scale="0.25"/>
***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">在JEI中查看配方</Color>
</Column>

微缩合成配方有其专属的JEI分类。每个配方条目会显示：

* **催化剂物品。**用于触发合成所丢入的物品。
* **方块结构的3D预览**，配有以下控制功能：
  * <Color id="aqua">逐层滑块</Color>：自底向上查看方块的具体摆放位置。
  * <Color id="aqua">切换拆解视图</Color>：一次性查看整个结构。
* **产物物品**及数量。

如果对结构中的某个方块感到陌生，可以在JEI中将鼠标悬停在上面以识别它。

<ItemImage id="minecraft:air" scale="0.25"/>
***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">常见错误</Color>
</Column>

* **未出现力场**→未放满四台投影仪、空白间距不属于“3/5/7/9/11/13/15”之一，或者某台投影仪方向放错。
* **力场已出现但配方不匹配**→方块偏离了一格、层数有误、或者使用了错误的方块变体。请对照JEI逐层进行核对。
* **催化剂未触发**→丢弃的物品必须落在力场空间**内部**。请在力场正上方丢弃，或站在力场内/靠近力场丢弃。
* **建造中途配方消失**→你放置的某个方块不属于任何有效配方。部分配方可以读取未完成的状态，并可能短暂匹配其他配方；但只有*完整*的结构才能在丢入催化剂时触发合成。

<ItemImage id="minecraft:air" scale="0.25"/>
***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">相关主题</Color>
</Column>

<SubPages icons={true} />
