# BGP TroubleShooting #

## %BGP-4-MSGDUMP ##

>%BGP-4-MSGDUMP: unsupported or mal-formatted message received from 209.165.201.6: FFFF FFFF FFFF FFFF FFFF FFFF FFFF FFFF 0039 0104 FFFF 00B4 D1A5 C9E1 1C02 0601 0400 0100 0102 0280 0002 0202 0002 0246 0002 0641 0400 00FF FF

當出現類似上方的Log時，可以檢查兩端的設定是否正確

- 錯誤的IP位置

- 找不到update-source loopback

- AS Number錯誤

- 錯誤的認證密碼

以上錯誤都有可能造成此情況