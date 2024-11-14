# Virtual Extensible Local Area Network(VXLAN)虛擬區域網擴展 #


## Network Virtualization Edge(NVE) ##

啟用VXLAN的設備及可稱為NVE

## VXLAN Network Identifier(VNI) ##

可以理解為VLAN Tag，包含在VXLAN Header中，以此來進行隔離

## VXLAN Tunnel Endpoints(VTEP) ##

類似於GRE Tunnel的概念，用於對VXLAN封包進行封裝後像對端發送，一條VTEP對應一條VXLAN隧道，通常使用設備的Loopback位置進行配置來源和目的地位置


## 集中式Gateway與分佈式
## EVPN路由類型 ##

**Route Type 1**

通告ESI，避免迴圈

**Route Type 2**

通告MAC位置

**Route Type 3**


**Route Type 4**

**Route Type 5**


