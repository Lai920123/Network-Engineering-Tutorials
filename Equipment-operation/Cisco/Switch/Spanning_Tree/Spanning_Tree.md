# Spanning-Tree

## Spanning-Tree的演變 ## 


    802.1D -> IEEE
    PVST+ -> Cisco
    802.1w(RSTP) -> IEEE
    Rapid PVST -> Cisco
    MST
    

## Bandwidth

|頻寬| 路徑成本(舊) | 路徑成本(新)|
| --- | --- | --- |
| 10M | 100 ||
| 100M | 19 ||
| 1G | 4 ||
| 10G | 2 ||

## 查看Spanning-Tree

```powershell
show spanning-tree summary
```

## 修改Spanning-Tree Mode

```powershell
spanning-tree mode [mst|pvst|rapid-pvst]
```

## 802.1D

### Max Age

預設BPDU每2秒會發送一次Hello，Max Age為20秒

### Topology Change

當拓樸中添加了新的裝置，Switch就會向Root Switch發送Topolohy Change Notification(TCN) BPDU，當Root Switch收到TCN BPDU後，會將Mac Address Table的Timeout時間縮短為15秒(Forward Delay)，所以Topology Change會持續35秒(Max Age + Forward Delay)

### uplink fast

### backbonefast

## RSTP

RSTP改善了Topology Change的收斂時間，並內建了Uplink fast及Backbone fast功能

### Max Age

RSTP將Max Age縮短為3秒一個Hello，Max Age為6秒

### Alternate port

### Backup port