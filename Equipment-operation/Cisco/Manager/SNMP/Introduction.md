# Simple Network Management Protocol 簡單網路管理協定 #

## 簡介 ##

    SNMP是幾乎所有企業與校園中都會啟用的協議，用於管理連上網路的裝置，使管理員能夠即時監控設備異常並迅速處理

## 使用端口 ##

    SNMP管理端使用UDP Port 162，代理端使用UDP Port 161

## 基本元件 ##

    SNMP管理的網路由以下三個基本元件組成
    1.Network-Management Systems(NMS):安裝於管理端電腦，負責與SNMP Agent進行溝通
    2.Managed Device:被管理的網路節點，透過管理資訊庫Management information base(MIB)收集並儲存管理資訊，並透過SNMP Agent與NMS進行溝通
    3.Agent:安裝於網路設備中，收集本地的管理資訊，並於NMS查詢時以與SNMP相容的格式傳送資訊

## 
## SNMP運作模式 ##

## 參考文章 ##

https://en.wikipedia.org/wiki/Simple_Network_Management_Protocol

https://www.manageengine.com/tw/network-monitoring/what-is-snmp.html