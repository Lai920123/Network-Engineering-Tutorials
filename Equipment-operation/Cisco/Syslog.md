# Syslog

## 配置Syslog Client

```bash
loggin buffered 32768 #本地日誌緩存
service sequence-numbers #啟動序號服務
loggin 10.1.1.100 #指定Syslog Server
loggin trap informational #日誌等級
clock timezone Taipei 8 #設定本地時區
service timestamps log datetime msec localtime show-timezone year #設定日誌格式
```