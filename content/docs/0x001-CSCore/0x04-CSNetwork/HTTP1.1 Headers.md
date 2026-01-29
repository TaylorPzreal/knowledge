
Review
1. 2020/07/13
2. 2024-09-27 07:55

> [!Summary]
> HTTP/1.1 RFC2626 定义了47种首部字段
> - 分为请求首部、响应首部、通用首部、实体首部、其他首部。
> - 逗号 `,` 分割多个值，分号 `;` 来配置参数，一般配置权重 `q=1.000;`（0≤q≤1）
> - 首部里面的时间数值单位都是**秒**

## 一、Introduction

##### 通用首部(9)

| 首部字段名                 | 说明                                                                                                                  |
| --------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Cache-Control         | 控制缓存的行为                                                                                                             |
| Connection            | 逐跳首部、连接的管理                                                                                                          |
| Date                  | 创建报文的日期时间                                                                                                           |
| Pragma(为向后兼容HTTP/1.0) | 要求所有中间服务器不返回缓存的资源；可直接使用：<br>Cache-Control:no-cache替换                                                                |
| Trailer               | 报文末端的首部一览；事先说明在报文主体后记录了哪些首部字段。可应用在分块传输编码时：<br>Transfer-Encoding: chunked<br>Trailer: Expires<br>…<br>Expires: date… |
| Transfer-Encoding     | 指定报文主体的传输编码方式，仅对分块传输编码有效（chunked）                                                                                   |
| Upgrade               | 升级为其他协议；需要配合Connection使用；<br>Upgrade: TLS/1.0<br>Connection: Upgrade                                                |
| Via                   | 代理服务器的相关信息；为了追踪传输路径；经常配合TRACE方法一起使用；                                                                                |
| Warning               | 错误通知；一般是缓存相关问题的警告；                                                                                                  |
|                       |                                                                                                                     |


##### 请求首部(19)

| 首部字段名                   | 说明                                                                                    |
| ----------------------- | ------------------------------------------------------------------------------------- |
| Accept                  | 用户代理（浏览器）可处理的媒体类型<br>application/json, text/plain                                     |
| Accept-Charset          | 优先的字符集                                                                                |
| Accept-Encoding         | 优先的内容编码；<br>gzip, compress, deflate, identity                                         |
| Accept-Language         | 优先的语言（自然语言）<br>zh-CN, zh;q=0.7, en-US                                                 |
| Authorization           | Web认证信息；<br>发生在客户端与服务器之间                                                              |
| Expect                  | 期待服务器的特定行为<br>Expect: 100-continue<br>等待状态码100响应的客户端，发生请求时，需要指定该请求头                   |
| From                    | 用户的电子邮箱地址                                                                             |
| Host                    | 请求资源所在的服务器                                                                            |
| If-Match                | 比较实体标记（ETag）<br>字段值与ETag值一致，才会执行请求；否则返回 `412 Precondition Failed`                     |
| If-Modified-Since       | 比较资源的更新时间<br>发生过更新之后，处理请求；否则返回 `304 Not Modified`                                     |
| If-None-Match           | 比较实体标记（与If-Match相反）字段值与ETag值不一致时返回200+新内容，一致时返回 `304 Not Modified`                    |
| If-Range                | 资源未更新时发送实体Byte的范围请求；配合Range；<br><br>若If-Range字段值（ETag值或时间）和请求资源的一致，则作为范围请求处理；否则返回全部资源 |
| If-Unmodified-Since     | 比较资源的更新时间（与If-Modified-Since相反）<br>未发生更新的情况下，处理请求；否则返回 `412 Precondition Failed`      |
| Max-Forwards            | 最大传输逐跳数<br><br>由于当Max-Forwards字段为0时，服务器就会立即返回响应；<br><br>主要用来排查代理服务器问题                 |
| Proxy-Authorization     | 代理服务器要求客户端的认证信息；发生在客户端与代理服务器之间；                                                       |
| Range                   | 实体的字节范围请求<br><br>处理返回206<br><br>无法处理范围请求返回200及全部资源                                    |
| Referer（正确拼写: Referrer） | 对请求中URI的原始获取方<br><br>即从哪个Web页面发起的                                                     |
| TE                      | 传输编码的方式及优先级；跟Accept-Encoding很像，但用于传输编码                                                |
| User-Agent              | HTTP客户端程序的信息<br><br>传达浏览器及用户代理名称等信息                                                   |

