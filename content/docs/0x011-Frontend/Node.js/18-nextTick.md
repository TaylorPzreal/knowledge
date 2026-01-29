
Review
1. 2024-08-13 08:00

> [!Summary]
> `process.nextTick()` 在当前执行栈清空后，下一轮事件循环的「立即」执行阶段被调用，优先级最高。有自己的 nextTick Queue。属于特殊微任务。

## 一、Introduction
Every time the event loop takes a full trip, we call it a **tick**.

When we pass a function to `process.nextTick()`, we instruct the engine to invoke this function at the end of the current operation, before the next event loop tick starts:

```js
process.nextTick(() => {
  // do something
});

```

The event loop is busy processing the current function code. When this operation ends, the JS engine runs all the functions passed to `nextTick` calls during that operation.

It's the way we can tell the JS engine to process a function asynchronously (after the current function), but as soon as possible, not queue it.

Calling `setTimeout(() => {}, 0)` will execute the function at the end of next tick, much later than when using `nextTick()` which prioritizes the call and executes it just before the beginning of the next tick.

Use `nextTick()` when you want to make sure that in the next event loop iteration that code is already executed.

```js
console.log('Hello => number 1');

setImmediate(() => {
  console.log('Running before the timeout => number 3');
});

setTimeout(() => {
  console.log('The timeout running last => number 4');
}, 0);

process.nextTick(() => {
  console.log('Running at next tick => number 2');
});

```


## Reference
<https://nodejs.org/en/learn/asynchronous-work/event-loop-timers-and-nexttick>
<https://nodejs.org/en/learn/asynchronous-work/understanding-processnexttick>

