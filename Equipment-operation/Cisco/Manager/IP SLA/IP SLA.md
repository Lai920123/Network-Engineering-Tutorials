# IP Service Level Agreements 服務級別協議 #

## 簡介 ##

    可透過多種方式持續測試網路是否斷線，並將統計結果儲存

## 測試方法 ##

## DHCP ##

```bash

```

## DNS ##

```bash

```

## Ethernet ##

```bash

```

## FTP ##

```bash

```

## HTTP ##

```bash

```

## ICMP Echo ## 

```bash
ip sla 1
    icmp-echo 8.8.8.8 source-ip 123.0.1.1 #測試方式為icmp-echo，目的地為8.8.8.8，來源為123.0.1.1
    request-data-size 300
    frequency 5 #執行頻率(每秒)
ip sla schedule 1 life forever start-time now #設定排程立即啟用並永久持續
track 1 ip sla 1 reachability #配置track物件，對應到ip sla 1
ip route 0.0.0.0 0.0.0.0 123.0.1.2 track 1 #配置預設路由，狀態為真時成立預設路由

show track
show ip sla statistics #查看統計數據
```

## ICMP Jitter ##

```bash

```

## MPLS ##

```bash

```

## Path Echo ## 

```bash

```

## Path Jitter ##

```bash

```

## TCP Connect ##

```bash

```

## UDP Echo ##

```bash

```

## UDP Jitter ##

```bash

```

## VoIP ##

```bash

```