##### 响应首部(9)

| 首部字段名              | 说明                                                                                                              |
| ------------------ | --------------------------------------------------------------------------------------------------------------- |
| Accept-Ranges      | 是否接受字节范围请求，值为：<br><br>bytes，none                                                                                |
| Age                | 推算资源创建经过时间                                                                                                      |
| ETag               | 资源的匹配信息；资源的唯一性标识<br><br>强ETag：实体多么微小的变化都会改变其值<br><br>若ETag：只用于提示资源是否相同，只有发生根本改变产生差异时，才会改变ETag值，并且在字段值最开始处附加“W/” |
| Location           | 令客户端重定向至指定URI<br><br>主要配合3xx：Redirection的响应；浏览器会强制性尝试对Location指定的资源访问                                           |
| Proxy-Authenticate | 代理服务器对客户端要求的认证信息                                                                                                |
| Retry-After        | 对再次发起请求的时机要求；<br><br>常配合503或3xx Redirect使用<br><br>字段值可以是具体日期时间，也可以是创建响应后的秒数                                     |
| Server             | HTTP服务器的安装信息                                                                                                    |
| Vary               | 代理服务器缓存的管理信息<br><br>源服务器对代理服务器缓存控制                                                                              |
| WWW-Authenticate   | 服务器对客户端要求的认证信息                                                                                                  |

  

##### 实体首部字段(10)

| 首部字段名            | 说明                                        |
| ---------------- | ----------------------------------------- |
| Allow            | 资源可支持的HTTP方法；GET                          |
| Content-Encoding | 实体主体适用的编码方式：gzip                          |
| Content-Language | 实体主体的自然语言：zh-CN                           |
| Content-Length   | 实体主体的大小（单位：字节）                            |
| Content-Location | 替代对应资源的URI                                |
| Content-MD5      | 实体主体的报文摘要                                 |
| Content-Range    | 实体主体的位置范围                                 |
| Content-Type     | 实体主体的媒体类型<br><br>text/html; charset=utf-8 |
| Expires          | 实体主体过期的日期时间                               |
| Last-Modified    | 资源的最后修改日期时间                               |


非正式首部字段在 **RFC4229** HTTP Header Field Registrations中定义
- Cookie
- Set-Cookie

首部类型
- 端到端首部（End-to-end Header）：首部会转发给请求/响应对应的最终接收目标，且必须保存在由缓存生成的响应中，另外规定它必须被转发。
- 逐跳首部(Hop-by-hop Header)：只对单次转发有效，会因通过缓存或代理而不再转发。

Http/1.1中逐跳首部字段（8个），其他都是端到端首部：
1. Connection
2. Keep-Alive
3. Proxy-Authenticate
4. Proxy-Authorization
5. Trailer
6. TE
7. Transfer-Encoding
8. Upgrade

形如：`If-xxx` 这样的请求首部字段，都可称为==条件请求==。


> [!Summary] Connection vs Keep-Alive
> Connection 首部和 Keep-Alive 首部都是对存活检测（持续连接）进行控制的首部。Web浏览器需要在 Connection 首部中设置 `keep-alive` ，并将支持存活检测的信息传递给 Web 服务器。相应地，Web 服务器也同样会在 Connection 首部中设置 `keep-alive` 进行响应。同时，需要使用 Keep-Alive 首部在下一次请求到达之前传递超时时间（timeout指定）和该 TCP 连接中的剩余请求数（max 指令）等与存活检测相关的信息。此外，如果在 Connection 首部中设置 `close` ，就可以断开 TCP 连接。


`Connection` Header
**`Connection`** 通用标头控制网络连接在当前会话完成后是否仍然保持打开状态。如果发送的值是 `keep-alive`，则连接是持久的，不会关闭，允许对同一服务器进行后续请求。
- `close` 表明客户端或服务器想要关闭该网络连接，这是 HTTP/1.0 请求的默认值
- `keep-alive` 保持该网络连接打开

