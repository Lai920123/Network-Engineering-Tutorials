# 初始化 #

## Graphical User Interface ##

打開browser輸入https://<ip address>進入管理頁面並登入，預設帳號為admin，密碼為空

![](Image/1.png)

在Dashboard找到Host Name，並點選Change 

![](Image/2.png)

輸入要更改的主機名稱，輸入之後點選OK即可

![](Image/3.png)

## Command Line ##

配置主機名稱

```bash
config system global 
    set hostname FW1
```

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
        set allowaccess ping ssh http https fgfm #允許哪些協定，需開啟http才可進入web管理介面
        set type physical #接口類型
        set snmp-index 1 #SNMP自動配置
    next
    edit port2 
        set vdom root 
        set ip 192.168.1.100 255.255.255.0 #手動配置
        set allowaccess ping ssh http https fgfm #允許哪些協定，需先開啟http才可進入web管理介面
        set type physical #接口類型
        set role wan #可選，設置為WAN介面
        set snmp-index 2 #SNMP自動配置
    end 
```

配置default gateway 

```bash
config router static 
    edit 1 #1為序號，可隨便取
    set device port1
    set gateway 192.168.1.1 
    end
```
配置好後就可以使用GUI輸入http://ipaddress/進入管理頁面進行管理
