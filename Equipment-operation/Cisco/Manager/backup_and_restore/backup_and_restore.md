# 備份和還原 #

![](topology1.png)

## 備份 ##

備份Router與Switch操作方式相同，就不特別分類

### 使用TFTP ###

```bash
copy running-config tftp: #複製running-config到TFTP Server
Address or name of remote host[]?192.168.1.100 #TFTP Server IP
Destination filename[Router-config]? #傳至TFTP Server的檔名，可自行更改
```

### 使用SCP ###

    使用SCP的好處在於，SCP有經過加密，可避免安全性問題，在Server開啟SSH功能，以下會寫出Windows以及Linux開啟OpenSSH Server的方法

### Windows ###

下面以Win11作為示範，Win10操作方法類似，點選左下角Windows Icon後選擇setting 

![](windows1.png)

點選左邊的Apps

![](windows2.png)

選擇optional features

![](windows3.png)

點選View features並找到OpenSSH Server

![](windows4.png)

勾選並安裝即可

![](windows5.png)

### Linux ###

安裝套件，以下以Ubuntu進行示範

```bash
sudo apt -y install openssh-server
systemctl start sshd #開啟服務
```

### 開始備份 ###

在Server都開啟SSH後，就可以進行備份

```bash
copy startup-config scp:C:\Users\user1\ #將startup-config copy至scp server，因此練習沒有特別安裝SCP Server軟體，以本機開啟服務作為SCP Server所以須指定目的地路徑，若有安裝軟體的話在軟體中選擇目的地路徑，並使用scp:即可
Address or name of remote host []? 10.1.1.100 #scp server IP
Destination username [SW1]? user1 #使用者名稱，輸入本機使用者即可，若是沒有密碼需新增密碼
Destination filename [C:\Users\user1\]? r1-config #目的地檔名
```


## 還原 ##

Router與Switch還原方式不同，下方示範兩者還原方式

## Router ##

### 使用TFTP ###

```bash
IP_ADDRESS=192.168.1.1 #Router IP
IP_SUBNET_MASK=255.255.255.0 #遮罩
DEFAULT_GATEWAY=192.168.1.1 #預設閘道
TFTP_SERVER=192.168.1.100 #TFTP Server IP
TFTP_FILE=c1841-adventerprisek9-mz.151-4.M.bin #要從TFTP載下來的系統檔
#以上都配置好以後使用以下指令下載
tftpdnld
#詢問是否繼續，輸入Yes
Do you wish to continue? y/n: [n]: yes
#跑完以後開機
boot
```

### 使用SCP ###

```bash
Address or name of remote host []? 10.1.1.100 #SCP Server IP 
Source username [R1]? user1 #登入帳號為user1
Source filename []? r1-config #要獲取的檔案名稱
Destination filename [startup-config]? #存到本地的檔案名稱
Password: #輸入user1的密碼
```

## Switch ##

### Xmodem ###

>Switch復原比較麻煩一點，因為無法單純使用TFTP或者SCP就還原，須使用xmodem將設定檔傳回flash:，不過此種方法速度非常慢，大約需要3小時左右，不過經過調整線路速率後，速度可能會變快，但因多次嘗試後，如果調太快，有可能造成傳到一半卡住的狀況，所以最適合我的速率為14400(我並沒有深入研究關於console線的細節)，若是大家測試時可以調快的話也可以依照實際情況進行調整，以下使用SecureCRT進行示範

開啟設備後，將Console插入設備中，並開啟SecureCRT，因xmodem傳輸速度太慢，下面就不附上連上設備後的圖，如果有機會遇到不小心刪掉ios的狀況(希望是不要)，會再將圖補上

```bash
#當Switch開機時讀不到系統，會出現以下畫面
switch:
#調整線路速率
set BAUD 14400
copy xmodem: flash:c3560-ipservicesk9-mz.150-1.SE.bin #打完這行後，馬上按照以下圖例點選
```

接著開啟SecureCRT -> 點選上方工具列的Transfer -> Send Xmodem -> 選擇傳入的系統檔 -> 等待傳送完成

```bash
#使用剛剛傳好的系統檔開機，以3560系統檔名稱為例
boot flash:c3560-advipservicek9-mz.122-15.SED.bin
#等待開機後，就完成系統還原
```

## 排程 ##

```bash
archive 
    path scp://user1:Cisco123@10.1.1.100/$h_$t #格式為scp://<使用者>:<密碼>@<SCP Server IP>/檔名，若不想將密碼寫於設定檔中，可以寫成scp://user1@10.1.1.100並於存檔時在輸入密碼
    write-memory #存檔時備份一次
    time-period 3 #每三分鐘備份一次
```
