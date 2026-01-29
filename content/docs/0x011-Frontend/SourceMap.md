
Review
1. 2024/04/02
## 简介
SourceMap（源代码映射）是一种文件，用于将转换后的代码映射回原始源代码。它在前端开发中起着重要的作用，特别是在调试和错误追踪方面。

SourceMap 可以帮助开发人员在浏览器中准确地定位和调试原始代码，即使在经过转换、压缩和合并后的代码中也能够追踪到源代码的位置。

SourceMap 的实现原理是通过将源代码和转换后的代码进行映射关联。它通常以 JSON 格式存储，其中包含了源代码文件和转换后的代码文件之间的映射关系。Sourcemap 还可以包含源代码的内容，以便在没有原始源代码文件的情况下进行调试。

SourceMap 在生产环境中也很有用。它可以帮助开发人员在生产环境中进行错误追踪和调试，同时也可以用于代码保护，避免泄露源代码。

## SourceMap工作原理
main.js -> main.js.map

*.js.map
```json
{
  "version" : 3,
  "file": "out.js",
  "sourceRoot": "",
  "sources": ["foo.js", "bar.js"],
  "sourcesContent": [null, null],
  "names": ["src", "maps", "are", "fun"],
  "mappings": "A,AAAB;;ABCDE"
  "ignoreList": [0]
}
```

### Webpack config
```js
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const webpack = require('webpack');
module.exports = {
  mode: 'production',
  entry: './src/index.js',
  output: {
    filename: '[name].js',
    path: path.resolve(__dirname, 'dist'),
  },
  plugins: [
    new HtmlWebpackPlugin(),
    new webpack.SourceMapDevToolPlugin({
      test: /\.js$/,
      publicPath: 'http://127.0.0.1:5500/dist/',
      filename: '[file].map[query]'
    }),
  ],
};
```


webpack devtool difference
1. inline-module-source-map
2. eval
3. cheap-eval-source-map
4. cheap-module-eval-source-map
5. eval-source-map
6. **cheap-source-map**
7. **cheap-module-source-map**
8. **source-map**

[SourceMapDevToolPlugin](https://webpack.js.org/plugins/source-map-dev-tool-plugin/)

### React Native SourceMap
[https://docs.sentry.io/platforms/react-native/sourcemaps/](https://docs.sentry.io/platforms/react-native/sourcemaps/) 

## Reference
- [https://tc39.es/source-map/](https://tc39.es/source-map/) 
- [https://github.com/tc39/source-map](https://github.com/tc39/source-map) 
- [Debug your original code instead of deployed with source maps](https://developer.chrome.com/docs/devtools/javascript/source-maps) 
- [https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/SourceMap](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/SourceMap) 
- [一文搞懂SourceMap以及webpack devtool](https://juejin.cn/post/6960941899616092167) 
