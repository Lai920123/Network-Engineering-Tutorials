# DMVPN OSPF Phase 1 #

## Topology ##

![](Image/Topology.png)

>拓樸已經預先配置了IP和Static Route指向ISP

## Phase 1 ##

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

>可以使用show dmvpn或show ip nhrp查看是否成功註冊NBMA以及Tunnel Address

確認Tunnel介面都可以連通後，接著要配置OSPF，因OSPF預設使用Tunnel建立鄰居網路類型為P2P，P2P無法建立多個鄰居傳遞路由，所以須將網路類型更改為Point-to-Multipoint

>不使用boardcast是因為如果使用boardcast建立鄰居的話會當成所有鄰居的鏈路都是可連通的，所以會導致spoke1要將路由傳遞給spoke2時，下一跳為spoke2而不是hub，但spoke1-spok2實際上是沒有線路互聯的，NHRP也查不到對方的映射，導致路由傳遞不過去

```bash
[HQ]
router ospf 1
    router-id 1.1.1.1 
    network 192.168.1.0 0.0.0.255 area 0
    network 192.168.100.0 0.0.0.255 area 0
int tun 0
    ip ospf network point-to-multipoint 
    ip ospf priority 255 #由Hub作為DR
[BRABCH1]
router ospf 1
    router-id 2.2.2.2 
    network 192.168.2.0 0.0.0.255 area 0
    network 192.168.100.0 0.0.0.255 area 0
int tun 0 
    ip ospf network point-to-multipoint 
    ip ospf priority #Spoke放棄DR/BDR選舉
[BRANCH2]
router ospf 1
    router-id 3.3.3.3 
    network 192.168.3.0 0.0.0.255 area 0
    network 192.168.100.0 0.0.0.255 area 0
int tun 0 
    ip ospf network point-to-multipoint 
    ip ospf priority #Spoke放棄DR/BDR選舉
```

最後檢查

```bash
show dmvpn #查看DMVPN是否成功啟用
traceroute 192.168.3.1 source 192.168.2.1 #在Phase 1 Spoke通信還是需要通過HUB
show ip nhrp brief #查看ip nhrp映射是否正確
show ip route ospf #從BRANCH1查看從BRANCH2收到的內網路由下一跳為HUB
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
