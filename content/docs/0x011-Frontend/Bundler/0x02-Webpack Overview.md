#Webpack 

**Review**
1. 2020/08/03
2. 2021/02/27
3. 2024-09-15


> [!Summary]
> 基于 `Webpack@5` 整理，Webpack 5 released at *2020-10-10*
> - Github <https://github.com/webpack/webpack> 
> - Webpack <https://webpack.js.org/>
> - Webpack zh <https://webpack.docschina.org/> 
> - SurviveJS - Webpack 5 <https://survivejs.com/books/webpack/> 
> 
> **Webpack** 是一个用于现代 JavaScript 应用程序的 _静态模块打包工具_。当 Webpack 处理应用程序时，它会在内部从一个或多个入口点构建一个 [依赖图(dependency graph)](https://webpack.docschina.org/concepts/dependency-graph/)，然后将你项目中所需的每一个模块组合成一个或多个 _bundles_，它们均为静态资源，用于展示你的内容。


**Core Concepts**:
- [Entry](https://webpack.js.org/concepts/#entry)
- [Output](https://webpack.js.org/concepts/#output)
- [Loaders](https://webpack.js.org/concepts/#loaders)
- [Plugins](https://webpack.js.org/concepts/#plugins)
- [Mode](https://webpack.js.org/concepts/#mode)
- [Browser Compatibility](https://webpack.js.org/concepts/#browser-compatibility)
- Modules --- files
- Chunks --- includes one or more modules, each chunk will have a corresponding file in the _dist_ directory.
- Assets
- Shims

## 一、Quick Start
**Installation**
```sh
npx webpack init

# Or
npm install webpack webpack-cli --save-dev
```

**Configuration**
```js
const path = require('path');

module.exports = {
  entry: './src/index.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js',
  },
};
```


> [!Tip]+ 
> [Webpack](https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.js.org%2F "https://webpack.js.org/") 本质上是一个函数，它接受一个配置信息作为参数，执行后返回一个 [compiler 对象](https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.js.org%2Fplugins%2Finternal-plugins%2F%23compiler "https://webpack.js.org/plugins/internal-plugins/#compiler")，调用 `compiler` 对象中的 [run](https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.js.org%2Fapi%2Fnode%2F%23run "https://webpack.js.org/api/node/#run") 方法就会启动编译。`run` 方法接受一个回调，可以用来查看编译过程中的错误信息或编译信息。


```js
// build.js
const { webpack } = require("webpack");
const webpackOptions = require("./webpack.config.js");
const compiler = webpack(webpackOptions);

//开始编译
compiler.run((err, stats) => {
  console.log(err);
  console.log(
    stats.toJson({
      assets: true, //打印本次编译产出的资源
      chunks: true, //打印本次编译产出的代码块
      modules: true, //打印本次编译产出的模块
    })
  );
});
```

执行 `node build.js`，产出 `dist/main.js` ，内容如下：

```js
(() => {
  var __webpack_modules__ = {
    "./src/age.js": (module) => {
      module.exports = "agevalue";
    },
    "./src/name.js": (module) => {
      module.exports = "namevalue";
    },
  };

  // The module cache
  var __webpack_module_cache__ = {};

  // The require function
  function __webpack_require__(moduleId) {
    // Check if module is in cache
    var cachedModule = __webpack_module_cache__[moduleId];
    if (cachedModule !== undefined) {
      return cachedModule.exports;
    }
    // Create a new module (and put it into the cache)
    var module = (__webpack_module_cache__[moduleId] = {
      exports: {},
    });

    // Execute the module function
    __webpack_modules__[moduleId](module, module.exports, __webpack_require__);

    // Return the exports of the module
    return module.exports;
  }

  var __webpack_exports__ = {};
  (() => {
    const name = __webpack_require__("./src/name.js");
    const age = __webpack_require__("./src/age.js");
    console.log("test", name, age);
  })();
})();
```


## 二、核心思想
`Webpack`内部高度插件化，通过插件将功能模块“外包”出去。`Webpack`大多数配置项逻辑都会交由插件实现，具体体现为配置项在初始化时会转为一个个插件，如下面的配置：
```js
module.exports = {
  // 1. 使用EntryPlugin
  entry: path.resolve(__dirname, 'src', 'index.js'),
  output: {
    path: path.resolve(__dirname, 'dist'),
  },
  // 2. 使用ExternalsPlugin
  externals: {
    react: 'react'
  },
  resolve: {
    // 3. 应用于一些插件的入参，如DllReferencePlugin的入参
    extensions: [
      '.ts',
      '.tsx',
      '.js',
      '.json'
    ],
  },
  // 4. 根据配置项转为EvalDevToolModulePlugin或EvalSourceMapDevToolPlugin等插件
  devtool: false,
}
```

配置项在初始化时处理为插件，插件通过监听 `Compiler` 或 `Compilation` 钩子事件从而内部闭环完成逻辑，这样做能够较大程度降低 `Webpack` 模块耦合度，对于新增或修改与主流程无关的能力时，无需修改核心代码，降低了维护成本。

1.  首先，根据配置信息（`webpack.config.js`）找到入口文件（`src/index.js`）
2.  找到入口文件所依赖的模块，并收集关键信息：比如`路径、源代码、它所依赖的模块`等
3.  根据上一步得到的信息，生成最终输出到硬盘中的文件`dist`：包括 modules 对象、require 模版代码、入口执行文件等

在这过程中，由于浏览器并不认识除 `html、js、css` 以外的文件格式，所以我们还需要对源文件进行转换 —— **`Loader 系统`**。

### Loader
> [!Abstract]
> **Loader 系统**： Loader 是一个转换器（模块预处理器），将 A 文件进行编译输出 B 文件，比如：将 `A.less` 转换为 `A.css`，单纯的文件转换过程。Webpack 自身只支持 `js` 和 `json` 这两种格式的文件，对于其他文件需要通过 loader 将其转换为 commonJS 规范的文件后，Webpack 才能解析。

*Features*
- loader 支持链式调用。链中的每个 loader 会将转换应用在已处理过的资源上。一组链式的 loader 将按照相反的顺序执行。链中的第一个 loader 将其结果（也就是应用过转换后的资源）传递给下一个 loader，依此类推。最后，链中的最后一个 loader，返回 Webpack 所期望的 JavaScript。
- loader 可以是同步的，也可以是异步的。
- loader 运行在 Node.js 中，并且能够执行任何操作。
- loader 可以通过 `options` 对象配置。
- 除了常见的通过 `package.json` 的 `main` 来将一个 NPM 模块导出为 loader，还可以在 `module.rules` 中使用 `loader` 字段直接引用一个模块。
- 插件(plugin)可以为 loader 带来更多特性。
- loader 能够产生额外的任意文件。

*编写自定义Loader*
```js
import { getOptions } from 'loader-utils';
import validateOptions from 'schema-utils';

import schema from './options.json';

export const raw = true;

export default function loader(source) {
  const { version, webpack } = this;

  const options = getOptions(this) || {};

  validateOptions(schema, options, 'Loader');

  const newSource = `
  /**
   * Loader API Version: ${version}
   * Is this in "webpack mode": ${webpack}
   */
  /**
   * Original Source From Loader
   */
  ${source}`;

  return `${newSource}`;
}
```

### Plugin
> [!Abstract]+ 
> **Plugin 系统**：plugin 是一个扩展器，它丰富了 Webpack 本身，针对的是 Loader 结束后，Webpack 打包的整个过程，它并不直接操作文件，而是**基于事件流机制工作**，会监听 Webpack 打包过程中的某些节点（类似生命周期），执行广泛的任务。 

> [!Tip] Loader vs Plugin
> While **loaders** are used to *transform* certain types of modules, **plugins** can be leveraged to perform a wider range of tasks like bundle optimization, asset management and injection of environment variables.

创建Plugin的标准方式
```javascript
const pluginName = 'LogWebpackPlugin';

class LogWebpackPlugin {
  apply(compiler) {
    compiler.hooks.run.tap(pluginName, (compilation) => {
      console.log('webpack 构建正在启动！');
    });
  }
}

module.exports = LogWebpackPlugin;
```


### Module
Webpack中的 **module** 是跟文件相关联的，简单理解，*module 就是文件的升级版本*。

> [!Abstract]+
> A module is an *upgraded version* of a file. A module, once created and built, contains a lot of meaningful information besides the raw source code, such as: the loaders used, its dependencies, its exports(if any), its hash and much more.
> **Each item** in the `entry` object can be thought of as the **root module** in a tree of modules.
> All these module trees are stored together in a `ModuleGraph`
> 
> 一个 module，一旦创建和构建，除了原始源代码之外，还包含许多有意义的信息，例如：使用的loaders、它的依赖项、它的导出（如果有的话）、它的哈希等等。 entry 对象中的每一项都可以被认为是 **module trees** 中的 **root module**。


Modules includes:
1. NormalModules(Simply as *modules*)
2. ExternalModule: When using **module federation** (模块联邦)
3. ConcatenatedModule: When using `require.context()` 


### Chunk
`Chunk` 是 `Module` 代码的封装，在代码生成阶段会将模块代码塞入`Chunk`中，并最终输出为产物文件。编译完成准备输出时才会创建Chunk。

- A `Chunk` encapsulates one or more *modules*.
- A `ChunkGroup` contains one or more *chunks*. A `ChunkGroup` can be a parent or a child to another `ChunkGroup` .
- An `EntryPoint` is a **type of** `ChunkGroup` which is created **for each item** in the `entry` object.  Also called the **EntryPoint chunk**

### ChunkGraph
A *node* that belongs to the `ChunkGraph` is called `[ChunkGraphChunk]` , it is just a _decorated_ chunk.

ChunkGraph 是整个应用的 Chunks 之间关系的标识

### Dependency
Any time one file depends on another, Webpack treats this as a _dependency_. This allows Webpack to take non-code assets, such as images or web fonts, and also provide them as _dependencies_ for your application.

### ModuleGraph
`ModuleGraph` 是项目文件引用拓扑图在内存中的映射，内部由 `ModuleGraphModule` 和 `ModuleGraphConnection` 组成：
- `ModuleGraphModule`：Graph的节点，是模块在 `ModuleGraph` 的映射；
- `ModuleGraphConnection`：Graph的边，是 `Dependency` 在 `ModuleGraph` 的映射。

### Bundle
> [!Tip]+
> Bundle 是 Webpack 打包的最终产物
> Produced from a number of distinct modules, bundles contain the final versions of source files that have already undergone the loading and compilation process.

### runtime
runtime，以及伴随的 manifest 数据，主要是指：在浏览器运行过程中，Webpack 用来连接模块化应用程序所需的所有代码。它包含：在模块交互时，连接模块所需的加载和解析逻辑。包括：已经加载到浏览器中的连接模块逻辑，以及尚未加载模块的延迟加载逻辑。

### manifest
一旦你的应用在浏览器中以 `index.html` 文件的形式被打开，一些 bundle 和应用需要的各种资源都需要用某种方式被加载与链接起来。在经过打包、压缩、为延迟加载而拆分为细小的 chunk 这些 Webpack 优化之后， `/src` 目录的文件结构都已经不再存在。所以 Webpack 如何管理所有所需模块之间的交互呢？这就是 manifest 数据用途的由来。

当 compiler 开始执行、解析和映射应用程序时，它会保留所有模块的详细要点。这个数据集合称为 "manifest"，当完成打包并发送到浏览器时，runtime 会通过 manifest 来解析和加载模块。无论你选择哪种模块语法，那些 `import` 或 `require` 语句现在都已经转换为 `__webpack_require__` 方法，此方法指向模块标识符(module identifier)。通过使用 manifest 中的数据，runtime 将能够检索这些标识符，找出每个标识符背后对应的模块。

- [分离 manifest](https://survivejs.com/webpack/optimizing/separating-manifest/)
- [使用 Webpack 提供可预测的长效缓存](https://medium.com/webpack/predictable-long-term-caching-with-webpack-d3eee1d3fa31)
- [缓存](https://webpack.docschina.org/guides/caching/)

## 三、架构设计
整个打包过程，大致可以分为三个阶段：
-   打包开始前的准备工作
-   打包过程中（也就是编译阶段）
-   打包结束后（包含打包成功和打包失败）

在 **Webpack** 源码中，`compiler` 就像是一个大管家，它代表上面说的三个阶段，在它上面挂载着各种生命周期函数，而 `compilation` 就像专管伙食的厨师，专门负责**编译**相关的工作，也就是`打包过程中`这个阶段。
![](./assets/4cd4e77c0d2a_73fde826.webp)

Webpack的可扩展性是通过 **hooks** 实现的。
事件流的实现是基于 [Tapable ](https://github.com/webpack/tapable)

### Tapable
Tapable 是一个类似于 Node.js 中的 [EventEmitter](https://www.npmjs.com/package/events) 的库，但**更专注于自定义事件的触发和处理**。通过 Tapable 可以注册自定义事件，然后在适当的时机去执行自定义事件。详见 [[Tapable原理]] 

```js
const {
	SyncHook,
	SyncBailHook,
	SyncWaterfallHook,
	SyncLoopHook,
	AsyncParallelHook,
	AsyncParallelBailHook,
	AsyncSeriesHook,
	AsyncSeriesBailHook,
	AsyncSeriesWaterfallHook
} = require("tapable");
```

```js
const { SyncHook } = require("tapable"); //这是一个同步钩子

//第一步：实例化钩子函数，可以在这里定义形参
const syncHook = new SyncHook(["author", "age"]);

//第二步：注册事件1
syncHook.tap("监听器1", (name, age) => {
  console.log("监听器1:", name, age);
});

//第二步：注册事件2
syncHook.tap("监听器2", (name) => {
  console.log("监听器2", name);
});

//第二步：注册事件3
syncHook.tap("监听器3", (name) => {
  console.log("监听器3", name);
});

//第三步：触发事件，这里传的是实参，会被每一个注册函数接收到
syncHook.call("不要秃头啊", "99");
```


### Webpack钩子
#### Compiler部分重要钩子
1.  environment
2.  entryOption
3.  beforeRun
4.  run
5.  watchRun
6.  shouldEmit
7.  emit
8.  afterEmit
9.  done
10.  log

#### Compilation部分重要钩子
1.  `buildModule`
2.  `optimise`
3. ` record`


## 四、具体实现
详见 [[Webpack build flow]] 


## Reference
1. <https://webpack.js.org/blog/2020-10-10-webpack-5-release/> 
2. Webpack Concepts: [https://webpack.js.org/concepts/](https://webpack.js.org/concepts/)
3.  Webpack系列（上）：<https://mp.weixin.qq.com/s?__biz=MzAxODE2MjM1MA==&mid=2651557989&idx=1&sn=74f22c5c721345a6dfc77e1c1b34ab92>
4.  Webpack系列（中）：<https://mp.weixin.qq.com/s?__biz=MzAxODE2MjM1MA==&mid=2651558008&idx=1&sn=447afddf7298c3a5c227c9fe80eeda64>
5.  Webpack系列（下）：<https://mp.weixin.qq.com/s?__biz=MzAxODE2MjM1MA==&mid=2651558041&idx=1&sn=ace886c5c317dd19930d441a273cfb7d>
6.  webpack插件原理分析：<https://mp.weixin.qq.com/s?__biz=MzAxODE2MjM1MA==&mid=2651566366&idx=2&sn=d87ea140ece97f4f3d3adf7af8ed1f29>
7.  Tapable: [https://github.com/webpack/tapable](https://github.com/webpack/tapable)
8. [二十张图片彻底讲明白Webpack设计理念，以看懂为目的](https://juejin.cn/post/7170852747749621791)
