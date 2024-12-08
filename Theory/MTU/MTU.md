# Maximun Tranmission Unit(MTU) 最大傳輸單元 #

| Network Type | MTU(Byte) |
| --- | --- |
| Hyper Channel | 65535 |
| 16MB/Token Ring | 17914 |
| 4MB/Token Ring | 4464 |
| FDDI | 4352 |
| Ethernet | 1500 |
| IEEE 802.3/802.2 | 1492 |
| X.25 | 576 |
| P2P | 296 |
| ATM | 48 |

## ## 

MTU指的是Frame內容的最大值，超過就會進行fragment，一個Ethernet Frame最大MTU為MTU 1500 bytes + Header 14 bytes + FCS 4 byte = 1518 bytes

## MTU超過大小後果 ##

MTU如果超過指定的大小，可能會造成封包被丟棄或分片，依照設備的不同