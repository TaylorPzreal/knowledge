
Review
1. 2024-10-15 07:31

> [!Summary]
> 

## 一、Introduction
React Native 要大规模实现 SSR，就得造一个 Next.js 的轮子。让 React Native 能同时在本地和服务端运行起来。首先开发者在本地，能通过 “类 Next.js” 的框架使用客户端渲染 CSR 的方式，开发 React Native 应用，然后在服务端能通过服务端渲染 SSR 的方式，执行 React Native 代码，输出一个序列化 Tree。这个序列化的 Tree 描述的就是 React Native 的静态布局结构。接着服务端把序列化的 Tree 下发到 iOS/Android 应用上，Native 应用对 Tree 进行反序列化后，直接通过 C++ 层的 Fabric 渲染器 ，执行布局、提交和挂载操作，生成 Native 页面。

CSR 渲染的渲染步骤分为 6 步：
1. 请求服务端获取最新的 Bundle 资源地址；
2. 通过返回的资源地址，下载 Bundle 资源，也就是 JavaScript 代码；
3. 初始化 JavaScript 引擎和 Native 模块；
4. 执行 JavaScript 代码，生成空页面；
5. 与此同时发起业务请求，请求最新的业务数据；
6. 业务数据回来后重新渲染，生成最终的页面。

SSR 渲染其实是对 CSR 渲染的步骤的重组，整体也是 6 步：
1. 并行请求 Tree，和最新的 Bundle 资源地址；
2. 初始化 Native 模块，同时开启后台线程并行请求 Bundle 资源；
3. 使用 Tree 文件，通过 Fabric 渲染器渲染首屏页面。这里画个重点，此时用户已经可以看到业务页面了；
4. 然后再初始化 JavaScript 引擎，开始执行 JavaScript 代码；
5. 这一步有个专有名词叫做 Hydration。大致的意思原来通过 Tree 生成的页面是不可交互的“静态”页面，这时需要通过执行 JavaScript，生成一个有交互的“动态”页面，把原来的“静态”页面替换掉；
6. 替换后的页面，就是可以交互“动态”页面了。

![](./assets/141e69151e23_d15d5513.webp)

## Reference

