# OSPF #

* [簡介](#簡介) 

	- [Link-State Protocols](#link-state-advertisement)

	- [Multicast Address](#multicast-address)

	- [SPF Algorithm](#spf-algorithm)
  
* [OSPF鄰接過程](#ospf鄰接過程)

	- [Down](#down)
	- [Init](#init)
	- [Two-way](#two-way)
	- [Exstart](#exstart)
	- [Exchange](#exchange)
	- [Loading](#loading)
	- [Full](#full)

* [OSPF封包類型](#ospf封包類型)

* [Neighbor和Adjacency的差異](#neighbor和adjacency的差異)

* [成為鄰居條件](#成為鄰居條件) 

* [路徑成本計算](#路徑成本計算)

	


## 簡介 ##

	OSPF為開放標準的Link-State路由協定，可運作於多廠牌設備當中

### Link-State Protocols ###

	在鍊路狀態的路由協定中，每個路由器都擁有一張網路拓樸，可以分辨出接收到的路由信息是由誰發出來的

### Multicast Address ###

	組播位置，OSPF的組播位置有兩種，分別為
	224.0.0.5 - DR,BDR向DROTHER發送DD,LSA Request和LSA Update時使用
	224.0.0.6 - DROTHER向DR,BDR發送DD,LSA Request和LSA Update時使用

### SPF Algorithm ###

	Shorest Path First Algorithm 最短路徑優先演算法，也可叫做Dijksra Algorithm，是以發明此演算法的人命名，OSPF使用此演算法算出最短路徑

## Area概念 ##

	1. 最小化路由表
	2. 本地的拓樸變動，只會影響到該區域
	3. 有些LSA只會在該區域內傳播，不會傳送到整個拓樸中

## Backbone area ##

	骨幹區域，又稱為Transit area或者area 0

## Regular area ##

	常規區域，又稱為nonbackbone areas，非骨幹區域的area

## BR ##

![](OSPF/BR.png)

	Backbone Router 骨幹路由器，最少一個Interface連接Area 0，稱為BR，以上圖為例，R2和R3為BR

## ABR ##

![](OSPF/ABR.png)

	Area Border Router 區域邊界路由器，連接兩個Area以上稱為ABR，以上圖為例，R2為ABR

## ASBR ##

![](OSPF/ASBR.png)

	Autonomous System Border Router 自治系統邊界路由器，連接其他AS的Router稱為ASBR，以上圖為例，R2為ASBR

## DR ##

	Designated Router 指定路由器，由DR跟BDR和DROTHERs進行LSA的溝通，再統一發送結果，DROTHERs之間不會進行LSA的溝通，避免造成過多不必要的流量

## BDR

	Backup Designated Router 備份指定路由器，若是DR故障，則BDR會晉升成為DR繼續進行LSA的溝通，但若是故障的DR又重新回到拓樸中，也不會重新進行election，等到下一次重啟OSPF時才會重新進行election

## DROTHERs

	不是DR也不是BDR則稱為DROTHERs


## OSPF封包類型 ##

|Type|用途|
|---|---|
|Hello|發現鄰居並建立鄰接，OSPF預設Hello Interval為10秒，Dead Interval為40秒|
|DBD(Database Description 資料庫描述)|DBD中包含了LSA的部份描述，接收到DBD後，就會發現缺少哪些LSA的訊息，再進行後續的請求
|LSR(Link-State Request 鍊路狀態請求)|向其他Router請求詳細的LSA信息|
|LSU(Link-State Update 鍊路狀態更新)|傳送指定請求的LSA|
|LSACK(Link-State Acknowledgment 鍊路狀態確認)|用來進行LSU的確認|

## Link-State Advertisement ##

	每個LSA都包含了一個Sequence number，Sequence number大小為4-byte，從-0x80000001 ~ 0x7FFFFFFF，在SPF的算法中，會經由比較LSA Sequence number的大小來判斷此LSA是否為新的LSA，越大則代表越新，接著在加入LSDB中

### LSDB ###

	Link-State Datebase 鍊路狀態資料庫，同個區域中的每個Router會有相同的LSDB

## Neighbor和Adjacency的差異 ##

	Neighbor - 建立鄰居的過程只到two-way就結束
	Adjacency - 建立鄰接包含整個過程

## OSPF鄰接過程 ##

    下面以此拓樸做說明

![Untitled](OSPF/Adjacency1.png)

    完整鄰接過程

![Untitled](OSPF/Adjacency2.png)

### Down ###

    不發送Hello 

### Init ###

![Untitled](OSPF/Init.png)

    開始向對方發送Hello

### Two-way ###

![Untitled](OSPF/2way.png)

    進行DR/BDR選舉，建立鄰居關係，以上圖為例，可以看到選舉結果DR為R1，BDR為R2

### Exstart ###

![Untitled](OSPF/exstart.png)

    預備交換鍊路資訊

### Exchange ###

![Untitled](OSPF/exchange.png)

    交換DBD，讓對方知道它需要哪些LSA

### Loading ###

![Untitled](OSPF/Loading.png)

    開始交換LSA

### Full ###

    交換完成，建立鄰接關係

## 成為鄰居條件 ##

	1.Area ID相同
	2.Area Type相同
	3.網段相同
	4.Hello Interval以及Dead Interval需相同
	5.認證類型以及密碼一致
	6.MTU相同


## 路徑成本計算

```bash
#公式，注意計算單位，10^8單位為bit，interface為K,M或G
10^8/interface
10^8 = 100M 
#範例
#介面卡頻寬為100M
100000000/100000000 = 1
#但有個問題是，若介面卡頻寬為1G也就是1000M，計算結果會取正整數，也就是1，這就會造成
#100M和1000M的計算結果是相同的，解決方法為修改介面卡頻寬
```

