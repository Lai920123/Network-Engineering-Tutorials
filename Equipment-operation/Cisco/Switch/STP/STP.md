# Spanning-Tree #

## STP的演變 ## 


    802.1D -> IEEE
    PVST+ -> Cisco
    802.1w(RSTP) -> IEEE
    Rapid PVST -> Cisco
    MST 

## Path Cost ## 

|頻寬| 路徑成本(舊) | 路徑成本(新)|
| --- | --- | --- |
| 10M | 100 ||
| 100M | 19 ||
| 1G | 4 ||
| 10G | 2 ||

## Max Age ## 

預設BPDU每2秒會發送一次Hello，Max Age為20秒

## Topology Change ## 

當拓樸中添加了新的裝置，Switch就會向Root Switch發送Topolohy Change Notification(TCN) BPDU，當Root Switch收到TCN BPDU後，會將Mac Address Table的Timeout時間縮短為15秒(Forward Delay)，所以Topology Change會持續35秒(Max Age + Forward Delay)

## UplinkFast ## 

UplinkFast是為了防止Access Layer交換機的Uplink發生故障時能夠快速進行轉換，不用等30秒的收斂時間，Uplinkfast會先將Block Port設定為Standby狀態，當Root Port斷掉時立刻轉換成Forwarding，不過在Rapid-pvst+中已經內建了uplinkfast，所以無需再下這條指令

>經由使用pvst開啟uplinkfast和開啟rapid-pvst+兩組進行測試發現到，雖說Rapid-pvst+內建了uplinkfast，但在Root Port斷掉時會Block Port會立即轉換成Root Port，ping卻會斷掉幾秒才繼續傳送，相反的使用pvst開啟uplinkfast在線路斷掉時會馬上轉成Root Port且網路不會中斷

```bash 
#查看是否開啟uplinkfast，若是在rapid-pvst+模式會顯示UplinkFast is enabled but inactive in rapid-pvst mode
show spanning-tree uplinkfast 
#開啟uplinkfast(全域配置)
spanning-tree uplinkfast 
```

## backbonefast ## 

```bash
#查看是否開啟backbonefast，若是在rapid-pvst+模式會顯示BackboneFast is enabled but inactive in rapid-pvst mode
show spanning-tree backbonefast 
spanning-tree backbonefast 
```

## Portfast ## 

Portfast通常用於Access Layer連接使用者端的介面，Portfast跳過Listening和Learning，直接將介面變成Forwarding，通常會與BPDU Guard一起使用，防止使用者攜帶自己的交換機接入機櫃造成Topology Change，開啟BPDU的介面只要接收到BPDU就會將介面變成err-disable，要復原只能由管理員手動shutdown再no shutdown，再下面的bpduguard會寫到如何進行自動復原err-disable 

```bash
int range e0/0-3 
    spanning-tree portfast edge 
    spanning-tree bpduguard enable 
```

## BPDU Guard ## 

上面已經介紹過如何開啟bpduguard，接下來就要介紹如何將err-disable的介面進行手動以及自動復原

查看被err-disable的介面 

```bash
show interface status err-disabled 
```

手動復原

```bash 
#先將介面關閉
shutdown 
#再開啟介面即可
no shutdown 
```

自動復原

```bash
#errdisable的原因，可以用下面提供的指令查看
errdisable recovery cause bpduguard 
#recovery間隔時間，單位為秒
errdisable recovery interval 30 
```

查看命令(很有用，需熟練)

```bash
#查看被err-disable的原因
show errdisable detect 
#查看甚麼原因有啟用errdiable recovery
show errdisable recovery 
```

## BPDU Filter ##



## Root Guard ##



## Loop Guard ##



## Reference ## 

https://www.cisco.com/c/zh_tw/support/docs/lan-switching/spanning-tree-protocol/69980-errdisable-recovery.html