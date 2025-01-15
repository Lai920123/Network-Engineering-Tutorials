# HQ-vEdge1 #

## 預配 ##

```bash
conf t
system
    host-name vEdge11
    system-ip 10.1.255.11 
    site-id 1 
    organization-name D107A-CCIE
    vbond 123.1.1.3
    vpn 0 
        int ge0/0
            ip address 10.100.102.2/24
            no shutdown 
            tunnel-interface
                encapsulation ipsec 
                color  mpls 
                allow-service all
        int ge0/1
            ip address 100.100.102.2/24
            no shutdown 
            tunnel-interface
                encapsulation ipsec 
                color biz-internet
                allow-service all  
```
