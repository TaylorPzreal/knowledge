
Review
1. 2024-08-17 17:27

> [!Summary]
> Stream <https://nodejs.org/api/stream.html> 
> Cheatsheet <https://devhints.io/nodejs-stream> 
> 
> 适用场景
> 1. File operations: Reading from or writing to large files.
> 2. Network communications
> 3. Data transformation: Compressing, encrypting, or modifying data on-the-fly.
> 4. Media processing: Handing audio or video data.
> 5. 实时生成的数据: log files, AIGC ...

## 一、Introduction
> Streams are a way to handle reading/writing files, network communications, or any kind of end-to-end information exchange in an efficient way.

Streams are a type of data handling methods and are used to read, write or transform chunks of data piece by piece *without keeping it in memory all at once*. 

Streams basically provide two major **advantages** compared to other data handling methods:
1. **Memory efficiency:** you don’t need to load large amounts of data in memory before you are able to process it
2. **Time efficiency:** it takes significantly less time to start processing data as soon as you have it, rather than having to wait with processing until the entire payload has been transmitted

There are four types of streams in Node.js.
- **Readable**: `Data emitter` streams from which data can be read. 
- **Writable**: `Data receiver` streams to which we can write data. 
- **Duplex**: `Emitter and receiver` streams that are both Readable and Writable. An example could be a ==TCP socket==.
- **Transform**: `Emitter and receiver independent` streams that can modify or transform the data as it is written and read. They are often used for data manipulation tasks like *compression*, *encryption*, or *formatting*.

Multiple streams can be chained together using `pipe()` method.


##### 1.1: 创建 Readable Stream
###### 使用 `fs.createReadStream`

```js
const fs = require('fs');

const readStream = fs.createReadStream('input.txt');

readStream.on('data', (chunk) => {
  console.log(`Received ${chunk.length} bytes of data.`);
});

readStream.on('end', () => {
  console.log('Finished reading the file.');
});

readStream.on('error', () => {
  console.log('some error.');
});
```

events
1. `data` 
2. `end` 
3. `error` 
4. `pause` 
5. `readable` 
6. `resume` 

> - 可读流默认处于 paused 态。
> - 一旦添加 data 事件监听，它就变为 flowing 态。
> - 删掉 data 事件监听，paused 态。
> - pause() 可以将它变为 paused。
> - resume() 可以将它变为 flowing。

###### 使用 `Readable` 

```js
const { Readable } = require('stream');
const myStream = new Readable({
  read() {
    this.push('Hello, world!');
    this.push(null); // 结束标志
  }
});
```

###### 通过pipe
```js
const zlib = require('zlib');
const fs = require('fs');

const readableStream = fs.createReadStream('data.txt');
const gzipStream = zlib.createGzip();
const writableStream = fs.createWriteStream('data.gz');

readableStream.pipe(gzipStream).pipe(writableStream);
```

##### 1.2: 创建 Writable Stream

Events
1. `close` 
2. `error` 
3. `finish`  
4. `drain` 
5. `pipe` 
6. `unpipe` 

###### 使用 `fs.createWriteStream` 

```js
const fs = require('fs');

const writeStream = fs.createWriteStream('output.txt');

const isOk = writeStream.write('Hello, ');
writeStream.write('World!');
writeStream.end();
writeStream.on('finish', () => { console.log('Finished writing'); });
```

> `write` 过快，会积压数据，此时会返回 false，需要监听 `drain` event，才能继续执行 `write` method.

###### `http` 基于 Stream 实现
```js
const http = require('http');
const fs = require('fs');

const server = http.createServer((req, res) => {
  if (req.url === '/upload') {
    // 处理文件上传
    const writeStream = fs.createWriteStream('uploaded.file');
    req.pipe(writeStream);
  } else if (req.url === '/download') {
    // 处理文件下载
    const readStream = fs.createReadStream('file.txt');
    readStream.pipe(res);
  }
});

server.listen(3000);
```

###### 使用 `Writable` 
```js
const {Writable} = require('stream')

const outStream = new Writable({
  // 如果别人调用，我们做什么
  write(chunk, encoding, callback) {
    console.log(chunk.toString())
    // 进入下一个流程
    callback()
  }
});

process.stdin.pipe(outStream);
```


##### 1.3: 使用 `pipe()` method
> 将一个可读流的输出连接到另一个可写流的输入

```js
const fs = require('fs');

const readStream = fs.createReadStream('input.txt');
const writeStream = fs.createWriteStream('output.txt');

readStream.pipe(writeStream);
```


```js
const fs = require('fs');
const zlib = require('zlib');

const readStream = fs.createReadStream('input.txt');
const writeStream = fs.createWriteStream('output.txt.gz');
const gzip = zlib.createGzip();

readStream.pipe(gzip).pipe(writeStream);
```


##### 1.4: 创建 Duplex Stream

```js
const {Duplex} = require('stream')

const inoutStream = new Duplex({
  write(chunk, encoding, callback) {
    console.log(chunk.toString())
    callback()
  },
  read(size) {
    this.push(String.fromCharCode(this.currentCharCode++));
    if (this.currentCharCode > 90) {
      this.push(null); // 表示数据结束
    }
  }
})

inoutStream.currentCharCode = 65;
process.stdin.pipe(inoutStream).pipe(process.stdout);
```

##### 1.5: 创建 Transform Stream
> 先接收数据，在转出数据

```js
const fs = require('fs');
const readStream = fs.createReadStream('input.txt');
const writeStream = fs.createWriteStream('output.txt');
const { Transform } = require('stream');

const upperCaseTransform = new Transform({
  transform(chunk, encoding, callback) {
    this.push(chunk.toString().toUpperCase());
    callback();
  }
});

// 使用转换流
readStream.pipe(upperCaseTransform).pipe(writeStream);
```

##### 1.6: 使用 `stream.PassThrough` 
> PassThrough 是一种特殊的 Transform Stream，它不对数据进行任何转换，只是简单地将输入数据传递给输出。

**使用场景:**
- **日志记录:** 将流中的数据写入日志文件。
- **错误处理:** 对流中的错误进行处理。
- **数据统计:** 统计流中数据的数量、大小等信息。

```js
const fs = require('fs');
const stream = require('stream');

const readStream = fs.createReadStream('test.txt');
const writeStream = fs.createWriteStream('output.txt');
const passThroughStream = new stream.PassThrough();

readStream.pipe(passThroughStream).pipe(writeStream);

passThroughStream.on('data', (chunk) => {
  console.log(`Observed chunk: ${chunk.toString()}`);
});

passThroughStream.on('end', () => {
  console.log('Observation complete.');
});

passThroughStream.write('**ok**');

```


## Backpressure
背压(Backpressure): 这是流的一个重要概念,用于处理数据生产速度快于消费速度的情况。Node.js会自动处理背压,确保快速的数据源不会压垮较慢的数据目标。


## Reference
<https://nodesource.com/blog/understanding-streams-in-nodejs>

