# IPv6 #

## IPv6-Header ##


## 類型 ##

    與IPv4不同，IPv6沒有了廣播，
    Unicast：提供啟動ipv6的介面一對一溝通
    
    Multicast：傳送單一ipv6封包至多個目的地
    
    Anycast：暫時不討論
    
## Default Gateway ##
    
    IPv6的default gateway與IPv4的不同,IPv6以Router的LLA來作為default gateway
    
## Prefix ID ##
    
    IPv6的Prefix ID就類似於IPv4的subnet mask用於判斷IPv6位置是否取於同一網段,普遍的作法是將128bit的分為64bit的Prefix ID和64bit的Interface ID,Prefix ID的表示方法也和IPv4時不同,使用/64的方式表示使用64bit的Prefix ID，一般來說組織會接收/32的Prefix ID，並使用推薦的/64來建立interface ID，留下32bit的Prefix ID，這代表此組織具有32bit也就是接近43憶的子網路，每個子網具有64bit的可用位置
        
    
## Interface ID ##
    
    與IPv4的Host ID相同，用來計算使用的主機數量
    
## Unicast Address ##
    
    與只有一個位置的IPv4不同，IPv6的裝置通常會有兩個單播位置，分別為GUA以及LLA

### Global Unicast Address(GUA) ###
    
    由IANA分配位置區塊給5個RIR，目前只分配了前三個bit,範圍在2000::/3~3fff::/3)，等於IPv4的Public IP，此位置為全球獨一無二，可在網際網路上繞送的位置，GUA可以以靜態或動態方式配置
    
### Link-local Address(LLA) ###
    LLA在每個啟用IPv6位置的裝置上是必須的，若裝置無手動配置LLA，則會自動創建LLA(EUI)，不須與DHCP Server溝通，LLA用作於本地設備的溝通(範圍在fe80::/10的網段，與IPv4的169.254.0.0/16相同)，和路由器之間交換訊息,無法繞送於網際網路

--- 

## Unique Local Address ##
    
    Unique Local Address(範圍在fc00::/7~fdff::/7)使用於那些不需要與外部溝通的裝置，如印表機

---

## EUI-64(Extended Unique Identifier) ##
    
    IEEE定義了EUI-64(擴展唯一識別碼)，EUI-64使用48bit的Mac Address，並且插入16bit在Mac Address的中間來創建64bit的Interface ID。
    
## MAC組成 ##

    MAC Address總共為48bit，由24bit的OUI + 廠商自行分配的24bit流水號 = 48bit

### Organizationally Unique Identifier組織唯一識別碼 ###
    
    OUI佔用24bit也就是6位數的16進制數字，由IEEE分配給每一家製造商，不會重複
    
### Device Identifier裝置識別碼 ###

    佔用24bit也就是6位數的16進制數字，由製造商自行分配的流水號碼
    
## EUI-64運作流程 ##
    
    假設int f0/0的Mac位置為00:d8:61:34:64:80

    1.將MAC轉換為二進制
    0000 0000 1101 1000 0110 0001 0011 0100 0110 0100 1000 0000

    2.將OUI和device identifier分開
    OUI：0000 0000 1101 1000 0110 0001
    Device identifier：0011 0100 0110 0100 1000 0000
    
    3.在中間加入fffe的十六進制數字,也就是二進制的1111 1111 1111 1110。
    0000 0000 1101 1000 0110 0001 + 1111 1111 1111 1110 + 0011 0100 0110 0100 1000 0000

    4. 將第7bit的值轉換為1
    0000 0010 1101 1000 0110 0001 1111 1111 1111 1110 0011 0100 0110 0100 1000 0000
    
    5.轉換為十六進制就可以得到EUI-64生成的結果為02:d8:51:ff:fe:34:64:80，最後在組合上RA或DHCPv6給予的prefix length，例如prefix length為2001:db8:A01:1::1/64這個網段，則最後拿到的GUA位置會是2001:db8:A01:1:2d8:51ff:fe34:6480
    
