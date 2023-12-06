# Time-range #

在Cisco的IOS作業系統中，可以使用time-range來配置一個時間範圍，並在其他配置中使用此時間範圍

## Periodic ## 

週期性時間，例如星期一到五的早上8:00到12:00拒絕https連線

```bash
time-range no-https
    #periodic [day-of-the-week][hh:mm]to[day-of-the-week][hh:mm] 
    #periodic list [hh:mm] to [hh:mm] all all代表一周所有星期
    periodic list 8:00 to 12:00 mon tue wed thu fri 
ip access-list extended strict 
    deny tcp any any eq https time-range no-https
    permit ip any any 
int g0/0
    ip access-group strict in 

```

## Absolute ##

絕對時間，從特定日期或立即開始，例如拒絕2023/01/01早上8:00到2023/01/05下午15:00的ssh流量

```bash
time-range no-ssh #no-ssh是time-range的名字，可以自己取
    #absulute start [hh:mm][day][month]
    absolute start 8:00 1 jan 2023 #在2023/01/01早上8:00開始
    absolute end 17:00 5 jan 2023 #在2023/01/05下午15:00結束
ip access-list extended strict 
    deny tcp any any eq ssh time-range no-ssh
    permit ip any any 
int g0/0 
    ip access-group strict in 
```

## Recurring ##


## 查詢命令 ##

```bash
show time-range 
```

## Reference ##

https://www.cisco.com/c/zh_tw/support/docs/smb/switches/cisco-small-business-300-series-managed-switches/smb5660-configure-time-range-settings-on-a-switch-through-the-comman.html