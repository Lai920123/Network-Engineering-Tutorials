# HQ-vEdge2 #

## 預配 ##

```bash
conf t
system
    host-name DC1-vEdge2
    system-ip 10.1.255.11 
    site-id 1 
    organization-name D107A-CCIE
    vbond 123.1.1.3
    vpn 0 
        int ge0/0
            ip address 100.100.100.2/24
            no shutdown 
            tunnel-interface
                allow-service all 
```