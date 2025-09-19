# BFD Down #

如果遇到設備Health為紅色叉叉時，有可能是BFD Session沒有起來，可以使用以下命令清除讓他重建BFD

```bash
clear sdwan bfd transition 
```