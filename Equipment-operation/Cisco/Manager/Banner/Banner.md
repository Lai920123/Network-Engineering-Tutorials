# Banner

Banner可以用來在登入時給予使用者提示或者歡迎詞

```bash
語法:開頭跟結尾相同符號即可，例如#Hi#
login，驗證帳密時會顯示的banner
prompt-timeout，驗證帳密timeout時會顯示的banner
motd，登入設備時會顯示的banner
exec，exec提示之前顯示的banner
incoming，反向telnet連接的使用者會顯示的banner
config-save，配置完成時顯示的banner
```

範例

```bash
banner motd /Hello World/ #包住字串的用甚麼符號都可以，只要前後相同即可
```