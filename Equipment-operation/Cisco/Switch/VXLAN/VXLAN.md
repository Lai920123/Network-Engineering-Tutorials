# Virtual Extensible LAN #

VXLAN是為了解決傳統網路中的問題，通過使用VTEP封裝MAC到UDP，再發送到遠端VTEP，遠程VTEP收到後進行拆封並轉發至目的地

## VLAN vs VXLAN ##

||VLAN|VXLAN|
|---|---|---|
|大小|12bit|24bit|
|可用範圍|4094個|1600萬個|
|協議|STP|ECMP routing|
|運作方式|在二層訊框中使用VLAN Tag進行封裝|使用MAC-in-UDP封裝|

## VTEP ## 
