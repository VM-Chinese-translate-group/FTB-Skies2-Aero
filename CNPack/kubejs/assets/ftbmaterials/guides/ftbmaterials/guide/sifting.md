---
navigation:
  title: 筛矿
  icon: minecraft:gravel
  position: 5
item_ids:
  - ftb:cloth_mesh
  - ftb:iron_mesh
  - ftb:gold_mesh
  - ftb:diamond_mesh
  - ftb:blazing_mesh
---
# <Color id="aqua">筛矿</Color>

<Column alignItems="center" fullWidth={true}>

# <Color id="aqua">筛矿</Color>

<ItemImage id="minecraft:gravel" scale="2"/>

筛矿是把方块送入动力筛子，从中筛出矿物、粉末和宝石。具体产物取决于投入的方块和使用的筛网等级。
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
## <Color id="gold">搭建设备</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

筛矿需要使用由旋转动力驱动的<Color id="aqua">动力筛子</Color>。放入筛网和原料方块，并让设备转速达到该筛网要求的最低值。

* <ItemImage id="ftb:cloth_mesh" scale="0.75"/> <ItemImage id="ftb:iron_mesh" scale="0.75"/> <Color id="aqua">布制</Color>和<Color id="aqua">铁制</Color>筛网需要<Color id="red">8 RPM</Color>。
* <ItemImage id="ftb:gold_mesh" scale="0.75"/> <Color id="aqua">金制</Color>筛网需要<Color id="red">16 RPM</Color>，并可解锁更多产物。
* <ItemImage id="ftb:diamond_mesh" scale="0.75"/> <ItemImage id="ftb:blazing_mesh" scale="0.75"/> <Color id="aqua">钻石</Color>和<Color id="aqua">烈焰</Color>筛网需要<Color id="red">32 RPM</Color>，可筛出最稀有的产物。

大多数原料需要用<Color id="gold">FTB Stuff模组的锤</Color>或机械动力的粉碎工序加工沙子可制成<ItemLink id="ftbstuff:dust"/>，玄武岩可制成<ItemLink id="ftbstuff:crushed_basalt"/>，下界岩可制成<ItemLink id="ftbstuff:crushed_netherrack"/>，<ItemLink id="xycraft_world:kivi"/>可制成<ItemLink id="ftb:crushed_kivi"/>。沙砾、沙子和泥土则可直接筛分。

<ItemImage id="minecraft:air" scale="0.25"/>

> <Color id="yellow">表格说明：</Color>每个单元格标示该原料能产出对应资源的最低筛网层级。<Color id="aqua">+</Color>表示更高层级筛网同样可以产出，且概率通常更高；破折号表示该组合无法产出此资源。

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
## <Color id="gold">各资源的产出位置</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

以下资源按筛分原料分类。

<ItemImage id="minecraft:air" scale="0.25"/>

### <Color id="aqua">矿石与金属</Color>

| 资源 | 沙砾 | 沙子 | FTB 粉尘 |
|---|:---:|:---:|:---:|
| <ItemImage id="ftbmaterials:iron_chunk" scale="0.5"/> 铁 | 布制+ | 布制+ | 布制 |
| <ItemImage id="ftbmaterials:copper_chunk" scale="0.5"/> 铜 | 布制+ | 布制+ | — |
| <ItemImage id="minecraft:coal" scale="0.5"/> 煤炭 | 布制+ | — | — |
| <ItemImage id="minecraft:flint" scale="0.5"/> 燧石 | 布制+ | — | — |
| <ItemImage id="ftbmaterials:tin_chunk" scale="0.5"/> 锡 | 铁制+ | 布制+ | — |
| <ItemImage id="ftbmaterials:lead_chunk" scale="0.5"/> 铅 | 铁制+ | 铁制+ | — |
| <ItemImage id="ftbmaterials:nickel_chunk" scale="0.5"/> 镍 | — | 铁制+ | 金制+ |
| <ItemImage id="ftbmaterials:gold_chunk" scale="0.5"/> 金 | — | 铁制+ | 铁制+ |
| <ItemImage id="ftbmaterials:silver_chunk" scale="0.5"/> 银 | — | 钻石+ | 金制+ |
| <ItemImage id="ftbmaterials:aluminum_chunk" scale="0.5"/> 铝 | 金制+ | 金制+ | 烈焰 |
| <ItemImage id="ftbmaterials:osmium_chunk" scale="0.5"/> 锇 | 钻石+ | 钻石+ | — |
| <ItemImage id="ftbmaterials:lapis_lazuli_chunk" scale="0.5"/> 青金石 | 金制+ | — | — |
| <ItemImage id="ftbmaterials:emerald_chunk" scale="0.5"/> 绿宝石 | 金制+ | — | — |
| <ItemImage id="ftbmaterials:diamond_chunk" scale="0.5"/> 钻石 | 钻石+ | — | — |
| <ItemImage id="ftbmaterials:redstone_chunk" scale="0.5"/> 红石 | — | — | 金制+ |
| <ItemImage id="ftbmaterials:bauxite_dust" scale="0.5"/> 铝土矿 | — | — | 金制+ |

