# Restore running-config #

## 使用SCP ##

```bash
Address or name of remote host []? 10.1.1.100 #SCP Server IP 
Source username [R1]? user1 #登入帳號為user1
Source filename []? r1-config #要獲取的檔案名稱
Destination filename [startup-config]? #存到本地的檔案名稱
#Erasing flash: before copying?[confirm] 舊版系統的問題，要注意，不要再copy前刪除flash
Password: #輸入user1的密碼
```

或者使用複寫的方式，可以在不用reload設備的狀況下還原

```bash
configure replace flash:r1-config list
Enter Y if you are sure you want to proceed. ? [no]: y
```
