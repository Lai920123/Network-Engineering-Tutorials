# Port Security #

>Port Security通常會配置於存取層交換機，用於防止未授權的設備連接，也可用於防護MAC flooding Attack

## 違規行為(violation) ##

### Protect ###

>不關閉介面，將封包Drop，不紀錄Log和SNMP，不建議使用

### Restrict ###

>不會關閉介面，將封包Drop，並紀錄Log和SNMP，

### Shutdown ###

>將介面變成err-disable，並記錄Log和SNMP，預設值

## 手動配置MAC Address ##

```bash
int range f0/1-11 #選取要配置Port Security的Port
    switchport mode access #須先設定模式才可配置Port Security 
    switchport port-security maximum 1 #最大MAC數量為1，若是只有一個MAC的話，這句可以省略，因為為預設值
    switchport port-security mac-address 1111.1111.1111 #手動配置MAC位置
    switchport port-security violation shutdown #違規行為為關閉
    switchport port-security #啟用port security 
```

## 動態Sticky配置MAC Address ## 

重複的指令就不再寫了，只需要將violation的參數更改即可

```bash
int range f0/1-11 #選取要配置Port Security的Port
    switchport port-security mac-address sticky #使用動態黏接MAC Address
```

## port security aging ## 

aging為比較細部的參數，所以另外寫出來，aging通常用於為sticky黏上的MAC Address設定存活時間

```bash
switchport port-security aging static #手動輸入的MAC Address也加入計時
switchport port-security aging min 5 #MAC Address可存活的時間為5分鐘，預設為0，表示永久有效
switchport port-security aging type <inactivity/absolute> #inactivity為當沒有封包通過時開始計時，absolute為絕對時間
```

## 自動恢復 ##

>當交換機因為使用者插入未授權的設備時，預設違規行為會將端口關閉，要將Port重新開啟的話只需管理員手動shutdown再no shutdown即可，也可設定自動恢復

```bash
errdisable recovery interval 300 #錯誤關閉恢復間隔時間為300秒
errdisable recovery cause psecure-violation #自動復原原因為port-securit的違規行為
```

## 查看err-disable的介面 ##

最後介紹一個超級好用的指令，查詢所有err-disable的介面

```bash
show interface status err-disabled 
```