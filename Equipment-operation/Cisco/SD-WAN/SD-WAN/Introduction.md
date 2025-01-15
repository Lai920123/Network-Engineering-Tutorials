# Introduction #

## SD-WAN 角色與功能 ##

**vManage** - Management Plane，管理SD-WAN，配置設定的儀表板，負責收集數據並分析對SD-WAN結構中的事件發出警報，可部屬於本地或雲端

**vBond** - Orchestration Plane，負責協調Edge Router與Controller的連接，幫助設備加入SD-WAN Fabric，設備要加入SD-WAN需先找到vBond進行認證

**vSmart** - Control Plane，通告路由、策略和安全性，不參與數據轉發

**vEdge** - Data Plane，根據vSmart的路由策略進行數據轉發

**Transport Locator(TLOC)** - TLOC用於標示和定位Cisco WAN Edge和每個站點的Edge節點，TLOC以System-IP(類似Router-ID，只用於定位，不須可達)、Transport Color(MPLS、Internet等...)、Encapsulation來識別節點

## ##