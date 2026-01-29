#简单请求 #复杂请求 #预检请求 #Options请求 

Review
1. 2021/02/27 16:03:20
2. 2022/09/10
3. 2023/01/28
2. 2024-10-15 21:56

> [!Summary]
> 

## 一、Introduction
**OPTIONS请求**，也称为**预检请求**，是一种HTTP请求方法，主要用于检测服务器允许的HTTP方法。

- **安全:** 防止恶意跨域请求对服务器造成损害。
- **控制:** 允许服务器对跨域请求进行更细粒度的控制。

##### 触发 OPTIONS 请求的场景
- **跨域请求(CORS)：** 当浏览器发起跨域请求时，为了防止跨站脚本攻击（XSS）等安全问题，浏览器会采取一些安全措施，其中之一就是发送 OPTIONS 请求，来询问服务器是否允许该跨域请求。
- **复杂请求：** 除了跨域，如果一个请求满足以下所有条件，则被视为复杂请求，需要进行预检：
	1. 请求方法是 `GET`、`HEAD` 之外的 (`POST`, `PUT`, `DELETE` )
	2. 请求头中包含*自定义的头部字段* 
	3. 请求包含一个 `Content-Type` 头信息，且其值不是 `application/x-www-form-urlencoded`、`multipart/form-data` 或 `text/plain` 

默认请求头字段（不含自定义头部）
- Accept
- Accept-Language
- Content-Language
- Content-Type
- DPR
- Downlink
- Save-Data
- Viewport-Width
- Width


请求示例
```http
OPTIONS /api/data HTTP/1.1
Origin: http://example.com
Access-Control-Request-Method: POST
Access-Control-Request-Headers: Content-Type
```

响应示例
```http
HTTP/1.1 200 OK
Access-Control-Allow-Origin: http://example.com
Access-Control-Allow-Methods: POST, GET, OPTIONS
Access-Control-Allow-Headers: Content-Type
Access-Control-Max-Age: 3600
```

- Access-Control-Allow-Origin: 指定允许跨域访问的源。可以使用`*` 表示允许所有源，也可以指定具体的域名或IP。
- Access-Control-Allow-Methods: 指定允许的HTTP方法，例如POST、GET、PUT、DELETE等。
- Access-Control-Allow-Headers: 指定允许的请求头。
- Access-Control-Max-Age: 指示预检请求的结果可以缓存多久（以秒为单位）。浏览器通常有一个默认值，需要取服务器设置的和浏览器默认的最小值。没有过期之前针对同一个请求只会发送一次预检请求
- Access-Control-Expose-Headers: 指定哪些响应头可以被JavaScript代码读取（`getAllResponseHeaders()` `getResponseHeader('')`）。
- Access-Control-Allow-Credentials: true

> 对于附带身份凭证的请求，服务器不得设置 `Access-Control-Allow-Origin=*` 。携带凭证的请求，浏览器端需要额外配置 
> - XHR请求： `xhr.withCredentials=true`
> - Fetch请求：`fetch(url, {credentials: 'include' })` 
> `fetch` 请求的 `credentials` 有3个可选值 `omit`, `same-origin` *default*, `include` 

##### 简单请求
1. 请求中的任意 XMLHttpRequestUpload 对象均没有注册任何事件监听器 (*未验证*)
	XMLHttpRequestUpload 对象可以使用 XMLHttpRequest.upload 属性访问
2. 请求中没有使用 ReadableStream 对象 (*未验证*)


> [!Warning] 注意
> 对于**跨域**==简单请求==，有一些限制，非跨域简单请求不受影响
> 1. 不能使用 `setRequestHeader()` 设置自定义头部
> 2. 默认不能发送和接收 `cookie`，需要配置 `withCredentials` 和 `Access-Control-Allow-Credentials` .
> 3. `getAllResponseHeaders()` 方法始终返回空字符串
> 

##### 为什么 POST 请求会触发 OPTIONS (预检) 请求？
**OPTIONS 请求（预检请求）** 主要目的是检测服务器是否允许跨域请求，以及允许哪些 HTTP 方法、头部字段等。


###### 为什么需要 OPTIONS 请求？
- **安全：** OPTIONS 请求可以帮助服务器提前了解客户端的意图，从而更好地控制访问权限。
- **避免潜在的攻击：** 通过预检，可以防止恶意请求对服务器造成损害。




## Reference

