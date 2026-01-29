
Review
1. 2020-08-07
2. 2024-07-29 13:49

> [!Summary]
> Render Props 指一种在 React 组件之间使用一个值为函数的 prop 共享代码的简单技术

## 一、Introduction
The term ‘render props’ refers to a technique for sharing code between React components using a prop whose value is a function.

A component with a render prop takes a function that returns a React element and calls it instead of implementing its own render logic.

```jsx
<DataProvider render={data => (
  <h1>Hello {data.target}</h1>
)} />
```

  

使用 Render Props 来解决横切关注点（Cross-Cutting Concerns）
render prop 是一个用于告知组件需要渲染什么内容的函数 prop。

将 Render Props 与 React.PureComponent 一起使用时要小心
为了绕过这一问题，有时你可以定义一个 prop 作为实例方法



## Reference
<https://www.robinwieruch.de/react-render-props/>
<https://www.patterns.dev/react/render-props-pattern>

