
Review
1. 2021/02/08
2. 2024-09-29 07:03

> [!Summary]
> CSRF攻击之所以能够成功，是因为它利用了Web应用程序的一个信任机制：浏览器发起的请求，会自动携带该域名下符合条件的 cookie 。只能使用Cookie不能获取。
> 
> 常用防御手段
> 1. 来源验证
> 2. SameSite
> 3. CSRF Token
> 4. 双重Cookie验证
> 5. 验证码验证
> 
> [CSRF Cheat Sheet](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.md) 
> 
> CSRF 检测
> 1. CSRFTester CSRF漏洞的测试工具
> 2. 网关监控

## 一、Introduction
CSRF/XSRF，全称Cross-Site Request Forgery（跨站请求伪造）。它是一种挟制用户在当前已登录的Web应用程序上执行非本意的操作的攻击方法。

> CSRF攻击可能导致未经用户同意的操作，如修改账户信息、进行转账等。

CSRF 可以是一个可以被存储型漏洞。 比如攻击者将攻击代码存储在被接受的 HTML 代码中就会导致存储型 CSRF（例如 `IMG` 或 `IFRAME` 标签）时。这意味着浏览该页面的任何人都可能受到影响。 该漏洞可以伪装成普通链接或隐藏在图像标签中。
```html
<img src=“malicious link” width=“0” height=“0” border=“0”>
```

```html
<a href=“malicious link”>Unsubscribe here</a>
```

### CSRF攻击的基本流程
1. 用户登录了一个受信任的网站 `a.com` 并获得了认证cookie。
2. 用户在不登出网站 `a.com` 的情况下访问了恶意网站 `b.com` 。
3. 恶意网站 `b.com` 向网站 `a.com` 发送一个请求 `a.com/api=xx` ，这个请求会自动带上用户在 `a.com` 网站的认证cookie。
4. 网站 `a.com` 接收到请求后，认为这是一个来自合法用户的有效请求，因此执行了相应的操作。

> 跨站请求可以用各种方式：图片URL、超链接、CORS、Form提交等等。部分请求方式可以直接嵌入在第三方论坛、文章中，难以进行追踪。

> CSRF通常是跨域的，因为外域通常更容易被攻击者掌控。但是如果本域下有容易被利用的功能，比如可以发图和链接的论坛和评论区，攻击可以直接在本域下进行，而且这种攻击更加危险。


为什么 `img`，`form` 可以自动携带cookie？
1. `Firefox-85.0.1` 跨域请求仍然会携带cookie
2. Chrome@76+增加了 `Sec-Fetch-*` 请求头支持，跨域不再携带目标域cookie

### CSRF攻击的危害
- **盗取用户信息：** 攻击者可以利用CSRF攻击盗取用户的敏感信息，如密码、银行卡号等。
- **非法转账：** 攻击者可以利用CSRF攻击进行非法转账，造成用户的经济损失。
- **篡改用户数据：** 攻击者可以利用CSRF攻击篡改用户的个人信息、订单信息等。

### 防御CSRF攻击常用方法
1. **同源检测**：验证 HTTP `Referer`, `Origin`, Header
2. **Cookie SameSite**：设置Cookie的SameSite属性为 `Strict` 或者 `Lax`，可以限制第三方的网站发送当前网站的Cookie。
3. **CSRF Token** 
4. **双重Cookie验证** 
5. 重要操作再次进行身份验证（验证码）
6. **使用Token：** 在每个请求的参数增加一个的token，并在服务器端验证这个token。token是根据一定的算法规则生成和验证的。
7. **自定义请求头：** 在请求头中加入一个自定义的参数，用于验证请求的合法性。
8. `X-Content-Type-Options: nosniff` 防止黑客上传HTML内容的资源（例如图片）被解析为网页。
9. 用户上传的图片，进行转存或者校验。不要直接使用用户填写的图片链接。
10. `Sec-Fetch-*` : `Sec-Fetch-Site` , `Sec-Fetch-Mode` , `Sec-Fetch-User` , `Sec-Fetch-Dest` 

> 如果Origin和Referer都不存在，并且没有使用随机CSRF Token作为第二次检查，建议直接进行阻止。

##### CSRF Token
要求所有的用户请求都携带一个CSRF攻击者无法获取到的Token。服务器通过校验请求是否携带正确的Token，来把正常的请求和攻击的请求区分开，也可以防范CSRF的攻击。

###### CSRF Token的防护策略分为三个步骤
1. 将CSRF Token输出到页面中（嵌入到表单、页面、或者HTTP Response 自定义Header或者Cookie(use SameSite Strict)中）
2. 页面提交的请求携带这个Token（query、Request Header）
3. 服务器验证Token是否一致

