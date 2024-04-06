# Route Reflector #

Route Reflector是用來讓IBGP網路中不需要全連接的情況下，也能夠達到全連接的效果，這樣就不需要每個BGP Peer都要連接到所有的BGP Peer上，這樣就可以減少BGP Peer的數量，也可以減少BGP Peer的配置。

## Route Reflector運作方式 ##

假設有一個IBGP網路，R1為Route Reflector，兩台Non Client和一台Client，如下圖所示：

![](Image/Route%20Reflector%201.png)

當R2使用network命令發佈一條路由時，R2是Non Client，Non Client不會將路由發給Non Client，但會發給Client，所以RR會將這條路由發給R3、R4，但不會發給R5

![](Image/Route%20Reflector%202.png)

當R3使用network命令發佈一條路由時，R3是Client，Client會將路由發給Non Client和Client還有自己，不過發給自己的會檢測是自己發出的接著丟棄，避免迴圈，所以RR會將這條路由發給R2、R4、R5

![](Image/Route%20Reflector%203.png)


## Cluster-ID ##

