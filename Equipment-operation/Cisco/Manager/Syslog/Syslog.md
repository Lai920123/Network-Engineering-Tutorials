# Syslog

## Log Level ##

|Level Keyword|Level|Description|
|     ---     | --- |    ---    |
|emergencies  |0    |System unstable
|alerts       |1    |Immediate action needed
|critical     |2    |Critical conditions
|errors       |3    |Error conditions 
|warnings     |4    |Warning conditions
|notifications|5    |Normal but significant conditions
|informational|6    |Informational messagges only 
|debugging    |7    |Debigging messages

## 配置Syslog Client

```bash
logging buffered 32768 #本地日誌緩存
service sequence-numbers #啟動序號服務
logging 10.1.1.100 #指定Syslog Server
logging trap informational #日誌等級
clock timezone Taipei 8 #設定本地時區
service timestamps log datetime msec localtime show-timezone year #設定日誌格式
```