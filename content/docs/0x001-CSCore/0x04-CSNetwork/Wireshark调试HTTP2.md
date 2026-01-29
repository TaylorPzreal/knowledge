
Review
1. 2024-10-26 07:37

> [!Summary]
> 

## 一、Introduction

1、安装 Wireshark
2、配置 `SSLKEYLOGFILE` 环境变量
3、启动Wireshark，配置 TLS `sslkey.log` 地址
4、启动 Chrome 浏览器，并打开目标网站

```sh
export SSLKEYLOGFILE=~/sslkey.log
```

```sh
open /Applications/Google\ Chrome.app
```


过滤 Wireshark 消息
```txt
http2 && (ip.dst == 60.222.11.204 || ip.src == 60.222.11.204)
```


## Reference

