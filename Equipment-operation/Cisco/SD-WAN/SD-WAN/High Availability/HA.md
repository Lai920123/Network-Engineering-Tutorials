# SD-WAN組件HA #

## vManager ##

vManager在建立Cluster時需要先達到以下要求

- 需使用VPN 0且非建立Tunnel的介面來建立Cluster
- 另外新增一組group為netadmin的帳號
- 建立介面速度至少為1G，建議為10G

- 設計方法: 

如果要跨地理區域建議各個區域各別建立單節點(無cluster)、三節點或六節點cluster，不建議vManager之間跨區域建立Cluster

Cluster僅能提供一台vManager故障

**Edge使用特定介面連線至vManager**

以下命令會配置於Tunnel-Interface中，Edge會使用較高preference和vManager建立Tunnel 

```bash
[cEdge]
config-transaction 
sdwan 
    interface GigabitEthernet1
        tunnel-interface
            vmanage-connection-preference 
```

使用vManager GUI配置

Feature Template -> Cisco VPN Interface Ethernet -> TUNNEL -> vManage Connections Preference 

**檢查建立完Cluster後服務是否正確啟用**

```bash
request nms cluster diagnostics
request nms all status 
```

## vSmart ##

## vBond ##

vbond如果是用DNS進行配置的而不是直接指定IPv4 Address，直接修改DNS Record即可

```bash
#假設原有的vbond是192.168.1.100，在後面新增一台192.168.1.101
ip host vbond.example.com 192.168.1.100 192.168.1.101 
```