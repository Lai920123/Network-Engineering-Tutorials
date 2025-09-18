# SD-WAN組件HA #

## vManager ##

vManager在建立Cluster時需要先達到以下要求

- 需使用VPN 0且非建立Tunnel的介面來建立Cluster
- 另外新增一組group為netadmin的帳號

**檢查建立完Cluster後服務是否正確啟用**

```bash
request nms cluster diagnostics
request nms all status 
```

## vSmart ##

## vBond ##

vbond如果是用DNS進行配置的而不是直接指定IPv4 Address，直接修改DNS Record即可

```bash
#假設原有的vbond是192.168.1.100，在後面新增一台192.168.1.101
ip host vbond.example.com 192.168.1.100 192.168.1.101 
```