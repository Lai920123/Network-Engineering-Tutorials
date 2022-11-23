# Port Security #

>Port Security通常會配置於存取層交換機，用於防止未授權的設備連接，也可用於防護MAC flooding Attack

## 違規行為(violation) ##

### Protect ###

>將不合法的訊匡Drop掉，不紀錄

### Restrict ###

>將不合法的訊匡Drop掉，並紀錄

### Shutdown ###

>

## 手動配置MAC Address ##

```bash
int range f0/1-11 #選取要配置Port Security的Port
    switchport mode access #須先設定模式才可配置Port Security 
switchport port-security maximum 1 #最大MAC數量為1
switchport port-security mac-address 1111.1111.1111 #手動配置MAC位置
switchport port-security violation shutdown #違規行為為關閉
switchport port-security #啟用port security 
```

## 動態Sticky配置MAC Address ## 

```bash
int range f0/1-11 #選取要配置Port Security的Port
    switchport mode access #須先設定模式才可配置Port Security 
switchport port-security maximum 1 #最大MAC數量為1
switchport port-security mac-address sticky #使用動態黏接MAC Address
switchport port-security violation shutdown #違規行為為關閉
switchport port-security #啟用port security 
```

>Note:當交換機因為使用者插入未授權的設備時，預設違規行為會將端口關閉，要將Port重新開啟的話只需管理員手動shutdown再no shutdown即可，也可設定自動恢復

## 自動恢復 ##

```bash
errdisable recovery interval 300 #錯誤關閉恢復間隔時間為300秒
errdisable recovery cause psecure-violation #自動復原原因為psecure-violation 
```


