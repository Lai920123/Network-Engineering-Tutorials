# SPAN #

## Local SPAN #

將流量從交換機的一個或多個介面鏡像到同一交換機的一個或多個介面

```bash
monitor session 1 source interface e0/0
monitor session 1 destination interface e0/1
```

## Remote SPAN #

```bash
[SW1]
vlan 100 
    remote-span 
int e0/0
    switchport encapsulation dot1q
    switchport mode trunk 
monitor session 1 source int e0/1
monitor session 1 destination remote vlan 300 
[SW2]
vlan 100
    remote-span 
int e0/0
    switchport encapsulation dot1q
    switchport mode trunk
monitor session 1 source remote vlan 300
monitor session 1 destination int et0/1 
```