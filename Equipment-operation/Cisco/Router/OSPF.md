# OSPF

## AS

Autonomous System自治系統，一個AS是一個能自主決定該採用何種路由協定的單位，例如企業或學校

## IGP

Interior Gateway Protocol內部路由服務，在一個AS內運作的路由協定

## Link-State Protocols

在鍊路狀態的路由協定中，每個路由器都擁有一張網路拓樸，可以分辨出接收到的路由信息是由誰發出來的

## Multicast Address

組播位置，OSPF的組播位置有兩種，分別為

224.0.0.5

224.0.0.6

## LSA

Link-State Advertisement 鍊路狀態通告

每個LSA都包含了一個Sequence number，Sequence number大小為4-byte，從-0x80000001 ~ 0x7FFFFFFF，在SPF的算法中，會經由比較LSA Sequence number的大小來判斷此LSA是否為新的LSA，越大則代表越新，接著在加入LSDB中

## LSDB

Link-State Datebase 鍊路狀態資料庫，同個區域中的每個Router會有相同的LSDB

## SPF Algorithm

Shorest Path First Algorithm 最短路徑優先演算法，也可叫做Dijksra Algorithm，是以發明此演算法的人命名，OSPF使用此演算法算出最短路徑

## Area概念

1. 最小化路由表
2. 本地的拓樸變動，只會影響到該區域
3. 有些LSA只會在該區域內傳播，不會傳送到整個拓樸中

## Backbone area

骨幹區域，又稱為Transit area或者area 0

## Regular area

常規區域，又稱為nonbackbone areas，非骨幹區域的area

## BR

Backbone Router 骨幹路由器，最少一個Interface連接Area 0，稱為BR

## ABR

Area Border Router 區域邊界路由，連接兩個Area以上稱為ABR

## ASBR

Autonomous System Border Router 自治系統邊界路由，連接其他AS的Router稱為ASBR

## DR

Designated Router 指定路由器，由DR跟BDR和DROTHERs進行LSA的溝通，在統一發送結果，DROTHERs之間不會進行LSA的溝通，避免造成過多不必要的流量

## BDR

Backup Designated Router 備份指定路由器，若是DR故障，則BDR會晉升成為DR繼續進行LSA的溝通，但若是故障的DR又重新回到拓樸中，也不會重新進行election，等到下一次重啟OSPF時才會重新進行election

## DROTHERs

不是DR也不是BDR則稱為DROTHERs

## Neighbor和Adjacency的差異

### Neighbor

鄰居，建立鄰居的過程只到two-way就結束

### Adjacency

鄰接，建立鄰接包含整個過程

## OSPF封包類型

### Hello

發現鄰居並建立鄰接，OSPF預設Hello Interval為10秒，Dead Interval為40秒

### DBD

Database Description 資料庫描述

DBD中包含了LSA的部份描述，接收到DBD後，就會發現缺少哪些LSA的訊息，再進行後續的請求

### LSR

Link-State Request 鍊路狀態請求

向其他Router請求詳細的LSA信息

### LSU

Link-State Update 鍊路狀態更新

傳送指定請求的LSA

### LSACK

Link-State Acknowledgment 鍊路狀態確認

用來進行LSU的確認

## OSPF鄰居建立過程

![Untitled](OSPF%207482c02b478f4f50aaace740ccd1ddfc/Untitled.png)

### Down

不發送Hello 

### Init

開始向對方發送Hello

### Two-way

選擇DR/BDR，建立鄰居關係

### Exstart

預備交換鍊路資訊

### Exchange

交換DBD，讓對方知道它需要哪些LSA

### Loading

開始交換LSA

### Full

交換完成，建立鄰接關係

## 路徑成本計算

```bash
#公式，注意計算單位，10^8單位為bit，interface為K,M或G
10^8/interface
10^8 = 100M 
#範例
#介面卡頻寬為100M
10^8/100 = 100/100 = 1
#但有個問題是，若介面卡頻寬為1G也就是1000M，計算結果會取正整數，也就是1，這就會造成
#100M和1000M的計算結果是相同的，解法為修改介面卡頻寬，以下為修改命令
#進入ospf修改
router ospf 1
auto-cost reference-bandwidth 1000 #單位為Mbits
#修改介面卡
int f0/0
ip ospf cost 1
```

## OSPF vs EIGRP

## OSPF設定

```bash
#設定OSPF
router ospf <PID> #PID不需要相同，好辨識即可
	router-id 1.1.1.1 #若不設定就會去抓取loopback，loopback也沒有的話就會找參與ospf中最大的interface
	network 10.0.0.0 0.0.0.255 area 0 #注意是使用wildcard mask
	network 172.16.0.0 0.0.0.255 area 1
	network 192.168.0.0 0.0.0.255 area 2
#調整Priority(選舉DR/BDR時會用到，越大越好)，更改完後，其他Router要重啟ospf process
int e0/0
	ip ospf priority 100
int e0/1
	ip ospf priority 0 #直接放棄選舉
#查看ospf建立鄰接過程
debug ip ospf adj
#重啟ospf
clear ip ospf process
#查看ospf
show ip ospf #查看ospf資訊，比較詳細
show ip ospf neighbor #查看ospf鄰居
show ip interface brief #查看哪個interface使用了ospf
show ip interface e0/0 #可以看到Hello Interval以及Dead Interval的時間
```