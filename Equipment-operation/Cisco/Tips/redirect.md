# Redirect #

Rdirect可以將命令的輸出重導向到外部的ftp/tftp Server等服務

```bash
show tech-support | redirect tftp://192.168.1.100/tech-support.txt #將報告重導向到tftp server
```

tee可以將輸出存一分至指定的外部Server同時也會輸出於Console畫面上

```bash
R1#
show ip int brief | tee tftp://192.168.1.100/show-int-brief.txt #會存一分至tftp://192.168.1,100/show-int-brief.txt，也會輸出
#Interface                  IP-Address      OK? Method Status                Protocol
#Ethernet0/0                192.168.50.10   YES TFTP   up                    up      
#Ethernet0/1                unassigned      YES TFTP   administratively down down    
#Ethernet0/2                unassigned      YES TFTP   administratively down down    
#Ethernet0/3                unassigned      YES TFTP   administratively down down 
```

append可以將內容附加到原有檔案內容底下

```bash
R2#
show ip int brief | append tftp://192.168.1.100/show-int-brief.txt #繼續剛剛tee的範例，如果想將R2的show ip int brief也輸出到同一個檔案，但不想覆蓋掉，即可使用append，但不會輸出
```
