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

配置OSPFv3有兩種方法，下面會示範兩種方法的配置方式

## 第一種 ##

配置單獨的IPv6 OSPF進程，若是要同時使用ipv4/ipv6的OSPF，就需要建立兩個單獨的進程，會消耗更多的系統資源

```bash
router ospf 1
    router-id 1.1.1.1 
	network 192.168.1.0 0.0.0.255 area 0
	network 192.168.100.0 0.0.0.255 area 1
ipv6 unicast-routing #開啟ipv6繞送，不管使用哪種方式都要開啟，一定要記得開
ipv6 router ospf 1
	router-id 1.1.1.1 
int e0/0
    ipv6 ospf 1 area 0
int e0/1
    ipv6 ospf 1 area 1 
```

## 第二種 ##

將ipv4/ipv6的設定配置於同一個進程，可以更有效的使用系統資源，也更好管理

```bash
ipv6 unicast-routing #開啟ipv6繞送
router ospfv3 1
	router-id 1.1.1.1 
	address-family ipv4 unicast 
	address-family ipv6 unicast 
int e0/0
    ospfv3 1 ipv4 area 0
	ospfv3 1 ipv6 area 0
int e0/1
    ospfv3 1 ipv4 area 1
	ospfv3 1 ipv6 area 1

```

