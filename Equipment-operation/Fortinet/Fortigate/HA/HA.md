# Hight Availability 高可用性 #

>高可用性是用於盡可能縮短因日常維護或突發系統崩潰導致的停機，

## 支援HA方式 ##

- FortiGate Cluster Protocol(FGCP Fortigate專有) 
- Virtual Router Redundancy Protocol(VRRP 公有協定)
- TCP Session synchronization

## FGCP ##

Active-Active 

Active-Passive 

## Active-Active配置 ##

```bash
[FW1]
config system ha 
    set group-name HA1
    set mode a-a #active-active
    set password P@ssw0rd #驗證密碼
    set priority 128 #預設值為128 
    set hbdev port4 0 #heartbeat介面
    set session-pickup enable 
    set config-sync enable 
    set monitor port2 port3 #監控介面
[FW2]
config system ha 
    set group-name HA1
    set mode a-a 
    set password P@ssw0rd #驗證密碼
    set priority 128 #預設值為128
    set hbdev port4 0 #heartbeat介面
    set session-pickup enable 
    set monitor port2 port3 #監控介面
[Check]
show system ha status #查看HA狀態
```

## Active-Passive配置 ##

## Reference ##

https://support.fortinet.com.cn/uploadfile/2012/0822/20120822103354901.pdf