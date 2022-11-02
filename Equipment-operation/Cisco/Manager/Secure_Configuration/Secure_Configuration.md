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

## 配置Log ##

```bash

```


## 交換機防護 ##

```bash

```

## 路由器防護 ##

```bash

```