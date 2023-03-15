# OSPF配置方法 #


## OSPFv2 ## 

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

## 路由匯總 ##

要在ABR匯總以下四筆路由可以使用以下命令

|network|subnet mask|
|---|---|
192.168.1.0|255.255.255.0|
192.168.2.0|255.255.255.0|
192.168.3.0|255.255.255.0|
192.168.4.0|255.255.255.0|

```bash
router ospf 1
	area 1 range 192.168.1.0 255.255.252.0 #這行指令會將上面四筆路由匯總成1筆192.168.1.0/22的路由
```

要在ASBR進行外部路由匯總可以使用以下命令

```bash
router ospf 1
	summary-address 192.168.20.0 255.255.252.0
```

## 預設路由 ##

```bash
default-information originate #如果沒加always，則需要先手動設一條預設路由
default-information originate always 
```

## Stub ## 

OSPF Stub可以將多筆再發佈的路由轉成一筆預設路由，讓末端的路由器只要路由表中找不到路由就直接找ABR

>再同一區域內的每台Router都要宣告area 1 stub，否則鄰居將會Down 

```bash
router ospf 1
	area 1 stub 
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

## OSPFv3 ##

