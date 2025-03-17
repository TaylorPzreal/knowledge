---
author: "Zeke"
date: 2025-03-15
title: Hugo 语法
tags: 'hugo'
categories: 'inbox'
---

Hugo的语法主要涉及 **模板引擎**、**内容格式（Front Matter）** 和 **短代码（Shortcodes）**，以下是详细的语法介绍：

---

### 一、Front Matter：内容的元数据
Front Matter是Hugo内容文件顶部的元数据块，用于定义页面的标题、日期、分类等属性，支持 **YAML**、**TOML**、**JSON** 三种格式。

#### 1. YAML格式
用`---`包裹：
```yaml
---
title: "Hello Hugo"
date: 2023-10-01
tags: ["SSG", "Hugo"]
draft: false
---
```

#### 2. TOML格式
用`+++`包裹：
```toml
+++
title = "Hello Hugo"
date = 2023-10-01T15:00:00+08:00
tags = ["SSG", "Hugo"]
draft = false
+++
```

#### 3. JSON格式
用`{ ... }`包裹：
```json
{
  "title": "Hello Hugo",
  "date": "2023-10-01",
  "tags": ["SSG", "Hugo"],
  "draft": false
}
```

#### 常用字段
- `title`: 页面标题
- `date`: 发布日期（支持时间戳）
- `draft`: 是否为草稿（`true`时默认不生成页面）
- `tags`/`categories`: 标签和分类（支持多级分类）
- `weight`: 控制页面在列表中的排序权重
- `aliases`: 页面别名（用于重定向）

---

### 二、Go模板语法
Hugo使用Go语言的 `html/template` 引擎，支持逻辑控制、变量、函数等。

#### 1. 变量与上下文
- 全局变量：通过 `.Site`、`.Page`、`.Params` 等访问。
  ```html
  <h1>{{ .Title }}</h1>       <!-- 页面标题 -->
  <p>作者：{{ .Site.Author }}</p>
  ```
- 页面变量：`{{ .Content }}` 渲染Markdown内容。

#### 2. 条件判断（if/else）

```go
{{ if eq .Section "posts" }}
  <div class="post-header">这是文章页</div>
{{ else if eq .Section "about" }}
  <div class="about-header">关于页面</div>
{{ else }}
  <div class="default-header">默认页眉</div>
{{ end }}
```

#### 3. 循环（range）

遍历页面集合（如文章列表）：
```html
{{ range .Pages }}
  <article>
    <h2><a href="{{ .RelPermalink }}">{{ .Title }}</a></h2>
    <p>{{ .Summary }}</p>
  </article>
{{ end }}
```

#### 4. 函数（Functions）

Hugo内置大量函数，例如：
- **字符串处理**：`lower`, `upper`, `replace`, `trim`
  ```html
  {{ "Hello Hugo" | lower }}  <!-- 输出：hello hugo -->
  ```
- **日期格式化**：`dateFormat`
  ```html
  {{ .Date | dateFormat "2006-01-02" }}  <!-- 输出：2023-10-01 -->
  ```
- **资源处理**：`resources.Get`, `image.Resize`
  ```html
  {{ $image := resources.Get "images/logo.png" }}
  {{ $resized := $image.Resize "300x" }}
  <img src="{{ $resized.RelPermalink }}">
  ```

#### 5. 部分模板（Partials）
复用代码片段，存放在 `layouts/partials/` 中：
```html
<!-- layouts/partials/header.html -->
<header>
  <h1>{{ .Site.Title }}</h1>
</header>

<!-- 在模板中引用 -->
{{ partial "header.html" . }}
```

#### 6. 模板继承（Blocks）

通过 `block` 定义可覆盖的区域：

