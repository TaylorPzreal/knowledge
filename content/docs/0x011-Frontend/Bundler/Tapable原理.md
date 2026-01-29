
Review
1. 2023-02-26 23:29
2. 2024-09-15


> [!Summary]
> Github <https://github.com/webpack/tapable> 


## 一、Introduction

```js
const {
	SyncHook,
	SyncBailHook,
	SyncWaterfallHook,
	SyncLoopHook,
	AsyncParallelHook,
	AsyncParallelBailHook,
	AsyncSeriesHook,
	AsyncSeriesBailHook,
	AsyncSeriesWaterfallHook,
	AsyncSeriesLoopHook,
} = require("tapable");
```

Each hook can be tapped with one or several functions. How they are executed depends on the hook type:

- **Basic hook** (without “Waterfall”, “Bail” or “Loop” in its name). This hook simply calls every function it tapped in a row.
- **Waterfall**. A waterfall hook also calls each tapped function in a row. Unlike the basic hook, it *passes a return value from each function to the next function*.
- **Bail**. A bail hook allows *exiting early*. When any of the tapped function returns anything, the bail hook will stop executing the remaining ones.
- **Loop**. *When a plugin in a loop hook returns a non-undefined value the hook will restart from the first plugin. It will loop until all plugins return undefined*.


Additionally, hooks can be synchronous or asynchronous. To reflect this, there’re “Sync”, “AsyncSeries”, and “AsyncParallel” hook classes:

- **Sync**. A sync hook can only be tapped with synchronous functions (using `myHook.tap()`). use `myHook.call()` trigger call.
- **AsyncSeries**. An async-series hook can be tapped with synchronous, callback-based and promise-based functions (using `myHook.tap()`, `myHook.tapAsync()` and `myHook.tapPromise()`). They *call each async method in a row*. use `myHook.promise` or `myHook.callAsync` trigger call.
- **AsyncParallel**. An async-parallel hook can also be tapped with synchronous, callback-based and promise-based functions (using `myHook.tap()`, `myHook.tapAsync()` and `myHook.tapPromise()`). However, they run each async method in parallel.

The hook type is reflected in its class name. E.g., `AsyncSeriesWaterfallHook` allows asynchronous functions and runs them in series, passing each function’s return value into the next function.

其他特性
- `HookMap` 
- `intercept` 

## Usage
```sh
npm install --save tapable
```



## Reference
1. [tapable Github](https://github.com/webpack/tapable)
2. [读一读 Tapable 源码](https://juejin.cn/post/7164175171358556173)
