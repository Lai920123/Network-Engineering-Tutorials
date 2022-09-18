# Virtual Router Redundancy Protocol 虛擬路由冗餘協定 #

## 簡介 ##
    VRRP與HSRP,GLBP的差別為，VRRP為標準協議，若是網路中存在非Cisco的設備，就須使用VRRP，VRRP用於進行閘道備援，閘道備援是非常重要的技術，不管在企業或校園網路中，只要閘道出現問題，可能造成整個園區網路癱瘓

## State ##

    VRRP State的表示方法為Master,Backup，與HSRP的Active,Standby不同，且VRRP預設Master Advertisement interval為1秒，

## 虛擬IP與虛擬MAC ##
    VRRP Virtual MAC為0000.5E00.0100 + Group ID，例如Group ID為15，則Virtual MAC為0000.5E00.0100 + 15 = 0000.5E00.010F

## 配置方法 ##

### IPv4 ###

```bash 
vrrp 1 ip 192.168.1.254 #VRRP Group Number 1，虛擬IP為192.168.1.254
vrrp 1 priority 110 #配置優先權 
```

### IPv6 ###