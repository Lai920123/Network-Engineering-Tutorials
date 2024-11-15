# Internet Group Mangement Protocol # 

分辨哪些為成員，要接收組播流量

## Any-Source Multicast ##


假設在一個組播環境中有三台伺服器同時發送某直播流量，組員無法選擇要接收哪台伺服器的流量，只能選擇是否接收

## Source-specific Multicast ##

假設在一個組播環境中有三台伺服器同時發送某直播流量，組員可以選擇要接收哪一台伺服器的組播，和哪些伺服器的流量不要接收


## IGMPv1 ##

**Membership Query** 查詢有哪些成員要接收組播流量，使用224.0.0.1(所有host、Router)，查詢間隔為預設為60秒

**Membership Report** 回復Query，不響應的終端即不加入組播，當一台設備加入組播時也會主動發送Report

**無離組手段，需等待超時**

**IGMPv1封包格式**

<table>
  <tr>
    <th>Version</th>
    <th>Type</th>
    <th>Unused</th>
    <th>Checksum</th>
  </tr>
  <tr>
    <td colspan="4" align="center">Group Address</td>
  </tr>
</table>

**Version** : IGMP版本

**Type** 
  - 1為Query
  - 2為Report 

**Group Address** : 組播位置

## IGMPv2 ##

**Group-specific query** 

**Leave Group message** 離組信息，使用224.0.0.2(所有Router)

## IGMPv3 ##
