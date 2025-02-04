# Auto Backup #

自動備份在企業環境中非常重要，可以自行架設SCP或TFTP Server等服務進行備份

## 備份方式 ##

使用Cisco提供的archive進行備份

### TFTP ###

```bash
archive 
path tftp://192.168.1.100/$t$h #$t為時間戳，$h為主機名稱
time-period 1440 #單位為分鐘，1440為每24小時更新一次
write-memory #當使用者手動備份(wr,copy running-config startup-config)時也會進行一次備份
```

### SCP ###

```bash
archive 
    path scp://user1:Cisco123@10.1.1.100/$h_$t #格式為scp://<使用者>:<密碼>@<SCP Server IP>/檔名，若不想將密碼寫於設定檔中，可以寫成scp://user1@10.1.1.100並於存檔時在輸入密碼
    write-memory #存檔時備份一次
    time-period 3 #每三分鐘備份一次
```