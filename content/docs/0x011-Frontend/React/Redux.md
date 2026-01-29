
Review
1. 2020/08/05
2. 2021/01/29
3. 2024-08-06 08:00


> [!Summary]
> redux <https://github.com/reduxjs/redux>
> redux-toolkit(RTK) <https://github.com/reduxjs/redux-toolkit> ***new*** 
> react-redux <https://github.com/reduxjs/react-redux>


> [!info]
> 1. 架构
> 2. 运行流程
> 3. 中间件运行机制

## 一、Introduction
> Redux is a JS library for predictable and maintainable global state management.

> Redux is really:
> - A single store containing "global" state
> - Dispatching plain object actions to the store when something happens in the app
> - Pure reducer functions looking at those actions and returning immutably updated state

Redux is a pattern and library for managing and updating application state, using events called "**actions**". It serves as a centralized store for state that needs to be used across your entire application, with rules ensuring that the state can only be updated in a predictable fashion.

Redux是一个模式和库，使用被称为“actions”的事件，来管理和更新应用程序的全局state。被当作全局集中的state存储，用规则确保只能被可预测的方式更新。

Data flows through a Redux app: "**one-way data flow**"
![](./assets/01cc19823255_f9cacb99.gif)


The Redux core is a very small and deliberately unopinionated library. It provides a few small API primitives:
- `createStore` to actually create a Redux store
- `combineReducers` to combine multiple slice reducers into a single larger reducer
- `applyMiddleware` to combine multiple middleware into a store enhancer
- `compose` to combine multiple store enhancers into a single store enhancer

### Why you might want to use it?
The patterns and tools provided by Redux make it easier to understand when, where, why, and how the state in your application is being updated, and how your application logic will behave when those changes occur. 

**Redux is more useful when:**
* You have large amounts of application state that are needed in many places in the app
* The app state is updated frequently over time
* The logic to update that state may be complex
* The app has a medium or large-sized codebase, and might be worked on by many people


### Key Redux terms and concepts
#### State
In redux, the *state* is a centralised object tree containing the information used by the application. The only way to modify the state is by _dispatching actions_.

#### Actions
An *action* is a **plain JavaScript object** that has a type field. You can think of an action as an event that describes something that happened in the application.

An action creator is a function that creates and returns an action object.

#### Reducers
A *reducer* is a function that receives the current state and an action object, decides how to update the state if necessary, and returns the new state: `(state, action) => newState`.

#### Store
The current Redux application state lives in an object called the store .

#### Dispatch
The Redux store has a method called *dispatch*. The only way to update the state is to call store.dispatch() and pass in an action object. 

#### Selectors
Selectors are functions that know how to extract specific pieces of information from a store state value. 

#### Subscribe


### react-redux


## Redux middleware
### Redux Middleware
- redux-thunk
- redux-promise
- [[Redux-Saga]]
- redux-observable
- …

**redux-thunk & redux-saga & redux-primise & redux-observable**
Async action creators are especially convenient for server rendering. You can create a store, dispatch a single async action creator that dispatches other async action creators to fetch data for a whole section of your app, and only render after the Promise it returns, completes. Then your store will already be hydrated with the state you need before rendering.

- You can use [redux-promise](https://github.com/acdlite/redux-promise) or [redux-promise-middleware](https://github.com/pburtchaell/redux-promise-middleware) to dispatch Promises instead of functions.
- You can use [redux-observable](https://github.com/redux-observable/redux-observable) to dispatch Observables.
- You can use the [redux-saga](https://github.com/yelouafi/redux-saga/) middleware to build more complex asynchronous actions.
- You can use the [redux-pack](https://github.com/lelandrichardson/redux-pack) middleware to dispatch promise-based asynchronous actions.

Asynchronous middleware like [redux-thunk](https://github.com/gaearon/redux-thunk) or [redux-promise](https://github.com/acdlite/redux-promise) wraps the store's [dispatch()](https://redux.js.org/api/store#dispatchaction) method and allows you to dispatch something other than actions, for example, functions or Promises. Any middleware you use can then intercept anything you dispatch, and in turn, can pass actions to the next middleware in the chain. For example, a Promise middleware can intercept Promises and dispatch a pair of begin/end actions asynchronously in response to each Promise.

**redux生态**
reduxsauce <[https://github.com/jkeam/reduxsauce](https://github.com/jkeam/reduxsauce)>


## Reference
1. redux-promise-middleware: https://github.com/pburtchaell/redux-promise-middleware
2. redux-saga: https://github.com/redux-saga/redux-saga/
3. redux-observable: https://github.com/redux-observable/redux-observable/
4. redux-promise: https://github.com/redux-utilities/redux-promise
5. redux-thunk: https://github.com/reduxjs/redux-thunk
6. redux-loop: https://github.com/redux-loop/redux-loop
7. thunkvspromisevssaga: https://juejin.cn/post/6844903504427892750
8. redux-saga漫谈: https://www.yuque.com/lovesueee/blog/redux-saga#apyvym
9. [Redux 4ways](https://medium.com/react-native-training/redux-4-ways-95a130da0cdc)
10. [Redux Middleware Comparison: Thunk, Sagas, Observable & Loop](https://sandstorm.de/de/blog/post/async-redux-middleware-comparison.html)
11. [A beginners guide to setting up redux-saga with Typescript **using reduxsauce**](https://tech.groww.in/a-beginners-guide-to-setting-up-redux-saga-with-typescript-using-reduxsauce-67740a6cc168)

