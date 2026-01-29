
Review
1. 2024-09-15 07:35

> [!Summary]
> <https://webpack.js.org/api/loaders/> 
> 
> 4 种 Loaders
> 1. Synchronous Loaders
> 2. Asynchronous Loaders
> 3. Raw Loaders
> 4. Pitching Loader

## 一、Introduction
- 在 Webpack 进入构建阶段后，首先会通过 IO 接口读取文件内容
- 之后调用 `LoaderRunner` 并将文件内容以 `source` 参数形式传递到 Loader 数组
- source 数据在 Loader 数组内可能会经过若干次形态转换，最终以标准 JavaScript 代码提交给 Webpack 主流程，以此实现内容编译功能

```js
const path = require('path');

module.exports = {
  output: {
    filename: 'bundle.js',
  },
  module: {
    rules: [
	    {
		    enforce: 'pre',
		    test: /\.txt$/,
		    use: 'raw-loader'
		}
    ],
  },
};

```


### Loader Interface
loader 本质上是导出为函数的 JavaScript 模块。[loader runner](https://github.com/webpack/loader-runner) 会调用此函数，然后将上一个 loader 产生的结果或者资源文件传入进去。函数中的 `this` 作为上下文会被 webpack 填充，并且 [loader runner](https://github.com/webpack/loader-runner) 中包含一些实用的方法，比如可以使 loader 调用方式变为异步，或者获取 query 参数。

起始 loader 只有一个入参：资源文件的内容。compiler 预期得到最后一个 loader 产生的处理结果。这个处理结果应该为 `String` 或者 `Buffer`（能够被转换为 string）类型，代表了模块的 JavaScript 源码。另外，还可以传递一个可选的 SourceMap 结果（格式为 JSON 对象）。

如果是单个处理结果，可以在 [同步模式](https://webpack.docschina.org/api/loaders/#synchronous-loaders) 中直接返回。如果有多个处理结果，则必须调用 `this.callback()`。在 [异步模式](https://webpack.docschina.org/api/loaders/#asynchronous-loaders) 中，必须调用 `this.async()` 来告知 [loader runner](https://github.com/webpack/loader-runner) 等待异步结果，它会返回 `this.callback()` 回调函数。随后 loader 必须返回 `undefined` 并且调用该回调函数。


##### Loader demo:
```js
/**
 *
 * @param {string|Buffer} content 源文件的内容
 * @param {object} [map] 可以被 https://github.com/mozilla/source-map 使用的 SourceMap 数据
 * @param {any} [meta] meta 数据，可以是任何内容
 */
function webpackLoader(content, map, meta) {
  // 你的 webpack loader 代码
}

module.exports {
	webpackLoader
}
```

##### 同步 Loaders
```javascript
module.exports = function (content, map, meta) {
  return someSyncOperation(content);
};
```

```javascript
module.exports = function (content, map, meta) {
  this.callback(null, someSyncOperation(content), map, meta);
  return; // 当调用 callback() 函数时，总是返回 undefined
};
```

##### 异步 Loaders
对于异步 loader，使用 [`this.async`](https://webpack.docschina.org/api/loaders/#thisasync) 来获取 `callback` 函数：
```javascript
module.exports = function (content, map, meta) {
  var callback = this.async();
  someAsyncOperation(content, function (err, result) {
    if (err) return callback(err);
    callback(null, result, map, meta);
  });
};
```

```javascript
module.exports = function (content, map, meta) {
  var callback = this.async();
  someAsyncOperation(content, function (err, result, sourceMaps, meta) {
    if (err) return callback(err);
    callback(null, result, sourceMaps, meta);
  });
};
```

##### Row Loader
默认情况下，资源文件会被转化为 UTF-8 字符串，然后传给 loader。通过设置 `raw` 为 `true`，loader 可以接收原始的 `Buffer`。每一个 loader 都可以用 `String` 或者 `Buffer` 的形式传递它的处理结果。complier 将会把它们在 loader 之间相互转换。

适用于图片、iconfont等场景

```javascript
module.exports = function (content) {
  assert(content instanceof Buffer);
  return someSyncOperation(content);
  // 返回值也可以是一个 `Buffer`
  // 即使不是 "raw"，loader 也没问题
};
module.exports.raw = true;
```

##### Pitching Loader
Loaders are **always** called from right to left. There are some instances where the loader only cares about the **metadata** behind a request and can ignore the results of the previous loader. The `pitch` method on loaders is called from **left to right** before the loaders are actually executed (from right to left).

loader **总是** 从右到左被调用。有些情况下，loader 只关心 request 后面的 **元数据(metadata)**，并且忽略前一个 loader 的结果。在实际（从右到左）执行 loader 之前，会先 **从左到右** 调用 loader 上的 `pitch` 方法。如果某个 loader 在 `pitch` 方法中给出一个结果，那么这个过程会回过身来，并跳过剩下的 loader。

```javascript
module.exports = {
  //...
  module: {
    rules: [
      {
        //...
        use: ['a-loader', 'b-loader', 'c-loader'],
      },
    ],
  },
};
```

将会发生这些步骤：
```diff
|- a-loader `pitch`
  |- b-loader `pitch`
    |- c-loader `pitch`
      |- requested module is picked up as a dependency
    |- c-loader normal execution
  |- b-loader normal execution
|- a-loader normal execution
```

if `b-loader` 
```javascript
module.exports = function (content) {
  return someSyncOperation(content);
};

module.exports.pitch = function (remainingRequest, precedingRequest, data) {
  if (someCondition()) {
    return (
      'module.exports = require(' +
      JSON.stringify('-!' + remainingRequest) +
      ');'
    );
  }
};
```

```diff
|- a-loader `pitch`
  |- b-loader `pitch` returns a module
|- a-loader normal execution
```


## 相关介绍
##### Rule.enforce

> [!Summary]
> 有 4 种 loader 类型，loader 有2个阶段 ，Pitching 和 Normal ，在每个阶段执行的时候，如果是同级别 loader，Pitching phase 从左到右执行，Normal phase 从右到左执行

Possible values: `'pre' | 'post'`. Specifies the category of the loader. No value means *normal loader*. There is also an additional category "*inlined loader*" which are loaders applied inline of the import/require.

There are two phases that all loaders enter one after the other:
1. **Pitching** phase: the pitch method on loaders is called in the order `post, inline, normal, pre`. See [Pitching Loader](https://webpack.js.org/api/loaders/#pitching-loader) for details.
2. **Normal** phase: the normal method on loaders is executed in the order `pre, normal, inline, post`. Transformation on the source code of a module happens in this phase.

**disable loader 规则**
- All **normal** loaders can be omitted (overridden) by prefixing `!` in the request.
- All **normal** and **pre** loaders can be omitted (overridden) by prefixing `-!` in the request.
- All **normal**, **post** and **pre** loaders can be omitted (overridden) by prefixing `!!` in the request.


## Reference

