# DMVPN OSPF Phase 2 #

## Topology ##

![](Image/Topology.png)

>拓樸已經預先配置了IP和Static Route指向ISP

## Phase 2 ##

確認Tunnel介面都可以連通後，接著要配置OSPF，在Phase 2中需要將OSPF網路類型更改回broadcast，因要讓Spoke-Spoke直接通訊，所以Spoke1的下一跳需要是Spoke2

```bash
[HQ]
int tun 0
    ip ospf network broadcast #將OSPF網路類型從P2P更改成Broadcast  
    ip ospf priority 255 #由Hub作為DR
[BRANCH1]
int tun 0 
    ip ospf network broadcast #將OSPF網路類型從P2P更改成Broadcast 
    ip ospf priority 0 #Spoke放棄DR/BDR選舉
[BRANCH2]
int tun 0 
    ip ospf network broadcast #將OSPF網路類型從P2P更改成Broadcast  
    ip ospf priority 0 #Spoke放棄DR/BDR選舉
```

最後檢查

```bash
show dmvpn #查看DMVPN是否成功啟用
traceroute 192.168.3.1 source 192.168.2.1 #確定spoke之間能夠不通過Hub通信，第一次traceroute還是會通過Hub，因為需要查詢NHRP映射並放入映射表中，第二次就可直接找到Branch2
show ip nhrp brief #traceroute完後可再次使用show ip nhrp brief就可看到一條D的映射
show ip route ospf #從BRANCH1查看從BRANCH2收到的內網路由下一跳為BRANCH2
```

## Reference ## 

https://network-insight.net/2015/02/03/design-guide-dmvpn-phases/
