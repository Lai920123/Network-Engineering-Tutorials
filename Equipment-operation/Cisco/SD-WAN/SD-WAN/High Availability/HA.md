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