# Secure Configuration #

>當一拿到網路設備時，所有設定都是預設值，但是只要是預設值，幾乎都是不安全的，以下會示範拿到設備時該如何配置，強化設備安全

## 物理訪問防護 ##

可藉由設定console密碼來防止物理連入

```bash
username admin secret P@ssw0rd
line console 0 
    login local #使用本地使用者登入
    exec-timeout 3 #也可設定超時，線路多久沒動時會斷開連接，單位為分鐘，預設是5分鐘
```

## 特權模式防護 ##

進入特權模式時要輸入的密碼

```bash
enable secret P@ssw0rd #建立使用secret而不是password，因password是以明文紀錄於設定檔中，且Cisco的加密演算法已被破解，參考此網頁https://packetlife.net/toolbox/type7/
```

## 遠端連線防護 ##

若是要進行遠端連線，請務必使用ssh進行連線，不要使用telnet

```bash
ip domain-name test.com #設定網域名稱
crypto key generate rsa modulus 2048 #生成金鑰
username admin secret P@ssw0rd #建立本地帳戶
line vty 0 4
    transport input ssh #使用ssh
    login local #使用本地使用者登入
    exec-timeout 3 #也可設定超時，線路多久沒動時會斷開連接，單位為分鐘，預設是5分鐘
```

## 配置Syslog ##

>將Log發送到Log Server，在發生事件時，能夠通過Log進行故障排除，非常重要，在配置Syslog時，要注意時間以及時區，這樣在傳輸時才會以正確的時間記錄

```bash
clock set 12:00:00 1 Oct 2022 #設定目前時間
clock timezone Taipei 8 #設定時區
```

```bash
service timestamps log datatime msec localtime show-timezone year #日誌格式
service sequence-numbers #啟用序號服務
logging buffered 32768 #本地日誌緩存大小
logging 192.168.100.100 #指定傳送的Log Server
```


## 交換機防護 ##

>交換機可對連入介面的主機進行MAC位置的綁定，阻止外來交換機或者主機接入至交換機，並且設定反制行為，反制行為有三種，Protect,Restrict和Shutdown，Protect會丟棄非法封包，不過不進行警告，Restrict丟棄不合法封包並發送Log和SNMP Trap，Shutdown會關閉port，並發送Log和SNMP Trap

### Port Security ###

```bash
int f0/1 #進入要防護的介面
    switchport mode access 
    switchport port-security maximum 1 #最大MAC數量為1
    switchport port-security mac-address xxxx.xxxx.xxxx #xxxx.xxxx.xxxx可靜態指定允許接入主機的MAC位置，也可使用sticky進行動態黏接
    switchport port-security violation shutdown #違規行為為shutdown
    switchport port-security #啟動port-security 
```

## 路由器防護 ##

```bash

```