
Review
1. 2024-09-29 09:07

> [!Summary]
> 

## 一、Introduction

Cookie 属性
1. Secure
2. HttpOnly
3. Samesite

关cookie前缀的提案，其要求使用诸如 `__Secure` 开头的cookie名称，以给cookie默认添加Secure属性，从而防止此问题发生。


##### Samesite
标明这个 Cookie是个“同站 Cookie”，同站Cookie只能作为第一方Cookie，不能作为第三方Cookie

###### `Samesite=Strict`
严格模式，表明这个 Cookie 在任何情况下都不可能作为第三方 Cookie，绝无例外。

###### `Samesite=Lax`
宽松模式，比 Strict 放宽了点限制：假如这个请求是导航请求（改变了当前页面或者打开了新页面，通常是a标签，form表单get请求）且同时是个GET请求，则这个Cookie可以作为第三方Cookie。

###### 示例
`b.com` 设置了如下Cookie
```txt
Set-Cookie: foo=1; Samesite=Strict
Set-Cookie: bar=2; Samesite=Lax
Set-Cookie: baz=3
```

`a.com` 点击链接（`<a href="b.com" />`）进入 `b.com` 时，`foo` 这个 Cookie 不会被包含在 `b.com` 主请求 Cookie 中，但 `bar` 和 `baz` 会


## Reference

