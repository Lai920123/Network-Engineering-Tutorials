# Initial #

當第一次拿到設備時會需要初始化來進到管理介面，依照一下步驟設定好初始化

## 連接Console後以預設密碼登入 ##

```bash
#預設帳號為admin/密碼為空
```

## 配置主機名稱/介面IP/預設閘道/DNS ##

```bash
#進入全域配置模式配置主機名稱
config system global
    set hostname FW1
#配置介面IP
config system interface 
    edit port1
        set mode static #設定為靜態，也可更改為DHCP
        set allowaccess http https ssh ping 
        set ip 192.168.1.200/24
        set role lan #介面角色
        set alias lan #描述
    next 
    edit port2
        set mode dhcp
        set ip 192.168.2.200/24 
        set allowaccess ping 
        set role wan 
        set alias wan 
    next 
    edit loopback0
        set mode static
        set ip 1.1.1.1/24 
        set type loopback 
        
#配置預設閘道
config router static #配置靜態路由
    edit 1 #sequence number
        set device port1 #分配給port1
        set gateway 192.168.1.1 
config system dns
    set primary 8.8.8.8
    set secondary 168.95.1.1 
[Check]
show system global #查看主機名稱是否配置正確
show system interface #查看介面IP是否配置正確
show router static #查看靜態路由是否配置正確
end #fortigate cli輸入end後會自動保存
```
