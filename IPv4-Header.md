# IPv4-Header

## IPv4表頭欄位

### Version

版本，IPv4為4，IPv6為6 ，4bit

### Header-Length

表達header的長度，也用來確定資料的偏移量，4bit

### Type of Service

提供Qos服務使用，左6為DSCP，右2為ECN，8bit

### Total Length

封包總長，包含首部和資料，最小為20byte，最大為2的16次方 = 65535，16bit

### identifier

用來標示封包的所有分片，每產生一筆資料報,計數器加1並賦值給此欄位，因為分片不一定按順序到達，這樣才能依序重組回原本的資料，16bit

### Flags

0 保留，必須為0 0 Don’t Fragment(禁止分片)

DF=0允許分片

DF=0不允許分片 

0 More fragment(更多分片)

MF=1代表後面還有分片

MF=0代表這是最後一個分片 

Fragment Offset  每個分片相對於原始封包開頭的偏移量 

3bit 

### Time to Live

避免路由迴圈，每經過一個路由器都將此欄位減1，欄位等於0時則丟棄封包，最大值為255，8bit

### Protocol

定義了使用的協定，8bit

詳細可以查看此網址

[IP协议号列表 - 维基百科，自由的百科全书](https://zh.wikipedia.org/zh-tw/IP%E5%8D%8F%E8%AE%AE%E5%8F%B7%E5%88%97%E8%A1%A8)

以下列出常見的 

0x01 ICMP 

0x04 IPv4 

0x29 IPv6 

0x06 TCP 

0x11 UDP 

0x59 OSPF 

0x58 EIGRP Header 

### Checksum

表頭確認碼，只針對header查錯，不包含資料，每一跳路由器都需要重新算出header checksum並與此欄位進行比對，若是不一致，將會被丟棄，16bit

### Source address

來源位置，32bit

### Destination address

目的地位置，32bit

### Options

較少用到，可以查看維基百科 

### data

資料不包含在表頭的欄位中，資料格式在表頭欄位中有指名，並且可以是任何的傳輸層協定