###### 放到 Request Header 中
可以使用如下请求头
-  `X-CSRF-Token` 
-  `X-XSRF-Token`  Angular 使用

###### 优点
- **有效性高：** 能够有效防止CSRF攻击，只要攻击者无法获取到正确的Token，就无法伪造用户的请求。
- **通用性强：** 适用于各种类型的Web应用。
- **易于实现：** 大多数Web框架都提供了内置的CSRF Token保护机制。

###### 缺点
- **开发成本：** 需要在前端和后端都进行相应的开发工作。
- **复杂性：** 相对于其他防御措施，实现CSRF Token的防护机制相对复杂一些。
- **用户体验：** 如果CSRF Token的生成和验证机制设计不合理，可能会影响用户体验。

> 由于使用Session存储，读取和验证CSRF Token会引起比较大的复杂度和性能问题，目前很多网站采用 *Encrypted Token Pattern* 方式。这种方法的Token是一个计算出来的结果，而非随机生成的字符串。这样在校验时无需再去读取存储的Token，只用再次计算一次即可。
> 
> 这种Token的值通常是使用UserID、时间戳和随机数，通过加密的方法生成。这样既可以保证分布式服务的Token一致，又能保证Token不容易被破解。


##### 双重Cookie验证
> 思路：利用CSRF攻击不能获取到用户Cookie的特点，可以要求Ajax和表单请求携带一个Cookie中的值，服务端通过请求参数和cookie中的值进行比较验证。

###### 流程
- 在用户访问网站页面时，向请求域名注入一个Cookie，内容为随机字符串（例如`csrfcookie=v8g9e4ksfhw`）。
- 在前端向后端发起请求时，取出Cookie，并添加到URL的参数中（`POST https://www.a.com/comment?csrfcookie=v8g9e4ksfhw`）。
- 后端接口验证Cookie中的字段与URL参数中的字段是否一致，不一致则拒绝。

*此方法并没有大规模应用，其在大型网站上的安全性还是没有CSRF Token高*

由于任何跨域都会导致前端无法获取Cookie中的字段（包括子域名之间），于是发生了如下情况：
- 如果用户访问的网站为`www.a.com`，而后端的api域名为`api.a.com`。那么在`www.a.com`下，前端拿不到`api.a.com`的Cookie，也就无法完成双重Cookie认证。
- 于是这个认证Cookie必须被种在`a.com`下，这样每个子域都可以访问。
- 任何一个子域都可以修改`a.com`下的Cookie。
- 某个子域名存在漏洞被XSS攻击（例如`upload.a.com`）。虽然这个子域下并没有什么值得窃取的信息。但攻击者修改了`a.com`下的Cookie。
- 攻击者可以直接使用自己配置的Cookie，对XSS中招的用户再向`www.a.com`下，发起CSRF攻击。

###### 优点：
- **简单易实现**：不需要引入额外的第三方库，无需使用Session，只需要前后端简单配置即可
- **通用性强：** 适用于各种类型的Web应用。
- **安全性高：** 结合SameSite属性，可以有效防止CSRF攻击。
- **性能开销小：** 相对于其他CSRF防护方案，性能开销较小，可以通过拦截器配置

###### 缺点：
- **依赖Cookie：** 如果浏览器禁用了Cookie，或者用户清理了Cookie，则该方案失效。通常 Cookie 中要增加额外的字段(`csrftoken=xxx` )。
- **容易被绕过：** 如果攻击者能够获取到用户的Cookie，仍然可以发起CSRF攻击。或者如果有其他漏洞（例如XSS），攻击者可以注入Cookie，那么该防御方式失效。
- 难以做到子域名的隔离。
- 为了确保Cookie传输安全，采用这种防御方式的最好确保用整站HTTPS的方式，如果还没切HTTPS的使用这种方式也会有风险。

## Reference
[前端安全系列（二）：如何防止CSRF攻击？](https://tech.meituan.com/2018/10/11/fe-security-csrf.html) 
[Prevent Cross-Site Request Forgery (CSRF) Attacks](https://auth0.com/blog/cross-site-request-forgery-csrf/) 
[Cross Site Request Forgery (CSRF)](https://owasp.org/www-community/attacks/csrf) 
[Reviewing Code for Cross-Site Request Forgery Issues](https://owasp.org/www-project-code-review-guide/reviewing-code-for-csrf-issues) 
[OWASP Code Review Guide](https://owasp.org/www-project-code-review-guide/) 
