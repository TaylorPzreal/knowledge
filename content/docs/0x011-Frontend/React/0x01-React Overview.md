
Review
1. 2021-08-24
2. 2023-02-04
3. 2024-06-01


> [!Summary]
> React is one of the most popular javascript libraries for building beautiful and interactive user interfaces which is created by **Jordan Walke** and other colleagues at Facebook in 2013.
> 
> 特点：Declarative + Component-Based
> 
> Features
> 1. Virtual DOM
> 2. JSX
> 3. Server-side rendering
> 4. Unidirectional data flow
> 5. Reusable components
> 
> React 属于*应用级*框架：每次更新流程都是从应用的根节点开始，遍历整个应用。
> 
> Version History，详见 [endoflife.date](https://endoflife.date/) 
> 1. v18.0.0 *2022/03/29*
> 2. v17.0.0 2020/10/20
> 3. v16.14.0 2020/10/14
> 4. v16.0.0 2017/09/26


> [!Summary] 前端框架主要解决的性能问题
> 1. 减少Dom操作
> 2. 批量更新
> 3. 异步更新
> 
> **频繁操作Dom导致的性能问题**
> 1. DOM 操作容易触发 Reflow(改变元素的几何属性), Repaint(改变元素的视觉属性)
> 2. 渲染线程和JS主线程是独立线程，造成通信开销
> 3. 频繁操作，导致CPU开销较高，容易掉帧
> 4. 事件处理：为大量DOM元素绑定事件处理器会增加浏览器的负担，因为每个事件处理器都会占用内存并需要浏览器跟踪
> 5. HTML元素集合的实时性：HTML元素集合如 `document.getElementsByTagName` 返回的是实时集合，每次访问都会重新计算
> 
> 最终影响
> 1. ***CPU使用率过高***
> 2. 内存占用激增
> 3. 渲染卡顿和掉帧
> 4. JS主线程被阻塞，无法响应用户交互


##### Awesome Blogs
1. React RFCs <https://github.com/reactjs/rfcs> 
2. React New Website: https://react.dev/ 
3. React Old Website: https://legacy.reactjs.org/ 
4. In depth dev: https://indepth.dev/react 
5. React技术揭秘 https://react.iamkasong.com/ 
6. React秘密 https://segmentfault.com/blog/react-secret 
7. 图解React原理 https://7kms.github.io/react-illustration-series/ 
8. React原理 https://buptlhuanyu.github.io/ReactNote/docs/react/react/intro 
9. 实现React / ReactDOM / React Reconciler https://github.com/lizuncong/mini-react 
10. [101 React Tips & Tricks for Beginners to Experts](https://dev.to/_ndeyefatoudiop/101-react-tips-tricks-for-beginners-to-experts-4m11) 

##### Books
1. Advanced React
2. Fluent React(2024) <https://www.oreilly.com/library/view/fluent-react/9781098138707/> 
3. Building Large Scale Web Apps - A React Field Guide
4. React设计原理

## 一、Introduction
React is a library. It lets you put components together, but it doesn’t prescribe how to do routing and data fetching.

```txt
UI = f(state)
```

React is also an architecture. Frameworks that implement it let you fetch data in asynchronous components that run on the server or even during the build. Read data from a file or a database, and pass it down to your interactive components.

React is a JavaScript library for building user interfaces.
- **Declarative:** React makes it painless to create interactive UIs. Design simple views for each state in your application, and React will efficiently update and render just the right components when your data changes. Declarative views make your code more predictable, simpler to understand, and easier to debug.
- **Component-Based:** Build encapsulated components that manage their own state, then compose them to make complex UIs. Since component logic is written in JavaScript instead of templates, you can easily pass rich data through your app and keep the state out of the DOM.
- **Learn Once, Write Anywhere:** We don't make assumptions about the rest of your technology stack, so you can develop new features in React without rewriting existing code. React can also render on the server using [Node](https://nodejs.org/en) and power mobile apps using [React Native](https://reactnative.dev/).

> **JSX** stands for JavaScript XML. It allows writing HTML in JavaScript and converts the HTML tags into React elements.

> **模板分类**
> 1. 扩展 HTML 语法：前端框架使用 HTML 描述UI，就扩展HTML语法，使它能够描述逻辑
> 2. 扩展 ES 语法：前端框架使用ES描述逻辑，扩展ES语法，使它能够描述UI

> React follows a **declarative approach** to rendering components, which means that developers specify what a component should look like, and React takes care of rendering the component to the screen. This is in contrast to an **imperative approach**, where developers would write code to manually manipulate the DOM (Document Object Model) to update the UI.


**Props vs State**
Props (short for “properties”) and state are both plain JavaScript objects. While both hold information that influences the output of component render, they are different in one important way: props get passed to the component (similar to function parameters) whereas state is managed within the component (similar to variables declared within a function).

### React skills
1. JavaScript: As React is a JavaScript library, a strong understanding of JavaScript fundamentals is essential.
2. React basics: Learn about **components**, **state**, and **props** in React. Understand how to use them to build user interfaces.
3. Components: Learn how to create and manage components in React. Know how to reuse components, pass data between components, and manage component state.
4. React Hooks: Get familiar with React Hooks, such as **useState**, **useEffect**, and **useContext**, which allow you to manage component state and add interactivity to your components.
5. React **Router**: Learn how to handle routing in a React application. Know how to use the React Router library to navigate between different pages of a React application.
6. **Redux**: Study the Redux library to manage state in large-scale React applications. Understand how to use Redux to maintain a single source of truth for your application's state.
7. Styling in React: Know how to style React components using CSS, styled-components, or other styling libraries.
8. React performance optimization: Learn how to optimize React applications for performance, such as using **lazy loading**, **memoization**, and avoiding unnecessary re-renders.
9. Testing in React: Know how to write and run tests for React components and applications, using testing libraries like **Jest** and Enzyme.
10. React ecosystem: Stay up-to-date with the latest trends and best practices in the React ecosystem. Follow blogs, forums, and social media to stay informed.

### Quick Start
Vite <https://vitejs.dev/>
```sh
npm create vite@latest my-react-app -- --template react-ts
```

Create React App <https://create-react-app.dev/>

```sh
npx create-react-app my-app
```

Chrome extensions
1. React Developer Tools
2. 

```tsx
import { createRoot } from 'react-dom/client';

function HelloMessage({ name }) {
  return <div>Hello {name}</div>;
}

const root = createRoot(document.getElementById('container'));
root.render(<HelloMessage name="Taylor" />);
```


### 状态管理（State management）
1. Redux/Redux Toolkit [[Redux]] 基于 Context 实现
2. MobX
3. **Zustand** [https://github.com/pmndrs/zustand](https://github.com/pmndrs/zustand)  基于 `useSyncExternalStore` 实现
4. `storeon` [https://github.com/storeon/storeon](https://github.com/storeon/storeon) 
5. `Valtio` [https://github.com/pmndrs/valtio](https://github.com/pmndrs/valtio) 
6. Rematch
7. **Jotai** <https://github.com/pmndrs/jotai> 
8. Recoil
9. `Hookstate` 
10. `Valtio` <https://github.com/pmndrs/valtio> 


### 组件库（Component）
1. Antd <https://github.com/ant-design/ant-design>
2. Material UI
3. Chakra UI <https://github.com/chakra-ui/chakra-ui>
4. Shadcn UI <https://ui.shadcn.com/>
5. Concis <https://github.com/fengxinhhh/Concis>

Form
1. `formik` <https://formik.org/> 
2. React Hook Form <https://react-hook-form.com/> 
3. TanStack Form <https://tanstack.com/form> 

Animations
1. `framer-motion` <https://www.framer.com/motion/> 

Headless UI
<https://headlessui.com/> 

### 路由管理（Routers）
1. React Router
2. Tanstack Router

### React18 new features
首先 `ReactDOM.render` 这个 API 在新版本中不被支持了，需要我们修改为如下码：

```jsx
// Before
import { render } from 'react-dom';
const container = document.getElementById('app');
render(<App tab='home' />, container);
```

```jsx
// After
import { createRoot } from 'react-dom/client';
const container = document.getElementById('app');
const root = createRoot(container);
root.render(<App tab='home' />);
```


### 数据请求
1. `swr` 
2. `ReactQuery` 

### 测试
[@testing-library/react](https://testing-library.com/docs/react-testing-library/intro/) 

E2E Tests
1. `Cypress`
2. `Playwright`

Mock
MSW(Mock Service Worker) <https://mswjs.io/> 
Mock Service Worker is an API mocking library that allows you to write client-agnostic mocks and reuse them across any frameworks, tools, and environments.

### 国际化（Internationalize）
1. `Format.js` 
2. `Lingui` 
3. `react-i18next` 

### 重构
1. `VSCode Glean`
2. `VSCode React Refactor` 


## Reference
1. The React Cheatsheet for 2021‬: https://www.freecodecamp.org/news/react-cheatsheet-with-real-world-examples/
2. React changelog https://github.com/facebook/react/blob/main/CHANGELOG.md#1820-june-14-2022 
3. [https://prodo-dev.github.io/state-management/](https://prodo-dev.github.io/state-management/)
4. <https://legacy.reactjs.org/docs/accessibility.html>


