# EIGRP Optimization #

## 調整最大跳躍數 ##

EIGRP預設最大跳躍數為100，可經由調整增加至255

```bash
router eigrp 1
    metric maximum-hops 255 
```

## 調整頻寬 ##

此頻寬非實際傳輸頻寬，而是用來計算用的頻寬，當有兩條相同路由指向不同路徑時，若線路頻寬相同，那就做負載平衡，但如果一條線路的頻寬為100M，一條為10M，就不適合做負載平衡，這時候就需要用bandwidth調整頻寬讓路由優先走速度較快的那條，直到這條down掉才會切換為速度較低的那條線路

```bash
int f0/0
    bandwidth 100 #單位為kb
```

## 調整間隔時間(雙方都必須調整) ##

調整間隔時間可加速收斂速度，預設Hello Interval為5秒，Hold Interval為15秒，建議設定比例為1:3，若Hello Interval大於Hold Interval會造成鄰居不斷中止和恢復，造成route flapping 

```bash
int f0/0 #須從介面調整
	ip hello-interval eigrp 1 1 #1為Autonomous System Number，10為要更改的Hello間隔
	ip hold-time eigrp 1 3 ##1為Autonomous System Number，10為要更改的Hold間隔
```

## 關閉不必要啟用EIGRP的介面 ##

```bash
passive-interface default #所有介面停止發送Hello,開啟後會停止發送路由更新，以及傳入的路由更新
no passive-interface e0/0 #此介面可發送Hello以及路由更新
```

## 自動路由匯總##

EIGRP預設將自動匯總關閉

```bash 
auto-summary 
```

## 手動路由匯總 ##

```bash 
ip summary-address eigrp 1 192.168.0.0 255.255.0.0 #1為Autonomous System Number，之後為匯總的範圍
```

## 使用雜湊驗證 ## 

使用MD5

```bash 
key chain EIGRP-Auth #建立key chain
	key 1 #新增key，id為1
	key-string P@ssw0rd #認證密碼	
int f0/0 
    ip authentication mode eigrp 1 md5 #介面啟用MD5驗證
	ip authentication key-chain eigrp 1 EIGRP-Auth #介面套用key-chain
```	

要使用SHA256，需用Virtual-Instance Name配置EIGRP 

```bash
router eigrp instance1 
    address-family ipv4 unicast autonomous-system 45000 
    address-family ipv6 unicast autonomous-system 46000 
    network 0.0.0.0 255.255.255.255 
    af-interface e0/0
        authentication mode hmac-sha-256 Cisco123 
```