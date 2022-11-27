# DHCP Snooping #

## 簡介 ##

    DHCP Snooping用於封鎖接入交換機的非法DHCP Server，開啟DHCP Snooping後，所有客戶端只能從管理員指定的DHCP Server獲取IP Address，DHCP Snooping將交換機的Port分為Trust以及Untrust，交換機只會轉發Trust的DHCP封包，並丟棄Untrust的封包


## 配置方法 ##

```bash
ip dhcp snooping #全域開啟DHCP Snooping 
ip dhcp snooping vlan 1 #套用至VLAN 1
no ip dhcp snooping information option #下方有解釋
int f0/0
    ip dhcp snooping trust #配置信任介面
int f0/1
    ip dhcp snooping limit rate 10 #在非信任介面配置速率限制
```


## Relay Agent Information Option ##

    DHCP的Option 82為Relay Agent Information Option，當Client傳送Discovery至Server時，若需要經過Relay Agent，

## 檢查命令 ##

```bash
show ip dhcp snooping #查看信任介面與非信任介面
show ip dhcp snooping binding #查看binding內容
```