> 这个请求头列表由头部名组成，这些头将被第一个非透明的代理或者代理间的缓存所移除：这些头定义了发出者和第一个实体之间的连接，而不是和目的地节点间的连接。

`Keep-Alive` Header
需要将 `Connection` 首部的值设置为 "keep-alive" 这个首部才有意义
用来设置超时时长和最大请求数
```HTTP
Keep-Alive: timeout=5, max=1000
```
- `timeout`：即**Debounce**机制。指定了一个空闲连接需要保持打开状态的最小时长（以秒为单位）。需要注意的是，如果没有在传输层设置 keep-alive TCP message 的话，大于 TCP 层面的超时设置会被忽略。
- `max`：仅管道连接可用。在连接关闭之前，在此连接可以发送的请求的最大值。在非管道连接中，除了 0 以外，这个值是被忽略的，因为需要在紧跟着的响应中发送新一次的请求。HTTP 管道连接则可以用它来限制管道的使用。

##### 其他首部字段

| 首部字段名            | 说明                                                     |
| ---------------- | ------------------------------------------------------ |
| X-Frame-Options  | 目的：防止点击劫持攻击<br><br>DENY：拒绝<br><br>SAMEORIGIN：仅同源于名下的页面 |
| X-XSS-Protection | 控制浏览器XSS防护机制的开关<br><br>0:无效状态<br><br>1:有效状态            |
| DNT              | 请求首部；拒绝个人信息被收集；                                        |
| P3P              | 通过P3P技术，让Web网站个人隐私变成一种仅供程序可理解的形式，达到保护用户隐私目的。           |

##### 尾随首部
**尾随首部** 是 HTTP/1.1 协议中支持的一种机制，它允许在消息主体之后添加额外的首部字段。与普通的 HTTP 首部不同，尾随首部在消息主体传输完成后才发送，主要用于一些需要在消息主体传输完毕后才能确定其长度或者其他属性的场景。

###### 为什么需要尾随首部？
- **动态生成的内容长度:** 当消息主体的内容长度无法在发送前确定时，可以使用尾随首部来携带实际的内容长度。
- **压缩后的内容:** 对于压缩过的消息主体，在压缩完成后才能确定其最终大小，这时也需要使用尾随首部来表示。
- **分块传输编码:** 在使用分块传输编码时，每个块的结尾都会有一个尾随首部来表示该块的大小。

###### 尾随首部的使用场景
- **Chunked Transfer Encoding:** 分块传输编码是 HTTP/1.1 中引入的一种机制，它允许服务器将消息主体分成多个块，每个块都包含一个尾随首部来表示该块的大小。
- **HTTP/2:** 在 HTTP/2 中，尾随首部被更广泛地应用，用于携带一些在消息传输过程中动态生成的信息。

###### 尾随首部的格式
尾随首部的格式与普通的 HTTP 首部类似，由一个首部名称和一个值组成，两者之间用冒号分隔。

```HTTP
Trailer: Content-MD5
```

上面的示例表示在消息主体之后会跟随一个名为 `Content-MD5` 的尾随首部。


## 二、Header 详解
### 2.1: Referer Header
Referer，记录了该HTTP请求的来源地址。 对于Ajax请求，图片和script等资源请求，Referer为发起请求的页面地址。对于页面跳转，Referer为打开页面历史记录的前一个页面地址。

### 2.2: `Referrer Policy`
**`Referrer-Policy`** 首部用来控制哪些访问来源信息会在 `Referer` 中发送。应该被包含在生成的请求当中。

Referrer Policy 规定的 `Referer` 策略
```HTTP
Referrer-Policy: no-referrer
Referrer-Policy: no-referrer-when-downgrade
Referrer-Policy: origin
Referrer-Policy: origin-when-cross-origin
Referrer-Policy: same-origin
Referrer-Policy: strict-origin
Referrer-Policy: strict-origin-when-cross-origin
Referrer-Policy: unsafe-url
```

default is `strict-origin-when-cross-origin` 

