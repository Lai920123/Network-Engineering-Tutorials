# 設備管理 #

## 變更設備名稱 ##

```bash
hostname SW
```

## Privilege Level ##

在一般網路設備預設出廠時，設備的密碼及系統名稱都是預設值，為了避免未經授權的使用者存取設備，在設定裝置時請先設定好EXEC Mode以及Privilege Mode的密碼。

Cisco提供了16種特權等級，分別為0~15，每個等級都對應著不同權限以及不同權限能使用的指令，但實際上只有3種特權等級，因為2~14功能是一樣的，以Cisco Catalyst 2960為例，未把所有指令寫完，請依照設備為準

| Privilege Level  | Available Commands  |
| --- | --- |
| 0 | call，disable，enable，exit，help，logout |
| 2~14 | 以上都可使用以外還可以使用以下指令clear，clock，configure，connect，copy，debug，delete，dir，disable，disconnect，enable erase，exit，logout，more，no，ping，reload，resume，setup，show，ssh，telnet，terminal，traceroute，undebug，write |
| 15 | 以上都可使用以外還可以使用以下指令aaa access-list，banner，boot，cdp，clock，crypto，default，do-exec，dotlx，enable，end，exit，hostname，interface，ip，line，lldp，logging，mac，mls，monitor，no，ntp，port-channel，privilege，sdm，service，snmp-server，spanning-tree，tacacs-server，username，vlan，vtp |

## 特權密碼 ##

```bash
#privilege可加可不加，代表特權等級
enable privilege 15 secret ?
0 不加密 
5 使用MD5雜湊演算法進行加密
8 使用PBKDF2雜湊演算法進行加密
9 使用SCRYPT雜湊演算法進行加密
```


