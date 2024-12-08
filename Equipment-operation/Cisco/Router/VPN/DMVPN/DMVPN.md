# Dynamic Multipoint Virtual Private Network #

DMVPN是一種用於建立高效且靈活的虛擬私人網路的技術。它通過結合點對點VPN和動態路由，使多個遠程站點能夠通過單個中心站點進行直接通信，同時實現了動態IP地址分配和隧道的動態建立，提供了簡化的網絡管理和更好的效能，DMVPN本身不提供加密，但可搭配IPSec達到加密功能，也可以和MPLS VPN搭配使用

## Next hop Resolution Protocol(NHRP) ##

根據路由表的下一跳IP(對端邊界Tunnel IP)，查找NHRP映射表，確定對端園區公網IP

Hub(NHS) 自動映射spoke的公網IP與Tunnel IP

每台spoke手工指定Hub的NHRP映射


## DMVPN Phase ## 

DMVPN分成三個Phase，下面會解釋三個階段分別在做甚麼

## Phase 1 ##

在Phase 1時，Hub可通過Tunnel介面到達所有Spoke，Spoke對Spoke的流量都需通過Hub

**優點** 
  - 可在Hub進行路由彙總以及過濾，管理較方便
  
**缺點**
  - 園區越多對Hub邊界路由器負載較大
  - Spoke對Spoke並非最佳路徑

## Phase 2 ##

在Phase 2時，允許Spoke和Spoke通過隧道直接通信，不需通過Hub

在Phase 2中，Spoke1發送NHRP查詢，HUB(NHS)發送NHRP應答來建立Spoke1與Spoke2的動態映射，Spoke1的NHRP有了Spoke2的NHRP映射後，就可以直接跟Spoke2通信，Spoke2與Spoke1通信也是相同概念

**優點** 
  - Spoke與Spoke可直接通信
  
**缺點**
  - 無法使用路由彙總

## Phase 3 ##

在Phase 3時，加強Phase 2的擴充性，可在設定中使用路由協定等功能

在Phase 3中，第一個包會向HUB取得Spoke2的NHRP映射，接下來Spoke1發送NHRP查詢，HUB會直接將查詢Redirect至Spoke2，讓Spoke2來應答

**優點** 
  - 123

**缺點**
  - 123

## Reference ## 

https://network-insight.net/2015/02/03/design-guide-dmvpn-phases/
