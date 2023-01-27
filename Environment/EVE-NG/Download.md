# 下載路徑存放 #

## Aruba ##

http://www.arubalab.work/AOS-CX/10.04.1000/

使用方法

```bash
#在EVE-NG中建立名為abc的資料夾，並放置在/root底下
mkdir abc
#將檔案下載下來之後傳入EVE-NG中
scp ArubaOS-CX_10_04_1000_ova.zip root@192.168.1.100:/root/abc
#解壓縮
unzip ArubaOS-CX_10_04_1000_ova.zip
#解壓縮後再次解壓縮.ova檔
tar xvf ArubaOS-CX_10_04_1000.ova
```