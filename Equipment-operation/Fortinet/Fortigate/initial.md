# 初始化 #

查看IP Address 

```bash
diagnose ip address list 
```

配置IP

```bash
config system interface 
    edit port1 端口編號
        set vdom root 
        set mode dhcp #自動配置
        set allowaccess ping ssh http https fgfm #允許哪些協定
        set type physical #接口類型
        set snmp-index 1 #SNMP自動配置
    next
    edit port2 
        set vdom root 
        set ip 192.168.1.100 255.255.255.0 #手動配置
        set allowaccess ping ssh http https fgfm #允許哪些協定
        set type physical #接口類型
        set role wan #可選，設置為WAN介面
        set snmp-index 2 #SNMP自動配置
```

配置好後就可以使用GUI輸入http://ipaddress/進入管理頁面