# Border Gateway Protocol 邊界閘道協定 #

## 簡介 ##

    BGP通常應用於大型網路當中，例如ISP之間的路由交換，因BGP有多種可調整的屬性，跟以往學到的OSPF，EIGRP比起來相對困難，因此使用實例讓大家能夠較好理解BGP

## Peer ##

    BGP預設keepalive interval為60秒，hold time為180秒
    在BGP裡，把Neighbors稱作Peers，Peers利用TCP 179 Port進行溝通，BGP要建立Peers須達成以下條件
    1.Autonomous System Number相同
    2.

## 指令列表 ##

因BGP可調整的東西非常多，以下列出所有，需用到時查詢即可

```bash
router bgp 1 #配置BGP ASN 1，ASN的範圍為1-4294967295
    bgp router-id 1.1.1.1 #Router-ID為1.1.1.1
    neighbor 123.0.1.1 remote-as 1 #鄰居IP以及ASN
    network 192.168.1.0 mask 255.255.255.0 #宣告網段
```

## 實例 ##

## Topology ##

![](Topology1.png)
