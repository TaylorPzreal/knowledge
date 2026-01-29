
Review
1. 2024-08-07 22:29


> [!Summary]
> Redux-Saga is used for large applications with complex logic.

## 一、Introduction
`redux-saga` is a library that aims to make application side effects (i.e. asynchronous things like data fetching and impure things like accessing the browser cache) easier to manage, more efficient to execute, easy to test, and better at handling failures.

The mental model is that a saga is like a separate thread in your application that's solely responsible for side effects. `redux-saga` is a redux middleware, which means this thread can be started, paused and cancelled from the main application with normal redux actions, it has access to the full redux application state and it can dispatch redux actions as well.

It uses an ES6 feature called Generators to make those asynchronous flows easy to read, write and test.

![](./assets/2b920c89f9de_01d05b36.gif)


```sh
yarn add redux-saga
```

```ts
import { configureStore } from '@reduxjs/toolkit'
import createSagaMiddleware from 'redux-saga'

import reducer from './reducers'
import mySaga from './sagas'

// create the saga middleware
const sagaMiddleware = createSagaMiddleware()

// mount it on the Store
const store = configureStore({
  reducer, 
  middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(sagaMiddleware),
})

// then run the saga
sagaMiddleware.run(mySaga)

// render the application
```




## Reference


> [!Summary] 名词解释
> **Sagas**
> Sagas/workers are the side-effects we want to run when a particular action is dispatched. These are *generator functions* that run some asynchronous logic like API calls, I/O operations etc.
> 
> **Watchers**
> Watchers watch for action dispatch and fork a saga/worker on that action (if mentioned). Watchers make use of *effect creators* which tell the watcher when to fork the saga.

