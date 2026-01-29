
Review
1. 2024-07-28 23:00

## 一、Introduction
- [x] Minify CSS ✅ 2024-10-06
- [x] Non-Blocking CSS ✅ 2024-10-06
- [x] Inline Critical CSS ✅ 2024-10-06
- [x] Avoid Inline CSS ✅ 2024-10-06
- [x] Inline Critical CSS ✅ 2024-10-06
- [x] Avoid Inline CSS: Avoid using embed or inline CSS inside your `<body>` (Not valid for HTTP/2) ✅ 2024-10-06


##### Minify CSS
> All CSS files are minified, comments, white spaces and new lines are removed from production files.

`cssnano`
[CSS Minifier](https://goonlinetools.com/css-minifier/)


##### Non-Blocking CSS
> CSS files need to be non-blocking to prevent the DOM from taking time to load.

CSS files can block the page load and delay the rendering of your page. Using `preload` can actually load the CSS files before the browser starts showing the content of the page.

[[HTML attribute rel value]]

##### Inline Critical CSS
> The CSS critical (or “above the fold”) collects all the CSS used to render the visible portion of the page. It is embedded before your principal CSS call and between `<style></style>` in a single line (minified if possible).

Inlining critical CSS help to speed up the rendering of the web pages reducing the number of requests to the server.

Generate the CSS critical with online tools or using a plugin like the one that Addy Osmani developed.

##### Avoid Inline CSS
> Avoid using embed or inline CSS inside your `<body>` (Not valid for HTTP/2)


## Reference

