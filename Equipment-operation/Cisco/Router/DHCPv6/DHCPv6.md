# DHCPv6 #

## Stateless address auto-configuration(SLAAC) ##

SLAAC可用來使IPv6節點能夠自動產生GUA，提供Prefix, Default Gateway，但不提供DNS以及域名資訊

```bash
#配置介面IP
int e0/0
    ipv6 address 2001:db8:1:1::1/64 
    ipv6 address FE80:1:1:1::1 link-local
#啟用ipv6單播繞送
ipv6 unicast-routing 
```

## Stateless DHCPv6 ## 

路由器提供SLAAC產生的GUA，Stateless DHCPv6 Server提供DNS Server以及域名資訊

```bash

```

## Stateful DHCPv6 ## 

路由器提供Default Gateway，DHCPv6 Server提供IPv6位置和其餘參數 

```bash
ipv6 dhcp pool POOL1
    address prefix 2001:db8:1:1:1::/64
    dns-server 2001:8:8:8::8
    domain-name cisco.com 
int e0/0
    ipv6 nd prefix 2001:db8:a01:1::/64 no-advertise
```




