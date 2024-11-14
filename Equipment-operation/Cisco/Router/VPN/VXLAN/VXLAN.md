# Virtual Extensible Local Area Network(VXLAN)虛擬區域網擴展 #


## Network Virtualization Edge(NVE) ##

啟用VXLAN的設備及可稱為NVE

## VXLAN Network Identifier(VNI) ##

可以理解為VLAN Tag，包含在VXLAN Header中，以此來進行隔離

## VXLAN Tunnel Endpoints(VTEP) ##

類似於GRE Tunnel的概念，用於對VXLAN封包進行封裝後像對端發送，一條VTEP對應一條VXLAN隧道，通常使用設備的Loopback位置進行配置來源和目的地位置

- **靜態VXLAN Tunnel**
  - 管理員手動配置每一個nve interface，配置較多
- **動態VXLAN Tunnel**
  - 使用BGP動態建立VXLAN Tunnel，利用BGP EVPN路由傳遞VNI和VTEP信息，從而動態建立VXLAN Tunnel

## 集中式與分佈式閘道 ##

**集中式Gateway**

- **優點**
  - 跨網段集中管理，簡單部屬 
- **缺點**
  - 非最佳轉發路徑，ARP表瓶頸
  - 閘道路由器須維護大量終端的MAC地址表，對設備負擔較大

**分佈式Gateway**

- **優點**
  - 擴展能力較強
  - VTEP節點只學習連接節點下的終端設備ARP表
- **缺點**
  - 部屬難度較高

## EVPN路由類型 ##

**Route Type 1**

通告ESI，避免迴圈

**Route Type 2**

通告MAC位置

**Route Type 3**


**Route Type 4**

**Route Type 5**


