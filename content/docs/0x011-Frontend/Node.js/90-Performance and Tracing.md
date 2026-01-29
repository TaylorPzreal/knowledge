

Review
1. 2024-10-03 17:33

> [!Summary]
> 

## 一、Introduction

Measure the performance
- use built-in `--prof` flag
- use perf tool
- use `benchmark.js` 

Tracing
The Tracing Objects are used for a set of categories to enable and disable the tracing. When tracing events are created then tracing objects is disabled by calling tracing.enable() method and then categories are added to the set of enabled trace and can be accessed by calling tracing.categories.



##### 慎用同步方法
如 `fs.readFileSync` 
- **阻塞主线程:** 同步方法会阻塞主线程，影响程序的性能和响应性。
- **影响事件循环:** 同步方法会阻碍事件循环的运行，导致其他异步任务无法及时处理。
- **降低并发性:** 同步方法会降低程序的并发性，因为在执行同步操作时，其他任务无法执行。


> 同步方法的本质
> - **阻塞主线程:** 同步方法会阻塞当前主线程和事件循环，直到操作完成才会返回结果。
> - **直接执行操作:** 同步方法会直接执行 I/O 操作，而不是将任务交给事件循环。

> *详细解释*
> Node.js 使用 libuv 库来处理异步 I/O 操作，对于同步操作，libuv 提供了同步 API 的实现。尽管 Node.js 主要是单线程的，但 libuv 维护了一个线程池。同步操作实际上是在这个线程池中执行的。同步操作直接在当前调用栈中执行，当调用同步方法（如 `fs.readFileSync`）时，Node.js 会阻塞事件循环，操作被发送到 libuv 的线程池中执行，同步操作的结果通过 V8 引擎传递回 JavaScript 代码。

###### 何时使用同步方法：
- **小文件操作:** 读取或写入小文件时，同步方法的性能开销可能并不明显。
- **顺序执行:** 当多个操作必须按照顺序执行时，同步方法可以保证顺序性。
- **简单的任务:** 对于一些简单的任务，同步方法的代码可能更简洁。

###### 何时使用异步方法：
- **I/O密集型任务:** 对于频繁的 I/O 操作，异步方法可以提高程序的性能。
- **并发操作:** 当需要同时处理多个任务时，异步方法可以提高并发性。
- **避免阻塞:** 异步方法可以避免阻塞主线程，提高程序的响应性。


## Reference

