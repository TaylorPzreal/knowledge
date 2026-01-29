
Review
1. 2024-09-01 07:32

> [!Summary]
> Renderer 工作的阶段被称为 commit phase。在 commit phase，会将各种副作用（flags表示）commit（提交）到宿主环境UI中。*不可中断*。
> 
> FiberTree 的切换会在 Mutation 阶段完成后，Layout 阶段还未开始时执行。


## 一、Introduction
commit 阶段的起点开始于 `commitRoot(root)` 的调用。

##### Committing
After rendering (calling) your components, React will modify the DOM.
- **For the initial render,** React will use the [`appendChild()`](https://developer.mozilla.org/docs/Web/API/Node/appendChild) DOM API to put all the DOM nodes it has created on screen.
- **For re-renders,** React will apply the minimal necessary operations (calculated while rendering!) to make the DOM match the latest rendering output.

> **React only changes the DOM nodes if there’s a difference between renders.**

commit phase 可以划分为 3 个子阶段
1. beforeMutation
2. mutation
3. layout


## Reference
1. <https://react.dev/learn/render-and-commit> 
2. [How React 18 Improves Application Performance](https://vercel.com/blog/how-react-18-improves-application-performance) 
