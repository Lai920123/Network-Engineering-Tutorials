# Radius #

## Configuration ## 

在啟用AAA前需要再本地先建立一對使用者帳密

```bash
username user1 privilege 15 secret P@ssw0rd
```

為確保不會因設定錯誤而被鎖在設備外，可以先進行存檔，以免再配置錯誤時無法回復到先前的設定檔

```bash
write
```

啟用AAA

```bash
aaa new-model 
```

指定外部Radius伺服器

```bash
radius server DC1 #DC1是可以自己取的名稱
    address ipv4 192.168.1.100 auth-port 1812 acct-port 1813 
    key P@ssw0rd
```

```bash
aaa authentication login default group radius local #exec訪問時先使用radius再使用local進行登入
aaa authentication enable default group radius enable #enable訪問時先使用radius再使用local進行登入

```