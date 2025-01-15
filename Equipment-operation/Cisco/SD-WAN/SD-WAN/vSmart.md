# vSmart #

## 集中控制策略 ##

**預設行為:** 
- vEdge以DTLS連線向vSmart傳送prefix、tlocs和service routes
- vSmart接受所有OMP路由後發送路由給每個vEdge

**具集中策略的行為:**
- 根據inbound策略過濾或修改vEdge傳送來的路由後再放入路由表
- 根據outbound策略過濾或修改vSmart通告到vEdge的路由


## Reference ##

https://www.networkacademy.io/ccie-enterprise/sdwan/control-connections