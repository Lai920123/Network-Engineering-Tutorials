# LLDP #

LLDP是一種Layer2協議，通過載本地傳輸LLDPPDU通告自身狀態，讓其他裝置可以取得設備資訊，可以運作於市面上大多數的網路設備，當拓樸中擁有不同廠牌的網路設備時，使用LLDP為較好的選擇

## 運作方式
    將本地設備的訊息組成TLV(Type/Length/Value)封裝於LLDPPDU中，發送給直連的設備，同時與將接收的LLDPPDU以MID形式保存，通過互相接收與傳送LLDPPDU，讓設備能夠取得鄰居設備的信息，以方便管理

## TLV Type ##

| TLV Type | TLV Name | 必要性 |
|   ---    | --- | --- |
|0         |End of LLDPPDU 標示LLDPPDU結束|必要|
|1         |Chassis ID 發送端MAC位址|必要|
|2         |Port ID 端口ID，例如g0/1|必要|
|3         |Time To Live 存活時間|必要|
|4         |Port Description 端口描述|可選|
|5         |System Name 系統名稱|可選|
|6         |System Description 系統描述|可選|
|7         |System Capabilities 系統啟用功能|可選|
|8         |Management Address 管理位址|可選|
|9~126     |Reserved for future standardization 為未來標準保留|-|
|127       |Organizationally Specific TLVS 組織特定的TLV|可選|

## 預設配置 ##

    LLDP global state          - Enable 
    LLDP holdtime              - 120 Seconds
    LLDP timer                 - 30 Seconds
    LLDP reinitialzation delay - 2 Seconds
    LLDP tlv-select            - Enabled to send and receive all TLVS
    LLDP interface state       - Enabled 
    LLDP recive                - Enabled
    LLDP transmit              - Enabled

## Command ##

### 全域啟動或關閉LLDP
```bash
#啟用LLDP
lldp run 
#關閉LLDP
no lldp run
```

### 調整LLDP更新，停留，初始化時間 ###
```bash
lldp holdtime <seconds> #指定接收LLDPPDU後停留的時間，範圍在0~65535
lldp reinit <seconds> #指定重新初始化時間，範圍在2~5秒
lldp timer <seconds> #指定傳送LLDP更新間隔時間，範圍在5~65534
lldp tlv-select #選擇傳送的TLV Type
```
### 關閉或啟用LLDP在特定端口 ###
```bash
lldp run #開啟LLDP
#g0/0關閉LLDP，g0/1開啟LLDP
int g0/0
    no lldp transmit 
    no lldp receive 
int g0/1
    lldp transmit
    lldp receive
```

### 查看LLDP信息 ###
```bash
#查看鄰居
show lldp neighbors detail
```