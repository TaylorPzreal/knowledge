
Review
1. 2024-07-27 17:43

> [!本文摘要]
> **Nested `setTimeout` allows to set the delay between the executions more precisely than `setInterval`.**
> - Zero delay is not zero in fact (in a browser). Zero delay scheduling with `setTimeout(func, 0)` (the same as `setTimeout(func)`) is used to schedule the call “as soon as possible, but after the current script is complete”.

## 一、Introduction
> - `setTimeout` allows us to run a function once after the interval of time.
> - `setInterval` allows us to run a function repeatedly, starting after the interval of time, then repeating continuously at that interval.


### `setTimeout`
```js
let timerId = setTimeout(func|code, [delay], [arg1], [arg2], ...);
clearTimeout(timerId);
```

```js
function sayHi(phrase, who) {
  alert( phrase + ', ' + who );
}

setTimeout(sayHi, 1000, "Hello", "John"); // Hello, John
```

**not recommended**
```js
setTimeout("alert('Hello')", 1000);
```


### `setInterval`
```js
let timerId = setInterval(func|code, [delay], [arg1], [arg2], ...);
clearInterval(timerId);
```


```js
let i = 1;
setInterval(function() {
  func(i++);
}, 100);
```

> **The real delay between `func` calls for `setInterval` is less than in the code!**
> That’s normal, because the time taken by `func`'s execution “consumes” a part of the interval.

It is possible that `func`'s execution turns out to be longer than we expected and takes more than 100ms.

In this case the engine waits for `func` to complete, then checks the scheduler and if the time is up, runs it again _immediately_.

In the edge case, if the function always executes longer than `delay` ms, then the calls will happen without a pause at all.


> **The nested `setTimeout` guarantees the fixed delay (here 100ms).**
> That’s because a new call is planned at the end of the previous one.


For `setInterval` the function stays in memory until `clearInterval` is called.

There’s a side effect. A function references the outer lexical environment, so, while it lives, outer variables live too. They may take much more memory than the function itself. So when we don’t need the scheduled function anymore, it’s better to cancel it, even if it’s very small.


### Zero delay setTimeout
There’s a special use case: `setTimeout(func, 0)`, or just `setTimeout(func)`.

This schedules the execution of `func` as soon as possible. But the scheduler will invoke it only after the currently executing script is complete.



## Reference
Scheduling: setTimeout and setInterval <https://javascript.info/settimeout-setinterval>

