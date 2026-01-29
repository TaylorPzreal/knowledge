
Review
1. 2024-09-30 08:57

> [!Summary]
> 

## 一、Introduction
新架构包括
1. Scheduler：接收到更新，开始调度，高优先级优先进入 Reconciler
2. Reconciler (Render Phase)：为VDOM标记各种flags，找出变化的组件
3. Renderer (Commit Phase)：根据flags执行相应的操作，将变化的组件渲染到页面上

> 整个**Scheduler**与**Reconciler**的工作都在内存中进行。只有当所有组件都完成**Reconciler**的工作，才会统一交给**Renderer**。

Time Slice 原理
每次循环都调用 `shouldYield` 判断当前 Time Slice 是否有剩余时间，没有剩余时间则暂停更新流程，将主线程交给渲染流水线，等待下一个宏任务再继续执行。


Rendering steps
1. **Triggering** a render
2. **Rendering** the component
3. **Committing** to the DOM


## Reference

