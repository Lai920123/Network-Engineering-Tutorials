# GUI #

在Cisco的設備中有一些型號是可以使用圖形化介面進行配置的，像是C1111路由器，不過要進入圖形化介面前，還是需要先使用命令行進行配置後才可以開始使用，以下為配置指令

```bash
username admin privilege 15 secret Cisco123 #先建立登入的帳號密碼
ip http server #開啟http 
ip http secure-server #開啟https(可選)
ip http authentication local #使用本地認證
```

上面都輸入完後，打開瀏覽器並輸入http://IPADDRESS/，接著使用剛剛建立的本地使用者登入即可