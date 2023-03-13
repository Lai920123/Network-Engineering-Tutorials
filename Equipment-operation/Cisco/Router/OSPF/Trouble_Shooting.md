# Trouble Shooting #

## NONBORADCAST ##

當OSPF遇到Frame Relay這種NBMA的網路，因NBMA不發組播只發單播，所以須手動指定鄰居，且hub須為DR，spoke不可進行選舉，所以須將priority調整為0

```bash
#手動宣告鄰居
router ospf 1
    neighbor 192.168.1.100 
#在spoke router的介面卡將priority調整成0(不選舉)
int e0/0
    ip ospf priority 0
```

## 建立鄰居時卡在EXSTART ## 

問題原因 - 端口的MTU不相同 

```bash
#進入介面將MTU變更為相同即可
int e0/0
    ip mtu 1500
```