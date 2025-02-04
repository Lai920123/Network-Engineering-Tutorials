# Restore system image #

Router與Switch還原方式不同，下方示範兩者還原方式

## Router ##

### 使用TFTP ###

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

## Switch ##

### Xmodem ###

>Switch復原比較麻煩一點，因為無法單純使用TFTP或者SCP就還原，須使用xmodem將設定檔傳回flash:，不過此種方法速度非常慢，大約需要3小時左右，不過經過調整線路速率後，速度可能會變快，但因多次嘗試後，如果調太快，有可能造成傳到一半卡住的狀況，所以最適合我的速率為14400(我並沒有深入研究關於console線的細節)，若是大家測試時可以調快的話也可以依照實際情況進行調整，以下使用SecureCRT進行示範

開啟設備後，將Console插入設備中，並開啟SecureCRT，因xmodem傳輸速度太慢，下面就不附上連上設備後的圖，如果有機會遇到不小心刪掉ios的狀況(希望是不要)，會再將圖補上

```bash
#當Switch開機時讀不到系統，會出現以下畫面
switch:
#調整線路速率
set BAUD 14400
copy xmodem: flash:c3560-ipservicesk9-mz.150-1.SE.bin #打完這行後，馬上按照以下圖例點選
```

接著開啟SecureCRT -> 點選上方工具列的Transfer -> Send Xmodem -> 選擇傳入的系統檔 -> 等待傳送完成

```bash
#使用剛剛傳好的系統檔開機，以3560系統檔名稱為例
boot flash:c3560-advipservicek9-mz.122-15.SED.bin
#等待開機後，就完成系統還原
```


