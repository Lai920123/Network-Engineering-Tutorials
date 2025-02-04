# Cisco設備更新系統 #

## 1.準備新的系統版本 ##

https://software.cisco.com/download/home

## 2.上傳系統至設備 ##

>假設ios版本為c3750e-universalk9-mz.152-4.E10.bin

**上傳系統有幾種方式**

- FTP
- TFTP
- USB

**FTP**

```bash
copy ftp: flash:
```

**TFTP**

```bash
copy tftp: flash:
```

**USB**
  
```bash
copy usbflash0:c3750e-universalk9-mz.152-4.E10.bin flash:
```

## 3.檢查設備啟動路徑 ##

```bash
show boot 
```

## 4.設置新的路徑啟用設備 ##

```bash
no boot system 
boot system flash:c3750e-universalk9-mz.152-4.E10.bin
```

## 5.檢查啟動路徑是否正確 ##

```bash
show boot 
```

## 6.重啟設備 ##

```bash
reload 
show version #檢察系統版本是否正確
```