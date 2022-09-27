# 實驗環境搭建 #

## EVE-NG ##

使用EVE-NG須先擁有VMware workstation play or VMware workstation Pro

### 1. 開啟VMware workstation Pro ###

![](environment/vmware1.png)

### 2.點選File -> Open -> 選取要開啟的檔案，編輯名稱後開啟即可 ###

## TroubleShooting ##

```bash
#Error Couldn't run /usr/bin/dumpcap in child process: Permission denied when starting Wireshark 因權限不足，無法開啟Wireshark進行抓包
#解決方法 - 將使用者加入群組wireshark即可
sudo usermod -aG wireshark $USER
sudo dpkg-reconfigure wireshark-common
```

```bash 
#使用Windows開啟抓包時，終端畫面出現Connection abandoned
#解決方法 - 使用系統管理員開啟終端機，輸入下方指令後重啟EVE-NG即可
cd C:\Program Files\EVE-NG #進入路徑
echo y | .\plink.exe -ssh -l <虛擬機使用者> -pw <密碼> <虛擬機IP>
#範例
echo y | .\plink.exe -ssh -l root -pw eve 192.168.1.100
reboot #將虛擬機重新啟動，再次開啟抓包就可以正常抓包了
```