# Virtual Router Redundancy Protocol 虛擬路由冗餘協定 #

## 簡介 ##

    VRRP與HSRP,GLBP的差別為，VRRP為標準協議，若是網路中存在多個廠牌的設備，就須使用VRRP進行閘道備援

## State ##

    VRRP State的表示方法為Master,Backup，與HSRP的Active,Standby不同，且VRRP預設Master Advertisement interval為1秒

## 虛擬IP與虛擬MAC ##

    VRRP Virtual MAC為0000.5E00.0100 + Group ID，例如Group ID為15，則Virtual MAC為0000.5E00.0100 + 15 = 0000.5E00.010F

## VRRPv2 ##

### 基礎配置 ###

```bash
vrrp 10 ip 192.168.1.254 #VRRP Group Number 10，虛擬IP為192.168.1.254
```

### 優化 ###

```bash
vrrp 10 priority 110 ##優先權，優先權高的會成為Master，低的成為Backup，預設為95
vrrp 10 timers advertise msec 200 #調整advertisement interval
vrrp 10 preempt #溝通過程中若是Priority發生變化，會依照最新的Priority決定設備將扮演Master or Backup，預設為開啟
```

### 防止對外端口Down ### 

```bash
ip sla 1 #新增IP SLA
    icmp-echo 8.8.8.8 source-ip 192.168.1.1 #ping測試8.8.8.8，來源ip為192.168.1.1
    frequency 2 #測試頻率為2秒一次
ip sla schedule 1 life forever start-time now #配置ip sla排程
track 1 ip sla 1 reachability #track 1 對應至ip sla 1
int vlan 10 #進入設置vrrp的介面
    vrrp 10 track 1 decrement 15 #套用track 1於priority較高的介面，若是Track 1 Down則Priority減15，追蹤對外介面，當介面出現問題時會自動將Priority降低，使其他正常的設備扮演Master
```

### 使用md5驗證 ###

```bash
#以下兩種方式擇一即可
#使用key-string
int f0/0 #進入要配置的介面
    vrrp 10 authentication md5 key-string Cisco123
#使用key-chain
key chain vrrp1 #chain的名字
    key 1 #key id 
    key-string Cisco123 #密碼
int f0/0 #進入要配置的介面
    vrrp 10 authentication md5 key-chain vrrp1 #將key-chain套用至介面
```

## VRRPv3(未完成) ##

VRRPv2支援IPv4，VRRPv3支援IPv4和IPv6

```bash
fhrp version vrrp v3 #只有vrrp需手動開啟v3，要注意的是若是預先有配置IPv4的VRRPv2，要先解除掉才可以設定成VRRPv3，否則會出現Can't select: VRRP monolith version still running錯誤信息
#R1
int e0/0.1
	vrrp 1 address-family ipv4
	address 10.1.1.254 primary 
	priority 110 
	timers advertise 200
	track 1 decrement 15 
	preempt 
	vrrp 1 address-family ipv6
	address FE80::A8BB:CCFF:FE00:2000 primary #填入要成為master的Link-Local Address 
	priority 110 
	timers advertise 200 
	track 1 decrement 15 
#R2
int e0/0.10
	vrrp 10 address-family ipv4
	address 10.1.10.254 primary 
	priority 110 
	timers advertise 200
	track 1 decrement 15 
	preempt 
	vrrp 10 address-family ipv6
	address FE80::A8BB:CCFF:FE00:2000 primary 
	priority 110 
	timers advertise 200 
	track 1 decrement 15 

int e0/0.20
	vrrp 20 address-family ipv4
	address 10.1.20.254 primary 
	timers advertise 200
	vrrp 20 address-family ipv6
	address FE80::A8BB:CCFF:FE00:3000 primary 
	timers advertise 200 

int e0/0.1
	vrrp 1 address-family ipv4
	address 10.1.1.254 primary 
	timers advertise 200
	vrrp 1 address-family ipv6
	address FE80::A8BB:CCFF:FE00:2000 primary 
	timers advertise 200 
int e0/0.10
	vrrp 10 address-family ipv4
	address 10.1.10.254 primary 
	timers advertise 200
	vrrp 10 address-family ipv6
	address FE80::A8BB:CCFF:FE00:2000 primary 
	timers advertise 200 
int e0/0.20
	vrrp 20 address-family ipv4
	address 10.1.20.254 primary 
	timers advertise 200
	priority 110
	vrrp 20 address-family ipv6
	address FE80::A8BB:CCFF:FE00:3000 primary 
	priority 110 
	timers advertise 200 
	track 1 decrement 15 
```