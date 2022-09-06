# PPP

## ppp(point to point Protocol)

### 查看ppp

```powershell
show ppp all  
```

## 認證方式

### PAP(password authentication protocol):

兩次握手,使用明文傳輸帳密進行認證 

認證端: 

```powershell
username user secret cisco 
int s1/0
	encapsulation ppp 
	ppp authentication pap
```

被認證端:

```powershell

int s1/0
  encapsulation ppp
  ppp pap sent-username user password cisco
```

### CHAP(Challenge-Handshake Authentication Protocol):

先將username和password hash後再傳送,username必須為對方的裝置名稱,且密碼需相同 

認證端: 

```powershell
username BRANCH secret cisco 
int s1/0 
	encapsulation ppp 
	ppp authentication chap
```

```powershell
被認證端:
username HQ password cisco
int s1/0
    encapsulation ppp
    ppp authentication chap
```

### Multi-Link ppp:

```jsx

```

### PPPoE(point to point protocol over ethernet):

將ppp封裝到ethernet,在ethernet實現認證與加密功能 

認證端:

建立帳號密碼

```
username user@isp.net secret cisco
```

排除IP範圍

```
ip dhcp excluded-address 123.0.1.1 123.0.1.10  
ip dhcp excluded-address 123.0.1.200 123.0.1.254
```

建立dhcp pool

```
ip dhcp pool ADSL  
	network 123.0.1.0 255.255.255.0 
	default-router 123.0.1.1
	dns-server 8.8.8.8
```

PPPoE用戶使用ADSL這個pool 

```
int virtual-template 1 
	ip unnumbered e0/1 
	peer default ip address dhcp-pool ADSL 
	ppp authentication pap #使用pap驗證 
	ip mtu 1492 
```

```
bba-group pppoe global 
	virtual-template 1 
int e0/1 
	pppoe enable group global 
	no shutdown
```

用戶端

```powershell
int dialer 1 #建立撥號介面
	ip address negotiated #IP協商取得
	ip mtu 1492 #撥號介面MTU調整為1492因PPP表頭8bytes
	ip tcp adjust-mss 1452 #指定TCP MTU最大為1452(TCP Header 20 bytes + IPv4 Header 20 bytes)
	encapsulation ppp #封裝為PPP 
	ppp pap sent-username user@isp.net password cisco #PAP送出驗證帳密
	ppp ipcp route default #PPP協商安裝default route
	dialer pool 1 #使用撥號pool 1
```

```powershell
int e0/1 
	pppoe-client dial-pool-number 1 #PPPoE用戶端使用pool 1
	no shutdown
```

```powershell
dialer-list 1 protocol ip permit #撥號清單1,IP流量觸發撥號
```