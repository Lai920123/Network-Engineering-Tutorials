# IPv6 ACL #


## 使用範例 ##

```bash
ipv6 access-list ACL1
    permit ipv6 host 2001:DB8:ACAA:1::1 host 2001:DB8:ACAD:2::1
    permit ipv6 2001:DB8:ACAB:1::/24 host 2001:DB8:ACAD:3::1
    permit ipv6 2001:DB8:ACAC:1::1 host 2001:DB8:ACAD:4::1
    deny ipv6 any any
interface GigabitEthernet 0/0/0
    ipv6 traffic-filter ACL1 in
```

## 查詢命令 ##

```bash
show ipv6 access-list 
```