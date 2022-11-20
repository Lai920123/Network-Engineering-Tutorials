# Hierarchical Architecture 分層式架構 #

>分層式架構將網路分為三層，分別為Core Layer,Distrubution Layer以及Access Layer

## Access Layer 存取層 ##

1.提供使用者存取
2.支援多種流量的收斂(Voice,Wireless...)
3.提供安全存取(Portsecurity)

## Disitrubution Layer 匯聚層 ##

將存取層的流量統一匯聚至匯聚層，此層的設備須支援較大的背版頻寬
主要用來做路由交換,ACL,QoS等

## Core Layer 核心層 ##

核心層主要處理繞送，需要比匯聚層更高的頻寬，Server DMZ的交換機也會接到核心層