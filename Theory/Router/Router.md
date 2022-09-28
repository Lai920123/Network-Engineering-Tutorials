# Router #

## Routing information Base 路由表 ##

    RIB用於儲存路由信息，可透過直連線路,靜態,動態路由取得路由並放入路由表中，Note:路由表並不會進行封包轉發
    
## Forwarding information Base 轉發表 ##
    FIB用於進行封包的轉發，在RIB從路由中選出最佳路徑後，會將最佳路徑的路由複製至FIB，再由FIB進行轉發

## 封包繞送過程 ##

    在Router接收到封包後，會先查詢IP Header中的Destination address是否存在於Route table中，若是沒有，就丟棄，若是有，Router會在進行第二次查詢，第二次查詢會找尋下一跳是否於Route table 中，有的話進行轉發，沒有的話則丟棄

## Cisco Express Forwarding ##