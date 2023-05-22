# EIGRP Metric #

## K Value # 

    K1 - Bandwidth 
    K2 - Loading 
    K3 - Delay 
    K4 - Reliability 
    K5 - MTU

預設K1和K3為1

## Metric Calculation ##

Metric計算公式為 $$ 256 x \left( \frac{10}{bandwidth}+\frac{Delay}{10} \right) $$