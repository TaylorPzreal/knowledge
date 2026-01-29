
Review
1. 2024-09-01 07:34

> [!Summary]
> 基于 `scheduler@0.23.0` 
> `scheduler/src/forks/Scheduler.js` 

## 一、Introduction
`unstable_scheduleCallback` -> 
`requestHostTimeout` 
`requestHostCallback` 


Priority
1. ImmediatePriority
2. UserBlockingPriority
3. NormalPriority
4. IdlePriority
5. LowPriority



## Lane
> Briefly, Lane is a 32-bit mask flag. Each bit represents a priority and a type of task. The closer the lane is to '0', the higher the priority.


| Name                         | Usage                                                                                                                                                                                  |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| NoLane                       | Default value                                                                                                                                                                          |
| **SyncLane**                 | ClickEvent, MouseMoveEvent, etc.                                                                                                                                                       |
| InputContinuousHydrationLane | Unknown. It is probably used for [Suspense](https://en.reactjs.org/docs/react-api.html#reactsuspense) and [hydrateroot](https://en.reactjs.org/docs/react-dom-client.html#hydrateroot) |
| **InputContinuousLane**      | MouseEnter, etc.                                                                                                                                                                       |
| DefaultHydrationLane         | Unknown. It is probably used for [Suspense](https://en.reactjs.org/docs/react-api.html#reactsuspense) and [hydrateroot](https://en.reactjs.org/docs/react-dom-client.html#hydrateroot) |
| **DefaultLane**              | It is mainly used for initial rendering.                                                                                                                                               |
| TransitionHydrationLane      | Unknown. It is probably used for [Suspense](https://en.reactjs.org/docs/react-api.html#reactsuspense) and [hydrateroot](https://en.reactjs.org/docs/react-dom-client.html#hydrateroot) |
| **TransitionLane1~16**       | It is used for `startTransition`. React uses a different number each time, and if React previously used TransitionLane16, it will use TransitionLane1.                                 |
| **RetryLane1~5**             | React uses it when `Suspense` is still loading.                                                                                                                                        |
| IdleHydrationLane            | Unknown. It is probably used for [Suspense](https://en.reactjs.org/docs/react-api.html#reactsuspense) and [hydrateroot](https://en.reactjs.org/docs/react-dom-client.html#hydrateroot) |
| IdleLane                     | Unknown                                                                                                                                                                                |
| OffscreenLane                | Unknown. It's probably used for the offscreen feature, which is not implemented yet.                                                                                                   |



## Reference

