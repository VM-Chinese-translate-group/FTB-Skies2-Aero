---
navigation:
  title: 回响时间水晶母岩
  icon: "justdynathings:echoing_budding_time"
  position: 2
item-ids:
  - justdynathings:echoing_budding_time
  - justdirethings:time_crystal_cluster
---

# 获取母岩资源的新途径

这些水晶母岩只需消耗**时间流体**与**能量**即可生长出晶簇。

<GameScene zoom="2" interactive={true}>
  <Block id="justdynathings:echoing_budding_time" p:alive="true"/>
  <Block x="1" id="justdynathings:echoing_budding_time" p:alive="true"/>
  <Block x="2" id="justdynathings:echoing_budding_time" p:alive="true"/>
  <Block x="3" id="justdynathings:echoing_budding_time" p:alive="true"/>
  <Block x="-1" id="justdynathings:echoing_budding_time" p:alive="false"/>

  <Block y="1" id="justdirethings:time_crystal_cluster_small" />
  <Block x="1" y="1" id="justdirethings:time_crystal_cluster_medium" />
  <Block x="2" y="1" id="justdirethings:time_crystal_cluster_large" />
  <Block x="3" y="1" id="justdirethings:time_crystal_cluster" />
</GameScene>