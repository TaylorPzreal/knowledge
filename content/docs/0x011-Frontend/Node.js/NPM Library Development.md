
#NPM 

Review
1. 2023/08/09
2. 2023-10-11 07:41

## 一、Introduction

1. 支持TypeScript
2. 支持CommonJS
3. 支持ESModule
4. 支持unit tests
5. Implementing security checks
6. Automating version management and publishing


```js
 // webpack.config.js
const path = require('path');

module.exports = {
  mode: 'production',
  entry: './src/index.ts',

  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'mylib.js',
    libraryTarget: 'umd',
    globalObject: 'this'
  },

  module: {
    rules: [
      {
        test: /\.ts$/,
        use: 'ts-loader',
        exclude: /node_modules/
      }
    ]
  },

  resolve: {
    extensions: ['.ts', '.js']
  },

  externals: {
    // 不打包这些导入的包,使其在运行时从环境中导入
  },

  experiments: {
    outputModule: true
  }
}
```

Rollup
[https://gist.github.com/aleclarson/9900ed2a9a3119d865286b218e14d226](https://gist.github.com/aleclarson/9900ed2a9a3119d865286b218e14d226)
[https://blog.logrocket.com/using-rollup-package-library-typescript-javascript/](https://blog.logrocket.com/using-rollup-package-library-typescript-javascript/)

```js
import dts from 'rollup-plugin-dts'
import esbuild from 'rollup-plugin-esbuild'

const name = require('./package.json').main.replace(/\.js$/, '')

const bundle = config => ({
  ...config,
  input: 'src/index.ts',
  external: id => !/^[./]/.test(id),
})

export default [
  bundle({
    plugins: [esbuild()],
    output: [
      {
        file: `${name}.js`,
        format: 'cjs',
        sourcemap: true,
      },
      {
        file: `${name}.mjs`,
        format: 'es',
        sourcemap: true,
      },
    ],
  }),
  bundle({
    plugins: [dts()],
    output: {
      file: `${name}.d.ts`,
      format: 'es',
    },
  }),
]
```


## Reference
1. [How to make a beautiful, tiny npm package and publish it](https://www.freecodecamp.org/news/how-to-make-a-beautiful-tiny-npm-package-and-publish-it-2881d4307f78/)
2. [Best practices for creating a modern npm package with security in mind](https://snyk.io/blog/best-practices-create-modern-npm-package/)
