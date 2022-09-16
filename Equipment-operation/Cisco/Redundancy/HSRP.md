# Hot Standby Redundancy Protocl 熱備援冗餘協定 #

## 簡介 ##

    HSRP是Cisco專有的FHRP協定，用於進行閘道備援，閘道備援是非常重要的技術，不管在企業或校園網路中，只要閘道出現問題，可能造成整個園區網路癱瘓


## Multicast Address ##

HSRP使用組播位置

    224.0.0.2

## 配置命令 ##

### IPv4 ###

```bash
standby 10 ip 192.168.1.254 #10為Group Number，兩端設定須相同
standby 10 priority 105 #優先權，優先權高的會成為Active，低的成為Standby，預設為100
standby 10 preempt #溝通過程中若是Priority發生變化，會依照最新的Priority決定設備將扮演Active or Standby 
standby 10 timers msec 200 msec 700 #調整Hello Interval和Hold Time，單位為毫秒，預設Hello Interval為3秒，Hold Time為10秒
standby 10 track f0/1 30 #追蹤對外介面，當介面出現問題時會自動將Priority降低，使其他正常的設備扮演Active
standby 10 authentication md5 key-string Cisco123 #MD5驗證
```

### IPv6 ###

```bash

```