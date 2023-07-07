# OSPF #

```bash
feature ospf

router ospf OSPF_UNDERLAY_NET
  log-adjacency-changes

interface Ethernet1/1-2
  medium p2p
  ip unnumbered loopback0
  ip router ospf OSPF_UNDERLAY_NET area 0.0.0.0

interface loopback0
  description Loopback
  ip address 192.168.0.6/32
  ip router ospf OSPF_UNDERLAY_NET area 0.0.0.0
```

## 查詢命令 ## 

```bash
show ip ospf neighbors #查看OSPF鄰居
sh ip route ospf-OSPF_UNDERLAY_NET #查看OSPF路由表
```