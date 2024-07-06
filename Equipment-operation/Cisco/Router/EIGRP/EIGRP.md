# Enhanced Interior Gateway Routing Protocol (增強型內部閘道路由協定) #

>EIGRP為Cisco專有的路由協定，屬於距離向量路由協定，收斂速度快，但只能用於使用Cisco設備的環境

## Multicast Address ##

	224.0.0.10

## Maximum hop count ##

	EIGRP在Cisco路由器上預設的最大跳躍數為100，不過這可藉由調整達到最高跳躍數255，使用metric maximum-hops 255進行調整

## Administrative Distance ##

	Internal EIGRP = 90
	External EIGRP = 170
	EIGRP Summary route = 5

## Neighbors ##

	EIGRP預設Hello Time為5秒，Hold Time為15秒
	EIGRP Neighbors建立條件，以下都須相同才可建立Neighbors 
	1.Autonomous System Number
	2.K值
	3.網段
	4.認證訊息
	5.Hello Time
	6.Hold Time

## EIGRP參數和設定 ##

## IPv4 ##

### 基本配置 ###

```bash
router eigrp 1 #Autonomous System Number必須相同
	eigrp router-id 1.1.1.1 #Router-id格式與IP相同，長度為32bit
	network 192.168.1.0 #要發佈的網段，0.0.0.0代表全發佈
```

### 再發佈 ###

```bash
redistribute static #再發佈靜態路由 
```

## IPv6 ##

EIGRP for IPv6可使用兩種方法配置

### 傳統配置方法 ###

```bash 
ipv6 unicast-routing #開啟ipv6單播繞送
ipv6 router eigrp 1 
	no shutdown #15.0以前版本才需要下 
int e0/0 
	ipv6 eigrp 1 #從介面啟用eigrp for ipv6
int e0/1 
	ipv6 eigrp 1 #從介面啟用eigrp for ipv6
```

### 檢查設定 ###

```bash
show ip protocols #查看目前使用的路由協定
show ip eigrp neighbors #可以看到鄰居IP,Port號,Hold Time,UP Time
show ip eigrp interface
show ip eigrp interface detail
show ip eigrp topology #檢查EIGRP拓樸表
```

## 實例 ##

### Route Summarization ###
路由匯總用於減少路由表數量以及加速收斂時間，此練習幫助大家能夠快速了解何為路由匯總，以及自動和手動匯總的配置方法，練習檔案下載


## Trouble Shooting ##
以下列出幾個配置EIGRP常見的錯誤Log以及解決辦法

```bash
#此錯誤為發送Hello的雙方網段不相同，將介面IP更改為正確網段即可
*Sep 7 11:55:27.574: %DUAL-6-NBRINFO: EIGRP-IPv4 1: Neighbor 10.1.13.3(Ethernet0/0) is blocked: not on common subnet (10.1.12.2/24)
```