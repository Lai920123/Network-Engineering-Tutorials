# Gateway Load Balancing Protocol 閘道負載平衡協定 #

## 簡介 ##

    GLBP與HSRP相同是Cisco專有的FHRP協定，用於進行閘道備援，閘道備援是非常重要的技術，不管在企業或校園網路中，只要閘道出現問題，可能造成整個園區網路癱瘓，不過GLBP與HSRP不同，多了Load Balancing的功能，HSRP與VRRP只能夠做到分流，無法做到完整的Load Balancing

## 配置方法 ##

### IPv4 ###

### 基礎配置 ###

```bash
glbp 10 ip 192.168.1.254
```
### 優化 ###

```bash
glbp 10 priority 110 ##優先權，優先權高的會成為Active，低的成為Standby，預設為100
glbp 10 preempt #溝通過程中若是Priority發生變化，會依照最新的Priority決定設備將扮演Active or Standby 
glbp 10 timers msec 200 msec 700 #調整Hello interval以及Dead interval，預設Hello interval為3秒，Dead interval為10秒
glbp 10 weighting 110 lower 99 upper 105 #
glbp 10 weighting track 1 decrement 15
```

### 防止對外端口Down ### 

```bash
ip sla 1
    icmp-echo 8.8.8.8 source-ip 192.168.1.1 #ping測試8.8.8.8，來源ip為192.168.1.1
    frequency 5 #測試頻率為2秒
ip sla schedule 1 life forever start-time now #配置ip sla排程
track 1 ip sla 1 reachability #track 1 對應至ip sla 1
int f0/0 #進入設置GLBP的介面
    glbp 10 track 1 decrement 15 #套用track 1，若是Track 1 Down則Priority減15 ，追蹤對外介面，當介面出現問題時會自動將Priority降低，使其他正常的設備扮演Active
```

### 使用md5驗證 ###

```bash
#以下兩種方式擇一即可
#使用key-string
int f0/0 #進入要配置的介面
    glbp 10 authentication md5 key-string Cisco123
#使用key-chain
key chain glbp1
    key 1
    key-string Cisco123
int f0/0 #進入要配置的介面
    glbp 10 authentication md5 key-chain glbp1
```

### IPv6 ###

```bash

```