# NTP

## 簡介 ## 
NTP，用於通過分佈式的NTP server與Client端進行時間同步，使網路中所有設備時間保持一致，讓設備能夠提供基於統一時間的應用，使用UDP 123 Port，所有NTP溝通都使用UTC

[UTC](/Protocol/UTC.md)

## Mode ##

    在Cisco的設備中可配置三種模式

### Server Mode ###

    在此模式中，Router從NTP Source同步時間，除非手動配置NTP Source，否則路由器會使用自己的時間作為NTP Source，配置NTP Source後，Router會通告此時間在網路中，在Server Mode中，Router只會發送NTP更新，不接受從其他NTP Server的任何更新

### NTP Server/Client Mode ###

    在此模式中，Router作為NTP Client從NTP Server接收更新，並且作為NTP Server將收到的更新訊息通告出去，此模式下，Router不使用自己的NTP Source，此功能允許我們在NTP Server上使用單個集中式的NTP Source

### Client Mode ###

    在此模式中，Router僅從NTP Server接收更新訊息，並同步自己的時間，不會通告收到的更新

## 配置 ##

### Topology ###
![](NTP/NTP.png)

    注意上方拓樸圖的NTP Mode

```bash
#R1[NTP Server/Client Mode]
enable 
configure terminal 
    clock timezone Taipei 8 #設定時區
    exit
clock set 08:33:00 19 Aug 2022 #設定時間
clock update-calendar #同步到硬體時鐘
configure terminal
    ntp master [stratum level] #設定層級，層級為距離權威時間源的NTP跳數，層級1為源頭像是無線電或原子鐘，層級2從層級1接收時間，以此類推，範圍為1~15，如果未指定，預設值為8
    ntp source e0/0 #NTP源，可設定外部NTP Server，如果要使用Router作為NTP源，配置Router的任意介面或IP即可


#R2[Server Mode]
enable 
configure terminal 
    clock timezone Taipei 8
    ntp server 192.168.1.2

#R3[Client Mode]
enable 
configure terminal 
    clock timezone Taipei 8
    ntp server 192.168.1.2

#R4[Client Mode]
enable 
configure terminal 
    clock timezone Taipei 8
    ntp server 192.168.1.2
```