
Review
1. 2020/04/17
2. 2024-09-29 08:36

> [!Summary]
> CSP 的本质是建立一个白名单，告诉浏览器哪些外部资源可以加载和执行，从而防止恶意代码的注入攻击。
> 
> [MDN CSP](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/CSP) 
> 
> 1. CSP 是一种主动防御机制，可以提前*预防 XSS 攻击*
> 2. CSP 提供了丰富的指令，可以灵活配置各种安全策略

## 一、Introduction
**CSP(Content Security Policy)**，即 **内容安全策略**，是一种安全机制，用于缓解包括跨站脚本（XSS）和数据注入攻击等多种类型的攻击。通过CSP，我们可以明确地告诉浏览器，哪些外部资源可以加载和执行，从而限制恶意代码的注入。

### CSP 的核心思想
- **白名单机制：** CSP 采用白名单的方式，开发者明确指定哪些来源的资源是可信的。
- **浏览器强制执行：** 浏览器会严格按照 CSP 的规则来加载和执行资源，拒绝加载来自未授权来源的资源。
- **防御 XSS 攻击：** CSP 的主要目的就是防止 XSS 攻击，通过限制可执行脚本的来源，有效地阻止恶意代码的执行。

### CSP 的作用
- **防止 XSS 攻击：** 这是 ==CSP 最重要的作用==。通过限制脚本的来源，可以有效地防止攻击者注入恶意脚本。
- **保护用户数据：** 防止敏感数据被恶意脚本窃取。
- **提高网站安全性：** CSP 是 Web 安全的重要一环，可以显著提高网站的安全性。

### CSP 的配置
1. 通过 HTTP Response Header `Content-Security-Policy` 配置
2. 通过 HTML `meta` 标签配置

```HTTP
Content-Security-Policy: default-src 'self'; script-src 'self' https://example.com;
```

```HTML
<meta
  http-equiv="Content-Security-Policy"
  content="default-src 'self'; img-src https://*; child-src 'none';" />

```
**
- `default-src 'self';`：默认情况下，只允许加载来自本站的资源。
- `script-src 'self' https://example.com;`：允许加载来自本站和 `https://example.com` 的脚本

#### CSP 的常用指令
- `default-src`：设置默认的源列表，如果其他指令没有覆盖，则使用该列表。
- `script-src`：指定允许加载脚本的源。
- `style-src`：指定允许加载样式表的源。
- `img-src`：指定允许加载图片的源。
- `media-src`: 
- `child-src`: 
- `font-src`: 
- `manifest-src`: 
- `object-src`: 
- `worker-src`: 
- `frame-ancestors`：指定允许嵌入当前页面的源。

### CSP 的局限性
- **配置复杂：** CSP 的配置比较复杂，需要仔细考虑各种安全需求。
- **性能影响：** 过度严格的 CSP 配置可能会影响网站的性能。

## Reference
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy
https://developer.mozilla.org/en-US/docs/Web/API/HTMLOrForeignElement

