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
