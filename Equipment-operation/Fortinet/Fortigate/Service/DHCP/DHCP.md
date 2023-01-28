# DHCP #

## Topology ##

![](Image/1.png)

## Graphical User Interface ##

打開browser輸入https://<ip address>進入管理頁面並登入，預設帳號為admin，密碼為空

![](Image/2.png)

左側列表選擇Network -> Interface 

![](Image/3.png)

選擇Port2，按下Edit 

![](Image/4.png)

填選以下欄位，填完選擇OK即可

![](Image/5.png)

將PC改為自動取得，使用ipconfig查看是否成功取得IP

![](Image/6.png)

## Command Line ##

初始化

```bash
config system global 
    set hostname FW1
config system interface 
    edit port1 
    set mode dhcp 
    set allowaccess ping http https 
end
```

配置DHCP

```bash

```