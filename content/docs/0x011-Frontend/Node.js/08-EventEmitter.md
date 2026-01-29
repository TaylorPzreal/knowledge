
Review
1. 2024-08-13 07:51

> [!Summary]
> EventEmitter 是发布订阅模式在 Node.js 中的具体实现，它通过事件、监听器、发布和订阅等机制，实现了对象之间松耦合的通信。

## 一、Introduction

```ts
import EventEmitter from 'node:events';

const eventEmitter = new EventEmitter();

const handler = (num: number) => {
  console.log('started', num);
}

eventEmitter.on('start', handler);

eventEmitter.emit('start', 111);

eventEmitter.off('start', handler);

eventEmitter.emit('start', 111);

eventEmitter.removeAllListeners('start'); // 取消所有 start 事件监听
```

- `emit` is used to trigger an event
- `on` is used to add a callback function that's going to be executed when the event is triggered
- `once()`: add a **`one-time` listener**
- `removeListener()` / `off()`: remove an event listener from an event
- `removeAllListeners()`: remove all listeners for an event


## Reference
- <https://www.digitalocean.com/community/tutorials/using-event-emitters-in-node-js>
- <https://nodejs.org/en/learn/asynchronous-work/the-nodejs-event-emitter>

