# 忘記密碼修改方式 #

>Hint: startup-config儲存於NVRAM中，重新啟動後不會揮發，而running-config只儲存於RAM中，下次開機會不見，所以不管做什麼都要記得存檔至startup-config或者外部伺服器中(TFTP、SCP...)

## Router ##

```bash
#重新開機後按下Ctrl+Break(通常於Page up上方或者跟Page up一起，若是一起要多按一個Function鍵)進入rommon模式
#進入修復模式後將register修改成0x2142，意思是忽略啟動設定檔，預設register為0x2102
rommon 1>confreg 0x2142
#開機，使用boot或reset都可以
rommon 2>boot
#開機後會發現沒有任何設定，所以要將startup-config複製至running-config 
copy startup-config running-config 
#接著修改密碼
configure termianl 
enable secret Cisco123
line console 0 
    password Cisco123
#接著會發現所有網路都斷線了，因使用copy startup-config running-config或者copy tftp: running-config時所做的都是合併而非覆寫，合併會將running-config預設的端口shutdown保留，所以端口是全部shutdown的，需手動啟用有在使用的端口
int range e0/0 - 4
    no shutdown 
#將register改回0x2142 
config-register 0x2142
#修改後存檔
copy running-config startup-config 
#重開機後使用新密碼可登入並且端口正常啟動即可
reload 
```

## Switch ## 

```bash
#重新啟動，在啟動時按住mode按鈕直到閃橘黃燈為止，進入修復模式
reload 
#將設定檔改名，因預設設定擋路徑於flash:/config.txt，若更改檔名，開機時就讀不到設定檔，會以空設定的狀態開機
rename flash:/config.txt flash:/old-config.txt
#開機
boot
#將設定檔複製到running-config 
copy flash:/old-config.txt running-config 
#進入全域配置模式配置密碼
configure terminal 
enable secret Cisco123
#存檔
copy running-config startup-config 
```