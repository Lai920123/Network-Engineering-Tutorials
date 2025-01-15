# vManager #

## 預配 ##

```bash
conf t
system
    host-name vManager #主機名稱
    system-ip 100.1.1.1 #用於標示設備，不須可達
    site-id 100 #類似BGP ASN，用於防環 
    organization-name D107A-CCIE #組織名稱
    vbond 123.1.1.3 #指定vBond位置
    vpn 0 #傳輸介面，所有連接WAN的都可由VPN0傳輸
        dns 8.8.8.8 primary 
        int eth0
            ip address 123.1.1.1/24
            tunnel-interface 
                allow-service all #所有服務都允許通過tunnel介面
                exit
            no shutdown 
        ip route 0.0.0.0/0 123.1.1.254 
        exit
    vpn 512 #管理介面
        int eth1 
            ip address 192.168.107.208/24
            no shutdown 
    commit 
```