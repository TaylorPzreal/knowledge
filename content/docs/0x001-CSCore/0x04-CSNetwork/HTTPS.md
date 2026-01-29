
Review
1. 2020/07/13
2. 2024-09-28 11:31

> [!Summary]
> HTTPS（HTTP Secure，超文本传输安全协议）
> HTTPS=HTTP+加密+认证+完整性保护
> HTTPS=HTTP+SSL/TLS
> 默认端口 443
> 
> IETF以 `SSL3.0` 为基准，制定了 TLS1.0, TLS1.1, TLS1.2, TLS1.3
> TLS是以 `SSL3.0` 为原型开发的协议
> TLS1.0, TLS1.1 不推荐使用
> 
> TLS1.3: <https://tools.ietf.org/html/rfc8446>
> TLS1.2: <https://tools.ietf.org/html/rfc5246>

## 一、Introduction
HTTPS不是新协议，只是HTTP通信接口部分用 *SSL* 或 *TLS协议* 代替而已。

HTTP不足
1. 通信使用ASCII明文（不加密）内容可能会被窃听
2. 不验证通信方的身份，可能遭遇伪装
3. 无法证明报文的完整性，有可能已遭篡改；中间人攻击（请求或响应在传输途中，遭攻击者拦截并篡改内容）


不验证通信方的身份就可能遭遇伪装：
- 无法确定请求发送至目标的Web服务器是否是按真实意图返回响应的那台服务器。有可能是已伪装的Web服务器。
- 伪装客户端
- 无法确定正在通信的对方是否具备访问权限
- 无法判定请求是来自何方，出自谁手。
- 即使是无意义的请求也会照单全手。无法阻止海量请求下的Dos共计（Denial Of Service，拒绝服务攻击）

操作系统默认的TLS库，在Linux下是OpenSSL，macOS下是LibreSSL，Windows下是SChannel。

### 加解密
加密处理方案
1. 通信加密
2. 内容加密（仍有被篡改的风险）

如何防止篡改？
- MD5
- SHA-1
- MAC（消息认证码）

HTTP协议确定报文完整性的方法，事实上并不便捷可靠。

SSL提供认证+加密处理+摘要功能；SSL是应用广泛的网络安全技术
SSL采用公开密钥加密的加密处理方式

共享密钥加密（也称为对称密钥加密）
加密和解密同用一个密钥的方式

公开密钥加密（也称为非对称加密）
使用一堆非对称的密钥，一把私有密钥，一把公有密钥。

HTTPS采用混合加密机制
在交换密钥环节使用公开密钥加密方式；建立通信交换报文阶段则使用共享密钥加密方式。

如何证明公开密钥本身是货真价实的公开密钥？
数字证书认证机构颁发的公开密钥证书
- 威瑞信（VeriSign）
- Let’s Encrypt

浏览器开发商发布新版本时，事先在内部植入常用认证机关的公开密钥。

HTTPS的问题
- 通信慢：SSL握手
- 增大了CPU使用率：加解密计算
- 不保护DNS查询（可通过DoH或DoT解决）
- 不隐藏IP地址和部分元数据
- 证书信任链的潜在问题


基本的运行过程
SSL/TLS协议的基本思路是采用公钥加密法，也就是说，客户端先向服务器端索要公钥，然后用公钥加密信息，服务器收到密文后，用自己的私钥解密。 

### 握手过程
> 先建立TCP连接，在建立TLS连接。

详见 [[HTTPS Handshake]] 

**TLS1.2建立连接过程**
1. Client Hello：包含 Client Random，客户端支持的加密套件，TLS Version等信息
2. Server Hello：选择的 TLS版本，选择的加密套件，Server Random；将证书下发给客户端；
	1. Certificate
	2. Server key Exchange
	3. Certificate Request
	4. Server Hello Done
3. Client Certificate
4. Client Key Exchange
5. Certificate Verify
6. Change Cipher Spec
7. Client Finished Message
8. Change Cipher Spec(server)
9. Server Finished Message

此后的所有通信都使用协商好的*对称加密算法和密钥*进行加密。
公钥私钥加密被称为非对称加密，因为它加密和解密消息时使用不同的密钥。这种类型的加密，在你连接到一个新的服务器时非常有必要，但它比较慢，所以这种加密方式用于协商一个对称加密的密钥，以便在创建连接之后使用对称密钥加密消息。

当HTTPS会话建立完成后，在同一个连接上的HTTP消息就不再需要这个协商过程了。类似地，后续的连接（不管是并发的额外连接，还是后来重新打开的连接）可以跳过其中的某些步骤 —— 如果它复用上次的加密密钥，这个过程就叫作 **TLS会话恢复**。

关键点：
- 非对称加密用于安全地交换生成对称密钥所需的信息
- 对称加密用于后续的实际数据传输，因为它更快、更高效
- 在 TLS 1.3 中，这个过程得到了简化，减少了往返次数

> 结合了非对称加密的安全性和对称加密的效率


## 验证网站 SSL 配置是否规范
- SSL Labs Test <https://www.ssllabs.com/ssltest/> 
- testssl <https://testssl.sh/>


## Reference
[[TLS-Transport Layer Security]]
[[HTTPS Handshake]]
