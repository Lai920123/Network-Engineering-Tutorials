# TrobleShooting #


## Router ##
### FLAPPING ###
Cisco設備發生FLAPPING有幾種可能
交換機MAC資料庫錯誤
環境中有偽造的MAC
出現LOOP
STP設定錯誤
HSRP設定錯誤
ETHERCHANNEL設定錯誤


## Switch ##

### 碰撞 ###

    交換機會出現碰撞只有一種可能，就是雙工不匹配，請檢察交換機的端口是否為全雙工


## Other ##

### 用戶端從DHCP收到未知網段 ###

    當用戶端收到不是由管理員，就幾乎可以確定是有人在環境中架設了另一台DHCP Server，有幾種解決方法
    1.從用戶端使用ipconfig /all查看DHCP Server的位置並查看ARP Cache找到Server的MAC，再從Switch將此Port Shutdown即可
    2.此方法較好，在端口設置DHCP Snooping，從根本上斷絕問題