---

### Randomly Generated Interface IDs ###

    根據操作系統，設備可能會使用隨機生成的Interface ID，而不是使用MAC位置和EUI-64，Interface ID建立後，不管透過EUI-64或者Randomly Generated，都可以與RA接收到的訊息結合

---

### Router Discovery ###

    在IPv6,裝置要動態取得IP,須使用ICMPv6的訊息來進行溝通,IPv6的router會每200秒傳送RA給所有啟用IPv6的設備,而主機端則使用RS訊息請求

    Router Advertisement(路由器通告)：路由器會傳送封包給啟動IPv6位置的節點，ICMPv6的RA訊息是對如何獲取IPv6 GUA的建議，預設並未開啟，若要開啟路由器RA，須使用指令ipv6 unicast-routing
    RA Message包含以下三個內容:
    prefix length:告訴設備所屬網段
    default gateway:告訴設備預設閘道
    dns address and domain name:告訴設備dns位置及網域名稱
        
    Router Solicitatiin (路由器請求):主機端對於IPv6的router進行請求資訊

### Neighbor Discovery ###

    IPv4透過ARP查找MAC與IP的對應，而IPv6使用ND來進行查找，ND分為以下兩種
    Neighbor Advertisement(鄰居通告)：回應MAC位置 

    Neighbor Solicitation(鄰居請求)：發送封包至Solicaited-Node Multicast Address，詢問對方的MAC位置

---

## 動態配置GUA的方法 ###
    動態配置GUA有以下三種方法
### SLAAC ###
    路由器RA會發送prefix length,default gateway的資訊給主機,此種方式不需要DHCPv6的服務。
    SLAAC的運作方式:
    1.Router先發送RA給本地鍊路
    2.PC使用SLAAC獲取RA給的資訊後使用EUI-64生成並創建自己的GUA

### SLAAC and stateless DHCPv6 Server ###
    路由器提供prefix length,default gateway,DHCPv6主機提供dns。
    SLAAC和stateless DHCPv6運作方式:
    1.PC傳送RS向所有IPv6的Router
    2.Router傳送RA並給予prefix length,default gateway
    3.PC向所有DHCPv6 Server傳送請求,以獲取必要資訊(dns server,domain name,prefix length...)
    配置SLAAC and stateless DHCPv6


### Stateful DHCPv6 ###
    有狀態的DHCPv6,路由器給予default gateway,其他資訊全部由DHCPv6給予。
    Stateful DHCPv6運作方式:
    1.PC傳送RS給所有的IPv6 Routers
    2.Router傳送RA訊息給所有IPv6的nodes,僅獲取default gateway
    3.PC向所有DHCPv6傳送請求,以獲取必要的資訊
    (dns server,domain name,prefix length...)
    配置Stateful DHCPv6

## 動態配置LLA ##

### EUI-64 Generated Interface ID ###
    同動態配置GUA

### Random 64-bit Generated Interface ID ###
    同動態配置GUA

在Cisco的Router上，預設使用EUI-64來生成Interface ID給所有的LLA，LLA一定是在鍊路中唯一的

![https://i.imgur.com/mQRcMN4.png](https://i.imgur.com/mQRcMN4.png)

---

## Multicast Address

常見的multicast group有:
### ff02::1 All-nodes multicast group ###
    和IPv4的廣播有一樣的效果,通常使用在在路由器傳送RA的時候。

### ff02::2 All-routers multicast group ###
    使用ipv6 unicast-routing將路由器啟用為IPv6路由器時,路由器就會成為此群組的成員,發送到此群組的封包會由本地或網計網路上的所有IPv6路由器做接收和處理。

![https://i.imgur.com/J9xhozW.png](https://i.imgur.com/J9xhozW.png)

Solicited-Node IPv6 Multicast 請求節點的IPv6多播 - 相似於All-routers multicast,他的優勢在於,可以通過定乙太網卡檢查目標MAC位置來過濾訊匡,而不將訊匡發送到非預期的目標