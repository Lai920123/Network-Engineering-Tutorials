# DHCP #

## Topology ##

![](Image/1.png)

## Initial ##

```bash
config system global 
    set hostname FW1
config system interface 
    edit port1 
    set mode dhcp 
    set allowaccess ping http https 
end
```