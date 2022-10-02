# 備份和還原 #

![](topology1.png)

## 備份 ##

```bash
copy running-config tftp: #複製running-config到TFTP Server
Address or name of remote host[]?192.168.1.100 #TFTP Server IP
Destination filename[Router-config]? #傳至TFTP Server的檔名，可自行更改
```

## 還原 ##

```bash
IP_ADDRESS=192.168.1.1 #Router IP
IP_SUBNET_MASK=255.255.255.0 #遮罩
DEFAULT_GATEWAY=192.168.1.1 #預設閘道
TFTP_SERVER=192.168.1.100 #TFTP Server IP
TFTP_FILE=c1841-adventerprisek9-mz.151-4.M.bin #要從TFTP載下來的系統檔
#以上都配置好以後使用以下指令下載
tftpdnld
#詢問是否繼續，輸入Yes
Do you wish to continue? y/n: [n]: yes
#跑完以後開機
boot
```