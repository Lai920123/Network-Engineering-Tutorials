# Hot Standby Redundancy Protocl 熱備援冗餘協定 #

## 簡介 ##

    HSRP是Cisco專有的FHRP協定，用於進行閘道備援，閘道備援是非常重要的技術，不管在企業或校園網路中，只要閘道出現問題，可
    能造成整個園區網路癱瘓

## 配置命令 ##

### IPv4 ###

```bash
standby 10 ip 192.168.1.254 #10為group number，兩端設定須相同
standby 10 priority 105 #優先權，優先權高的會成為active，低的成為standby，預設為100
standby 10 preempt #溝通過程中若是priority發生變化，會依照最新的priority決定設備將扮演active or standby 
standby 10 timers msec 200 msec 700 #
standby 10 track f0/1 30 #追蹤上行介面
```