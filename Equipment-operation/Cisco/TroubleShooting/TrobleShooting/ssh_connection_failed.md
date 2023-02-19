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

## 或者將大部分算法都開啟(不建議，但是方便) ##

```bash
Host *
        KexAlgorithms curve25519-sha256@libssh.org,diffie-hellman-group14-sha1,ecdh-sha2-nistp256,ecdh-sha2-nistp384,diffie-hellman-group1-sha1,diffie-hellman-group-exchange-sha1,diffie-hellman-group-exchange-sha256
        HostKeyAlgorithms ecdsa-sha2-nistp256,ecdsa-sha2-nistp256-cert-v01@openssh.com,ecdsa-sha2-nistp384,ecdsa-sha2-nistp384-cert-v01@openssh.com,ecdsa-sha2-nistp521,ecdsa-sha2-nistp521-cert-v01@openssh.com,ssh-ed25519,ssh-ed25519-cert-v01@openssh.com,ssh-dss-cert-v01@openssh.com,ssh-rsa,ssh-rsa-cert-v01@openssh.com
        PubkeyAcceptedKeyTypes ecdsa-sha2-nistp256,ecdsa-sha2-nistp256-cert-v01@openssh.com,ecdsa-sha2-nistp384,ecdsa-sha2-nistp384-cert-v01@openssh.com,ecdsa-sha2-nistp521,ecdsa-sha2-nistp521-cert-v01@openssh.com,ssh-ed25519,ssh-ed25519-cert-v01@openssh.com,ssh-dss-cert-v01@openssh.com,ssh-rsa,ssh-rsa-cert-v01@openssh.com
        Ciphers aes128-ctr,aes128-gcm@openssh.com,aes192-ctr,aes256-ctr,chacha20-poly1305@openssh.com,aes128-cbc,3des-cbc
```

## Reference ##

預設SSH支援演算法

https://privx.docs.ssh.com/docs/supported-ssh-key-exchange-algorithms


