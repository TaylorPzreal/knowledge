#webpack

**Review**
1.  2020/08/03
2.  2021/02/27 16:30:28

**HMR原理**

Hot Module Replacement（HMR）特性最早由 webpack 提供，能够对运行时的 JavaScript 模块进行热更新（无需重刷，即可替换、新增、删除模块）：

热替换，此功能可以很大程度提高生产效率。

监听到文件变化后，通知构建工具（HMR plugin），将发生变化的文件（模块）发送给跑在应用程序里的运行时框架（HMR Runtime），由运行时框架把这些模块塞进模块系统（新增/删除，或替掉现有模块）

其中，HMR Runtime 是构建工具在编译时注入的，通过统一的模块 ID 将编译时的文件与运行时的模块对应起来，并暴露出一系列 API 供应用层框架（如 React、Vue 等）对接

基于WebSocket

文件变化 -> 通知构建工具 -> 变更传输给页面中HMR Runtime

**Proxy原理**
为解决在本地开发时XHR异步请求跨域问题（如果你的后端小伙伴愿意给你处理，无需配置）

proxy工作原理实质上是利用http-proxy-middleware 这个http代理中间件，实现请求转发给其他服务器。

必须配置：changeOrigin= true；

HTTP代理
1.  正向代理（Forward Proxy）：客户端通过代理服务器访问目标服务器，如VPN
2.  反向代理（Reverse Proxy）：服务器利用代理服务器给客户端提供服务，如Nginx反向代理（属于七层代理）

其他代理
-   二层代理
-   三层代理
-   四层代理
-   七层代理

Webpack proxy实现原理

通过webpack-dev-server -> webpack-dev-middleware -> http-proxy-middleware -> node-http-proxy