<ItemImage id="minecraft:air" scale="0.25"/>

### <Color id="aqua">下界材料</Color>

| 资源 | 粉碎玄武岩 | 粉碎下界岩 |
|---|:---:|:---:|
| <ItemImage id="minecraft:netherrack" scale="0.5"/> 下界岩 | 金制+ | — |
| <ItemImage id="ftbmaterials:sulfur_dust" scale="0.5"/> 硫磺 | 金制+ | — |
| <ItemImage id="mekanism:dirty_netherite_scrap" scale="0.5"/> 污浊下界合金碎片 | 金制+ | — |
| <ItemImage id="mysticalagriculture:soulium_dust" scale="0.5"/> 离魂粉 | — | 金制+ |
| <ItemImage id="minecraft:glowstone_dust" scale="0.5"/> 荧石 | — | 金制+ |
| <ItemImage id="minecraft:quartz" scale="0.5"/> 下界石英 | — | 金制+ |
| <ItemImage id="actuallyadditions:black_quartz" scale="0.5"/> 焦黑石英 | — | 烈焰 |
| <ItemImage id="minecraft:blaze_powder" scale="0.5"/> 烈焰粉 | — | 钻石+ |

<ItemImage id="minecraft:air" scale="0.25"/>

### <Color id="aqua">Xy晶宝石</Color>

使用钻石或烈焰筛网筛分<ItemLink id="ftb:crushed_kivi"/>，即可集齐全部五种颜色的Xy晶宝石。

| 资源 | 粉碎基维 |
|---|:---:|
| <ItemImage id="xycraft_world:xychorium_gem_light" scale="0.5"/> 亮色 | 钻石+ |
| <ItemImage id="xycraft_world:xychorium_gem_dark" scale="0.5"/> 暗色 | 钻石+ |
| <ItemImage id="xycraft_world:xychorium_gem_blue" scale="0.5"/> 蓝色 | 钻石+ |
| <ItemImage id="xycraft_world:xychorium_gem_green" scale="0.5"/> 绿色 | 钻石+ |
| <ItemImage id="xycraft_world:xychorium_gem_red" scale="0.5"/> 红色 | 钻石+ |

<ItemImage id="minecraft:air" scale="0.25"/>

### <Color id="aqua">试剂与精华</Color>

| 资源 | 沙子 | FTB模组尘土 |
|---|:---:|:---:|
| <ItemImage id="ftbmaterials:salt_dust" scale="0.5"/> 盐 | — | 布制+ |
| <ItemImage id="ftbmaterials:niter_dust" scale="0.5"/> 硝石 | — | 铁制+ |
| <ItemImage id="minecraft:gunpowder" scale="0.5"/> 火药 | — | 铁制+ |
| <ItemImage id="minecraft:bone_meal" scale="0.5"/> 骨粉 | — | 布制+ |
| <ItemImage id="mysticalagriculture:dirt_essence" scale="0.5"/> 泥土精华 | — | 布制 |
| <ItemImage id="mysticalagriculture:prosperity_shard" scale="0.5"/> 活化水晶碎片 | 金制+ | — |

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
## <Color id="gold">泥土与滤水器</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

筛矿产出的并不全是材料：

* <ItemImage id="minecraft:dirt" scale="0.75"/> 筛分<ItemLink id="minecraft:dirt"/>时，使用<Color id="aqua">布制</Color>筛网可获得作物种子，使用<Color id="aqua">铁制</Color>筛网则可获得树苗。
* <ItemImage id="createsifter:stone_pebble" scale="0.75"/> 将<Color id="gold">滤水器</Color>放入水中后，无需供能即可被动收集石子、树苗和水生植物。
