# MPLS #

## LDP ##

在建立LDP鄰居時要注意，LDP使用的Router-ID需要雙方都可達，否則無法建立鄰居，預設LDP會使用路由器的Router-ID，也可手動指定

```bash
mpls ldp router-id lo0 force #加上Force才會立即改變
```

## Reference ##

Implicit Explicit https://blog.ipspace.net/kb/tag/MPLS/Implicit_Explicit_NULL/

MPLS Janho https://www.jannet.hk/multi-protocol-label-switching-mpls-zh-hant/#Implicit_null_Explicit_null