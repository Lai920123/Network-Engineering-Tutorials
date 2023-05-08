# DR BDR election #

## DR/BDR/DROTHERs ##

- Designated Router 指定路由器，由DR跟BDR和DROTHERs進行LSA的溝通，再統一發送結果，DROTHERs之間不會進行LSA的溝通，避免造成過多不必要的流量

- Backup Designated Router 備份指定路由器，若是DR故障，則BDR會晉升成為DR繼續進行LSA的溝通，但若是故障的DR又重新回到拓樸中，也不會重新進行election，等到下一次重啟OSPF時才會重新進行election(重啟修改priority那台以外的的其他台)，重啟ospf使用clear ip ospf process

- DROTHERs 不是DR也不是BDR就稱為DROTHERs

## DR/BDR如何選舉 ##

OSPF會在每個區域選出DR與BDR，用於統一發放鏈路狀態更新，DR/BDR選舉會先看Priority，Priority大的成為DR，第二大的成為BDR，其餘成為DROTHER，若是Priority相同，就會比router-id，較大的為DR，第二大的成為BDR，其他成為DROTHER

## 範例 ##

![](Image/Topology2.png)

以上面的拓樸為例，在這個區域中有三顆路由器，所以會選出DR、BDR和DROTHER，配置如下

```bash
R1#
int e0/0 
    ip address 123.0.1.1 255.255.255.0
    no shutdown 
router ospf 1
    router-id 1.1.1.1 
    network 123.0.1.0 0.0.0.255 area 0
R2#
int e0/0
    ip address 123.0.1.2 255.255.255.0
    no shutdown
router ospf 1
    router-id 2.2.2.2
    network 123.0.1.0 0.0.0.255 area 0
R3#
int e0/0
    ip address 123.0.1.3 255.255.255.0
    no shutdown 
router ospf 1
    router-id 3.3.3.3 
    network 123.0.1.0 0.0.0.255 area 0
```

