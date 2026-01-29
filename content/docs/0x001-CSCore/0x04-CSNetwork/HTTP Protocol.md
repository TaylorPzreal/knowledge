
Review
1. 2024-09-26 22:09

> [!Summary]
> HTTP <https://developer.mozilla.org/zh-CN/docs/Web/HTTP> 
> 超文本传输协议（HTTP）是一个用于传输超媒体文档（例如 HTML）的**应用层协议**。它是为 Web 浏览器与 Web 服务器之间的通信而设计的，但也可以用于其他目的。HTTP 遵循经典的**客户端—服务端模型**，客户端打开一个连接以发出请求，然后等待直到收到服务器端响应。HTTP 是无状态协议，这意味着服务器不会在两个请求之间保留任何数据（状态）。
> 
> HTTP is defined by these [IETF](https://ietf.org/) **RFCs** and [IANA](https://www.iana.org/) **registries**.
> The [IETF](http://www.ietf.org/) **HTTP Working Group** maintains and develops the Hypertext Transfer Protocol - the core protocol of the **World Wide Web**.


> [!Summary]
> 书籍推荐📚
> 1. 《图解HTTP》2014
> 2. 《HTTP权威指南》2012
> 3. 《TCP/IP详解》卷1：协议 2016
> 4. 《HTTP/2 in Action》
> 5. 《HTTPS权威指南》
> 6. 《解析QUIC/HTTP3：未来互联网的基石》2024/07
> 
> 在线学习平台
> 1. [MDN HTTP](https://developer.mozilla.org/zh-CN/docs/Web/HTTP) 
> 2. [HTTP Documentation](https://httpwg.org/specs/) 
> 3. [HTTP Extensions](https://httpwg.org/http-extensions/) 
> 4. RFC <https://datatracker.ietf.org/> 
> 5. HTTP-WG <https://httpwg.org/>
> 
> 必读资料
> 1. [How browsers work](https://web.dev/articles/howbrowserswork) 



> [!Warning] Core Specifications
> 
> The “core” semantics of the HTTP protocol are defined by:
> 
> - RFC 9110: [HTTP Semantics](https://httpwg.org/specs/rfc9110.html)
> - RFC 9111: [HTTP Caching](https://httpwg.org/specs/rfc9111.html)
> 
> Those semantics are expressed “on the wire” in three ways:
> 
> - RFC 9112: [HTTP/1.1](https://httpwg.org/specs/rfc9112.html) June 2022
> - RFC 9113: [HTTP/2](https://httpwg.org/specs/rfc9113.html) June 2022
> - RFC 9114: [HTTP/3](https://httpwg.org/specs/rfc9114.html) June 2022
> 
> Later versions of HTTP offer field compression:
> 
> - RFC 7541: [HPACK Header Compression for HTTP/2](https://httpwg.org/specs/rfc7541.html)
> - RFC 9204: [QPACK Field Compression for HTTP/3](https://httpwg.org/specs/rfc9204.html)
> 
> These RFCs collectively obsolete all preceding RFCs defining HTTP, including **RFC 1945**, **RFC 2068**, **RFC 2616**, **RFC 2617**, **RFC 7230-5**, and **RFC 7540**.


## 一、Introduction

##### Message Format
```txt
HTTP-message   = start-line CRLF
			   *( field-line CRLF )
			   CRLF
			   [ message-body ]
```

> start-line     = request-line / status-line

##### 请求
```http
请求行
消息头

消息体
```

##### 响应
```http
状态行
消息头

消息体
```

> 准确来说，响应消息体的格式会通过响应的消息头中的 `Content-Type` 字段来定义（MIME类型）。


##### Web服务器
1. Nginx
2. Apache/ApacheHTTPD
3. Apache Traffic Server
4. LiteSpeed
5. H2O
6. IIS
7. `nghttpd` 
8. NodeJS
9. Shimmercat
10. CaddyServer
11. HAProxy
12. HS
13. AWS ELB
14. LiteSpeed

##### 查看HTTP请求的工具
1. curl
2. wget
3. `httpie`
4. `nc` (`netcat`)
5. Wireshark
6. Fiddler
7. Chrome `net-internals`   <chrome://net-export/>  <chrome://net-internals/> <https://netlog-viewer.appspot.com/> 
8. Advanced REST Client
9. Postman
10. Rested
11. RESTClient
12. RESTMan
13. `nghttp` 基于 Firefox 实现


## Reference

