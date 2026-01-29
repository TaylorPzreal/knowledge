
Review
1. 2024-10-01 12:39

> [!Summary]
> 

## 一、Introduction

MobX 的实现原理主要基于以下几个关键技术:
1. 可观察状态（Observable State）: MobX 使用 ES6 的 Proxy 或 Object.defineProperty（在旧版本中）来包装对象和数据，使其变为可观察的。这允许 MobX 拦截对这些对象的读取和写入操作。
2. 依赖收集（Dependency Tracking）: 当一个 reaction（如渲染函数）访问可观察状态时，MobX 会自动追踪这些依赖关系。
3. 派发更新（Change Propagation）: 当可观察状态发生变化时，MobX 会通知所有依赖于该状态的 reactions。
4. 批量更新（Batching Updates）: MobX 使用事务（transactions）来批量处理更新，以避免不必要的重复计算和渲染。
5. 计算值（Computed Values）: MobX 支持派生状态，只有当其依赖的可观察状态发生变化时才会重新计算。


MobX 与 React 集成
1. `mobx-react` 
2. `mobx-react-lite`


在 React 集成方面，MobX 通过以下方式驱动组件更新：
1. 组件包装器: `mobx-react` 提供了 `observer` 高阶组件（HOC）或装饰器，用于包装 React 组件。这个包装器使得组件成为一个 reaction，能够响应其渲染函数中使用的可观察状态的变化。
2. 强制重渲染: 当与组件相关的可观察状态发生变化时，`observer` 包装器会强制组件重新渲染。这是通过调用组件的 `forceUpdate` 方法或更新一个内部状态 (`setState`) 来实现的。
3. 细粒度更新: 由于 MobX 精确地知道哪些数据发生了变化，它可以只更新真正需要更新的组件，而不是整个组件树。
4. 异步调度: MobX 使用微任务（Microtask）来调度更新，这允许多个同步更改被批处理到一个渲染周期中。



## Reference

