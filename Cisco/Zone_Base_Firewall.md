# Zone Based Firewall

可以配置區域並把流量區隔開來

配置Zone

```powershell
zone security DMZ
zone security INSIDE
zone security OUTSIDE
```

指派介面到zone

```powershell
int e0/0
	zone-member security DMZ
int e0/1
	zone-member security OUTSIDE
int e0/2
	zone-member security INSIDE
```

配置Configure Interzone

```powershell
ip access-list extended INSIDE-TO-OUTSIDE
	permit tcp 10.1.1.0 0.0.0.255 any eq www
	permit tcp 10.1.1.0 0.0.0.255 any eq telnet
	permit icmp 10.1.1.0 0.0.0.255 any
class-map type inspect match-all INSIDE-TO-OUTSIDE-CLASS
	match access-group name INSIDE-TO-OUTSIDE
ip access-list extended OUTSIDE-TO-INSIDE
	permit icmp any 10.1.1.0 0.0.0.255
class-map type inspect match-all OUTSIDE-TO-INSIDE-CLASS
	match access-group name OUTSIDE-TO-INSIDE
ip access-list extended OUTSIDE-TO-DMZ
	permit tcp any 192.168.1.0 0.0.0.255 eq www
class-map type inspect match-all OUTSIDE-TO-DMZ-CLASS
	match access-group name OUTSIDE-TO-DMZ
ip access-list extended INSIDE-TO-DMZ
	permit tcp 10.1.1.0 0.0.0.255 192.168.1.0 0.0.0.255 eq www
	permit icmp 10.1.1.0 0.0.0.255 192.168.1.0 0.0.0.255
class-map type inspect match-all INSIDE-TO-DMZ-CLASS
	match access-group name INSIDE-TO-DMZ
```

設定policy-map

```powershell
policy-map type inspect INSIDE-TO-OUTSIDE-POLICY
	class type inspect INSIDE-TO-OUTSIDE-CLASS
	inspect
	class class-default
	drop log
policy-map type inspect OUTSIDE-TO-INSIDE-POLICY
	class type inspect OUTSIDE-TO-INSIDE-CLASS
	pass
	class class-default
	drop log
policy-map type inspect OUTSIDE-TO-DMZ-POLICY
	class type inspect OUTSIDE-TO-DMZ-CLASS
	inspect 
	class class-default
	drop log
policy-map type inspect INSIDE-TO-DMZ-POLICY
	class type inspect INSIDE-TO-DMZ-CLASS
	pass
	class class-default
	drop log
```

建立並套用policy maps to Zone Pairs 

```powershell
zone-pair security IN-TO-OUT source INSIDE destination OUTSIDE
	service-policy type inspect INSIDE-TO-OUTSIDE-POLICY
zone-pair security OUT-TO-IN source OUTSIDE destination INSIDE
	service-policy type inspect OUTSIDE-TO-INSIDE-POLICY
zone-pair security OUT-TO-DMZ source OUTSIDE destination DMZ
	service-policy type inspect OUTSIDE-TO-DMZ-POLICY
zone-pair security IN-TO-DMZ source INSIDE destination DMZ
	service-policy type inspect INSIDE-TO-DMZ-POLICY
```