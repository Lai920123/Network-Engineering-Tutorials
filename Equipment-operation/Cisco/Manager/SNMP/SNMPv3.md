# SNMPv1配置方法 #

>SNMPv3提供了完整的驗證,加密功能，並且能夠向下相容

## 安全級別 ##

    SNMPv3安全級別分為以下三種
    1.noAuthNoPriv:提供使用者驗證但不加密
    2.authNoPriv:提供雜湊驗證完整性(md5,sha)但不加密
    3.authPriv:提供雜湊驗證完整性(md5,sha)並提供加密(DES,3DES,AES)


## 配置方法 ## 

>因其他兩種比較少用到，所以下方只提供authPriv的配置方法

```bash
snmp-server view VIEW1 iso included #
snmp-server view VIEW1 mib-2 included #建立SNMP View 
snmp-server group SNMPGROUP1 v3 priv read VIEW1 write VIEW1 access 1 #建立SNMPv3 group名為SNMPGROUP1，版本為SNMPv3，讀寫使用VIEW1，並只有ACL 1能夠存取
snmp-server user Admin SNMPGROUP1 v3 auth md5 Cisco123 priv des Cisco123 #建立SNMPv3 User名為Admin，驗證使用md5並使用des加密
snmp-server location Taoyaun #設備位置(選填)
snmp-server contact admin@gmail.com #聯絡人(選填)
snmp-server enable traps #設置通知類型，後面空白代表全部通知
```


