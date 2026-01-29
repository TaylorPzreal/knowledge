
Review
1. 2024-07-28 23:00

## 一、Introduction
- [ ] Avoid iframes
- [ ] Minify CSS
- [ ] Non-Blocking CSS
- [ ] Inline Critical CSS
- [ ] Avoid Inline CSS
- [ ] Inline Critical CSS
- [ ] Avoid Inline CSS: Avoid using embed or inline CSS inside your `<body>` (Not valid for HTTP/2)
- [ ] 



##### Avoid iframes
Use iframes only if you don’t have any other technical possibility. Try to avoid iframes as much as you can. Iframes are not only bad for performance, but also for accessibility and usability. Iframes are also not indexed by search engines.

##### Minify CSS
> All CSS files are minified, comments, white spaces and new lines are removed from production files.

cssnano
[CSS Minifier](https://goonlinetools.com/css-minifier/)


##### Non-Blocking CSS
> CSS files need to be non-blocking to prevent the DOM from taking time to load.

CSS files can block the page load and delay the rendering of your page. Using `preload` can actually load the CSS files before the browser starts showing the content of the page.

[[preconnect vs preload vs prefetch vs prerender]]

##### Inline Critical CSS
> The CSS critical (or “above the fold”) collects all the CSS used to render the visible portion of the page. It is embedded before your principal CSS call and between `<style></style>` in a single line (minified if possible).

Inlining critical CSS help to speed up the rendering of the web pages reducing the number of requests to the server.

Generate the CSS critical with online tools or using a plugin like the one that Addy Osmani developed.

##### Avoid Inline CSS
> Avoid using embed or inline CSS inside your `<body>` (Not valid for HTTP/2)



## Reference

