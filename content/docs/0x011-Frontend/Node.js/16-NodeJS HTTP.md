
Review
1. 2024-10-03 07:42

> [!Summary]
> HTTP
> HTTPS
> HTTP2

## 一、Introduction
> - **Creating HTTP Servers:** Understand how to create HTTP servers in Node.js.
> - **Handling Requests and Responses:** Learn about handling HTTP requests and sending responses.
> - **HTTP Methods:** Be familiar with different HTTP methods (GET, POST, PUT, DELETE, etc.).


```js
const http = require('http');

const server = http.createServer((req, res) => {
    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.end('Hello, World!');
});

server.listen(3000, () => {
    console.log('Server listening on port 3000');
});
```


## Reference

