# GRE over IPSec Remote Access #

```bash
aaa new-model 
aaa authentication login abc1 local 
aaa authorization network abc2 local 
username admin password Cisco123 
```

```bash
crypto isakmp policy 10
    encryption aes
    hash md5 
    authetication pre-share
    group 2
```

```bash
ip local pool REMOTE_ACCESS_VPN 192.168.1.1 192.168.1.50
```

```bash
crypto isakmp client configuration group cisco 
    key cisco 123
    pool REMOTE_ACCESS_VPN
```

```bash
crypto ipsec transform-set TRANS esp-aes esp-sha-hmac 
```

```bash
crypto dynamic-map 
```