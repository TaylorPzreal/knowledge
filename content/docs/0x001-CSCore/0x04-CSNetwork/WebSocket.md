

Review
1. 2024-09-28 08:20

> [!Summary]
> 

## 一、Introduction
2011/12/11 被 **RFC 6455** - The WebSocket Protocol 定为标准

全双工通信标准，WebSocket协议由IETF定为标准，WebSocket API由W3C定为标准。
优点：
1. 推送功能
2. 减少通信量（ws 首部信息很小）

通过HTTP协议升级为WebSocket协议：
Request
```HTTP
Upgrade: WebSocket
Connection: Upgrade
```

Response
```HTTP
HTTP/1.1 101 Switching Protocols
Upgrade: WebSocket
Connection: Upgrade
```


## Reference

