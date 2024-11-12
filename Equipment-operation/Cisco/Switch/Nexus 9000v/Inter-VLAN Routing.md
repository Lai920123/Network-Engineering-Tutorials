# Inter-VLAN Routing #

## 開啟功能 ##

```bash
feature interface-vlan 
```

## 配置int vlan ip ##

```bash
int vlan 10
    ip address 10.1.1.1 255.255.255.0
    no shutdown 
```