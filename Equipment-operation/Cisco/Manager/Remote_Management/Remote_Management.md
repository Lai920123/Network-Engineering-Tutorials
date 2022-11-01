# Remote Management #

## Telnet ##

```bash
username admin privilege 15 secret 123456 #建立帳號密碼
line vty 0 4
	transport input telnet
	login local #也可以打no login代表登入不需輸入密碼
```

## SSH ##

### 基本配置 ###

```bash
ip domain-name lai.com #要使用ssh需要設定domain-name
username admin privilege 15 secret 123456 #建立帳號密碼 
crypto key generate rsa modulus 2048 #生成金鑰
line vty 0 4
	login local
	transport input ssh
```

### 安全設定 ###

```bash
enable #進入特權模式
configure terminal #進入全域配置模式  
login block-for 120 attempts 3 within 30 #30秒內密碼3次不正確鎖定120秒
login delay 5 #登入後延遲5秒
login quiet-mode access-class 1 #鎖定期間允許ACL 1登入
login on-failure log #登入失敗要記錄
login on-success log #登入成功要記錄
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
