# DMVPN-OSPF #

## Topology ##

![](Image/Topology.png)

>拓樸已經預先配置了IP和Static Route指向ISP

## Phase 1 ##

HQ

```bash
int tunnel 0 
    tunnel mode gre multipoint #模式調整成mGRE
    tunnel source G0/0 #來源
    ip address 192.168.100.1 255.255.255.0 #目的地
    ip nhrp network-id 100 #Router-ID需相同
    ip nhrp map multicast dynamic #傳送給所有開啟NHRP Dynamic Learn的Spoke Router 
```

Branch1 

```bash
int tunnel 0
    tunnel source g0/0 
    tunnel destination 123.0.1.1
    ip address 192.168.100.2 255.255.255.0 
    ip nhrp network-id 100 #Router-ID需相同
    ip nhrp nhs 192.168.100.1 
    ip nhrp map 192.168.100.1 123.0.1.1 
    ip nhrp map multicast 123.0.1.1 
```

Branch2 

```bash
int tunnel 0
    tunnel source g0/0 
    tunnel destination 123.0.1.1
    ip address 192.168.100.3 255.255.255.0 
    ip nhrp network-id 100 #Router-ID需相同
    ip nhrp nhs 192.168.100.1 
    ip nhrp map 192.168.100.1 123.0.1.1 
    ip nhrp map multicast 123.0.1.1 
```

>可以使用show dmvpn或show ip nhrp查看是否成功註冊NBMA以及Tunnel Address

確認Tunnel介面都可以連通後，接著要配置路由協定

HQ

```bash
router eigrp CISCO 
```

Branch1 

```bash

```

Branch2 

```bash

```



## Phase 2 ##

在Phase 2時，允許Spoke和Spoke通過隧道直接通信，不需通過Hub

## Phase 3 ##

在Phase 3時，加強Phase 2的擴充性，可在設定中使用路由協定等功能

## Reference ## 

https://network-insight.net/2015/02/03/design-guide-dmvpn-phases/
