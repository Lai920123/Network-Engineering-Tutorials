## OSPF封包類型 ##

|Type|用途|
|---|---|
|Hello|發現鄰居並建立鄰接，OSPF預設Hello Interval為10秒，Dead Interval為40秒|
|DBD(Database Description 資料庫描述)|DBD中包含了LSA的部份描述，接收到DBD後，就會發現缺少哪些LSA的訊息，再進行後續的請求
|LSR(Link-State Request 鍊路狀態請求)|向其他Router請求詳細的LSA信息|
|LSU(Link-State Update 鍊路狀態更新)|傳送指定請求的LSA|
|LSACK(Link-State Acknowledgment 鍊路狀態確認)|用來進行LSU的確認|

## Link-State Advertisement ##

	每個LSA都包含了一個Sequence number，Sequence number大小為4byte，從-0x80000001 ~ 0x7FFFFFFF，在SPF的算法中，會經由比較LSA Sequence number的大小來判斷此LSA是否為新的LSA，越大則代表越新，接著在加入LSDB中

### LSDB ###

	Link-State Datebase 鍊路狀態資料庫，同個區域中的每個Router會有相同的LSDB