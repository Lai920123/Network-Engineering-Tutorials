# Fortigate LAB #

## 配置 ##

```bash
[Internet]

[MPLS]

[Branch1-FW1]
config system global 
    set hostname Branch1-FW1
    set admin-console-timeout 0 #console不超時
config system interface 
    edit port4 
        set mode static
        set ip 192.168.1.200/24 
        set allowaccess ping https ssh http fgfm

[Branch1]

[Branch2-FW1]
config system global 
    set hostname Branch2-FW1
    set admin-console-timeout 0 #console不超時
config system interface 
    edit port4 
        set mode static
        set ip 192.168.1.201/24 
        set allowaccess ping https ssh http fgfm
[Branch2]

[Branch3-FW1]
config system global 
    set hostname Branch1-FW1
    set admin-console-timeout 0 #console不超時
config system interface 
    edit port4 
        set mode static
        set ip 192.168.1.202/24 
        set allowaccess ping https ssh http fgfm
[Branch3]

[HQ-Core1]

[HQ-Core2]

[HQ-FW1]
config system global 
    set hostname HQ-FW1
    set admin-console-timeout 0 #console不超時
config system interface 
    edit port3
        set mode static
        set ip 192.168.1.203/24 
        set allowaccess ping https ssh http fgfm
[HQ-FW2]
config system global 
    set hostname HQ-FW2
    set admin-console-timeout 0 #console不超時
config system interface 
    edit port3
        set mode static
        set ip 192.168.1.204/24 
        set allowaccess ping https ssh http fgfm
[SRV-SW1]

[FAZ]

[FMG]

[DSW1]

[DSW2]

```