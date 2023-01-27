# Power over Ethernet #

## Management Modes ##

```
auto - 自動檢測連接設備是否需要電源，若發現連接設備的端口擁有足夠的功率，會授予端口足夠的功率為設備供電，若功率超過系統預算，會拒絕功率，確保電源關閉並生成日誌信息
static - 預先分配端口配置最大瓦數的電源給端口，並保證端口有可用電源
never - 關閉端口PoE功能和設備檢測，此端口僅為數據端口
``` 

## Reference ##

https://www.cisco.com/en/US/docs/switches/lan/catalyst3850/software/release/3.2_0_se/multibook/configuration_guide/b_consolidated_config_guide_3850_chapter_011010.html#con_1901925