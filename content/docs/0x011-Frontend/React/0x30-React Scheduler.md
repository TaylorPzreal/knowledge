
Review
1. 2024-09-01 07:34

> [!Summary]
> 基于 `scheduler@0.23.0` 
> `scheduler/src/forks/Scheduler.js` 
> 
> Scheduler 作用就是执行回调，把 `react-reconciler` 提供的callback包装到一个任务对象中，在内部维护一个任务队列，优先级高的排在前面。但是低优先级时间已经过期了也会被高优执行，防止*饥饿问题*。

## 一、Introduction
> 根据 Priority 和 Time Slice 实现

React 实现了一套基于 lane 模型的优先级算法，并基于这套算法实现了 `Batched Updates` 、任务打断/恢复机制等低级特性。

2种任务队列
1. 未过期的：timerQueue，依据 `currentTime + delay` 排序
2. 已过期的：taskQueue，依据 task `expirationTime` 排序，值越小优先级越高

`unstable_scheduleCallback` -> 
`requestHostTimeout` 
`requestHostCallback` 


Scheduler Priority
1. NoPriority = 0 // 无优先级
2. ImmediatePriority = 1 // 立刻执行，级别最高
3. UserBlockingPriority = 2 // 用户阻塞级别的优先级
4. NormalPriority = 3 // 正常的优先级
5. IdlePriority = 4 // 较低优先级
6. LowPriority 5 // 最低优先级

> 通过小顶堆实现优先级队列：一颗完全二叉树，堆中每一个节点的值都小于等于其子树的每一个值。

根据任务优先级，确定 timeout 时间

```js
// Times out immediately
var IMMEDIATE_PRIORITY_TIMEOUT = -1;
var USER_BLOCKING_PRIORITY_TIMEOUT = 250;
var NORMAL_PRIORITY_TIMEOUT = 5000;
var LOW_PRIORITY_TIMEOUT = 10000;
var IDLE_PRIORITY_TIMEOUT = maxSigned31BitInt;

var timeout;
switch (priorityLevel) {
	case ImmediatePriority:
	  timeout = IMMEDIATE_PRIORITY_TIMEOUT;
	  break;
	case UserBlockingPriority:
	  timeout = USER_BLOCKING_PRIORITY_TIMEOUT;
	  break;
	case IdlePriority:
	  timeout = IDLE_PRIORITY_TIMEOUT;
	  break;
	case LowPriority:
	  timeout = LOW_PRIORITY_TIMEOUT;
	  break;
	case NormalPriority:
	default:
	  timeout = NORMAL_PRIORITY_TIMEOUT;
	  break;
}

var expirationTime = startTime + timeout;
```

调度时机
1. `requestIdleCallback` ❌ 空闲时间执行，兼容性不好，触发频率不稳定。目的是为了执行低优先级的工作，而不影响高优先级的事件（动画、用户输入）。
2. `requestAnimationFrame` ❌ 每一帧前执行，16ms执行一次，执行频率不高
3. `Generator`, `Async` 具有传染性，`Generator` 执行的中间状态是上下文关联的
4. `setImmediate` ✅
5. `MessageChannel` ✅
6. `setTimeout` ✅


## 二、Lane
> Briefly, Lane is a 32-bit mask flag. Each bit represents a priority and a type of task. The closer the lane is to '0', the higher the priority.

React 中的优先级跟事件相关，被称为 EventPriority 
1. DiscreteEventPriority 离散事件，如 click, focus, `touchstart`
2. ContinuousEventPriority 连续事件，如 drag, `mousemove`, scroll
3. DefaultEventPriority 默认
4. IdleEventPriority 空闲情况

需要将 lane 优先级转换为 scheduler 优先级
1. 将 lane 转换为 EventPriority，`lanesToEventPriority` 
2. 将 EventPriority 转换为 Scheduler 优先级，`switch(lanesToEventPriority(nextLanes))` 


### Lane 优先级定义
Lane是32bit Integer，不同优先级对应不同lane，越低的位代表越高额优先级。

| Name                               | Usage                                                                                                                                                                                  |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| NoLane `00000`                     | Default value                                                                                                                                                                          |
| **SyncLane** `00001`               | ClickEvent, MouseMoveEvent, etc.                                                                                                                                                       |
| InputContinuousHydrationLane `010` | Unknown. It is probably used for [Suspense](https://en.reactjs.org/docs/react-api.html#reactsuspense) and [hydrateroot](https://en.reactjs.org/docs/react-dom-client.html#hydrateroot) |
| **InputContinuousLane** `00100`    | MouseEnter, etc.                                                                                                                                                                       |
| DefaultHydrationLane `01000`       | Unknown. It is probably used for [Suspense](https://en.reactjs.org/docs/react-api.html#reactsuspense) and [hydrateroot](https://en.reactjs.org/docs/react-dom-client.html#hydrateroot) |
| **DefaultLane** `10000`            | It is mainly used for initial rendering.                                                                                                                                               |
| TransitionHydrationLane            | Unknown. It is probably used for [Suspense](https://en.reactjs.org/docs/react-api.html#reactsuspense) and [hydrateroot](https://en.reactjs.org/docs/react-dom-client.html#hydrateroot) |
| **TransitionLane1~16**             | It is used for `startTransition`. React uses a different number each time, and if React previously used TransitionLane16, it will use TransitionLane1.                                 |
| **RetryLane1~5**                   | React uses it when `Suspense` is still loading.                                                                                                                                        |
| IdleHydrationLane                  | Unknown. It is probably used for [Suspense](https://en.reactjs.org/docs/react-api.html#reactsuspense) and [hydrateroot](https://en.reactjs.org/docs/react-dom-client.html#hydrateroot) |
| IdleLane                           | Unknown                                                                                                                                                                                |
| OffscreenLane                      | Unknown. It's probably used for the offscreen feature, which is not implemented yet.                                                                                                   |

###### Automatic Batching (Batched Updates)
基于某一个优先级，计算出属于同一批的所有优先级。
将多次更新流程合并为一次处理的技术。

> 基于 `expirationTime` 的优先级算法，对于高优先级先执行没有问题，但不能很好的支持并发更新，也不能很好的表示批。耦合了“优先级”和“批”两个概念。

基于 Lane 的算法
1. 以优先级为依据，对 update 进行排序
2. 表达“批”的概念：通过位运算，很容易计算是否属于同一批

### Lanes
lanes 代表一个或多个 lane 的集合

1. TransitionLanes
2. root.pendingLanes
3. root.suspendedLanes
4. root.pingedLanes
5. root.expiredLanes
6. 实现 entangle
7. 不依赖优先级划定“批”


## Reference
1. [一篇长文帮你彻底搞懂React的调度机制原理](https://segmentfault.com/a/1190000039101758) 
