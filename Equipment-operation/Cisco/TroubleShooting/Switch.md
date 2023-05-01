# Switch #

Switch可能的錯誤點 

## Error-Disabled ## 

- Port security violation mac位置不對，觸發違規

- STP BPDUGUARD activated 當開啟BPDUGUARD的介面收到BPDU時觸發

- EtherChannel misconfiguration 速率不相同

- UDLD activation 

可使用此命令查看介面是否err-disabled

```bash
show interfaces status err-disabled 
```

