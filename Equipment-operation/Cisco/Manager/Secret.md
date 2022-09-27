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

## 遠端管理 ##

### Telnet ###

```bash
username admin privilege 15 secret 123456 #建立帳號密碼
line vty 0 4
	transport input telnet
	login local #也可以打no login代表登入不需輸入密碼
```

### SSH ###

```bash
ip domain-name lai.com #要使用ssh需要設定domain-name
username admin privilege 15 secret 123456 #建立帳號密碼 
crypto key generate rsa modulus 2048 #生成金鑰
line vty 0 4
	login local
	transport input ssh
```

### 更改預設Port ###
```bash
ip ssh port 8888 rotary 1
line vty 0 4
	transport input ssh
	login local #使用本地登入，需要建立使用者
	rotary 1
```

### 使用金鑰驗證 ###

```bash
ip ssh pubkey-chain 
	username admin
	key-string 
	#須將公鑰分為72字元一行的格式，並逐行複製貼上
	AAAAB3NzaC1yc2EAAAADAQABAAABAQCTqyLjjg+v/Gs1FTHMAbEg5soDYHw6T/sGhI7J2+X
	tSuqce4ouit5VAe9737V5OMo3SUOz5flcglSJg+a+jjkpoq8g0UiZhrtPpY8CcvPBUXm/7f
	m0rHDRn6fknPC7moMThsuWNBGZXxIileAh4qNIeh8cZZuGgXtWR47cMtCOk5+rMIY+XWFLU
	VG1QkdUVoagjDFekZS4l8fj94libg69/T8lLCtja+0IrPS8ZHBUW/HzHMq9Py6sfLQSQpNr
	tK0Jtyre5fHD8yXalY31XZkqhsC04P5K8DKO5itd/QblpsXUKMBCdiJ60tpjWPSI3tjiuOc
	47msmSsqARzirdRDB 
#另外，使用終端設備連入時，須注意演算法是否有誤，若是無法連線，可嘗試以下指令
ssh -v -c aes256-cbc admin@10.1.1.11
```

