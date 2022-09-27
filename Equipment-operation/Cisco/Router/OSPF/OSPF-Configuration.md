# OSPF配置方法 #


## 基礎配置 ##
```bash
#設定OSPF
router ospf <PID> #PID不需要相同，但通常會為了好辨識設定為相同
	router-id 1.1.1.1 #若不設定就會去抓取loopback，loopback也沒有的話就會找參與ospf中最大的interface
	network 10.0.0.0 0.0.0.255 area 0 
	network 172.16.0.0 0.0.0.255 area 1
	network 192.168.0.0 0.0.0.255 area 2
```

## 調整Priority ##

```bash
#選舉DR/BDR時會用到，越大越好，更改完後，要重啟ospf process
int e0/0
	ip ospf priority 100
int e0/1
	ip ospf priority 0 #直接放棄選舉
```

## 修改介面頻寬(計算成本用,非真實頻寬) ##
```bash
router ospf 1
auto-cost reference-bandwidth 1000 #單位為Mbits
#修改介面卡
int f0/0
    ip ospf cost 1
```

## 查找資訊 ##

```bash
#查看ospf
show ip ospf #查看ospf資訊，比較詳細
show ip ospf neighbor #查看ospf鄰居
show ip interface brief #查看哪個interface使用了ospf
show ip interface e0/0 #可以看到Hello Interval以及Dead Interval的時間
```

## 重啟ospf process ##

```bash
#查看ospf建立鄰接過程
debug ip ospf adj
#重啟ospf process 
clear ip ospf process
```
