# DHCP #

在Aruba SW配置DHCP的方法

## 配置 ##

```bash
dhcp-server vrf default #使用全域VRF也就是default 
    pool wlan1 #pool名稱為pool1
        range 192.168.1.100 192.168.1.199 prefix-len 24 
        dns-server 8.8.8.8 168.95.1.1 
        default-router 192.168.1.1 
        option 43 ip 192.168.100.100 #使用option 43讓AP能夠找到Controller 
    pool wlan2
        range 192.168.2.100 192.168.2.199 prefix-len 24
        dns-server 168.95.1.1
        default-router 192.168.2.1 
        option 43 ip 192.168.100.100
    authoritative 
    enable #啟用dhcp server
```