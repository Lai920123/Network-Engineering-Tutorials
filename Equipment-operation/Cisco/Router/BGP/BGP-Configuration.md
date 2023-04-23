# BGP Configuration #

## 基本配置 ##

>因BGP可調整的東西非常多，以下列出常見的幾種

```bash
router bgp 1 #配置BGP ASN 1，ASN的範圍為1-4294967295
    bgp router-id 1.1.1.1 #Router-ID為1.1.1.1
    neighbor 123.0.1.1 remote-as 1 #鄰居IP以及鄰居的ASN
    network 192.168.1.0 mask 255.255.255.0 #宣告網段
```

>若是兩點之間有其他網路設備使兩點無法建立鄰居，可使用Multihop指令將兩個Router連起來

```bash
neighbor 123.0.1.1 ebgp-multihop 2 #2為最大跳躍數，就是兩台Router中間相隔的Hop數目，依照實際情況更改
```

## 優化 ##

### 使用Loopback做為鄰居IP ###

>在IGP中，可使用Loopback做為鄰居IP，因Loopback為邏輯端口，會永遠開啟，且IGP中通常會配置其他IGP(RIP,OSPF,EIGRP等...)，可防止因為介面關閉導致無法路由，此方法較少使用於EBGP，因為eBGP並不會使用IGP將兩個AS連起來

```bash
router bgp 1
    neighbor 8.8.8.8 remote-as 1 #IP要跟改為Loopback位置
    neighbor 8.8.8.8 update-source loopback0
```

### 密碼驗證 ###

>在兩端都輸入密碼，即可透過密碼認證

```bash
router bgp 1
    neighbor 8.8.8.8 password Cisco123
```

### Peer Group ###

>若有多個Neighbor要做相同設定，可使用Peer Group來簡化

```bash
router bgp 1
    neighbor group1 peer-group #配置peer group名稱為group1
    neighbor group1 remote-as 1 #設定ASN
    neighbor group1 password Cisco123 #設定密碼
    neighbor 1.1.1.1 peer-group group1 #套用peer group
    neighbor 2.2.2.2 peer-group group1 #套用peer group 
    neighbor 3.3.3.3 peer-group group1 #套用peer group
```

## 參考文章 ##

[https://www.jannet.hk/border-gateway-protocol-bgp-zh-hant/](https://www.jannet.hk/border-gateway-protocol-bgp-zh-hant/)