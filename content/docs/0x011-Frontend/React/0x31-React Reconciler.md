#协调器 

Review
1. 2024-09-30 11:28

> [!Summary]
> Reconciler 工作的阶段在 React 内部被称为 `render phase` 。根据 `Scheduler` 调度的结果，执行 `performSyncWorkOnRoot` or `performConcurrentWorkOnRoot` 
> 
> Reconciler 支持异步可中断

## 一、Introduction
##### 功能
1. 输入：提供 API (`sheduleUpdateOnFiber`) 给外界调用
2. 注册Scheduler：与 Scheduler 交互，注册调度任务 (`ensureRootIsScheduled`)
3. 执行回调：执行 `performSyncWorkOnRoot` or `performConcurrentWorkOnRoot`，构造 FiberTree，创建新的FiberTree，提交（commitRoot）给 Renderer
4. 输出：Renderer（`react-dom`, `react-native`） 渲染页面


##### 流程
###### Rendering
- **On initial render,** React will call the root component.
- **For subsequent renders,** React will call the function component whose state update triggered the render.

Reconciler 的流程，采用 DFS 的顺序构建 workInProgress Fiber Tree，整个过程分为“递”与“归”两个阶段，分别对应 `beginWork` 和 `completeWork` 方法。

`beginWork` 会根据当前 fiberNode 创建下一级 fiberNode，在 update 阶段标记 Placement(新增、移动)，ChildDeletion（删除）。

`completeWork` 在 mount 阶段会构建 Fiber Tree，初始化属性，在 update 时标记 Update（属性更新），最终执行 flags 冒泡。

当最终 HostRootFiber 完成 completeWork 时，Reconciler的工作流程结束。

此时得到的结果是
1. 代表本次更新的 wip fiber tree
2. 被标记的 flags


> Rendering 阶段可以被暂停，通过调用下面的方法/组件
> 1. `Suspense` 
> 2. `useTransition` -> `startTransition` 

##### eagerState 策略
当一个组件的状态发生变化时，React 通常会重新渲染该组件及其子组件。然而，如果新状态与旧状态相同，那么重新渲染就是没有必要的。eagerState 就是为了解决这个问题而诞生的。

- **提前计算下一个状态：** 在某些特定情况下，React 可以提前计算出下一个状态，并将其与当前状态进行比较。
- **避免不必要的渲染：** 如果新旧状态相同，那么 React 就可以跳过该组件的渲染过程，从而提高性能。

###### 触发条件
- **当前组件没有其他更新：** 也就是说，当前组件的更新队列中只有这一次状态更新。
- **更新队列中只有一个更新：** 如果有多个更新，那么无法确定最终的状态，也就无法提前计算。

##### Bailout 策略
> Reconciler 阶段执行

命中 Bailout 策略，可以复用子 FiberNode，可以跳过子树的 beginWork。eagerState 算是一种 Bailout 的优化方式。

满足条件
1. oldProps === newProps
2. Legacy Context (old Context API) 没有变化
3. fiberNode.type 没有变化
4. 当前 fiberNode 没有更新发生

相关性能优化API
1. `React.memo()` 
2. shouldComponentUpdate
3. PureComponent

##### reconciliation

> 执行 beginWork ，进入 `mountChildFibers` or `reconcileChildFibers` 

> *reconcile 流程的本质*，是对比 current fiberNode 与 JSX 对象，生成 workInProgress fiberNode。

对比算法（diffing algorithm）规则
1. 只对同级元素进行Diff
2. 两个不同类型的元素会产生不同的树
3. 开发者可以通过 key 来暗示子元素在不同的渲染下能够保持稳定

Diff算法可细分为
1. 单节点 diff
2. 多节点 diff

单节点 diff 需要考虑
1. 节点复用问题
2. 多余节点删除

多节点 diff 需要考虑
1. 节点复用问题
2. 节点的增删
3. 节点的移动


## Reference

