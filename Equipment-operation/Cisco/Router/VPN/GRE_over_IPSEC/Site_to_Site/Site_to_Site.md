# GRE over IPSec Site to Site #

## 實例 ##
    
### ISP ###

```python
enable 
configure terminal
hostname ISP
int e0/0
    ip address 123.0.1.254 255.255.255.0
    no shutdown
int e0/1
    ip address 123.0.2.254 255.255.255.0
    no shutdown
router ospf 1 #routing protocol
    router-id 1.1.1.1
    network 123.0.1.0 0.0.0.255 area 0
    network 123.0.2.0 0.0.0.255 area 0
```

## HQ ##

```python
enable
configure terminal
hostname HQ
ip route 0.0.0.0 0.0.0.0 123.0.1.254 #預設路由指向ISP
access-list 1 permit 10.1.1.0 0.0.0.255 #NAT內部網段
ip nat inside source list 1 interface e0/0 overload #NAT
int e0/0
    ip nat outside
    ip address 123.0.1.1 255.255.255.0
    no shutdown
int e0/1
    ip nat inside
    ip address 10.1.1.254 255.255.255.0
    no shutdown
int tunnel 0 
    ip address 192.168.1.1 255.255.255.0
    tunnel mode gre ip #mode為gre
    tunnel source e0/0 #來源介面
    tunnel destination 123.0.2.1 #目的IP
router ospf 1 #routing protocol 
    router-id 2.2.2.2
    network 123.0.1.0 0.0.0.255 area 0
    network 192.168.1.0 0.0.0.255 area 0
#IPSec 
access-list 100 permit gre host 123.0.1.1 host 123.0.2.1 #感興趣流量
crypto isakmp policy 10 #配置IKE Phase 1
    authentication pre-share #驗證使用PSK
    encryption aes #加密使用aes
    hash sha #驗證資料完整性使用sha
    group 14 #金鑰交換使用DH14
    exit
crypto isakmp key cisco address 123.0.2.1 #isakmp PSK
crypto isakmp transform-set TS esp-aes esp-sha-hmac #配置IPSec Phase 2，可選擇AH或ESP的驗證和加密方式
    mode transport #封裝模式使用Transport Mode
    exit
crypto map GRE_OVER_IPSEC 10 ipsec-isakmp #設定關聯
    set peer 123.0.2.1 
    set transform-set TS
    match address 100
    exit
int e0/0 #套用
    crypto map GRE_OVER_IPSEC 
```

## BRANCH ##

```python
enable
configure terminal
hostname BRANCH
ip route 0.0.0.0 0.0.0.0 123.0.2.254 #預設路由指向ISP
access-list 1 permit 172.16.1.0 0.0.0.255  #NAT內部網段
ip nat inside source list 1 interface e0/0 overload  #NAT
int e0/0
    ip nat outside
    ip address 123.0.2.1 255.255.255.0
    no shutdown
int e0/1
    ip nat inside
    ip address 172.16.1.254 255.255.255.0
    no shutdown
int tunnel 0 
    ip address 192.168.1.2 255.255.255.0
    tunnel mode gre ip #mode為gre
    tunnel source e0/0 #來源介面
    tunnel destination 123.0.1.1 #目的IP
router ospf 1 #routing protocol 
    router-id 3.3.3.3
    network 123.0.2.0 0.0.0.255 area 0
    network 192.168.1.0 0.0.0.255 area 0
#IPSec 
access-list 100 permit gre host 123.0.2.1 host 123.0.1.1 #感興趣流量
crypto isakmp policy 10 #配置IKE Phase 1
    authentication pre-share #驗證使用PSK
    encryption aes #加密使用aes
    hash sha #驗證資料完整性使用sha
    group 14 #金鑰交換使用DH14
    exit
crypto isakmp key cisco address 123.0.1.1 #isakmp PSK
crypto isakmp transform-set TS esp-aes esp-sha-hmac #配置IPSec Phase 2，可選擇AH或ESP的驗證和加密方式
    mode transport #封裝模式使用Transport Mode
    exit
crypto map GRE_OVER_IPSEC 10 ipsec-isakmp #設定關聯
    set peer 123.0.1.1 
    set transform-set TS
    match address 100
    exit
int e0/0 #套用
    crypto map GRE_OVER_IPSEC 
```

## PC1 ##

```python
enable
configure terminal
hostname PC1
ip default-gateway 10.1.1.254
int e0/0
    ip address 10.1.1.100 255.255.255.0
    no shutdown 
```

## PC2 ##

```python
enable 
configure terminal
hostname PC2
ip default-gateway 172.16.1.254
int e0/0
    ip address 172.16.1.100 255.255.255.0
    no shutdown 
```