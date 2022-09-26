# EtherChannel

!!!設定EtherChannel時最好先將一台Switch的port shudown掉,否則設定時可能會造成迴圈

## L2 EtherChannel ##

### Static ###

建立channel-group 

```bash
channel-group <1-255> mode on
```

### LACP(Link Aggregation Control Protocol) 鏈路聚合控制協定 ###

建立channel-group 

```bash
#主動
channel-group <1-255> mode active 
#被動
channel-group <1-255> mode passive
```

LACP還具有Hot Standby的功能,最多可以有8+8的線路加入port-channel 選取Port Priority最小的作為Active,如果都相同,就取Port ID 更改port-priority 

```bash
lacp port-priority <0-65535>
```

### PAgP(Port Aggregation Protocol) 端口聚合協定 ###

Cisco專有 

```bash
#主動
channel-group <1-255> mode auto 
#被動
channel-group <1-255> mode desirable
```

### Load Balance EtherChannel ###

將多條線綁成一條線後，要如何知道流量經由哪一條實體的線路出去，單條線路負載過大或過小都不好，要做到load balance，有幾種方式

```bash
port-channel load-balance ? 
dst-ip     用目的地ip的最後3bit來計算出PortID,例如192.168.1.10,最後3bit為010也就是2,那PortID為2 
dst-mac 
src-ip     同dst-ip,只是IP位置改為來源 
src-mac 
src-dst-ip 找出目的地和來源IP的最後3bit在進行XOR運算,例如來源為192.168.1.10,目的地為192.168.1.15 取最後3bit,來源010,目的111,進行XOR後為101,所以portID就是5 
src-dst-mac
```

## L3 EtherChannel ##

### 