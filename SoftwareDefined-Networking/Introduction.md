# Introduction #

SDN是一種新型的網路結構，利用[OpenFlow](OpenFlow.md)將路由器中的control plane以及data plane分離，以軟體進行實做，使管理員能夠在不更動實體設備的狀況下，能夠以中央控制方式更改網路設定。


## Plane ## 

    不同plane各自的用途
    Management plane - 用於管理網路設備，如SNMP
    Control plane    - 控制封包轉發，由一個地方發送至另一個地方，如RIP,EIGRP,OSPF
    Data plane       - 將封包由input送至output，如FIB(Forwarding information Base 轉發表)

## Southbound interface and Northbound interface ##

Southbound interface : 
Northbound interface :

## 傳統網路與SDN的差別 ##
    
傳統網路為分散式控制架構，每台設備均有獨立的control plane以及data plane

