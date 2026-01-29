

Review
1. 2024-07-26 21:12

> [!本文摘要]
> *"I will finish later!"*
> Functions running in **parallel** with other functions are called **asynchronous**
> **同步与异步**
> - 同步行为：按顺序执行，对应内存中顺序执行的处理器指令；
> - 异步行为：类似于系统中断，即当前进程外部的实体可以触发代码执行；异步行为是为了优化计算量大而时间长的操作；
> 

## 一、Introduction
> Asynchronous programming is a technique that enables your program to start a potentially long-running task and still be able to be responsive to other events while that task runs, rather than having to wait until that task has finished. Once that task has finished, your program is presented with the result.

The trouble with long-running synchronous task

JavaScript program is _single-threaded_. A thread is a sequence of instructions that a program follows. Because the program consists of a single thread, it can only do one thing at a time: so if it is waiting for our long-running synchronous call to return, it can't do anything else.


What we need is a way for our program to:
1. Start a long-running operation by calling a function.
2. Have that function start the operation and return immediately, so that our program can still be responsive to other events.
3. Have the function execute the operation in a way that does not block the main thread, for example by starting a new thread.
4. Notify us with the result of the operation when it eventually completes.

That's precisely what asynchronous functions enable us to do.


**异步编程实现方式**
1. Events
2. callback function: callback hell or pyramid of doom
3. Promise
4. Async/Await
5. Generator
6. 发布订阅（观察者模式）

Depending on the asynchronous operation at hand, it was either backed by an e**vent-based** system or by a **callback-based** system.

For example, the [`XMLHttpRequest` API](https://www.codeguage.com/courses/ajax/introduction), used to dispatch HTTP requests in the background, was completely based on an **event** model, with such events as `readystatechange`, `load`, `error`, `abort`, and so on.

Similarly, the [`setTimeout()` function](https://www.codeguage.com/courses/js/misc-timers#setTimeout), used to set up timers in the background, was based on a **callback** approach.

In the case of an event-based approach, the asynchronous operation would happen in the background and then dispatch events to be ultimately handled in the main thread.

In the case of callbacks, the asynchronous operation would once again happen in the background, but this time directly invoke a callback as soon as it reaches completion (which might represent a success or a failure).

> // ❶ 回调函数
> // 优点：简单、容易理解
> // 缺点：不利于维护，代码耦合高
> 
> // ❷ 事件监听
> // 采用时间驱动模式，取决于某个事件是否发生
> // 优点：容易理解，可以绑定多个事件，每个事件可以指定多个回调函数
> // 缺点：事件驱动型，流程不够清晰
> 
> // ❸ 发布/订阅（观察者模式）
> // 类似于事件监听，但是可以通过‘消息中心’，了解现在有多少发布者，多少订阅者
> 
> // ❹ Promise 对象
> // 优点：可以利用 then 方法，进行链式写法；可以书写错误时的回调函数；
> // 缺点：编写和理解，相对比较难
> 
> // ❺ Generator 函数
> // 优点：函数体内外的数据交换、错误处理机制
> // 缺点：流程管理不方便
> 
> // ❻ async 函数
> // 优点：内置执行器、更好的语义、更广的适用性、返回的是 Promise、结构清晰。
> // 缺点：错误处理机制

### Callbacks
> A callback is a function passed as an argument to another function.
> *"I will call back later!"*

The callback hell is when we try to write asynchronous JavaScript in a way where execution happens visually from top to bottom, creating a code that has a pyramid shape with many }) at the end.

See more [Callback Hell](http://callbackhell.com/)

### Promise
> *"I Promise a Result"*
> "Producing code" is code that can take some time
> "Consuming code" is code that must wait for the result
> A Promise is an Object that links Producing code and Consuming code


```js
const fetchPromise = fetch(
  "https://mdn.github.io/learning-area/javascript/apis/fetching-data/can-store/products.json",
);

fetchPromise
  .then((response) => response.json())
  .then((data) => {
    console.log(data[0].name);
  });
```

详见[[Promise]]

### Async
> _"async and await make promises easier to write"_
> **async** makes a function return a Promise
> **await** makes a function wait for a Promise

```js
async function myDisplay() {  
  let myPromise = new Promise(function(resolve) {  
    resolve("I love You !!");  
  });  
  document.getElementById("demo").innerHTML = await myPromise;  
}  
  
myDisplay();
```


## Reference
introduction: callbacks <https://javascript.info/callbacks>
Promises, async/await <https://javascript.info/async>
[[19异步编程（AsyncAwait）]]
