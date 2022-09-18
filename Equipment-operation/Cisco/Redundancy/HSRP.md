# Hot Standby Redundancy Protocl 熱備援冗餘協定 #

## 簡介 ##

    HSRP是Cisco專有的FHRP協定，用於進行閘道備援，閘道備援是非常重要的技術，不管在企業或校園網路中，只要閘道出現問題，可能造成整個園區網路癱瘓


## Multicast Address ##

HSRP使用組播位置

    224.0.0.2

## 配置方法 ##

### IPv4 ###

### 基礎配置 ###
```bash
standby 10 ip 192.168.1.254 #10為Group Number，兩端設定須相同
```
### 優化 ###

```bash
standby 10 priority 105 #優先權，優先權高的會成為Active，低的成為Standby，預設為100
standby 10 preempt #溝通過程中若是Priority發生變化，會依照最新的Priority決定設備將扮演Active or Standby 
standby 10 timers msec 200 msec 700 #調整Hello Interval和Hold Time，單位為毫秒，預設Hello Interval為3秒，Hold Time為10秒
standby 10 authentication md5 key-string Cisco123 #MD5驗證
```

### 防止對外端口Down ### 
```bash
ip sla 1 #新增IP SLA
    icmp-echo 8.8.8.8 source-ip 192.168.1.1 #ping測試8.8.8.8，來源ip為192.168.1.1
    frequency 2 #測試頻率為2秒
ip sla schedule 1 life forever start-time now #配置ip sla排程
track 1 ip sla 1 reachability #track 1 對應至ip sla 1
int vlan 10 #進入設置hsrp的介面
    standby 10 track 1 decrement 15 #套用track 1，若是Track 1 Down則Priority減15 
#追蹤對外介面，當介面出現問題時會自動將Priority降低，使其他正常的設備扮演Active
```

### IPv6 ###

```bash

```