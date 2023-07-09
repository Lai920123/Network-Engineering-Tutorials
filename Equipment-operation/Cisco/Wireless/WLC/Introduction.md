# WLC

## 簡介 ##

Wireless LAN Controller無線區域網路控制器，主要用於讓企業和學校有多個AP環境時，能夠更只在網路控制器進行管理，不需要一台一台進行設定
    
## 使用技術 ##

### Flexconnect ###
    
FlexConnect是一種分公司與遠端辦公的的解決方案，使你可以透過WAN在公司配置分公司的AP，而不用在每個分公司個別部屬網路控制器
        
### CAPWAP ###
        
CAPWAP是Control And Provisioning of Wireless Access Points的縮寫，
        
    
### Local AP Mode 和 Flexconnect AP Mode的差別 ###

- Local AP Mode中，Lightweight AP會創建兩條CAPWAP Tunnel，一條用於管理，另一條用於資料傳輸，這種行為稱為Centrally switched(集中交換)，因為Lightweight AP須先將資料流量送給Controller接著才會進行路由
- flexconnect允許資料傳輸在本地進行交換不須回到Controller，每一台Lightweight AP就像是一般AP一樣自行管理資料流量，但實際是從WLC進行管理，此模式中，即使Lightweight AP AP與WLC斷開連線，仍可以正常工作

## AP發現WLC的方法 ##

AP發現WLC有以下幾種方法:
- Layer 3 Broadcast 
- Previously known WLCs 
- DHCP Option 43
- Resolve DNS hostname (CISCO-CAPWAP-CONTROLLER.localdomain)
- Manually configured controllers 
    
LAP啟動過程:
1. 若未分配Static IP位置，LAP會通過DHCP獲取IP位置
2. 通過發現算法發現控制器並發送Discovery Request 

>Hint: LAP會記住啟動後加入的控制器管理IP位置，因此，如果先將LAP放在和控制器相同的子網上，他會找到控制器的管理介面IP並記住此位置，若是更換了LAP的網段後，有可能會找不到WLC的位置，因此Cisco建議使用DHCP Option 43找尋WLC

## Reference ## 

https://community.cisco.com/t5/%E6%97%A0%E7%BA%BF%E8%AE%A8%E8%AE%BA%E5%8C%BA/option43-dns-%E6%89%8B%E5%8A%A8%E8%AE%BE%E7%BD%AE%E8%BF%99%E5%87%A0%E7%A7%8D%E6%96%B9%E5%BC%8F%E5%8F%91%E7%8E%B0wlc%E7%9A%84%E4%BC%98%E5%85%88%E7%BA%A7/td-p/4788627