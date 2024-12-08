# DMVPN OSPF Phase 2 #

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
[Branch1]
int tunnel 0
    ip mtu 1492
    tunnel source 123.0.2.1 
    ip address 192.168.100.2 255.255.255.0 
    ip nhrp network-id 100 #Router-ID需相同，用於區分假設需要多個Tunnel介面來建立DMVPN
    ip nhrp map 192.168.100.1 123.0.1.1 #手動配置nhrp映射表項
    ip nhrp map multicast 123.0.1.1 #指定Hub的公網IP
    ip nhrp nhs 192.168.100.1 #配置Hub(NHS)的Tunnel IP，讓Spoke向他發起NHS查詢
    ip nhrp authentication cisco #驗證，可選
[Branch2]
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

確認Tunnel介面都可以連通後，接著要配置OSPF，在Phase 2中需要將OSPF網路類型更改回broadcast，因要讓Spoke-Spoke直接通訊，所以Spoke1的下一跳需要是Spoke2

```bash
[HQ]
router ospf 1
    router-id 1.1.1.1 
    network 192.168.1.0 0.0.0.255 area 0
    network 192.168.100.0 0.0.0.255 area 0
int tun 0
    ip ospf network broadcast #將OSPF網路類型從P2P更改成Broadcast  
    ip ospf priority 255 #由Hub作為DR
[BRANCH1]
router ospf 1
    router-id 2.2.2.2 
    network 192.168.2.0 0.0.0.255 area 0
    network 192.168.100.0 0.0.0.255 area 0
int tun 0 
    ip ospf network broadcast #將OSPF網路類型從P2P更改成Broadcast 
    ip ospf priority #Spoke放棄DR/BDR選舉
[BRANCH2]
router ospf 1
    router-id 3.3.3.3 
    network 192.168.3.0 0.0.0.255 area 0
    network 192.168.100.0 0.0.0.255 area 0
int tun 0 
    ip ospf network broadcast #將OSPF網路類型從P2P更改成Broadcast  
    ip ospf priority #Spoke放棄DR/BDR選舉
```

最後檢查

```bash
show dmvpn #查看DMVPN是否成功啟用
traceroute 192.168.3.1 source 192.168.2.1 #確定spoke之間能夠不通過Hub通信，第一次traceroute還是會通過Hub，因為需要查詢NHRP映射並放入映射表中，第二次就可直接找到Branch2
show ip nhrp brief #traceroute完後可再次使用show ip nhrp brief就可看到一條D的映射
show ip route ospf #從BRANCH1查看從BRANCH2收到的內網路由下一跳為BRANCH2
```
