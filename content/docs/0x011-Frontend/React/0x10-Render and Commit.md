
Review
1. 2024-09-01 07:32

> [!Summary]
> 

## 一、Introduction
Rendering steps
1. **Triggering** a render
2. **Rendering** the component
3. **Committing** to the DOM


Lifecycle
1. mount
2. update


### Rendering
- **On initial render,** React will call the root component.
- **For subsequent renders,** React will call the function component whose state update triggered the render.


Rendering阶段可以被暂停，通过调用下面的方法/组件
1. `Suspense` 
2. `useTransition` -> `startTransition` 


### Commiting
After rendering (calling) your components, React will modify the DOM.

- **For the initial render,** React will use the [`appendChild()`](https://developer.mozilla.org/docs/Web/API/Node/appendChild) DOM API to put all the DOM nodes it has created on screen.
- **For re-renders,** React will apply the minimal necessary operations (calculated while rendering!) to make the DOM match the latest rendering output.

**React only changes the DOM nodes if there’s a difference between renders.**

3 个字阶段
1. beforeMutation
2. mutation
3. layout


## Reference
1. <https://react.dev/learn/render-and-commit> 
2. [How React 18 Improves Application Performance](https://vercel.com/blog/how-react-18-improves-application-performance) 
