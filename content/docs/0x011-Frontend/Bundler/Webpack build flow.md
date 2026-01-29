
Review
1. 2024-09-15 07:33

> [!Summary]
> 


大致步骤
1. 搭建结构，读取配置参数
2. 用配置参数对象初始化 `Compiler` 对象
3. 挂载配置文件中的插件
4. 执行 `Compiler` 对象的 `run` 方法开始执行编译
5. 根据配置文件中的 `entry` 配置项找到所有的入口
6. 从入口文件出发，调用配置的 `loader` 规则，对各模块进行编译
7. 找出此模块所依赖的模块，再对依赖模块进行编译
8. 等所有模块都编译完成后，根据模块之间的依赖关系，组装代码块 `chunk`
9. 把各个代码块 `chunk` 转换成一个一个文件加入到输出列表
10. 确定好输出内容之后，根据配置的输出路径和文件名，将文件内容写入到文件系统


## 一、Introduction
`Compiler` 是 `Webpack` 运行的引擎，应用运行时常驻，内部每次构建任务都会由一个 `Compilation` 实例完成

*Compiler*对象包含了Webpack环境的所有配置信息，包含options、loaders、plugins等信息。这个对象在 Webpack 启动时被实例化，它是全局唯一的，可以简单地将它理解为Webpack实例。

*Compilation*对象包含了当前的模块资源、编译生成资源、变化的文件等。当Webpack以开发模式运行时，每当检测到一个文件发生变化，便有一次新的Compilation被创建。Compilation对象也提供了很多事件回调供插件进行扩展。通过Compilation也能读取到Compiler对象。


```js
const webpack = require('webpack');

const compiler = webpack({
  // ...
	entry: './index.js',
	output: { filename: 'bundle.js' }
}, (err, stats) => {
	if (err) {
      console.error(err);
      return;
    }

    console.log(
      stats.toString({
        chunks: false, // Makes the build much quieter
        colors: true, // Shows colors in the console
      })
    );
});

compiler.run((err, stats) => {
  // ...

  compiler.close((closeErr) => {
    // ...
  });
});
```


**整体流程分为3个阶段**
1. 初始化阶段
2. 构建阶段
3. 生成阶段

##### 1、初始化阶段：Compiler, Compilation

1. *初始化参数*：根据配置文件、命令行参数和 Webpack 默认配置，合并出完整的参数；
2. *创建Compiler*：用上面构建出的参数，创建 Compiler 对象（全局构建管理器）
3. *初始化Plugins*：遍历 plugins 数组，执行插件的 apply 方法；根据 Webpack 配置动态注入其它插件（比如根据 mode 值注入一些对 development 或 production 模式友好的插件）
4. *开始编译*：执行 `compiler.run()`，生成 ==Compilation== 对象（单次构建管理器，通常 build 只有1个，dev watch 模式，文件每次更新，都会重新创建 compilation 对象）
5. *生成Dependence*：确定入口，根据 entry 配置，执行 `compilation.addEntry()`， 将入口模块转换成 Dependence 对象。

![](./assets/812fab362d7c_a13ba142.png)

> There is the `EntryOptionPlugin` which practically takes in the `entry` object and creates an `EntryPlugin` **for each item** in the object.  The `EntryPlugin` is also the place where an `EntryDependency` is created.

![](./assets/17498bb05e81_885967ce.png)


##### 2、构建阶段：ModuleGraph

1. 根据 entry 对应的 dependence 创建 Module 对象，调用相关 loader，将入口文件的内容转换成标准的 JS；
2. 再调用 JS 解析器 Acorn，将 JS 转换成 AST，并从 AST 中获取该模块的依赖；
3. 递归遍历依赖，重复上面两个步骤的处理，获取所有模块的标准 JS 内容和依赖，最终生成 ModuleGraph 对象。

##### 3、生成阶段：Chunk, ChunkGraph, Asset

1. Chunk, ChunkGraph：遍历 ModuleGraph 对象，根据模块之间的关系，将模块封装进若干 Chunk 中，并根据 Chunk 之间的关系创建 ChunkGraph 对象；
2. 优化：对每一个 Chunk 执行一些优化操作，比如 `tree-shaking`，`splitChunks`，compression等；
3. Asset：将最终处理好的内容，封装成 Asset，写入 output 配置的出口文件中。


开始进入构建时，编译器抛出事件，`EntryPlugin`根据入口配置往`Compilation` 注册入口 `Dependency`，`Compilation` 以此 `Dependency` 为起点进入构建阶段，每个模块构建都会经过四个阶段：
1. 实例化模块
2. 添加模块
3. 构建模块
4. 处理模块依赖


## 解决循环依赖问题




## Reference
1. [Under The Hood](https://webpack.js.org/concepts/under-the-hood/) 
2. [An in-depth perspective on webpack's bundling process](https://angular.love/an-in-depth-perspective-on-webpacks-bundling-process) 
3. [一文吃透 Webpack 核心原理](https://juejin.cn/post/6949040393165996040) 
4. [图解 Webpack 核心源码架构](https://juejin.cn/post/7224402365453074490) 

