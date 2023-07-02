# Protocol Independent Multicast(PIM) #

## Dense Mode ##



## Sparse Mode ##



## 配置方法 ##

```bash
ip multicast-routing #開啟組播路由
int range e0/0-2
    ip igmp join-group 100.1.1.1
```

## 查看命令 ##

```bash
show ip mroute #查看組播路由表
show ip pim neighbor #查看pim鄰居表
```