# DMVPN-OSPF #

## Topology ##

![](Image/Topology.png)

>拓樸已經預先配置了IP和Static Route指向ISP

## Phase 1 ##

```bash
[HQ]
int tunnel 0 
    tunnel mode gre multipoint #模式調整成mGRE
    tunnel source G0/0 #來源
    ip address 192.168.100.1 255.255.255.0 #目的地
    ip nhrp network-id 100 #Router-ID需相同，用於區分假設需要多個Tunnel介面來建立DMVPN
    ip nhrp map multicast dynamic #在HUB(NHS配置)，實際上Tunnel為NBMA介面，用於將Spoke傳遞的路由複製一份傳送給所有開啟NHRP Dynamic Learn的Spoke Router 
    ip nhrp authentication cisco #驗證，可選
[Branch1]
int tunnel 0
    tunnel source g0/0 
    ip address 192.168.100.2 255.255.255.0 
    ip nhrp network-id 100 #Router-ID需相同，用於區分假設需要多個Tunnel介面來建立DMVPN
    ip nhrp nhs 192.168.100.1 #配置Hub(NHS)的Tunnel IP，讓Spoke向他發起NHS查詢
    ip nhrp map 192.168.100.1 123.0.1.1 #手動配置nhrp映射表項
    ip nhrp map multicast 123.0.1.1 #指定Hub的公網IP
    ip nhrp authentication cisco #驗證，可選
[Branch2]
int tunnel 0
    tunnel source g0/0 
    tunnel destination 123.0.1.1
    ip address 192.168.100.3 255.255.255.0 
    ip nhrp network-id 100 #Router-ID需相同，用於區分假設需要多個Tunnel介面來建立DMVPN
    ip nhrp nhs 192.168.100.1 
    ip nhrp map 192.168.100.1 123.0.1.1 
    ip nhrp map multicast 123.0.1.1 
    ip nhrp authentication cisco #驗證，可選
```

>可以使用show dmvpn或show ip nhrp查看是否成功註冊NBMA以及Tunnel Address

確認Tunnel介面都可以連通後，接著要配置路由協定，因OSPF預設使用Tunnel建立鄰居網路類型為P2P，P2P無法建立多個鄰居傳遞路由，所以須將網路類型更改為Point-to-Multipoint

>不使用boardcast是因為如果使用boardcast建立鄰居的話會當成所有鄰居的鏈路都是可連通的，所以會導致spoke1要將路由傳遞給spoke2時，下一跳為spoke2而不是hub，但spoke1-spok2實際上是沒有線路互聯的，NHRP也查不到對方的映射，導致路由傳遞不過去

HQ

```bash

```

Branch1 

```bash

```

Branch2 

```bash

```




## Reference ## 

https://network-insight.net/2015/02/03/design-guide-dmvpn-phases/
