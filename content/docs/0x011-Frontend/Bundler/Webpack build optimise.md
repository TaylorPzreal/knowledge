

Review
1. 2024-09-15 07:25

> [!Summary]
> 

## 一、Introduction
优化构建效率
1. 持久化缓存：内置cache
2. 并行构建：`thread-loader` 

优化Bundle
1. 压缩：`html-webpack-plugin`, `optimise-css-assets-webpack-plugin` , `cssnano`, `terser` , `image-webpack-loader` 
2. 分包：Entry chunk / Async Chunk / Runtime chunk / `splitChunks` 
3. Tree-Shaking: `useExports`, `sideEffect` 

CSS Tree Shaking
`purgecss-webpack-plugin` 

JS Tree Shaking
`optimization: { useExports: true }`


## Reference

