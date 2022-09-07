# Enhanced Interior Gateway Routing Protocol (增強型內部閘道路由協定) #

EIGRP為Cisco專有的路由協定，屬於距離向量路由協定


## Multicast Address ##

EIGRP的組播位置為

	224.0.0.10

## Administrative Distance ##

EIGREP的管理距離值

	EIGRP Summary route = 5
	Internal EIGRP = 90
	External EIGRP = 170

## EIGRP參數和設定 ##

### EIGRP IPv4 ###

```powershell
router eigrp 1 #Autonomous System Number必須相同
	eigrp router-id 1.1.1.1 #Router-id格式與IP相同，長度為32bit
	network 192.168.0.0 #要發佈的網段，0.0.0.0代表全發佈
	redistribute static #再發佈靜態路由 
	passive-interface default  
	no passive-interface e0/0
```	


### EIGRP IPv6 ###

```powershell
EIGRP IPv6 
ipv6 router eigrp 1 
	no shutdown #15.0以前版本才需要下 
	passive-interface default 
	no passive-interface e0/0 
int e0/0 
	ipv6 eigrp 1 
int e0/1 
	ipv6 eigrp 1
```

### 檢查設定 ###

```bash
show ip protocols 
```

## 實例 ##

## Trouble Shooting ##
以下列出幾個配置EIGRP常見的錯誤Log以及解決辦法

```bash
#此錯誤為發送Hello的雙方網段不相同，將介面IP更改為正確網段即可
*Sep 7 11:55:27.574: %DUAL-6-NBRINFO: EIGRP-IPv4 1: Neighbor 10.1.13.3(Ethernet0/0) is blocked: not on common subnet (10.1.12.2/24)
```