# Vlan Trunking Protocol #

## 模式 ##

## Server Mode ##

>可更改本機的VLAN Database，收到較新的VLAN資訊會將更新資訊傳送給其他switch

## Client Mode ##

>不可更改本機的VLAN Database，收到較新的VLAN資訊會將更新資訊傳送給其他switch

## Transparent Mode ##

>可更改本機的VLAN資訊，收到較新的VLAN資訊會將更新資訊傳送給其他switch，但不會更新自己的VLAN Database

## 查看VTP狀態

```powershell
show vtp status
```

## VTP version 2

!!!switch對接的線路必須要是Trunk

### Server

```powershell
#當所有Vlan配置完成後，最好將client端的vtp mode更改為transport mode，否則如果使用vtp version 2會有Server mode被搶走的問題
vtp mode server [server|client|transport]
vtp domain cisco.com
vtp password cisco123
vtp version 2
vtp pruning 
```

### Client

```powershell
vtp mode client
vtp domain cisco.com
vtp password cisco123
```

### VTP version2缺陷

在VTP version2中，若是Client switch故障需要維修，但接回拓樸中時Configuration Revision的值大於Server的話，原本故障的switch就會成為Server開始向其他Switch更新他的VLAN Database

## VTP version 3

VTP Version3改善了VTP Version1和Version2一個重大的缺陷，在VTP Version3中加入了Primary Server，需先升級至Primary Server才可以更改VLAN，不會再因為收到較新的VLAN資訊而將Server Mode的Switch VLAN Database給替換掉

### Server

```bash
vtp domain cisco.com
vtp password cisco hidden 
vtp version 3
```

### Client

```bash
vtp domain cisco.com
vtp password cisco hidden  
vtp version 3 
```

### 升級至Primary Server

```bash
#在特權模式下
vtp primary vlan 
#接著需輸入vtp密碼，密碼驗證完畢後，就可升級成為Primary Server
```

### 將Primary Server降級回Server Mode

```bash
#先更改為Transparent Mode再更改回Server Mode
vtp mode transparent 
vtp mode server 

```

## 關閉VTP

```bash
#目前沒有查到關閉VTP的指令，只能將模式更改為Transparent
vtp mode transparent 
#較新作業系統
vtp mode off
```