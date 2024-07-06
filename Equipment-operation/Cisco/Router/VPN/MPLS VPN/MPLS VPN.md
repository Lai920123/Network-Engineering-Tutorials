# Multi-Protocol Label Switching 多協定標籤交換 #

## Label Distribution Protocol(LDP) 標籤分散協定 ## 

Cisco預設使用LDP作為MPLS標籤分散協定，LDP是一種基於TCP的協定，用於在MPLS網路中分發標籤，LDP使用TCP 646埠，LDP使用Hello封包來建立鄰居關係，並使用Label Mapping封包來分發標籤，可以使用mpls label protocol tdp來將協定更改為TDP。


## Tag Distribution Protocol(TDP) 標籤分散協定 ## 

Cisco專有協定，用於在MPLS網路中分發標籤，TDP使用TCP 711埠，TDP使用Hello封包來建立鄰居關係，並使用Label Mapping封包來分發標籤，可以使用mpls label protocol ldp來將協定更改為LDP。

