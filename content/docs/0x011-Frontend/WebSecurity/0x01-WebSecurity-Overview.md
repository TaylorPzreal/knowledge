

#Security #Web攻击技术 #CommonAttacks #网络安全 

Review
1. 2020/09/22
2. 2021/02/07 16:29:50
3. 2024/03/01
4. 2024-08-11


> [!Summary]
> OWASP Cheat Sheet Series <https://github.com/OWASP/CheatSheetSeries>  
> Github [OpenSource Security](https://github.com/CaledoniaProject/awesome-opensource-security) 


> [!Summary] 主要攻击
> 1. XSS (Cross-Site Scripting)
> 2. CSRF (Cross-Site Request  Forgeries)
> 3. SQL Injection
> 4. Clickjacking（点击劫持）


> [!Summary] CTFs (Capture the Flag)
> 1. HackTheBox <https://www.hackthebox.com/>
> 2. TryHackMe <https://tryhackme.com/>
> 3. VulnHub <https://www.vulnhub.com/>
> 4. picoCTF <https://picoctf.org/>
> 5. SANS Holiday Hack Challenge <https://www.sans.org/mlp/holiday-hack-challenge-2023/>
> 


针对Web的攻击对象：
1. 服务器
2. 客户端
3. Web应用（大多是此）


针对Web应用的攻击模式
- 主动攻击（active attack）：攻击者通过直接访问Web应用，把攻击代码传入的攻击模式。主要攻击服务器上的资源；代表性攻击是SQL注入攻击和OS命令注入攻击。
- 被动攻击（passive attack）：利用圈套策略（诱使触发设置的陷阱）执行攻击代码的攻击模式。主要攻击用户的资源和权限；代表性攻击是跨站脚本攻击和跨站点请求伪造。


## 一、根据攻击原因分类
### **1）因输出值转义不完全引发的安全漏洞**

> [!Seccuss] 安全对策：
> - 客户端验证
> - 服务器验证
> - 输入值验证
> - 输出值转义
> 
> 保留客户端验证只是为了尽早地辨识输入错误，起到提高UI体验的作用。
> 输入值验证通常是指检查是否是符合系统业务逻辑的数值或检查字符编码等预防对策。
> 针对输出做值转义处理是一项至关重要的安全策略。

#### 1: 跨站脚本攻击
`Cross-Site Scripting, XSS`
详见 [[0x04-XSS]] 
攻击者将恶意脚本注入到网页中，当用户访问该网页时，恶意脚本就会在用户的浏览器中执行，从而窃取用户的信息或控制用户的行为。

*XSS是攻击者利用预先设置的陷阱触发的被动攻击*

#### 2: SQL注入攻击
`SQL Injection`
> SQL 注入攻击指的是攻击者在 HTTP 请求中注入恶意的 SQL 代码，服务器使用参数构建数据库 SQL 命令时，恶意 SQL 被一起构造，破坏原有 SQL 结构，并在数据库中执行，达到编写程序时意料之外结果的攻击行为。

是指针对Web应用使用的数据库，通过运行非法的SQL而产生的攻击。

影响
- 非法查看或篡改数据库内的数据
- 规避认证
- 执行和数据库服务器业务关联的程序

**防护:**
- **参数化查询:** 使用参数化查询可以有效防止SQL注入。
- **输入验证:** 对所有用户输入进行严格过滤和验证。
- **最小权限原则:** 数据库用户应只拥有执行必要操作的权限。

#### 3: OS命令注入攻击
`OS Command Injection`
通过Web应用，执行非法的OS命令达到攻击的目的。
能调用Shell函数的地方，就存在被攻击的风险。

#### 4: HTTP首部注入攻击
`HTTP Header Injection` 
攻击者通过在*响应首部字段*内插入换行，添加任意响应首部或主体的一种被动攻击。

向首部主体内添加内容的攻击，称为HTTP响应截断攻击（HTTP Response Splitting Attack）

影响
- 设置任何Cookie信息
- 重定向至任意URL
- 显示任意的主体（HTTP响应截断）

`%0D%0A` 代表HTTP报文中的换行符；
`%0D%0A%0D%0A` 作为HTTP首部与主体分割所需的空行，就可以接伪造的主体了

#### 5: 缓存污染
滥用HTTP/1.1中*汇集多响应*返回功能，会导致缓存服务器对任意内容进行缓存操作。

**HTTP/1.1 汇集多响应返回** 的核心思想是，服务器可以在*单个TCP连接中发送多个HTTP响应*。这在理论上可以提高传输效率，但如果被恶意利用，则可能导致严重的安全问题。

##### 攻击原理
攻击者可以通过以下方式滥用这一特性：
1. **构造恶意请求：** 攻击者精心构造HTTP请求，在其中包含多个URL，这些URL指向不同的资源，包括恶意脚本、广告或其他有害内容。
2. **诱骗服务器合并响应：** 攻击者利用服务器的漏洞或配置不当，诱使服务器将多个响应合并成一个，并将其缓存。
3. **用户访问被污染的缓存：** 当其他用户访问同一个URL时，他们会得到被污染的响应，从而遭受攻击。

攻击者通过向缓存服务器发送精心构造的请求，将恶意内容注入到缓存中。当用户访问被攻击的网站时，他们的浏览器会从缓存中获取被污染的页面，从而导致各种安全问题。

#### 6: 邮件首部注入攻击
`Mail Header Injection` 
Web应用中的邮件发送功能，攻击者通过向邮件首部`To`或`Subject`内任意添加非法内容发起的攻击。

利用存在安全漏洞的Web网站，可对任意邮件地址发送广告邮件或病毒邮件。

利用 `%0D%0A`；

#### 7: 目录遍历攻击
`Directory Traversal` 
对本无意公开的文件目录，通过非法截断其目录路径后，达成访问目的的一种攻击。

**防护:**
- **输入验证:** 对用户输入的文件路径进行严格验证。
- **禁止目录列表:** 禁止服务器列出目录内容。

#### 8: 远程文件包含漏洞
`Remote File Inclusion` 
是指当部分脚本内容需要从其他文件读入时，攻击者利用指定外部服务器的URL充当依赖文件，让脚本读取之后，就可以运行任意脚本的一种攻击。

主要是PHP存在的安全漏洞。

**防护:**
- **白名单机制:** 只允许包含白名单中的文件。
- **输入过滤:** 对包含的文件路径进行严格过滤。

### **2）因设置或设计上的缺陷引发的安全漏洞**
#### 9: 强制浏览
`Forced Browsing` 
从安置在Web服务器的公开目录下的文件中，浏览那些原本非自愿公开的文件。
影响
- 泄露顾客的个人信息等重要情报
- 泄露原本需要具有访问权限的用户才可查阅的信息内容
- 泄露未外连到外界的文件

Web网页文本内容具有访问对象的控制，但不具备对图片访问对象的控制，从而产生了安全漏洞。

#### 10: 不正确的错误消息处理
`Error Handing Vulnerability` 
Web应用的错误信息内包含对攻击者有用的信息

Web主要错误信息：
- Web应用抛出的错误信息
- 数据库等系统抛出的错误信息：PHP或ASP等脚本错误；数据库或中间件的错误；Web服务器的错误；

> Web应用不必在用户的浏览画面上展现详细的错误消息。

#### 11: 开放重定向
`Open Redirect` 
是一种对指定的任意URL作重定向跳转的功能。
假如指定的重定向URL到某个具有恶意的Web网站，那么用户就会被诱导至那个Web网站。

### **3）因会话管理疏忽引发的安全漏洞**

#### 12: 会话劫持
`Session Hijack` 
攻击者通过某种手段拿到了用户的会话ID，并使用此会话ID伪装成用户，达到攻击的目的。

获得会话ID的途径：
- 通过非正规的生成方法推测会话ID
- 通过窃听或XSS攻击盗取会话ID
- 通过会话固定攻击（Session Fixation）强行获取会话ID

**防护:**
- **HTTPS:** 使用HTTPS加密传输，保护会话ID不被窃听。
- **会话超时:** 设置较短的会话超时时间。
- **会话固定防护:** 防止攻击者固定会话ID。

#### 13: 会话固定攻击
`Session Fixation` 
强制用户使用攻击者指定的会话ID，属于被动攻击。

#### 14: 跨站点请求伪造
`Cross-Site Request Forgeries, CSRF` 
详见 [[0x05-CSRF]] 

攻击者通过设置好的陷阱，强制对已完成认证的用户进行非预期的个人信息或设定信息等某些状态更新，属于被动攻击。

影响
- 利用已通过认证的用户权限更新设定信息等
- 利用已通过认证的用户权限购买商品
- 利用已通过认证的用户权限在留言板上发表言论

### **4）其他安全漏洞**

#### 15: 密码破解攻击
`Password Cracking`
即算出密码，突破认证。

##### 攻击方式
- 穷举法（Brute-force Attack，暴力破解法）：是指对所有密钥集合构成的密钥空间（Keyspace）进行穷举。
- 字典攻击：利用事先收集好的候选密码，枚举字典中的密码，尝试通过认证的一种攻击方法。
- 彩虹表（Rainbow Table）彩虹表是一种预先计算好的密码哈希值查找表，黑客通过查询彩虹表，可以快速找到与目标密码对应的哈希值。
- 社会工程学攻击: 黑客通过各种手段，如钓鱼邮件、电话诈骗等，诱骗用户泄露密码。
- 加密算法的漏洞

#### 16: 点击劫持
`Clickjacking` 
利用透明的按钮或链接做成陷阱，覆盖在Web页面之上。诱使用户在不知情的情况下，点击那个链接访问内容的一种攻击手段。

又称为界面伪装（UI Redressing）

**防御**
可以在 http 响应头中设置 `X-FRAME-OPTIONS` 来防御用 iframe 嵌套的点击劫持攻击。通过不同的值，可以规定页面在特定的一些情况才能作为 iframe 来使用。

1. `X-FRAME-OPTIONS` 机制
	- `DENY`：任何网页都不能使用iframe载入该网页
	- `SAMEORIGIN`：符合同源策略的网页可以使用iframe载入该网页
2. 使用 FrameBusting 代码：前端JS检测、阻止载入。如果浏览器禁用了JavaScript功能，则该办法失效。
3. 使用认证码认证用户：重要事件，再次通过认证码等方式确认


#### 17: DoS攻击
> Denial of Service attack，服务停止攻击，拒绝服务攻击

是一种让运行中的服务呈停止状态的攻击。DoS攻击不仅限于Web，还包括网络设备及服务器等。

DoS攻击方式：
- *集中利用访问请求造成资源过载*，资源用尽的同时，实际上服务也就呈停止状态。
- 通过攻击安全漏洞使服务停止

多台计算机发起的DoS攻击称为 **DDoS攻击**（Distributed Denial of Service attack）即分布式拒绝服务攻击。

#### 18: 后门程序
`Backdoor`
开发设置的隐藏入口，可不按正常步骤使用受限功能。

类型
- 开发阶段作为Debug调用的后门程序
- 开发者为了自身利益植入的后门程序
- 攻击者通过某种方法设置的后门程序

#### 19: SSRF
服务器端请求伪造(SSRF) 操纵服务器发送恶意请求到内部网络或其他外部系统。

SSRF漏洞的产生通常是因为服务器端提供了从其他服务器获取数据的功能，但是却没有对目标地址进行严格的过滤和限制。比如，一个网站允许用户输入一个URL地址，然后将该URL地址对应的网页内容显示出来，如果没有对这个输入的URL地址进行过滤，那么攻击者就可以构造一个恶意的URL地址，让服务器去访问其他内部系统。

#### 20: WebShell攻击
**WebShell**，通俗来说就是网站的后门。攻击者通过各种手段（比如SQL注入、文件上传漏洞等）将一段恶意脚本（通常是ASP、PHP、JSP等）上传到网站服务器上，这个脚本就相当于一个后门，攻击者可以通过它远程控制服务器。

#### 21: 内网渗透
- **未经授权的内网渗透** 属于违法行为，是一种攻击。
- **授权的渗透测试** 是一种防御性的行为，目的是为了提升系统的安全性。

#### 22: 中间人攻击
**中间人攻击** 是一种网络攻击方式，攻击者在两个通信端之间插入自己，并同时与两端分别建立独立的联系，使通信的两端认为他们正在通过一个私密的连接与对方直接对话，但实际上整个会话都被攻击者完全控制。

##### 中间人攻击的常见场景
- **公共Wi-Fi:** 公共Wi-Fi网络安全性较低，容易受到中间人攻击。
- **钓鱼网站:** 攻击者通过伪造网站，诱导用户输入账号密码。
- **DNS欺骗:** 攻击者通过修改DNS服务器的记录，将用户引导到虚假的网站。
- **SSL/TLS劫持:** 攻击者通过劫持SSL/TLS连接，窃取加密数据。

#### 23: 零日漏洞攻击
介绍：
- **未知且未修复的漏洞:** 零日漏洞是指软件或硬件中存在的安全漏洞，但该漏洞还没有被软件开发商或硬件制造商发现并修复。也就是说，在这个漏洞被公开之前，没有任何补丁或更新可以用来修补这个漏洞。
- **攻击者先知先觉:** 由于漏洞是未知的，所以软件或硬件的使用者并不知道自己正在使用存在安全风险的产品。而攻击者一旦发现并利用了这个漏洞，就可以在软件厂商发布补丁之前，对系统发起攻击。
- **高危威胁:** 由于零日漏洞是未知的，所以传统的安全防护措施往往无法有效防范。攻击者可以利用这个漏洞进行各种恶意活动，比如窃取敏感数据、控制系统、甚至发起大规模的网络攻击。

##### 如何防范零日漏洞
- **及时更新系统:** 始终保持操作系统、应用程序和软件的更新，以便及时修复已知的漏洞。
- **使用安全软件:** 安装可靠的安全软件，如杀毒软件和防火墙，可以提供一定的保护。
- **谨慎点击链接:** 不要点击来自未知来源的链接或下载附件，以免感染恶意软件。
- **加强网络安全意识:** 提高员工的网络安全意识，让他们了解常见的网络攻击手段和防范措施。


## 二、安全检查
1. 使用网站检查工具进行检查：web-check
2. 代码审计：代码审计(JS source code analyzer)


## 参考
1. 《图解HTTP》
2. OWASP Top 10 - 2021 <https://owasp.org/Top10/> 
3. OWASP Top Ten: [https://owasp.org/www-project-top-ten/](https://owasp.org/www-project-top-ten/)
4. 7 Common Front End security attacks [https://dev.to/tinymce/7-common-front-end-security-attacks-372p](https://dev.to/tinymce/7-common-front-end-security-attacks-372p)
5. unicode domains: https://www.vgrsec.com/post20170219.html
6. How I found a $5,000 Google Maps XSS (by fiddling with Protobuf) – Medium: https://medium.com/@marin_m/how-i-found-a-5-000-google-maps-xss-by-fiddling-with-protobuf-963ee0d9caff
7. ECMAScript 6 from an Attacker's Perspective - Breaking Frameworks, Sa...: https://www.slideshare.net/x00mario/es6-en
8. Phishing with Unicode Domains - Xudong Zheng: https://www.xudongz.com/blog/2017/idn-phishing/
9. qazbnm456/awesome-web-security: 🐶 A curated list of Web Security materials and resources.: https://github.com/qazbnm456/awesome-web-security#practices-aws
10. alert(1) to win: https://alf.nu/alert1
11. prompt(1) to win - 0x0: http://prompt.ml/0
12. 浅谈Web客户端追踪 - FreeBuf.COM | 关注黑客与极客: http://www.freebuf.com/articles/web/127266.html
13. "alert(1) to win" writeup - kngxscn - 博客园: http://www.cnblogs.com/renzongxian/p/5617551.html
14. escape.alf.nu XSS挑战赛writeup | 乘物游心: https://blog.spoock.com/2016/03/10/escape-alf-nu-xss-challenges-writeups/
15. 一次较为深刻的CSRF认识: https://m.2cto.com/article/201505/400902.html
