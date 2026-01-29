#webpack 

Review
1. 2023-03-02 06:15

## 一、Introduction
> Module Federation 建立在“微服务”的理念之上，允许创建可以独立部署和管理的真正 ==模块化== 的应用程序。更容易维护和修改。

多个独立的 **构建** 可以组成一个应用程序，这些独立的构建之间不应该存在依赖关系，因此可以单独开发和部署它们。这是模块联邦（Module Federation）可以实现的功能。很像微前端，但不仅如此。

> 适用于团队大，页面数量多，需要共同开发维护的场景。

### Features
1. 开源，无维护成本，易于扩展
2. 促进代码复用
3. 基于Webpack插件机制，学习成本低、配置快速
4. 不需要对每个项目进行重新架构
5. 在构建时处理，而不是运行时
6. 与Web框架独立
7. 不需要处理路由问题
8. Shell和Micro Apps是松耦合的
9. 可以更轻松的独立测试和调试每个组件

### 基本概念
-   **webpack构建**：一个独立项目通过webpack打包编译而产生资源包。
-   **remote**：一个暴露模块供其他 `webpakc构建` 消费的 `webpack构建`。
-   **host**：一个消费其他 `remote` 模块的 `webpack构建`。


## 二、实践
更多示例参考 [module-fereration-examples](https://github.com/module-federation/module-federation-examples)
`webpack@^5` 支持的特性

```sh
mkdir shell
cd shell

yarn add webpack webpack-cli webpack-dev-server html-webpack-plugin css-loader style-loader babel-loader -E -D
```


一共有三个微应用:`lib-app`、`component-app`、`main-app`，角色分别是：
-   `lib-app` as remote,暴露了两个模块`react`和`react-dom`
-   `component-app` as remote and host,依赖`lib-app`,暴露了一些组件供`main-app`消费
-   `main-app` as host,依赖`lib-app`和`component-app`

`lib-app` configuration
```js
//webpack.config.js
const { ModuleFederationPlugin } = require('webpack').container;

module.exports = {
  entry: './src/index',
  mode: 'development',
  devServer: {
    port: 3002,
  },
  output: {
    publicPath: 'auto',
    clean: true,
  },
  module: {},
  plugins: [
    new ModuleFederationPlugin({
      name: 'libs',
      filename: 'remoteEntry.js',
      exposes: {
        './react': 'react',
        './react-dom': 'react-dom',
      },
    }),
  ],
};
```

```js
// component webpack.config.js
	new ModuleFederationPlugin({
      name: 'remote',
      filename: 'remoteEntry.js',
      remotes: {
        'libs': 'libs@http://localhost:3002/remoteEntry.js'
      },
      exposes: {
        './Button': './src/Button'
      },
    }),
```

```js
// shell webpack.config.js
	new ModuleFederationPlugin({
      name: 'host',
      remotes: {
        'remote': 'remote@http://localhost:3001/remoteEntry.js',
        'libs': 'libs@http://localhost:3002/remoteEntry.js',
      },
    }),
```

- `name` 应用程序的名称，用来跟其他App通信
- `filename` 是入口文件，其他应用可以访问，如 `libs@http://localhost:3002/remoteEntry.js` 访问该应用程序
- `exposes` 允许从当前应用程序共享组件、页面、或整个应用程序到另一个应用程序。每一个公开的内容都是作为单独的构建创建的。每个构建都是以文件的MD5哈希命名，不必担心缓存。
- `shared` 指定当前应用程序将对其他应用程序共享哪些依赖项。
- `remotes` 确定从哪些应用程序接收组件、页面或应用程序本身。

每个应用程序都可以指定 `exposes` 和 `remotes` 。


`src/bootstrap.js` 
```jsx
import React from 'libs/react';
import ReactDom from 'libs/react-dom';

const Button = React.lazy(() => import('remote/Button'));

function App() {
  return <div>
    <div style={{ height: 100 , backgroundColor: '#005599', textAlign: 'center'}}>test</div>
    <React.Suspense fallback="Loading Button">
      <Button />
    </React.Suspense>
  </div>
}

ReactDom.render(<App />, document.getElementById('root'))
```

由于需要等待基础模块加载完毕，所以需要配置懒加载入口`bootstrap.js` 。
`src/index.js`
```js
import('./bootstrap');
```

lib执行 `yarn build` 
```txt
dist
├── main.js         // 项目入口文件
├── remoteEntry.js  // 远程入口文件
├── remoteEntry.js.map
├── vendors-node_modules_react-dom_index_js.js    // 暴露的模块
├── vendors-node_modules_react-dom_index_js.js.map
├── vendors-node_modules_react_index_js.js        // 暴露的模块
└── vendors-node_modules_react_index_js.js.map
```


module federation策略
1. 模块尽可能小和独立
2. 模块尽可能松耦合



## Reference
1. [Module Federation](https://webpack.docschina.org/concepts/module-federation/)
2. [模块联邦在微前端架构中的实践](https://mp.weixin.qq.com/s/WXeUuUdgF_3djqBhh1siQA)
3. [Micro Frontends Architecture with Webpack Module Federation (Part 1)](https://medium.com/trendyol-tech/micro-frontend-architecture-with-webpack-module-federation-part-1-9827d436bd1e)
4. [Micro Frontends Architecture with Webpack Module Federation (Part 2)](https://medium.com/@dogan.ozturk/micro-frontends-architecture-with-webpack-module-federation-part-2-40a23fa53e26)

