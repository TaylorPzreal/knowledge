
Review
1. 2024-08-17 10:30

> [!Summary]
> 

## 一、Introduction
`Exiting` is a way of terminating a Node.js process by using node.js process module.


1. Exiting of Script Implicitly
2. Using `process.exit(code)`
3. Using `process.kill(pid)`
4. Using `process.on('event', callback)`
5. Using `process.abort()` 立即终止当前的 Node.js 进程，不进行任何清理操作。由于是突然终止，不会执行任何退出回调或 `process.on('exit')` 事件处理程序。


## Reference
<https://www.knowledgehut.com/blog/web-development/node-js-process-exit>
<https://nodejs.org/docs/latest/api/process.html#process>

