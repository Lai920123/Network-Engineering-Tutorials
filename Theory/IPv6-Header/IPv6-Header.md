
# IPv6-Header

IPv6表頭刪除了許多IPv4中不需要的欄位，所以相對IPv4更有效率 

## IPv6標頭欄位

### Version

跟IPv4相同，設定為6，4bit

### Traffic Class

識別IPv6封包的類別或優先等級，8bit

### Flow Label

來源與目標之間的標示符,IPv6的封包能夠在該欄位留下標記，在傳輸時，一連串的封包會要求所經過的路由器，提供特別的處理。 而路由器則會透過該欄位，辨識封包的Flow Level；而Priority則可以設定封包傳輸的優先順序，透過這欄位的檢查，讓較重要 的封包優先傳送。 

### Payload Length

有效負載的大小，包括任何擴展表頭 

### Next Header

指定下個標頭的類型，跟IPv4的Protocol欄位相似，8bit

### Hop Limit

相似於IPv4的Time to Live,每經過一個hop值減1,直到歸0封包將被丟棄，8bit

### Source IP Address

來源位置，128bit

### Destination IP Address

目的地位置，128bit