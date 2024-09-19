# IPv6 #

## IPv6 位置配置方式 ##

1. 手動配置IPv6位置
2. ICMPv6自動生成
3. DHCPv6自動配置

## 位置分配原則 ##

假設今天拿到一段/56的網段，可以依照以下原則進行分配

1. Loopback位置分配/128
2. 點到點線路分配/127

>hint:因ipv6沒有廣播位置，所以分配127等於有兩個可用位置，例如2001:db8:a10:10::/127可用位置為2001:db8:a10:10::0/127和2001:db8:a10:10::1/127

3. 每個伺服器區/無線區域網路/內部區域等區域配置1個/64網段


## IPv6 Address ##

IPv6有三種位置類型，分別是Unicast、Multicast和Anycast，詳細可參考下圖

![](Image/IPv6%20address.png)

**Unicast**

單播位置可分成以下幾種

- Global Unicast 可通過網際網路進行溝通的IPv6位置，類似於IPv4的Public IP，範圍為從2000::/3開始的位置
- Unique Local Unicast 類似於IPv4的Private IP，無法進行互聯網上的路由轉發，但可作為組織內部通信使用，範圍為FC00::/7開始的位置
- Link Local Unicast 僅在本地有效，無法路由，通常用於同一鏈路中的通信或者用於ND，範圍為FE80::/10開始的位置
- Embedded IPv4 Address 嵌入式IPv4地址允許IPv6地址中包含一個IPv4地址，用於支持雙協議設備之間的通信，這是為IPv6過渡機制設計的，範圍為::ffff:0:0/96 開頭的IPv6地址，後面包含一個IPv4地址

**Multicast**

常見的組播有以下兩種

- FF02::1 所有支援IPv6的主機都會加入
- FF02::2 所有IPv6的Router都會加入(開啟ipv6 unicast-routing)

**Anycast**

IPv6並沒有廣播，Anycast主要用於NDP通信


## Reference ## 

https://ipv6.twnic.tw/download/SOP/1/01.IPv6_SOP_IP_Network_final3.pdf

https://blog.csdn.net/m0_55708805/article/details/115798614