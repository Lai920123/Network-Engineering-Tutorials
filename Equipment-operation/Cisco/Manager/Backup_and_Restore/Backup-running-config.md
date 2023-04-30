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


