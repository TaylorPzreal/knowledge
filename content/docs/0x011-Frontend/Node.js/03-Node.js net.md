
Review
1. 2023-02-18 17:40

## 一、Introduction
The `node:net` module provides an asynchronous network API for creating stream-based TCP or [IPC](https://nodejs.org/docs/latest-v18.x/api/net.html#ipc-support) servers ([`net.createServer()`](https://nodejs.org/docs/latest-v18.x/api/net.html#netcreateserveroptions-connectionlistener)) and clients ([`net.createConnection()`](https://nodejs.org/docs/latest-v18.x/api/net.html#netcreateconnection)).

```js
// server.js
const net = require('net');

const server = net.createServer((socket) => {
	
})

server.listen(3000)
```


**通信方式**
1. 单工通信
2. 半双工通信
3. 全双工通信

特殊情况
- 粘包
- 不完整包



## Reference
[Node.js net API](https://nodejs.org/docs/latest-v18.x/api/net.html)
