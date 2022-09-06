# VOIP

![Untitled](VOIP%20d09869a36cb7411caa6bd3e5aae4eae8/Untitled.png)

## R1

```bash
enable
configure terminal
hostname R1
int f0/0
    no shutdown
int f0/0.10
    encapsulation dot1q 10
    ip address 10.1.10.1 255.255.255.0
int f0/0.20
    encapsulation dot1Q 20
    ip address 10.1.20.1 255.255.255.0
ip dhcp pool VOIP #建立DHCP Pool提供IP Phone自動取得IP
    network 10.1.20.0 255.255.255.0
    default-router 10.1.20.1
    option 150 ip 10.1.20.1 
```

## SW1

```bash
enable
configure terminal 
hostname SW1
vlan 10
    name PC 
vlan 20 #建立一個VLAN給IP Phone使用
    name VOICE 
int range g1/0/1-2
    switchport mode access
    switchport voice vlan 20
    switchport access vlan 10
    spanning-tree portfast
    exit
int g1/0/24
    switchport mode trunk
```

### 檢查

```powershell
show power inline #查看PoE供電狀態
```