```html
<!-- layouts/_default/baseof.html -->
<html>
  <head>
    <title>{{ block "title" . }}{{ .Site.Title }}{{ end }}</title>
  </head>
  <body>
    {{ block "main" . }}{{ end }}
  </body>
</html>

<!-- 子模板中覆盖区块 -->
{{ define "title" }} {{ .Title }} | {{ .Site.Title }} {{ end }}
{{ define "main" }}
  <h1>{{ .Title }}</h1>
  {{ .Content }}
{{ end }}
```

---

### 三、短代码（Shortcodes）
短代码允许在Markdown中嵌入HTML组件，分为 **内置短代码** 和 **自定义短代码**。

#### 1. 内置短代码
- **Figure**（带标题的图片）：
  ```markdown
  < figure src="/images/photo.jpg" title="示例图片" >
  ```
- **Highlight**（代码高亮）：
  ```markdown
  < highlight python >
  def hello():
      print("Hello Hugo!")
  < /highlight >
  ```

#### 2. 自定义短代码
在 `layouts/shortcodes/` 下创建HTML文件：

```html
<!-- layouts/shortcodes/notice.html -->
<div class="notice {{ .Get 0 }}">
  {{ .Inner | markdownify }}
</div>
```

在Markdown中使用：

```md
< notice "warning" >
**注意**：这是自定义警告短代码！
< /notice >
```

---

### 四、变量与作用域
Hugo的变量作用域分为 **全局作用域** 和 **局部作用域**。

#### 1. 全局变量
- `.Site.Params`: 在 `config.toml` 中定义的全局参数。
  ```toml
  [params]
    author = "John Doe"
  ```
  ```html
  <footer>作者：{{ .Site.Params.author }}</footer>
  ```

#### 2. 页面级变量
- `.Params`: 当前页面的Front Matter参数。
- `.Resources`: 页面关联的图片、文件等。

#### 3. 自定义变量
使用 `{{ $var := value }}` 定义局部变量：
```html
{{ $featuredPosts := where .Site.RegularPages "Params.featured" true }}
{{ range first 3 $featuredPosts }}
  <!-- 显示前3篇精选文章 -->
{{ end }}
```

---

### 五、多语言语法
在 `config.toml` 中配置多语言：
```toml
[languages]
  [languages.en]
    title = "My Site"
    weight = 1
  [languages.zh]
    title = "我的网站"
    weight = 2
```

内容文件中通过文件名标记语言：
```
content/
  posts/
    hello.en.md
    hello.zh.md
```

模板中根据语言切换内容：
```html
{{ if eq .Language.Lang "en" }}
  <p>Welcome!</p>
{{ else }}
  <p>欢迎！</p>
{{ end }}
```

---

### 六、高级用法示例

#### 1. 菜单配置
在 `config.toml` 中定义菜单：
```toml
[[menu.main]]
  name = "首页"
  url = "/"
  weight = 1

[[menu.main]]
  name = "博客"
  url = "/posts/"
  weight = 2
```

模板中渲染菜单：
```html
<nav>
  {{ range .Site.Menus.main }}
    <a href="{{ .URL }}">{{ .Name }}</a>
  {{ end }}
</nav>
```

#### 2. 数据文件（Data Files）
将数据存放在 `data/` 目录下的YAML/JSON文件中：
```yaml
# data/team.yml
- name: Alice
  role: Developer
- name: Bob
  role: Designer
```

模板中读取数据：
```html
{{ range .Site.Data.team }}
  <div class="member">
    <h3>{{ .name }}</h3>
    <p>{{ .role }}</p>
  </div>
{{ end }}
```

---

### 七、调试与错误处理
- **调试输出**：使用 `{{ printf "%#v" . }}` 打印上下文变量。
- **Hugo命令检查**：

```bash
hugo server -D        # 启动本地服务器（包含草稿）
hugo --templateMetrics  # 分析模板执行时间
```

---

### 总结
Hugo的语法核心围绕 **Go模板** 和 **内容元数据**，通过灵活的组合可以实现复杂的页面逻辑。建议结合官方文档（[gohugo.io](https://gohugo.io/documentation/)）和社区主题深入学习。
