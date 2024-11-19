# Protocol Independent Multicast(PIM) #

用於傳遞組播流量的協定，負責建立和維護組播路由表，以確保流量以最佳路徑達到組播成員


## Reverse path forward(RPF) ##



## Dense Mode ##


```bash
ip multicast-routing 
int range g0/0-2
    ip pim dense-mode 
```

## Sparse Mode ##



## 配置方法 ##

```bash
ip multicast-routing #開啟組播路由
int range e0/0-2
    ip igmp join-group 239.1.1.1
```

## 查看命令 ##

```bash
show ip mroute #查看組播路由表
show ip pim neighbor #查看pim鄰居表
show ip igmp membership #檢查IGMP成員
```

## Reference ##

https://www.networkacademy.io/ccie-enterprise/multicast/multicast-ip-to-mac-mapping