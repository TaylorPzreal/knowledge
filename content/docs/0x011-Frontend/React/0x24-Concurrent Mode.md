
Review
1. 2024-08-21 07:47

> [!Summary]
> *Concurrent Features* can often be used without fully adopting *Concurrent Mode*
> 
> With Concurrent Rendering, React can interrupt, pause, resume, or abandon a render. This allows React to respond to the user interaction quickly even if it is in the middle of a heavy rendering task.
> 
> 并不是真正的并发执行，（类似于单核的操作系统），通过时间分片（Time Slice，将任务拆分成更小的单位）、优先级调度（通过Lane实现，高优先级可以打断低优先级任务）、可中断（shouldYield）等功能实现的感觉上是并发的效果。更准确的说是一种“协同多任务”或“伪并发”

## 一、Introduction
Concurrent React, previously referred to as Concurrent Mode, is a set of new features in React that allows React to *interrupt the rendering process to consider more urgent tasks*, making it possible for React to be more responsive to user input and produce smoother user experiences. It lets React keep the UI responsive while rendering large component trees by splitting the rendering work into smaller chunks and spreading it over multiple frames.


渲染模式发展阶段
1. Sync Mode：同步
2. Async Mode：过渡期，引入工作分块概念
3. Concurrent Mode：
4. Concurrent Features：*渐进式Concurrent Mode*；由Concurrent Mode支持的具体功能。升级到 Concurrent Mode 工作量较大，React团队正在推动这些特性的渐进式采用，使得开发者可以在不完全采用Concurrent Mode的情况下使用部分并发特性。

### Concurrent Features
#### 背景
In our testing, we’ve upgraded thousands of components to React 18. What we’ve found is that nearly all existing components “just work” with concurrent rendering, without any changes. *However, some of them may require some additional migration effort*. Although the changes are usually small, you’ll still have the ability to make them at your own pace. The new rendering behavior in React 18 is **only enabled in the parts of your app that use new features.**

> Concurrent Features 是渐进升级，不需要直接升级到 Concurrent Mode，在 react 18 中就可以使用并发特性的方案。

React 18 使用下面的方法，会自动启用 Concurrent Features
- `Suspense` for data fetching
- `useTransition` hook
- `useDeferredValue` hook
- `startTransition` method



## Reference
1. [React v18.0](https://react.dev/blog/2022/03/29/react-v18) 
2. [Performance Optimization with React 18 Concurrent Rendering](https://curiosum.com/blog/performance-optimization-with-react-18-concurrent-rendering) 

