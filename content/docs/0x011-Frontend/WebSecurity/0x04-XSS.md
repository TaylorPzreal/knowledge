
Review
1. 2021/02/07
2. 2024-09-29 07:03

> [!Summary]
> 1. 反射型和存储型攻击主要发生在 SSR 场景中
> 2. DOM型攻击主要发生在客户端，不需要服务器参与
> 3. 使用 `innerHTML` 插入内容，`script` 标签不会被执行，但是元素的事件仍然会被执行，如 `onerror="alert('xss')"`, `href="javascript:alert('xss')"`

## 一、Introduction
**XSS（Cross-Site Scripting）**，即跨站脚本攻击，是一种常见的网站应用程序安全漏洞。它允许恶意攻击者将恶意代码注入到网页上，当其他用户浏览该网页时，这些恶意代码就会在用户的浏览器中执行，从而达到攻击者的目的。

### XSS攻击原理
- **代码注入：** 攻击者通过各种方式（比如留言板、评论区、搜索框、富文本、注册登录表单等）将恶意脚本注入到网站中。
- **浏览器执行：** 当受害者访问包含恶意脚本的页面时，浏览器会将这些脚本视为正常代码并执行。
- **攻击达成：** 恶意脚本可以执行各种操作，比如窃取用户的Cookie、Session等敏感信息，修改页面内容，甚至控制用户的浏览器。

> XSS 的本质是因为网站没有对恶意代码进行过滤，与正常的代码混合在一起了，浏览器没有办法分辨哪些脚本是可信的，从而导致了恶意代码的执行。

### XSS攻击的分类
- **反射型XSS：** 攻击者将恶意脚本嵌入到*URL或表单数据*中，当用户点击链接或提交表单时，恶意脚本就会被服务器返回到浏览器执行。
- **存储型XSS：** 攻击者将恶意脚本*存储在服务器端*，比如数据库、文件系统等，当用户访问包含恶意脚本的页面时，恶意脚本就会从服务器端读取并执行（在客户端/服务端执行）。
- **DOM型XSS：** 攻击者利用DOM（文档对象模型）的漏洞，将恶意脚本*注入到页面的DOM*中，当页面渲染时，恶意脚本就会被执行。通过修改页面的DOM环境来实现攻击，而不直接依赖于服务器的响应。如通过URL获取数据，直接渲染到页面上。

### XSS攻击的危害
- **窃取用户信息：** 攻击者可以窃取用户的Cookie、Session等敏感信息，从而冒充用户进行各种操作。
- **篡改页面内容：** 攻击者可以修改页面内容，向用户展示虚假信息，或者进行钓鱼攻击。
- **传播恶意软件：** 攻击者可以利用XSS漏洞传播恶意软件，比如病毒、木马等。
- **破坏网站功能：** 攻击者可以利用XSS漏洞破坏网站的正常功能，导致网站崩溃或无法使用

### 如何防范XSS攻击
- **输入验证：** 对所有用户输入的数据进行严格的过滤和验证，禁止包含HTML标签、JavaScript代码等特殊字符。
- **输出编码：** 在将数据输出到页面之前，对数据进行适当的编码，防止恶意脚本被执行。`npm libs` : `xss` , `dompurify` 
- **内容安全策略（CSP）：** 使用CSP来限制浏览器加载的资源，防止恶意脚本从不受信任的来源加载。
- **框架和库：** 使用成熟的Web框架和库，它们通常内置了XSS防护机制。
- **定期安全扫描：** 定期对网站进行安全扫描，发现并修复潜在的XSS漏洞。
- Cookies：使用 `HttpOnly` 标志保护cookies


### Cheat Sheet
[Cross Site Scripting Prevention Cheat Sheet](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.md) 


### 攻击示例
#### 反射型攻击示例
```php
<?php
// search.php
?>
<!DOCTYPE html>
<html>
<head>
    <title>Search Results</title>
</head>
<body>
    <h1>Search Results</h1>
    <?php
    if(isset($_GET['query'])) {
        $search_query = $_GET['query'];
        echo "<p>You searched for: " . $search_query . "</p>";
        // 这里应该有搜索逻辑和结果显示
    }
    ?>
    <form action="search.php" method="get">
        <input type="text" name="query" placeholder="Enter search term">
        <input type="submit" value="Search">
    </form>
</body>
</html>
```

