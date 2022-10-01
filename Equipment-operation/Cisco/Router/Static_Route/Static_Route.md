# Static-Route #

## 路由類型 ##

### 靜態路由 ###

    手動於路由器或三層交換機中配置路由

### 預設路由 ###

    預設路由為一組能到任何地方的路由，用於在當目的地未知時，路由器會選擇的路由

### 浮動靜態路由 ###

    靜態路由可藉由調整Metric(成本)來達到備援的作用，Metric較低的不會顯示出來，當Metric高的那條線路Down，會轉為Metric較低的線路

## 配置方法 ##

```bash 
#靜態路由
ip route 192.168.100.0 255.255.255.0 123.0.1.2
#預設路由
ip route 0.0.0.0 0.0.0.0 123.0.1.2 
#浮動靜態路由
ip route 192.168.100.0 255.255.255.0 1.1.1.1 5 #5為成本
ip route 192.168.100.0 255.255.255.0 2.2.2.2 10 #Metric較低的不會顯示在FIB中
```

## Next-Hop使用IP或Interface的差異 ## 

### 使用IP作為Next-Hop ###

    在進行查找時，如果不知道Next-Hop的Mac Address會進行一次ARP請求詢問Next-Hop的Mac Address，並記錄於ARP Table中，下次只要為同一個Next-Hop的流量都不須再發ARP請求

### 使用Interface作為Next-Hop ###

    在進行查找時，發現Next-Hop為Interface而不是IP的話，路由器會進行ARP詢問目的地的MAC Address，所以若是每一次要傳送封包到目的地都需經過一次ARP查詢，會大大的降低路由器效能，因此不推薦使用