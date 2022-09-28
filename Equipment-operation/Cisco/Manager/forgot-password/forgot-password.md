# 忘記密碼修改方式 #

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