> - **no-referrer:** 不会发送任何 Referer 信息。
> - **no-referrer-when-downgrade:** 在协议降级（例如从 HTTPS 访问 HTTP）时，不会发送 Referer 信息。
> - **origin:** 仅发送原始的 origin（协议、域名、端口）信息。
> - **origin-when-cross-origin:** 对于跨域请求，仅发送原始的 origin 信息；对于同源请求，发送完整的 URL。
> - **strict-origin:** 对于跨域请求，仅发送原始的 origin 信息；对于同源请求，发送完整的 URL，但*不包括查询字符串*。
> - **strict-origin-when-cross-origin:** 对于跨域请求，仅发送原始的 origin 信息；对于同源请求，发送完整的 URL，但*不包括片段标识*符（#）。
> - **unsafe-url:** 发送完整的 URL，包括协议、域名、端口、路径、查询字符串和片段标识符。

设置 `Referrer-Policy` 的方法有三种：
1. 在CSP设置
2. 页面头部增加meta标签
3. a标签增加 `referrerpolicy` 属性

`meta` 标签配置
```HTML
<meta name="referrer" content="origin" />
```

用 `<a>、<area>、<img>、<iframe>、<script> 或者 <link>` 元素上的 `referrerpolicy` 属性为其设置独立的请求策略。

```HTML
<a href="http://a.com" referrerpolicy="origin">Go</a>
```

```HTML
<a href="http://example.com" rel="noreferrer">…</a>
```

| Policy                                | Document                        | Navigation to                        | Referrer                        |
| ------------------------------------- | ------------------------------- | ------------------------------------ | ------------------------------- |
| **`strict-origin-when-cross-origin`** | `https://example.com/page.html` | `https://example.com/otherpage.html` | `https://example.com/page.html` |
| **`strict-origin-when-cross-origin`** | `https://example.com/page.html` | `https://mozilla.org`                | `https://example.com/`          |
| **`strict-origin-when-cross-origin`** | `https://example.com/page.html` | `http://example.org` *http protocol* | no referrer                     |
|                                       |                                 |                                      |                                 |

### 2.3: `X-Content-Type-Options`
`X-Content-Type-Options` 是一个HTTP响应头，它的主要作用是告诉浏览器：**不要对服务器返回的内容进行MIME类型嗅探**。强制浏览器严格按照服务器提供的Content-Type来处理内容，从而避免MIME类型嗅探带来的安全风险。

**MIME类型嗅探的风险：**
- 浏览器会根据内容本身来猜测MIME类型，而不是完全依赖服务器提供的Content-Type头。
- 这种行为可能导致安全风险，例如：
    - 将一个脚本文件误认为是文本文件，从而导致XSS攻击。
    - 将一个可执行文件误认为是图片文件，从而导致恶意代码执行。

**nosniff:** 告诉浏览器不要嗅探MIME类型，严格按照服务器提供的Content-Type来处理。这是最常用的值。


### 2.4: `Sec-Fetch-*`
`Sec-Fetch-*` 请求头是 HTTP 请求中的一组重要的元数据，它们可以帮助服务器更好地理解请求的意图，提高 Web 应用的安全性。

*`Sec-Fetch-*` 头部是浏览器自动添加的，不能被用户或脚本修改*

- **Sec-Fetch-Site:** 表示请求发起者的源与其目标源之间的关系：
    - `cross-site`：跨域请求
    - `same-origin`：同源请求
    - `same-site`：同站点请求
    - `none`：无
- **Sec-Fetch-Mode:** 指示请求的模式，常见的值有：
    - `navigate`：导航请求（例如，点击链接）
    - `same-origin`：同源请求
    - `cors`：跨域请求
    - `websocket`：WebSocket 请求
- **Sec-Fetch-Dest:** 指示请求的目标，常见的值有：
    - `document`：请求一个 HTML 文档
    - `empty`：请求一个空文档（例如，HEAD 请求）
    - `iframe`：请求一个 iframe
    - `image`：请求一个图片
    - `manifest`：请求一个 Web Manifest 文件
    - `object`：请求一个嵌入对象
    - `script`：请求一个脚本
    - `style`：请求一个样式表
    - `video`：请求一个视频
    - `worker`：请求一个 Worker


## Reference

