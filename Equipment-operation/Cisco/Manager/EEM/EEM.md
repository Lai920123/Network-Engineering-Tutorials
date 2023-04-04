# Embedded Event Manager(EEM) 嵌入式事件管理器 #

## 常用作法 #

帶起人為關閉端口，防止人員誤關

```bash
enable 
configure terminal 
event manager applet INTERFACE-DOWN
    event syslog pattern "*.%LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to down.*"
    action 1.0 cli command "enable" #當端口被人為關閉時執行的命令
    action 1.1 cli command "configure terminal" 
    action 1.2 cli command "int e0/0" 
    action 1.3 cli command "no shutdown" 
    action 2.0 syslog msg "Interface Ethernet0/0 was brought up via EEM" #顯示系統日誌 
```

進入全域配置模式時顯示警告訊息

```bash
enable 
configure terminal
event manager applet ENTER-GLOBAL-MODE
    event cli pattern "conf.* t.*" enter
    action 1.0 syslog priority critical msg "Configuration mode was entered" 
    action 2.0 syslog priority information msg "All command are monitored and recorded Disconnect IMMEDIATELY if you are not an authorized user!"
```
