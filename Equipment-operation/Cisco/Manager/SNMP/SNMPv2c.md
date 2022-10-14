# SNMPv2c配置方法 #

>SNMPv2c與SNMPv1相比，增加了基本的認證與加密功能，不過SNMPv2c與SNMPv1不相容

```bash
access-list 1 permit 10.1.1.0 0.0.0.255 #可適當的配置ACL
snmp-server community Cisco123 ro 1 #community後接著的為SNMP的密碼，ro代表唯獨(Read Only),rw代表可讀可寫，1為允許ACL 1進行存取
snmp-server location Taoyaun #設備位置(選填)
snmp-server contact admin@gmail.com #聯絡人(選填)
snmp-server host 10.1.1.1 version 2c Cisco123 #NMS IP為10.1.1.1，版本為SNMPv2c，密碼為Cisco123
snmp-server enable traps #設置通知類型，後面空白代表全部通知
```