# 初始化 #

## 拓樸 ##

![](Image/SD-WAN.png)

## vManage ##

```bash
system
    host-name vManage
    system-ip 1.1.1.20
    site-id 1
    organization-name cisco.com
    vbond 192.168.1.101

vpn 0
    interface eth0
    ip address 192.168.10.200/24
    no shutdown

vpn 512
    interface eth1
    ip address 192.168.1.100/24
    no shutdown
```

## vBond ## 

```bash
system
    host-name vBond
    system-ip 1.1.1.10
    site-id 1
    organization-name cisco.com
    vbond 192.168.1.101 local vbond-only

vpn 0
    interface ge0/0
    ip address 192.168.1.101/24
    no tunnel-interface
    no shutdown
```

## vSmart ##

```bash
system
    host-name vSmart
    system-ip 1.1.1.30
    site-id 1
    organization-name cisco.com
    vbond 192.168.10.101
    
vpn 0
    interface eth0
    ip address 192.168.10.102/24
    no tunnel-interface
    no shutdown
```

## vEdge ##

```bash
system
    host-name vEdge-1
    system-ip 1.1.1.40
    site-id 100
    organization-name cisco.com
    vbond 192.168.10.101

vpn 0
    interface ge0/0
    ip address 192.168.10.103/24
    no tunnel-interface
    no shutdown
```
