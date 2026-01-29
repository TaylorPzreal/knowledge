
Review
1. 2020/07/29
2. 2021/02/16
3. 2024-10-05 07:15

端性能优化并非“一刀切”的解决方案，通常需要多种策略组合使用。在选择方案时，应根据项目的具体需求、瓶颈所在、团队技术栈以及目标用户群体来权衡。
1. 对于计算密集型应用，Wasm 和 Workers 会是关键；
2. 对于 PWA，Service Worker 和 Cache API 必不可少；
3. 对于大多数网站，基础的资源压缩、缓存和加载优化仍然是最具性价比的措施。


> [!Summary]
> 根据底层机制进行优化
> 
> *优化方向（Optimization direction）*
> 1. SEO(Search Engine Optimization)
> 2. Application accessibility（可访问性）
> 3. Responsiveness
> 4. Performance（性能）
> 5. User experience（用户体验）
> 6. Developer experience（开发体验）
> 7. Security（安全性优化）
> 
> 书籍 📚
> 《Web Performance in Action》
> 《大型网站性能优化实战》


[Fast load times](https://web.dev/explore/fast) improve your site's performance.


## 一、Introduction
1. 性能优化方向
2. 各个维度的性能统计指标
3. 各个维度的性能优化方案

##### 性能优化方向
1. 前端性能优化
2. 服务端性能优化

##### 资源加载优化
1. TCP优化
2. DNS优化
3. CDN优化

- **图片优化：**
    - **压缩：** 使用工具（如 ImageOptim、TinyPNG）无损或有损压缩图片。
    - **选择合适格式：** JPG (照片)、PNG (透明度、细节)、SVG (矢量图)、WebP (新一代格式，更高压缩率)、AVIF。
    - **响应式图片：** `srcset` 和 `sizes` 属性，或 `<picture>` 元素，根据设备和视口加载不同尺寸的图片。
    - **懒加载 (Lazy Loading)：** `loading="lazy"` 属性或 Intersection Observer API，只加载进入视口或即将进入视口的图片。
- **字体优化：**
    - **Subset 字体：** 只包含所需字符的子集。
    - **`font-display` 属性：** 控制字体加载时的显示行为（如 `swap`、`fallback`）。
    - **Woff2 格式：** 压缩率更高的 Web 字体格式。
- **CSS 和 JavaScript 优化：**
    - **代码压缩 (Minification)：** 移除空格、注释、缩短变量名等。
    - **代码分割 (Code Splitting)：** 按需加载 JS/CSS 模块，减小初始包大小。
    - **移除未使用的代码 (Tree Shaking)：** 现代打包工具（如 Webpack、Rollup）支持。
    - **预加载/预连接/预取：** `preload`、`preconnect`、`prefetch` 标签，提前加载关键资源或建立连接。
    - **异步加载 JS：** `async` 和 `defer` 属性，不阻塞 HTML 解析。
- **HTTP/2 或 HTTP/3：**
    - **多路复用：** 单个 TCP 连接上同时发送多个请求和响应。
    - **头部压缩：** 减小请求头大小。
    - **服务器推送：** 服务器可以主动推送客户端可能需要的资源。
    - **QUIC (HTTP/3):** 基于 UDP，提供更低的延迟和更好的丢包恢复。


##### 渲染性能优化
- **DOM 操作优化：**
    - **减少 DOM 操作：** 批量操作、使用文档碎片 (DocumentFragment)。
    - **避免强制同步布局 (Reflow/Layout Thrashing)：** 读写 DOM 属性交替操作会导致频繁重排。
    - **CSS 性能：** 避免使用昂贵的 CSS 属性（如 `box-shadow`），使用 `transform` 和 `opacity` 进行动画（由 GPU 加速）。
- **动画优化：**
    - **使用 CSS 动画/过渡：** 浏览器通常可以优化这些动画，将其放到合成器线程执行。
    - **使用 `requestAnimationFrame`：** 在浏览器下一次重绘之前执行动画逻辑，确保动画平滑。
    - **虚拟列表/无限滚动：** 对于长列表，只渲染用户可见的部分。
- **避免长任务：** 将长时间运行的 JavaScript 代码分割成小块，在多个帧中执行，或者放入 Web Workers。


##### 网络性能优化
- **CDN (内容分发网络)：** 将静态资源部署在全球各地的服务器上，用户可以从离自己最近的节点获取资源，降低延迟。
- **缓存策略 (HTTP Cache Headers)：** 设置 `Cache-Control`、`Expires`、`ETag` 等 HTTP 头部，控制浏览器缓存行为。
- **Gzip/Brotli 压缩：** 在服务器端压缩文本资源（HTML、CSS、JS），传输到客户端后再解压，大幅减小传输大小。
- **减少请求数量：** 合并 CSS/JS 文件（虽然 HTTP/2 时代重要性降低）、使用雪碧图、内联小文件。
- **DNS 预解析：** `<link rel="dns-prefetch" href="//example.com">`，提前解析域名。


##### 用户体验感知优化
- **骨架屏 (Skeleton Screens)：** 在内容加载完成前显示页面的大致结构，提升用户感知速度。
- **加载指示器：** 提供明确的加载反馈（进度条、旋转图标）。
- **服务端渲染 (SSR) / 预渲染 (Pre-rendering)：**
    - **SSR：** 在服务器端将页面渲染成 HTML，直接发送给浏览器，用户可以更快看到内容，对 SEO 友好。
    - **预渲染：** 在构建时将特定页面（如营销页）预渲染成静态 HTML。
- **关键 CSS (Critical CSS)：** 提取首屏所需的 CSS 并内联到 HTML 中，消除渲染阻塞。


##### 其他方向
1. 基于用户体验的性能优化要素
2. 网站性能分析
3. 网站性能监控体系
4. 网站容量评估
5. 系统架构模式
6. 数据分析驱动性能优化





## Reference
1. Web Performance: Leveraging the Metrics that Most Affect User Experience (Google I/O '17): https://www.youtube.com/watch?v=6Ljq-Jn-EgU&ab_channel=GoogleChromeDevelopers
2. Web Performance: https://developer.mozilla.org/zh-CN/docs/Web/Performance
