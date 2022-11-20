# Hierarchical Architecture 分層式架構 #

>分層式架構將網路分為三層，分別為Core Layer,Distrubution Layer以及Access Layer

## Access Layer 存取層 ##

靠近使用者端，可針對使用者做防護，例如port-security

## Disitrubution Layer 匯聚層 ##

將存取層的流量統一匯聚至匯聚層，此層的設備須支援較大的背版頻寬
主要用來做路由交換,ACL,QoS等

## Core Layer 核心層 ##