# Multi-Protocol Label Switching 多協定標籤交換 #

## Label Distribution Protocol(LDP) 標籤分散協定 ## 

Cisco預設使用LDP作為MPLS標籤分散協定，LDP是一種基於TCP的協定，用於在MPLS網路中分發標籤，LDP使用TCP 646埠，LDP使用Hello封包來建立鄰居關係，並使用Label Mapping封包來分發標籤，可以使用mpls label protocol tdp來將協定更改為TDP。


## Tag Distribution Protocol(TDP) 標籤分散協定 ## 

Cisco專有協定，用於在MPLS網路中分發標籤，TDP使用TCP 711埠，TDP使用Hello封包來建立鄰居關係，並使用Label Mapping封包來分發標籤，可以使用mpls label protocol ldp來將協定更改為LDP。

## MP-BGP ##

MPLS使用MP-BGP來分發標籤，MP-BGP向下兼容，使支持BGP擴展與不支持BGP擴展之間的路由器可以互通，MP-BGP支援IPv4、IPv6、MPLS和EVPN等擴展協定的路由信息交換

## Label Switch Router (LSR) ##

執行MPLS的路由器

## Ingress LSR ## 

進入MPLS網路的第一個路由器

## Egress LSR ##

離開MPLS網路的路由器

## Core LSR ##

除了Ingress LSR和Egress LSR之外的路由器就稱為Core LSR

