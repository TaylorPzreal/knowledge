
Review
1. 2023-10-10 22:36
2. 2024-10-03

## 一、Introduction
Error handling is a way to find bugs and solve them as quickly as humanly possible. The errors in Node.js can be either operation or programmer errors.


有两种错误
- 编程错误：程序员写出的错误（语法错误、引用错误、类型错误）
- 业务错误：外部因素导致服务不能正常运行（超时、服务端异常、输入错误）


## Error handling techniques
1. `throw` 
2. `try…catch` blocks
3. Callbacks
4. Promises or Async/await 
5. Event emitters(events)
6. Middleware
7. `unhandledRejection`, `uncaughtException`, `uncaughtExceptionMonitor` 

```js
process.on('uncaughtException', function(err) {
  console.log('Caught exception: ' + err);
});
```

```js
process.on('unhandledRejection', (err) => {

})
```


**Common exit codes in Node.js:**

- **0:** The program exited normally.
- **1:** A generic error occurred.
- **12:** The program received a SIGTERM signal (termination signal).
- **13:** The program received a SIGKILL signal (kill signal).
- **14:** The program received a SIGALRM signal (alarm signal).
- **15:** The program received a SIGTERM signal and had a timeout.

**Other possible exit codes:**

- **2:** A syntax error occurred.
- **3:** A runtime error occurred.
- **4:** A system error occurred.
- **5:** A disk full error occurred.
- **6:** An unknown error occurred.


## Reference
- [Node.js Error Handling Made Easy: Best Practices On Just About Everything You Need to Know](https://sematext.com/blog/node-js-error-handling/)
- [Error handling in Node.js](https://blog.logrocket.com/error-handling-node-js/)
