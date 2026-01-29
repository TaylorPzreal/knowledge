
Review
1. 2024-10-06 18:01

> [!Summary]
> - Dependency Graph
> - Module Graph
> - Chunk Graph

## 一、Introduction

- `compiler.make` 阶段：
    - `entry` 文件以 `dependence` 对象形式加入 `compilation` 的依赖列表，`dependence` 对象记录有 `entry` 的类型、路径等信息
    - 根据 `dependence` 调用对应的工厂函数创建 `module` 对象，之后读入 `module` 对应的文件内容，调用 `loader-runner` 对内容做转化，转化结果若有其它依赖则继续读入依赖资源，重复此过程直到所有依赖均被转化为 `module`
- `compilation.seal` 阶段：
    - 遍历 `module` 集合，根据 `entry` 配置及引入资源的方式，将 `module` 分配到不同的 `chunk`
    - 遍历 `chunk` 集合，调用 `compilation.emitAsset` 方法标记 `chunk` 的输出规则，即转化为 `assets` 集合
- `compiler.emitAssets` 阶段：
    - 将 `assets` 写入文件系统


默认生成 Chunk 的规则是
1. 每个 entry 对应一个 chunk
2. 每个动态引入模块（`require.ensure()`, `import()`）会生成一个独立 chunk


存在的问题
多个 entry 可能有相同的依赖（dependence），默认规则打包后，存在冗余。

解决方案
- `CommonsChunkPlugin` 
- `SplitChunksPlugin`：`seal` 阶段优化
- `DllPlugin` &  `DllReferencePlugin` 拆分 bundles 



## Reference

