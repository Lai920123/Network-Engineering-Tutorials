# DMVPN EIGRP Phase 2 #

## Topology ##

![](Image/Topology.png)

>拓樸已經預先配置了IP和Static Route指向ISP

## Phase 2 ##

```bash
[HQ]
int tunnel 0 
    ip mtu 1492 
    tunnel mode gre multipoint #模式調整成mGRE
    tunnel source 123.0.1.1 #來源
    ip address 192.168.100.1 255.255.255.0 #目的地
    ip nhrp network-id 100 #Router-ID需相同，用於區分假設需要多個Tunnel介面來建立DMVPN
    ip nhrp map multicast dynamic #在HUB(NHS配置)，實際上Tunnel為NBMA介面，用於將Spoke傳遞的路由複製一份傳送給所有開啟NHRP Dynamic Learn的Spoke Router 
    ip nhrp authentication cisco #驗證，可選
[BRANCH1]
int tunnel 0
    ip mtu 1492
    tunnel source 123.0.2.1 
    ip address 192.168.100.2 255.255.255.0 
    ip nhrp network-id 100 #Router-ID需相同，用於區分假設需要多個Tunnel介面來建立DMVPN
    ip nhrp map 192.168.100.1 123.0.1.1 #手動配置nhrp映射表項
    ip nhrp map multicast 123.0.1.1 #指定Hub的公網IP
    ip nhrp nhs 192.168.100.1 #配置Hub(NHS)的Tunnel IP，讓Spoke向他發起NHS查詢
    ip nhrp authentication cisco #驗證，可選
[BRANCH2]
int tunnel 0
    ip mtu 1492
    tunnel source 123.0.3.1 
    ip address 192.168.100.3 255.255.255.0 
    ip nhrp network-id 100 #Router-ID需相同，用於區分假設需要多個Tunnel介面來建立DMVPN
    ip nhrp map 192.168.100.1 123.0.1.1 #手動配置nhrp映射表項
    ip nhrp map multicast 123.0.1.1 #指定Hub的公網IP
    ip nhrp nhs 192.168.100.1 #配置Hub(NHS)的Tunnel IP，讓Spoke向他發起NHS查詢
    ip nhrp authentication cisco #驗證，可選
[檢查]
show ip int br #查看Tunnel介面是否up
show ip nhrp brief #查看ip nhrp映射是否正確，從HQ看後面會顯示D，因HQ是使用動態映射，而從Branch看會顯示S，因Spoke是使用靜態映射
show ip nhrp nhs #從spoke查看nhs是否已經註冊，R代表NHS正常工作並回應NHRP查詢，E代表期望從NHS接收回應，W代表路由器正等待與NHS的通信，顯示RE代表正常，priority用於多台Hub時選擇主要路由器，Cluster用於在多Hub時將不同Hub分組
```

## Tranditional ## 

```bash
[HQ]
router eigrp 100 
    eigrp router-id 1.1.1.1 
    network 192.168.1.0 0.0.0.255 
    network 192.168.100.0 0.0.0.255 
int tun 0 
    no ip split-horizon eigrp 10 #練習時一開始先不要加這條，在建立完EIGRP時使用show ip route查看路由表，會發現收不到BRANCH2發的路由，就是因為水平分割
    no ip next-hop-self eigrp 100 
[Branch1]
router eigrp 100 
    eigrp router-id 2.2.2.2 
    network 192.168.2.0 0.0.0.255
    network 192.168.100.0 0.0.0.255 
[Branch2]
router eigrp 100 
    eigrp router-id 3.3.3.3 
    network 192.168.3.0 0.0.0.255 
    network 192.168.100.0 0.0.0.255 
```

## Named-Mode ##

```bash
[HQ]
ipv6 unicast-routing 
router eigrp DMVPN
    address-family ipv4 unicast autonomous 10 
        eigrp router-id 1.1.1.1 
        network 192.168.100.0 0.0.0.255 
        network 192.168.1.0 0.0.0.255 
        af-interface tunnnel 0
            no split-horizon #練習時一開始先不要加這條，在建立完EIGRP時使用show ip route查看路由表，會發現收不到BRANCH2發的路由，就是因為水平分割
            no next-hop-self #讓從BRANCH2接收到的路由傳遞出去時下一跳依舊是BRANCH2而不是更改為HUB
[Branch1]
router eigrp DMVPN 
    address-family ipv4 unicast autonomous 10 
        eigrp router-id 2.2.2.2
        network 192.168.100.0 0.0.0.255 
        network 192.168.2.0 0.0.0.255 
[Branch2]
router eigrp DMVPN 
    address-family ipv4 unicast autonomous 10 
        eigrp router-id 3.3.3.3
        network 192.168.100.0 0.0.0.255 
        network 192.168.3.0 0.0.0.255  
```