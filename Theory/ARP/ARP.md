# Address Resulation Protocol 位置解析協定 #

## 查看與清除方法 ##

```bash
#查看
show arp-cache
#清除，因Cisco設備會在使用清除指令時重新發ARP詢問設備的Mac Address，所以須先將Port關閉，才能夠得到乾淨的ARP Table 
int f0/0
    shutdown 
    exit #退回特權模式
clear arp #清除APR快取
```