
Review
1. 2020-05-26
2. 2022-12-06
3. 2024-03-29
4. 2024-07-27 09:48

> [!本文摘要]
> 

## 一、Introduction
Promise是对尚不存在结果的一个替身。
1. 执行器(executor)函数是**同步执行**的，因为执行器函数是期约的初始化程序。有2项职责，初始化Promise的异步行为和控制状态的最终转换；
2. Promise的状态是私有的，不能通过JS检测到，也不能被外部JS代码修改。

A JavaScript Promise object can be:
- Pending
- Fulfilled
- Rejected

待定（pending）初始状态，可以**落定（settled）** 为fulfilled, rejected，落定后，不可逆，即使再修改，静默失败。

The Promise object supports two properties: **state** and **result**.
- While a Promise object is "pending" (working), the result is undefined.
- When a Promise object is "fulfilled", the result is a value.
- When a Promise object is "rejected", the result is an error object.

**包含方法**
1. Promise.all();
2. Promise.allSettled();
3. Promise.race();
4. Promise.resolve();
5. Promise.reject(); 
6. .then
7. .catch
8. .finally: 返回一个Promise


`allSettled`
```js
Promise.allSettled() // returns a promise that is fulfilled with an array of promise state snapshots, but only after all the original promises have settled, i.e. become either fulfilled or rejected.

Promise.allSettled([
  Promise.resolve(1),
  Promise.reject(2),
]).then((v) => {
  console.log(v);
});

// Response:
// [
//   { status: 'fulfilled', value: 1 },
//   { status: 'rejected', reason: 2 }
// ]
```

`finally` 返回新Promise，有2种形式：
- onFinally返回了pending promise( `=> new Promise(() => {})`)，或者抛出了错误(throw 'error'，`=> Promise.reject()`)，会返回相应的Promise
- 除此之外，都是表现为父Promise的传递

**非重入特性（non-reentrancy）**
1. 当Promise进入落定状态时，与该状态相关的 **处理程序(.then)** 仅仅会被 **排期**，而非立即执行。跟在添加这个处理程序的代码之后的同步代码一定会在处理程序之前先执行。即使Promise一开始就是与附加处理程序关联的状态，执行顺序也是这样的。这个特性由JavaScript运行时保证。
2. 如果添加处理程序后，同步代码才改变Promise状态，那么处理程序仍然会基于该状态变化表现出非重入特性。
3. 非重入适用于 onResolved/onRejected处理程序、catch处理程序和finally处理程序

`reject`
1. 错误并没有抛到执行同步代码的线程里，而是通过浏览器异步消息队列来处理的。因此`try/catch`块不能捕获该错误。
2. 正常情况下，通过 `throw()` 关键字抛出错误时，JS运行时的错误处理机制会停止抛出错误之后的任何指令
3. 在Promise中抛出错误时，因为错误实际上是从消息队列中异步抛出的，所以并不会阻止运行时继续执行同步指令

**Async/Await**
异步函数（async/await）让同步方式写的代码，能够异步执行。`ES8新增`；
1. 异步函数始终返回Promise对象
2. 使用`async`关键字可以让函数具有异步特征，但总体上其代码仍然是同步求值的；
3. 使用`await`关键字可以暂停异步函数代码的执行，等待Promise解决
4. 通过`try/catch`捕获异步函数的await 返回的错误；也可以通过async函数的catch捕获；
5. 单独的`Promise.reject()`不会被异步函数捕获，而会抛出未捕获错误。对拒绝的Promise使用`await`则会释放（unwrap）错误值。
6. 即使await后面跟着一个立即可用的值，函数的其余部分也会被**异步**求值。

```js
async function foo() {
  console.log(1)
  await Promise.reject(3)
}

foo().catch(console.log)
console.log(2)
// 1 2 3
```

## 二、实现原理
> 思考问题：
> 1. then、catch链中，如果状态都是fulfilled，是如何忽略中间的catch方法的？（同理，出现rejected的时候，是如何忽略第一个catch之前的then方法的？） 


**异步函数的使用场景**
1. 实现`sleep()`
2. 利用平行执行：如果顺序不是必须保证的，那么可以先一次性初始化所有Promise，然后再分别等待他们的结果，虽然Promise没有按着顺序执行，但是`await`按顺序收到了每个Promise的值；
3. 串行执行Promise
4. 栈追踪与内存管理：对于重视性能的应用，优先使用async


```js
Promise.resolve(1, 2, 3, 4).then(console.log) => 1 // 只接受一个参数
```


```js
async function init() {
  const p1 = Promise.resolve(1);
  const p2 = Promise.resolve(2);

  const p1Res = await p1;
  const p2Res = await p2;
  console.log(p1Res, '**', p2Res);
}
init();
```


## Reference
1. [Promisejs.org](https://www.promisejs.org/)
2. [JavaScript Promises - Introduction](https://www.codeguage.com/courses/advanced-js/promises-introduction)
3. [JavaScript Promises - Basics](https://www.codeguage.com/courses/advanced-js/promises-basics)
4. [Promises Chaining](https://www.codeguage.com/courses/advanced-js/promises-chaining)
5. [Promises Error Handing](https://www.codeguage.com/courses/advanced-js/promises-error-handling)
6. https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise
7. https://juejin.im/entry/56c46015c24aa800528da4d5
8. allSettled: https://tc39.es/proposal-promise-allSettled/
9. Promise/A+:https://promisesaplus.com/
10. Promise Implementing: https://www.promisejs.org/implementing/
11. 手写Promise原理，最通俗易懂的版本 https://juejin.cn/post/6994594642280857630
12. JavaScript Visualized: Promise Execution https://www.lydiahallie.com/blog/promise-execution
