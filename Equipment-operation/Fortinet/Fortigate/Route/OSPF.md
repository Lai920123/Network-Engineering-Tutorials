# OSPF #

## 配置OSPF ##

```bash
config router ospf 
    set router-id 1.1.1.1 
    config area 
        edit 0.0.0.0 #area id 
    config network 
        edit 1 
            set prefix 192.168.1.0 255.255.255.0 #發佈此網段
        edit 2
            set prefix 192.168.2.0 255.255.255.0 #發佈此網段
[Check]
get router info ospf neighbor #查看ospf鄰居
get router info ospf database #查看LSDB
get router info ospf route #查看OSPF路由
get router info ospf interface #查看開啟ospf的介面
```