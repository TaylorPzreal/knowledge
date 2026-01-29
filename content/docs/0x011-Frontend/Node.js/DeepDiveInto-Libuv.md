
Review
1. 2024-10-04 10:06

> [!Summary]
> 

## 一、Introduction
**Libuv** is a C library that is used to abstract non-blocking I/O operations to a consistent interface across all supported platforms. It provides mechanisms to handle file system, DNS, network, child processes, pipes, signal handling, polling and streaming. It also includes a thread pool for offloading work for some things that can't be done asynchronously at the operating system level.

**libuv** is a high-performance, cross-platform asynchronous I/O library for Node.js and other applications. It provides a flexible and efficient way to handle asynchronous operations, such as file I/O, network I/O, and timers.

**Key Features:**
- **Asynchronous I/O:** libuv handles asynchronous operations efficiently, allowing your application to perform other tasks while waiting for I/O operations to complete.
- **Cross-platform:** libuv supports a wide range of operating systems, including Windows, macOS, Linux, and Unix-like systems.
- **High performance:** libuv is designed for performance and scalability, making it suitable for demanding applications.
- **Thread pool:** libuv uses a thread pool to handle blocking operations, such as file I/O, without blocking the main event loop.
- **Event loop:** libuv provides an event loop for managing asynchronous operations and handling events.
- **Handles and requests:** libuv uses handles and requests to represent asynchronous operations. Handles are long-lived objects that represent resources, while requests are short-lived objects that represent specific operations.
- **Timers:** libuv provides timers for scheduling asynchronous operations to be executed after a certain amount of time.
- **Child processes:** libuv allows you to create and manage child processes, making it easy to run external programs from within your application

### How does libuv work under the hood?
There is only one thread that executes JavaScript code and this is the thread where the event loop is running provided by **libuv**. The execution of callbacks (know that every userland code in a running Node.js application is a callback) is done by the event loop.

Libuv by default creates a thread pool with `four threads` to offload asynchronous work to. Today’s operating systems already provide asynchronous interfaces for many I/O tasks (e.g. AIO on Linux). Whenever possible, libuv will use those asynchronous interfaces, avoiding usage of the thread pool.

The event loop as a process is a set of phases with specific tasks that are processed in a round-robin manner. Each phase has a FIFO queue of callbacks to execute. While each phase is special in its own way, generally, when the event loop enters a given phase, it will perform any operations specific to that phase, then execute callbacks in that phase's queue until the queue has been exhausted or the maximum number of callbacks has executed. When the queue has been exhausted or the callback limit is reached, the event loop will move to the next phase, and so on.

- **timers**: this phase executes callbacks scheduled by `setTimeout()` and `setInterval()`.
- **pending callbacks**: executes I/O callbacks deferred to the next loop iteration.
- **idle, prepare**: only used internally.
- **poll**: retrieve new I/O events; execute I/O related callbacks (almost all with the exception of close callbacks, the ones scheduled by timers, and `setImmediate()`); node will block here when appropriate.
- **check**: `setImmediate()` callbacks are invoked here.
- **close callbacks**: some close callbacks, e.g. `socket.on('close', ...)`.



## Reference

