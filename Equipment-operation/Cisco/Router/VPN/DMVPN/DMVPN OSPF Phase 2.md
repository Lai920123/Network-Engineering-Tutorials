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

## DMVPN over IPSEC ##

```bash
[HQ]
crypto isakmp policy 10 #建立isakmp policy 
    authentication pre-share #驗證使用PSK
    hash sha256 #驗證資料完整性使用sha256
    encryption aes 256 #加密使用aes 256
    group 14 #金鑰交換使用DH14
    lifetime 3600 #SA的生命週期為3600秒
    exit 
crypto isakmp key Cisco123 address 0.0.0.0 #設定PSK以及指定對端IP
crypto ipsec transform-set TS esp-aes 256 esp-sha256-hmac #配置IPSec Phase 2，可選擇AH或ESP的驗證和加密方式
    mode tunnel #模式為tunnel mode，視情況可選擇transport mode
    exit
crypto ipsec profile IPSEC_PROFILE #建立IPSec profile
    set transform-set TS #設定IPSec transform set
int tunnel 0 
    tunnel protection ipsec profile IPSEC_PROFILE
[BRANCH1]
crypto isakmp policy 10 #建立isakmp policy 
    authentication pre-share #驗證使用PSK
    hash sha256 #驗證資料完整性使用sha256
    encryption aes 256 #加密使用aes 256
    group 14 #金鑰交換使用DH14
    lifetime 3600 #SA的生命週期為3600秒
    exit 
crypto isakmp key Cisco123 address 0.0.0.0 #設定PSK以及指定對端IP
crypto ipsec transform-set TS esp-aes 256 esp-sha256-hmac #配置IPSec Phase 2，可選擇AH或ESP的驗證和加密方式
    mode tunnel #模式為tunnel mode，視情況可選擇transport mode
    exit
crypto ipsec profile IPSEC_PROFILE #建立IPSec profile
    set transform-set TS #設定IPSec transform set
int tunnel 0 
    tunnel protection ipsec profile IPSEC_PROFILE
[BRANCH2]
crypto isakmp policy 10 #建立isakmp policy 
    authentication pre-share #驗證使用PSK
    hash sha256 #驗證資料完整性使用sha256
    encryption aes 256 #加密使用aes 256
    group 14 #金鑰交換使用DH14
    lifetime 3600 #SA的生命週期為3600秒
    exit 
crypto isakmp key Cisco123 address 0.0.0.0 #設定PSK以及指定對端IP
crypto ipsec transform-set TS esp-aes 256 esp-sha256-hmac #配置IPSec Phase 2，可選擇AH或ESP的驗證和加密方式
    mode tunnel #模式為tunnel mode，視情況可選擇transport mode
    exit
crypto ipsec profile IPSEC_PROFILE #建立IPSec profile
    set transform-set TS #設定IPSec transform set
int tunnel 0 
    tunnel protection ipsec profile IPSEC_PROFILE
[檢查]
ping 192.168.3.1 source 192.168.2.1 #查看spoke是否可以互相通信
show crypto ipsec sa detail #查看SA是否建立且有流量通過
```

## Reference ## 

https://network-insight.net/2015/02/03/design-guide-dmvpn-phases/