1. 正常情况下,用户可能会使用这样的URL进行搜索: `http://example.com/search.php?query=interesting+topic`
2. 服务器会接收这个查询，并在结果页面中显示搜索词。
3. 攻击者可以构造一个包含恶意JavaScript的URL，例如: `http://example.com/search.php?query=<script>alert('XSS');</script>`
4. 攻击者诱导受害者点击这个恶意URL(例如通过电子邮件或社交媒体消息)。
5. 当受害者访问这个URL时，服务器会将未经过滤的查询参数包含在响应中。
6. 受害者的浏览器接收到响应,解析HTML并执行嵌入的JavaScript代码。

#### 存储型攻击示例
```php
<?php
// comments.php

// 假设这个函数从数据库获取评论
function getComments() {
    // 在实际应用中,这里会是数据库查询
    return [
        ['user' => 'Alice', 'comment' => 'Great article!'],
        ['user' => 'Bob', 'comment' => 'I learned a lot, thanks!'],
        // 恶意评论会被存储在这里
    ];
}

// 假设这个函数添加新评论
function addComment($user, $comment) {
    // 在实际应用中,这里会将评论保存到数据库
    // 注意: 这里没有进行任何验证或清理!
    echo "Comment added successfully";
}

// 处理提交的评论
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    addComment($_POST['user'], $_POST['comment']);
}

?>
<!DOCTYPE html>
<html>
<head>
    <title>Blog Post Comments</title>
</head>
<body>
    <h1>Comments</h1>
    <?php
    $comments = getComments();
    foreach ($comments as $comment) {
        echo "<p><strong>" . $comment['user'] . "</strong>: " . $comment['comment'] . "</p>";
    }
    ?>
    <h2>Add a comment</h2>
    <form method="post">
        <input type="text" name="user" placeholder="Your name"><br>
        <textarea name="comment" placeholder="Your comment"></textarea><br>
        <input type="submit" value="Post Comment">
    </form>
</body>
</html>
```

1. 攻击者提交一个包含恶意脚本的评论,例如: `<script>alert(document.cookie);</script>Great article!`
2. 由于缺乏适当的验证和清理,这个恶意评论被存储在数据库中。
3. 每当有用户访问这个博客文章页面时,他们的浏览器会加载所有评论,包括恶意脚本。
4. 浏览器解析HTML并执行嵌入的JavaScript,导致XSS攻击对每个访问页面的用户生效。


#### DOM型攻击示例
```html
<!DOCTYPE html>
<html>
<head>
    <title>Welcome</title>
</head>
<body>
    <h1>Welcome</h1>
    <div id="greeting"></div>

    <script>
        // 获取URL中的name参数
        var name = new URLSearchParams(window.location.search).get('name');
        
        // 直接将name插入到DOM中 (这是不安全的!)
        document.getElementById('greeting').innerHTML = 'Hello, ' + name + '!';
    </script>
</body>
</html>
```

1. 这个页面旨在根据URL参数显示个性化欢迎信息。正常使用时,URL可能是这样的: `http://example.com/welcome.html?name=Alice`
2. JavaScript代码从URL中获取`name`参数,并将其直接插入到页面的DOM中。
3. 攻击者可以构造一个包含恶意JavaScript的URL,例如: `http://example.com/welcome.html?name=<script>alert('XSS');</script>`
4. 当受害者访问这个URL时,浏览器会加载页面并执行JavaScript。
5. JavaScript代码会将未经过滤的`name`参数值插入到DOM中。
6. 浏览器解析插入的HTML,执行嵌入的`<script>`标签,从而触发XSS攻击。

> DOM型XSS攻击的一个关键特点是,漏洞完全存在于客户端代码中,这使得它们有时难以被传统的服务器端安全扫描工具检测到。因此,在进行前端开发时必须格外小心。


### 扩展
`innerHTML` 里面的script标签不会被执行

## Reference

