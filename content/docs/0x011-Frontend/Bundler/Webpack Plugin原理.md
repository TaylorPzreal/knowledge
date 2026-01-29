
Review
1. 2024-09-15 07:39

> [!Summary]
> 

## 一、Introduction
- Webpack 插件是一个带有 `apply` 函数的类，`constructor(ops)` 中的 opts 参数可以获取传给插件的参数
- Webpack 在启动时会调用插件对象的 apply 函数，并以参数方式传递核心对象 `compiler`
- compiler 对象可以触发多种钩子 Hook (Webpack5 暴露了多达 200+ 个 Hook)，表示在 webpack 构建过程的哪个阶段执行插件方法，比如：
    - `compiler.hooks.compilation`：Webpack 刚启动完，创建出 compilation 对象后触发（参数：当前编译的 compilation 对象）
    - `compiler.hooks.make`：正式开始构建时触发（当前编译的 compilation 对象）
    - `compilation.hooks.onEmit`：完成代码构建与打包操作，准备将产物发送到输出目录之前触发（当前编译的 compilation 对象）
    - `ompiler.hooks.done`：编译完成后触发（stats 对象）
- Hook 有多种调用方式，比如
    - `tap`：当钩入到编译(compile) 阶段时，只有同步的 tap 方法可以使用
    - `tapAsync/tapPromise`：对于可以使用 AsyncHook 的 run 阶段， 则需使用 tapAsync 或 tapPromise（以及 tap）方法
- 在 Webpack 运行过程中，随着构建流程的推进会触发各个钩子回调，并传入上下文参数，每个钩子传递的上下文参数不同，但主要包含如下几种类型
    - `complation`：单次构建管理器
    - `compiler`：全局构建管理器
    - `module`：资源模块
    - `chunk`：模块封装容器
    - `stats`：构建过程收集到的统计信息
- webpack 为上述的上下文参数提供了多种 Side Effect 的交互接口，插件通过调用上下文接口、修改上下文状态等方式「篡改」构建逻辑，从而将扩展代码「勾入」到 Webpack 构建流程中，比如
    - `compilation.assets`：获取或修改产物列表
    - `compilation.errors/wranings`：输出错误/警告信息，处理异常信息
    - `compilation.warnings`：输出警告信息

```js
// 编写插件的重点：
// 1. Hook 调用时机
// 2. Hook 回调传递的上下文参数
class MyWebpackPlugin {
  constructor(opts) {}
  apply(compiler) {
    compiler.hooks.emit.tapAsync(this.name, (compilation, cb) => {});
  }
}
```

## Reference

