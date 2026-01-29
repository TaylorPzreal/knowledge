
Review
1. 2024-10-03 17:51

> [!Summary]
> 

## 一、Introduction

```js
const { Resolver } = require('node:dns');
const resolver = new Resolver();
resolver.setServers(['4.4.4.4']);

// This request will use the server at 4.4.4.4, independent of global settings.
resolver.resolve4('example.org', (err, addresses) => {
  // ...
});
```


```js
const dns = require('node:dns');

// 解析域名，获取 IPv4 地址
dns.lookup('www.example.com', (err, address, family) => {
  if (err) {
    console.error('DNS lookup failed:', err);
  } else {
    console.log('address: %j family: IPv%s', address, family);
  }
});

// 解析域名，获取 IPv4 地址
dns.resolve4('www.example.com', (err, addresses) => {
  if (err) {
    console.error(err);
  } else {
    console.log('addressv4: %j', addresses);
  }
});

dns.resolve6('www.example.com', (err, addresses) => {
  if (err) {
    console.error(err);
  } else {
    console.log('addressv6: %j', addresses);
  }
});


// 解析 MX 记录
dns.resolveMx('example.com', (err, addresses) => {
  if (err) {
    console.error(err);
  } else {
    addresses.forEach((record) => {
      console.log('ms', record.exchange, '--', record.priority);
    });
  }
});
```


- `dns.resolve(hostname[, rrtype], callback)` 
- `dns.reverse(ip, callback)`: 根据 IP 地址反向解析域名。
- `dns.setServers(servers)`: 设置 DNS 服务器。
- `dns.getServers()` Returns an array of IP address strings


## Punycode
Punycode 是一种编码方案，主要用于将包含非 ASCII 字符（如中文、日文等）的域名转换为 ASCII 字符，以便在 DNS 系统中使用。因为 DNS 系统最初是为英文域名设计的，只能处理 ASCII 字符。

[punycode.js](https://github.com/mathiasbynens/punycode.js) 

```sh
npm install punycode --save
```

> ⚠️ Note that userland modules don't hide core modules. For example, `require('punycode')` still imports the deprecated core module even if you executed `npm install punycode`. Use `require('punycode/')` to import userland modules rather than core modules.

```js
const punycode = require('punycode/');

// 将 "你好，世界" 编码为 Punycode
const punycodeString = punycode.encode('你好，世界');
console.log(punycodeString); // 输出类似 xn--nihao-xld.com 的结果
```


##### Punycode 在 Node.js 中的应用场景
- **域名解析：** 在处理国际化域名时，需要将域名转换成 Punycode 格式，然后进行 DNS 查询。
- **URL 处理：** 在处理包含国际化域名的 URL 时，需要对域名部分进行编码和解码。
- **构建国际化应用：** 在构建支持多语言的应用时，需要处理用户输入的包含非 ASCII 字符的域名。



## Reference

