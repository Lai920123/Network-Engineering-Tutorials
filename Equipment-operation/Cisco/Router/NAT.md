# NAT #

## 兩個對外接口NAT ##

假設e0/0為1G，e0/1為1.54M，平時對外走e0/0，若是e0/0損壞，才走e0/1做備援

![](NAT/topology1.png)

```bash
#R1
enable 
configure terminal
hostname R1
int e0/0
    ip address 123.0.1.1 255.255.255.252
    no shutdown 
int e0/1
    ip address 123.0.1.5 255.255.255.252
    no shutdown 
int e0/2
    ip address 192.168.1.1 255.255.255.0
    no shutdown 

int range e0/0-1
    ip nat outside
int e0/2
    ip nat inside 

access-list 1 permit 192.168.1.0 0.0.0.255

route-map e0/0 permit 1
    match ip address 1
    match interface e0/0    
route-map e0/1 permit 1
    match ip address 1
    match interface e0/1

ip nat inside source route-map e0/0 interface e0/0 overload
ip nat inside source route-map e0/1 interface e0/1 overload

ip route 0.0.0.0 0.0.0.0 123.0.1.2 5
ip route 0.0.0.0 0.0.0.0 123.0.1.6 10

#R2
enable 
configure terminal
hostname R2
int e0/0
    ip address 123.0.1.2 255.255.255.252
    no shutdown 
int e0/1
    ip address 123.0.1.5 255.255.255.252
    no shutdown 
int loopback 0 
    ip address 8.8.8.8 255.255.255.255
```
