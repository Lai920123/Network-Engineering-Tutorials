# Easy Virtual Network #

EVN（Easy Virtual Network） 是 Cisco 為 簡化多租戶網路（Multi-Tenant Network） 而開發的技術，主要用於 多 VRF（Virtual Routing and Forwarding）環境。它可以讓網管人員更輕鬆地管理多條邏輯獨立的網路，而不需要繁瑣的 VRF 設定。

## 配置 ##

**Topology**

```bash
[R1]
vrf definition red 
    address-family ipv4
        vnet tag 10 
vrf definition blue 
    address-family ipv4 
        vnet tag 20 
[R2]

[R3]

[R4]

[R5]

[R6]

```