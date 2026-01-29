
Review
1. 2024-10-03 07:16

> [!Summary]
> [Github: NodeJS Interview Questions](https://gist.github.com/paulfranco/9f88a2879b7b7d88de5d1921aef2093b) 
> 

## 一、Introduction

1. [ ] Event Loop [[07-NodeJS Event Loop]]
2. [ ] Non-blocking I/O [[15-NodeJS Non blocking IO]]
3. [ ] Modules and npm, Module Resolution [[05-NodeJS Modules]]
4. [x] Streams: [[14-NodeJS Streams]] ✅ 2024-10-03
5. [x] Buffers [[02-NodeJS Buffer]] ✅ 2024-10-03
6. [ ] Error handling [[06-NodeJS Error Handing]]
7. [x] Callbacks, Promises, and Async/Await [[18-nextTick]] ✅ 2024-10-03
8. [x] EventEmitter [[08-EventEmitter]] ✅ 2024-10-03
9. [ ] HTTP module [[16-NodeJS HTTP]] 
10. [ ] ExpressJS/Koa/NextJS [[DeepDiveInto-Koa]] [[DeepDiveInto-Express]] 
11. [ ] 本地调试线上API（线上API映射到本地）
12. [ ] 高性能服务的最佳实践（支持高并发）
13. [ ] 性能优化 [[90-Performance and Tracing]] 
14. [x] Why is Node.js Single-threaded? ✅ 2024-10-03
15. [x] `fork()`  vs  `spawn()` ✅ 2024-10-04
16. [x] What's Libuv? ✅ 2024-10-03
17. [x] Node.js vs JavaScript ✅ 2024-10-03
18. [x] 什么时候使用NodeJS ✅ 2024-10-03
19. [x] readFile vs createReadStream ✅ 2024-10-03
20. [x] 如何处理NodeJS中未捕获的异常 ✅ 2024-10-04
21. [x] NodeJS能否充分利用多核处理器；cluster/fork ✅ 2024-10-03
22. [x] 响应式设计模式（reactor pattern）是什么 ✅ 2024-10-04
23. [ ]  单线程与多线程网络后端相比有哪些好处
24. [x] REPL是什么；Read, Evaluate, Print, Loop ✅ 2024-10-03
25. [x] process.nextTick vs setImmediate ✅ 2024-10-03
26. [x] stub是什么？单元测试里面的代替真实函数，返回指定值 ✅ 2024-10-03
27. [x] 为什么在express中分离“应用程序”和“服务器”是一种好的做法 ✅ 2024-10-04
28. [ ]  yarn vs npm
29. [x] Node.js是单线程吗？ ✅ 2024-10-03
30. [x] Node.js 做耗时的计算时候，如何避免阻塞？// process, threds ✅ 2024-10-03
31. [x] Node.js如何实现多进程的开启和关闭？// fork, cluster ✅ 2024-10-04
32. [x] Node.js可以创建线程吗？`worker_threads` ✅ 2024-10-03
33. [ ]  开发过程中如何实现进程守护的？PM2
34. [ ]  除了使用第三方模块，你们自己是否封装过一个多进程架构?
35. [x] What is WASI? ✅ 2024-10-03
36. [x] What's crypto module? ✅ 2024-10-04
37. [ ] 如何实现断点续传？（上传/下载）
38. [ ] 数据库driver的原理是什么
39. [ ] 什么是机器码(machine code) 
40. [ ] 什么是 `stdin`, `stdout`, `stderr` 
41. [ ] Explain how blocking is prevented in Node.js.
42. [x] How to solve "Process out of Memory Exception" in Node.js ? (`node --max-old-space-size=1024 file.js`) ✅ 2024-10-04
43. [x] How many threads does Node actually create? (1+4) ✅ 2024-10-04
44. [x] vm module use cases; VM(executing JavaScript) ✅ 2024-10-04
45. [x] domain module use cases; @deprecated ✅ 2024-10-04
46. [ ] Why to use Buffers instead of binary strings to handle binary data ?


---

###### Why to use Buffers instead of binary strings to handle binary data ?

**Performance:**

- **Direct memory access:** Buffers offer direct access to underlying memory, eliminating the need for intermediate string encoding and decoding. This results in significantly improved performance for operations like reading, writing, and manipulating binary data.
- **Efficient memory allocation:** Buffers are allocated in fixed-size chunks, which can be more efficient than allocating and deallocating memory for each individual character in a string.
- **Avoidance of encoding/decoding overhead:** When working with binary data, encoding and decoding to and from strings introduces unnecessary overhead, as binary data is already in a suitable format for manipulation. Buffers bypass this overhead, leading to better performance.

**Correctness:**

- **Preservation of binary data integrity:** Buffers ensure that binary data is handled correctly without any unintended modifications or data loss that can occur when converting between binary and string representations.
- **Avoidance of encoding issues:** Different character encodings can lead to unexpected results when working with binary data. Buffers eliminate these issues by working directly with binary data, preventing encoding-related errors.

**Flexibility:**

- **Direct manipulation:** Buffers provide direct access to binary data, allowing you to perform various operations on it, such as copying, slicing, filling, and concatenation, without the need for intermediate string conversions.
- **Compatibility with native modules:** Many native modules expect binary data in Buffer format, making Buffers essential for seamless integration with these modules.
- **Interoperability:** Buffers can be easily converted to and from other data types, such as Typed Arrays and ArrayBuffers, providing flexibility and interoperability with other JavaScript libraries and APIs.

**Readability and Maintainability:**

- **Clarity and intent:** Using Buffers explicitly indicates that you're working with binary data, making your code more readable and easier to understand for other developers.
- **Reduced complexity:** By avoiding string conversions, you can simplify your code and reduce the potential for errors.

**In summary:**

- **Performance:** Buffers offer superior performance for handling binary data due to direct memory access, efficient memory allocation, and avoidance of encoding/decoding overhead.
- **Correctness:** Buffers ensure the integrity of binary data and prevent encoding-related issues.
- **Flexibility:** Buffers provide direct manipulation of binary data, compatibility with native modules, and interoperability with other data types.
- **Readability and Maintainability:** Using Buffers improves code clarity and reduces complexity.


---

###### What is V8 Templates?
**Answer:** A template is a blueprint for JavaScript functions and objects. You can use a template to wrap C++ functions and data structures within JavaScript objects. V8 has two types of templates: Function Templates and Object Templates.

- **Function Template** is the blueprint for a single function. You create a JavaScript instance of template by calling the template’s GetFunction method from within the context in which you wish to instantiate the JavaScript function. You can also associate a C++ callback with a function template which is called when the JavaScript function instance is invoked.
- **Object Template** is used to configure objects created with function template as their constructor. You can associate two types of C++ callbacks with object templates: accessor callback and interceptor callback. Accessor callback is invoked when a specific object property is accessed by a script. Interceptor callback is invoked when any object property is accessed by a script. In a nutshell, you can wrap C++ objects/structures within JavaScript objects.

---

###### How many threads does Node actually create?
> **4 extra threads** are for use by V8. V8 uses these threads to perform various tasks, such as GC-related background tasks and optimizing compiler tasks.

Node.js typically operates on a single thread, known as the "main thread" or "event loop thread". However, the full picture is a bit more nuanced:

1. Main thread: This is the primary thread where the JavaScript code runs and where the event loop operates.
2. Background threads: Node.js uses a pool of background threads (usually 4) to handle asynchronous I/O operations. These threads are part of the `libuv` library, which Node.js uses for its event loop implementation.
3. Worker threads: Since Node.js 10.5.0, there's an experimental Worker Threads API that allows creating additional threads for CPU-intensive tasks.

So, while most Node.js applications primarily run on a single thread, the actual number of threads can vary depending on the specific use case and configuration. By default, it's the main thread plus the libuv thread pool (typically 4 threads).

---

###### Reactor Pattern in NodeJS

**Reactor Pattern** is an idea of non-blocking I/O operations in Node.js. This pattern provides a handler(in case of Node.js, a _callback function_) that is associated with each I/O operation. When an I/O request is generated, it is submitted to a _demultiplexer_.

This _demultiplexer_ is a notification interface that is used to handle concurrency in non-blocking I/O mode and collects every request in form of an event and queues each event in a queue. Thus, the demultiplexer provides the _Event Queue_.

At the same time, there is an Event Loop which iterates over the items in the Event Queue. Every event has a callback function associated with it, and that callback function is invoked when the Event Loop iterates.


---

The time required to run this code in Google Chrome is considerably more than the time required to run it in Node.js Explain why this is so, even though both use the v8 JavaScript Engine.
```js
{
  console.time("loop");
  for (var i = 0; i < 1000000; i += 1) {
    // Do nothing
  }
  console.timeEnd("loop");
}
```

---

1: Stack exploded (Maximum call stack size exceeded)
```js
var EventEmitter = require("events");

var crazy = new EventEmitter();

crazy.on('event1', function () {
    console.log('event1 fired!');
    crazy.emit('event2');
});

crazy.on('event2', function () {
    console.log('event2 fired!');
    crazy.emit('event3');

});

crazy.on('event3', function () {
    console.log('event3 fired!');
    crazy.emit('event1');
});

crazy.emit('event1');
```

2: 正常
```js
var EventEmitter = require('events');

var crazy = new EventEmitter();

crazy.on('event1', function () {
    console.log('event1 fired!');
    setImmediate(function () {
        crazy.emit('event2');
    });
});

crazy.on('event2', function () {
    console.log('event2 fired!');
    setImmediate(function () {
        crazy.emit('event3');
    });

});

crazy.on('event3', function () {
    console.log('event3 fired!');
    setImmediate(function () {
        crazy.emit('event1');
    });
});

crazy.emit('event1');
```

3: out of memory，事件循环被完全阻塞
```js
var EventEmitter = require('events');

var crazy = new EventEmitter();

crazy.on('event1', function () {
    console.log('event1 fired!');
    process.nextTick(function () {
        crazy.emit('event2');
    });
});

crazy.on('event2', function () {
    console.log('event2 fired!');
    process.nextTick(function () {
        crazy.emit('event3');
    });

});

crazy.on('event3', function () {
    console.log('event3 fired!');
    process.nextTick(function () {
        crazy.emit('event1');
    });
});

crazy.emit('event1');
```


## Reference
<https://www.simplilearn.com/tutorials/nodejs-tutorial/nodejs-interview-questions> 
<https://www.geeksforgeeks.org/node-interview-questions-and-answers/> 
<https://www.turing.com/interview-questions/node-js>

