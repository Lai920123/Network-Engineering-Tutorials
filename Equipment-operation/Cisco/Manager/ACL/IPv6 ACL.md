# IPv6 ACL #


## 使用範例 ##

```bash
ipv6 access-list ACL1
    permit ipv6 host 2001:DB8:ACAA:1::1 host 2001:DB8:ACAD:2::1
    permit ipv6 2001:DB8:ACAB:1::/24 host 2001:DB8:ACAD:3::1
    deny ipv6 any any
interface GigabitEthernet 0/0/0
    ipv6 traffic-filter ACL1 in
```

## 查詢命令 ##

```bash
show ipv6 access-list 
```

## Reference ##

https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/ipv6_basic/configuration/xe-3s/asr903/ip6b-xe-3s-asr903-book/Configuring_an_IPv6_Access_Control_List_on_the_Cisco_ASR_903_Router.pdf