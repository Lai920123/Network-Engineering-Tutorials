# DMVPN EIGRP Phase 2 #

## Topology ##

![](Image/Topology.png)

>拓樸已經預先配置了IP和Static Route指向ISP

## Phase 2 ##

## Tranditional ## 

```bash
[HQ]
int tun 0 
    no ip split-horizon eigrp 10 #練習時一開始先不要加這條，在建立完EIGRP時使用show ip route查看路由表，會發現收不到BRANCH2發的路由，就是因為水平分割
    no ip next-hop-self eigrp 100 
```

## Named-Mode ##

```bash
[HQ]

router eigrp DMVPN
    address-family ipv4 unicast autonomous 10 
        eigrp router-id 1.1.1.1 
        af-interface tunnnel 0
            no split-horizon #練習時一開始先不要加這條，在建立完EIGRP時使用show ip route查看路由表，會發現收不到BRANCH2發的路由，就是因為水平分割
            no next-hop-self #讓從BRANCH2接收到的路由傳遞出去時下一跳依舊是BRANCH2而不是更改為HUB
```

## Reference ## 

https://network-insight.net/2015/02/03/design-guide-dmvpn-phases/
