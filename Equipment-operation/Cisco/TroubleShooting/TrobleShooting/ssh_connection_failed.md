# ssh connection failed #

>在使用Windows cmd或者Linux的terminal進行SSH遠端連線Cisco設備時，可能會出現加密方式錯誤的訊息

## 解決方式 ##

## 較好 ##

將Cisco設備加密演算法強度調高

```bash
#查看ssh使用的算法
show ip ssh 

```

## 較差 ##

錯誤訊息:

Unable to negotiate with 192.168.1.100 port 22: no matching key exchange method found. Their offer: diffie-hellman-group1-sha1

更改~/.ssh/config並加入以下內容

```bash
Host *
    KexAlgorithms +diffie-hellman-group1-sha1
```

錯誤訊息

Unable to negotiate with 192.168.107.157 port 22: no matching cipher found. Their offer: aes128-cbc,3des-cbc,aes192-cbc,aes256-cbc

更改~/.ssh/config並加入以下內容

```bash
Host *
    Ciphers +aes256-cbc 
```

錯誤訊息

no matching host key type found. Their offer: ssh-rsa 

更改~/.ssh/config並加入以下內容

```bash
Host *
    HostKeyAlgorithms +ssh-rsa
    PubkeyAcceptedKeyTypes +ssh-rsa
```

## Reference ##

預設SSH支援演算法

https://privx.docs.ssh.com/docs/supported-ssh-key-exchange-algorithms


