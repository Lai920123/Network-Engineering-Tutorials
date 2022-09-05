# EIGRP

EIGRP為cisco專有的路由協定,屬於距離向量路由協定,使用組播位置224.0.0.10 

## IGP

## Distance Vector

## Multicast Address

## EIGRP設定

### EIGRP IPv4

```powershell
router eigrp 1 
	redistribute static #在發布靜態路由 
	network 192.168.0.0 
	network 172.16.0.0 
	network 10.0.0.0 
	passive-interface default 
	no passive-interface e0/0
```

### EIGRP IPv6

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