# Config-register

設定組態暫存器可以在全域配置模式設定或是從ROMmon模式設定 

```bash
0x2100 #開機時不找startup-config直接尋找ROM monitor
0x2102~210F #正常載入IOS以及startup-config 
0x2142
```

全域配置:

ROMmon: