
#Webpack 

Review
1. 2023-02-26 22:58
2. 2024-09-15


> [!Summary]
> 模块热替换(HMR - hot module replacement)功能会在应用程序运行过程中，替换、添加或删除 [模块](https://webpack.docschina.org/concepts/modules/)，而无需重新加载整个页面。主要是通过以下几种方式，来显著加快开发速度：
> 
> - 保留在完全重新加载页面期间丢失的应用程序状态。
> - 只更新变更内容，以节省宝贵的开发时间。
> - 在源代码中 CSS/JS 产生修改时，会立刻在浏览器中进行更新，这几乎相当于在浏览器 devtools 直接更改样式。

## 一、Introduction

### 术语解释
1. **Live Reloading(Page Reloading)**: On every change, the whole application is rebuilt/recompiled, the browser is refreshed and the application is reloaded in the browser.
2. **HMR(Hot Module Replacement or Hot Reloading or Fast Refresh)**: Watching changes in the application and then reflect those changes in the browser *without reloading the whole application*.

**Fast refresh** is great when we change the component for example style. It will only load the app on the current page. Most edits should be visible within a second or two.

**Hot reloading** is to keep the app running and to inject new versions of the files that you edited at runtime.

For the **Fast refresh** If we edit a module that only exports React component(s), Fast Refresh will update the code only for that module and re-render your component.

If we edit a module with exports that aren't React components, Fast Refresh will re-run both that module and the other modules importing it.

If we edit a file that's imported by modules outside of the React tree, Fast Refresh will fall back to doing a full reload

In other words, it is great and more full than **hot reloading**


### Live Reloading has a few issues
1. On every change, the whole application is rebuilt/recompiled, the browser is refreshed and the application is reloaded in the browser. All of this can take a long time when working on big applications.
2. Sometimes while working on something like a modal or a dialog box or the third page of a navigation wizard, when we make a change, we want to see the change taking place to the page we’re on, but the browser reloads and takes us back to the initial screen.
3. Live reload also loses your state, so if you are developing a feature deep within a large single page application, that can be annoying.

HMR can significantly speed up development as:
1. It saves up development time by only updating what has changed.
2. It retains the state of the application which is normally lost during a full reload.

Webpack provides two components to make HMR possible.
1. HMR Runtime
2. HMR Server (included in `webpack-dev-server` as middleware).


## 二、运行原理
通过以下步骤，可以做到在应用程序中置换(swap in and out)模块：
1. 应用程序要求 HMR runtime 检查更新。
2. HMR runtime 异步地下载更新，然后通知应用程序。
3. 应用程序要求 HMR runtime 应用更新。
4. HMR runtime 同步地应用更新。


1. **文件变更监听:** `webpack-dev-server` 持续监听项目文件变更。一旦检测到文件（如a文件）发生变化，就会触发重新编译。
2. **增量编译:** Webpack只会重新编译发生变化的文件（a文件）以及直接或间接依赖它的模块（如b文件）。
3. **生成更新信息:** Webpack会生成一个JSON格式的更新信息，描述哪些模块发生了变化，以及新的模块代码。
4. **发送更新信息:** `webpack-dev-server` 通过WebSocket将更新信息发送给浏览器中的HMR runtime。
5. **HMR runtime接收更新:** 浏览器中的HMR runtime接收到更新信息后，会解析更新内容。
6. **模块替换:**
    - **找到对应模块:** HMR runtime根据更新信息找到需要替换的模块（b文件）。
    - **执行accept回调:** 如果b文件配置了`module.hot.accept`，则会执行对应的回调函数。在这个回调函数中，你可以执行一些更新逻辑，比如重新渲染组件。
    - **替换模块:** HMR runtime会将新的b模块替换掉旧的b模块，并且保持应用的状态。


## 三、实现了HMR接口的Loaders
1. [React Fast Refresh](https://github.com/pmmmwh/react-refresh-webpack-plugin)
2. `style-loader` 
3. `vue-loader` 


自行实现 HMR，参照文档
[API - Hot Module Replacement](https://webpack.docschina.org/api/hot-module-replacement/) 
[Guide - 模块热替换](https://webpack.docschina.org/guides/hot-module-replacement/) 


```js
const path = require('path');
const webpack = require('webpack');

module.exports = {
  // ... 其他配置
  mode: 'development',
  devServer: {
    hot: true,
    // ... 其他 devServer 配置
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin()
  ]
};
```

代码文件
```js
if (module.hot) {
  module.hot.accept('./other-module', () => {
    // 当 other-module 模块发生变化时，执行此回调函数
    // 可以在这里重新加载或更新组件
  });
}
```

## Reference
1. [Webpack深度进阶：两张图彻底讲明白热更新原理](https://juejin.cn/post/7176963906844246074)
2. [Webpack — Hot Module Replacement](https://medium.com/js-imaginea/hot-module-replacement-8b634c2a4348)
3. [HMR Concepts](https://webpack.docschina.org/concepts/hot-module-replacement/)
4. [HMR API](https://webpack.docschina.org/api/hot-module-replacement)

