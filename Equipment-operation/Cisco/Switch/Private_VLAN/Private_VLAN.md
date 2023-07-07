# Private VLAN # 

## 簡介 ##

    Private VLAN可在主VLAN底下關聯次要VLAN並做到隔離，常用於DMZ

## 主要VLAN ##

## 次要VLAN ##

    Private VLAN有三種Port類型，分別是
    Promiscuous Port(混雜)- 
    Isolated Port(隔離) - 與isolated VLAN相關的的Port都可到達主要VLAN，但無法訪問其他次要VLAN
    Community Port(共有) - 與community VLAN相關的Port都可互相通信，

## 配置方法 ##

```bash
vlan 10 
    private-vlan primary #設定為主要VLAN
vlan 11
    private-vlan isolated #設定為隔離VLAN
vlan 12
    private-vlan community #設定為共有VLAN
vlan 10
    private-vlan association 11,12 #VLAN 10關聯VLAN11,12
```