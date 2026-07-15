---
navigation:
  title: 微缩力场投影仪
  icon: compactcrafting:field_projector
  parent: index.md
  position: 1
item_ids:
  - compactcrafting:field_projector
---
# <Color id="light_purple">微缩力场投影仪</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="light_purple">微缩力场投影仪</Color>
  <ItemImage id="field_projector" scale="2"/>
  这是Compact Crafting的核心方块。两台或更多台投影仪相互对齐时，会在其间的空白立方体区域内生成一个**微缩力场**。
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>
***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">合成配方</Color>
</Column>

<RecipeFor id="field_projector"/>

<ItemImage id="minecraft:air" scale="0.25"/>
***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">放置投影仪</Color>
</Column>

投影仪会朝其**面对的方向**（即放置它时你所面对的方向）发射力场。带有盘的那一面即为发射端。

要形成力场，你需要在立方体区域的四个水平侧面各放置一台**微缩力场投影仪（共四台）**，每台投影仪需居中放置并向内对准对面的投影仪。缺少任意一台或朝向错误都无法形成力场。

立方体的顶部和底部则是特意敞开的：你可以在这里投入方块来搭建结构、丢入催化剂，以及让合成产物掉落出来。

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="minecraft:air" scale="0.25"/>
  *必要条件：在四个侧面放置四台投影仪，且必须全部朝内。*
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>
***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">力场大小</Color>
</Column>

力场的边长等于**两台相对的投影仪表面之间的空白距离**，且必须为以下数值之一：

<Color id="aqua">**3, 5, 7, 9, 11, 13, 15**</Color>

| 力场大小 | 投影仪之间的空白方块数 | 方块到方块的总距离 |
|---|---|---|
| 3×3×3   | 3  | 4 |
| 5×5×5   | 5  | 6 |
| 7×7×7   | 7  | 8 |
| 9×9×9   | 9  | 10 |
| 11×11×11 | 11 | 12 |
| 13×13×13 | 13 | 14 |
| 15×15×15 | 15 | 16 |

如果间距不在此列表中，则**无法形成力场**，投影仪将保持静止状态且无发光边框。请使用建筑小帮手重新测量，或仔细清点方块数量。

<ItemImage id="minecraft:air" scale="0.25"/>
***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">使用力场</Color>
</Column>

力场激活后（可看到发光的立方体边框）：

1. **在JEI中选择**“微缩合成”分类下的配方。留意所需的催化剂以及每层的方块结构。
2. **在力场内的空中搭建结构。**站在临时脚手架上（或使用建筑小帮手），按照JEI显示的精确位置放置方块。
   * JEI中的第1层 = 力场的底层（Y轴最低处）。
   * 对于对称配方，绕垂直轴的旋转方向无关紧要；对于非对称配方，请调整建筑的朝向，使其与JEI中的结构相匹配。
3. **检查结构是否匹配。**安装了JADE或TOP后，将指针悬停在任意一台投影仪上，应当会显示<Color id="green">已找到有效配方</Color>。如果未显示，说明结构搭建有误。
4. **向力场丢入催化剂。**手持催化剂物品，对准力场并按下<Color id="aqua">Q</Color>键（丢弃键），使物品落在立方体内部。随后方块将被消耗，合成产物会掉落在催化剂落下的位置。

<ItemImage id="minecraft:air" scale="0.25"/>
***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">自动化接口</Color>
</Column>

对于自动化装置，请参阅<ItemLink id="rescan_proxy"/>页面上的<ItemLink id="match_proxy"/>与<ItemLink id="rescan_proxy"/>。它们可以让你在不靠近投影仪的情况下，将力场接入红石逻辑电路。这在漏斗传输催化剂或管道系统放置方块时非常实用。

<ItemImage id="minecraft:air" scale="0.25"/>
***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">故障排除</Color>
</Column>

* **无发光边框**→缺少了一台或多台投影仪、间距不为“3/5/7/9/11/13/15”之一，或者投影仪未直接对准其对面的投影仪（轴线偏移或方向错误）。
* **出现边框但配方始终不匹配**→仔细对照JEI检查每一层，包括方块的变体（如羊毛颜色错误、石材类型错误等）。
* **催化剂消失了但无事发生**→它落在了力场空间*之外*。请往更中心的位置重新丢入。
* **产物掉落在了错误的位置**→产物会在催化剂进入力场的位置生成。可以在力场正下方使用漏斗来收集它。
* 