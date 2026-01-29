
#Threads 


Review
1. 2020/03/15
2. 2024-07-17 08:29
3. 2024-08-17


> [!Summary]
> 1. `child_process` : `fork`, `spawn`, `exec` 
> 2. Cluster 
> 3. Worker Threads 


## 一、Introduction
> Node.js is a **single-threaded** language and gives us ways to work parallelly to our main process. Taking note of nowadays multicore system single threading is very memory efficient.

> 进程 `Process` 是计算机中的程序关于某数据集合上的一次运行活动，是系统进行资源分配和调度的基本单位，是操作系统结构的基础，进程是线程的容器。进程是资源分配的最小单位。多进程就是进程的复制（fork），fork 出来的每个进程都拥有自己的独立空间地址、数据栈，一个进程无法访问另外一个进程里定义的变量、数据结构，只有建立了 IPC 通信，进程之间才可数据共享。

> 线程是操作系统能够进行运算调度的最小单位，首先我们要清楚线程是隶属于进程的，被包含于进程之中。**一个线程只能隶属于一个进程，但是一个进程是可以拥有多个线程的**。


> **Node 严格讲并非只有一个线程，通常说的 “Node 是单线程” 是指 JS 的执行主线程只有一个**。

![](./assets/f00abdf89b33_108349a4.webp)

- 应用层： 即 JavaScript 交互层，常见的就是 Node.js 的模块，比如 http，fs
- V8引擎层： 即利用 V8 引擎来解析JavaScript 语法，进而和下层 API 交互
- NodeAPI层： 为上层模块提供系统调用，一般是由 C 语言来实现，和操作系统进行交互 。
- LIBUV层： 是跨平台的底层封装，实现了 事件循环、文件操作等，是 Node.js 实现异步的核心

**Node 进程中并非只有一个线程**。事实上一个 Node 进程通常包含：1 个 Javascript 执行主线程；1 个 watchdog 监控线程用于处理调试信息；1 个 v8 task scheduler 线程用于调度任务优先级，加速延迟敏感任务执行；4 个 v8 线程，主要用来执行代码调优与 GC 等后台任务；以及用于异步 I/O 的 libuv 线程池。


```js
const http = require('http');

const server = http.createServer();
server.listen(3000,()=>{
    process.title='程序员成长指北测试进程';
    console.log('进程id',process.pid)
})

```


## NodeJS实现多进程
多进程可充分利用多核CPU性能
1. `child_process.fork`
2. `cluster` 调用的仍然是 `child_process.fork` 

The Cluster module allows you to easily create child processes that each runs simultaneously on their own single thread, to handle workloads among their application threads.


diff
- `child_process.spawn()`：适用于返回大量数据，例如图像处理，二进制数据处理。
- `child_process.exec()`：适用于小量数据，maxBuffer 默认值为 200 * 1024 超出这个默认值将会导致程序崩溃，数据量过大可采用 spawn。
- `child_process.fork()`： 衍生新的进程，进程之间是相互独立的，每个进程都有自己的 V8 实例、内存，系统资源是有限的，不建议衍生太多的子进程出来，通长根据系统 **CPU 核心数**设置。


## Worker Threads
Worker thread is a continuous parallel thread that runs and accepts messages until it is explicitly closed or terminated. With worker threads, we can achieve a much efficient application without creating a deadlock situation. Workers, unlike children’s processes, can exchange memory.


## Reference
1. [浅析 Node 进程与线程](https://www.infoq.cn/article/g6gcqifgphhetfow2vdd)
2. [深入理解Node.js 中的进程与线程](https://juejin.cn/post/6844903908385488903) 
3. [[07-NodeJS Event Loop]]
4. <https://nodejs.org/api/child_process.html#child-process> 
5. <https://nodejs.org/api/cluster.html#cluster> 
