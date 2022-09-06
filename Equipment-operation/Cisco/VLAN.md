# Vlan

## 創建Vlan

```powershell
vlan 10
	name Sales #指定Vlan名稱
```

## 設定端口Vlan

```powershell
switchport mode access
switchport access vlan 10
```

## 設定Native Vlan

```powershell
#switchport trunk encapsulation dot1Q 三層交換器需下此指令
switchport mode trunk
switchport trunk native vlan 999
```