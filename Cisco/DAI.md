# DAI #
### 簡介 ###
    
    DAI為Dynamic ARP Inspection的縮寫，主要用來防止ARP Spoofing攻擊      

### 配置方法 ###
```powershell
ip dhcp snooping
ip dhcp snooping vlan 1 #snooping native vlan 
int f0/1 
ip dhcp snooping trust #設定信任的port
ip arp inspection vlan 1 #檢查Vlan1
int f0/1
ip arp inspection trust #設定信任的port
```