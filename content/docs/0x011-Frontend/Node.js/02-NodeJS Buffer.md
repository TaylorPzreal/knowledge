
#Buffer  #Stream #二进制 #Archive 

Review
1. 2023-02-18 15:40
2. 2024-10-03

> [!Summary]
> *在 Node.js 中，Buffer 是一块原始的内存分配，用于存储二进制数据。*
> Buffer class stores raw data similar to an array of integers but corresponds to a raw memory allocation outside the V8 heap. Buffer class is used because pure JavaScript is not compatible with binary data.
> - **Buffer Creation:** Know how to create buffers in Node.js.
> - **Buffer Operations:** Understand common operations performed on buffers.

## 一、Introduction
`Buffer` objects 是用来表示固定长度字节的序列，可以在TCP streams和文件系统操作等上下文中与八位字节流进行交互，使操作二进制数据流或与之交互成为可能。

The `Buffer` class is a subclass of JavaScript's [`Uint8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) class and extends it with methods that cover additional use cases. Node.js APIs accept plain `Uint8Array`s wherever `Buffer`s are supported as well.

The Buffer class in Node.js is used to perform operations on raw binary data. Generally, Buffer refers to the particular memory location in memory. Buffer and array have some similarities, but the difference is array can be any type, and it can be resizable. Buffers only deal with binary data, and it can not be resizable. Each integer in a buffer represents a byte.

###### 为什么需要 Buffer？
- **JavaScript 的局限性：** JavaScript 是一门面向对象的脚本语言，其核心数据类型是字符串。然而，在处理诸如*网络数据*、*文件系统操作*等场景时，我们经常需要处理二进制数据。Buffer 就弥补了 JavaScript 在==处理二进制数据==方面的不足。
- **底层操作：** Buffer 提供了与底层 C++ 的交互能力，可以直接操作内存，这使得 Node.js 在处理 I/O 操作时具有很高的性能。

###### Buffer 的用途
- **网络数据传输：** 在 TCP 流或文件流中，数据以二进制形式传输。Buffer 可以用来存储和处理这些数据。
- **文件系统操作：** 读取文件内容或写入文件时，Buffer 可以用来暂存数据。
- **图像处理：** 图像数据本质上也是二进制数据，Buffer 可以用来存储和操作图像数据。
- **加密解密：** 加密解密算法通常操作二进制数据，Buffer 提供了方便的接口。

### What's binary data?
Each number in a binary, each 1 and 0 in a set are called a **Bit**, which is a short form of **Binary digIT.**

为了存储或表示一段数据，计算机需要将该数据转换为其二进制表示形式。 例如，要存储数字 12，计算机需要将 12 转换为其二进制表示形式，即 1100。

要将任何字符存储在二进制文件中，计算机首先将该字符转换为数字，然后将该数字转换为其二进制表示形式。

比如字符串 `L` 的二进制表示是什么？
计算机首先将该字符转换为数字，然后将该数字转换为二进制表示形式。
```js
'L'.charCodeAt(0) // 76
```
The number 76? That is the number representation or Character Code or Code Point of the character `L`.

==How does it know to use the number 76 to represent `L`?==

**Character Sets（字符集）**
==字符集是已经定义了确切数字代表每个字符的规则==。 我们对这些规则有不同的定义。非常流行的字符集包括 **Unicode** 和 **ASCII**。

**Character Encoding（字符编码）**
正如有一些规则定义什么数字应该代表一个字符一样，也有一些规则定义了该数字应该如何在二进制文件中表示。 具体来说，==用多少位来表示数字。 这称为字符编码==。

字符编码的定义之一是 **UTF-8**。 ==UTF-8 声明字符（characters）应以字节(bytes)为单位进行编码==。 **一个字节是八位一组——八个 1 和 0**。 所以应该用8个1和0来表示二进制中任意字符的Code Point。

> A byte is a set of eight bits — eight 1s and 0s. 

Therefore, 76 should be stored as `01001100`.

> Likewise, computers also have specified rules on how images and videos should be converted or encoded and stored in binaries. The point here is, computers stores all data types in binaries, and this is known as binary data.


### Stream
> Stream in Node.js simply means a sequence of data being moved from one point to the other over time. The whole concept is, you have a huge amount of data to process, but you don’t need to wait for all the data to be available before you start processing it.

Node.js 中的 Stream 仅表示随着时间的推移从一个点移动到另一个点的一个序列数据。 整个概念是，你有大量的数据要处理，但你不需要等到所有数据都可用后再开始处理。

基本上，这个大数据被分解并以块的形式发送。因此，从缓冲区的原始定义来看，这仅意味着二进制数据在文件系统中移动。详见 [[14-NodeJS Streams]] 

> But how exactly does buffer help us interact with or manipulate binary data while streaming? What exactly is this buffer btw?


### Buffer
数据的移动通常是为了处理它或读取它，并根据它做出决策。 但是随着时间的推移，进程可能会接收最少和最多的数据量。 因此，如果数据到达的速率快于进程消耗数据的速率，则多余的数据需要在某个地方等待轮到它被处理。

另一方面，如果进程消耗数据的速度快于数据到达的速度，则较早到达的少数数据需要等待一定数量的数据到达才能被发送出去进行处理。

那个“**等候区（waiting place）**”就是 **缓冲区（Buffer）**！ 它位于计算机中的一个比较小位置，通常在 RAM 中，数据临时收集、等待并最终在流式传输期间发送出去进行处理。

> That is the Buffer to Node.js! Node.js can’t control the speed or time of data arrival, the speed of the stream. It only can decide when it’s time to send out the data. If it’s not yet time, Node.js will put them in the buffer — the “waiting area” — a small location in the RAM, until it’s time to send them out for processing.

Node.js 无法控制数据到达的速度或时间，即流的速度。 它只能决定何时发送数据。 如果还没到时间，Node.js 会将它们放入缓冲区——“等待区”——RAM 中的一个小位置，直到将它们发送出去进行处理。

> 一个典型的例子是当你在线播放视频时，你可以看到缓冲区在起作用。 如果您的互联网连接足够快，流的速度将足够快以立即填满缓冲区并将其发送出去进行处理，然后填充另一个缓冲区并发送出去，然后再发送一个，再发送一个……直到流 完成了。
> 
> 但是如果你的连接速度很慢，在处理完第一组到达的数据后，视频播放器会显示一个加载图标，或者显示文本“正在缓冲”，这意味着收集更多的数据，或者等待更多的数据到达。 当缓冲区填满并进行处理时，播放器会显示数据和视频。 在播放时，更多数据将继续到达并在缓冲区中等待。
> 
> 如果播放器处理完或播放完之前的数据，缓冲区还没有填满，会再次显示“buffering”字样，等待收集更多数据处理。

从缓冲区的原始定义来看，它表明在缓冲区中，我们可以操作或与正在流式传输的二进制数据进行交互。 我们可能与这些原始二进制数据进行什么样的交互？ Node.js 中的 Buffer 实现为我们提供了一个完整的可行列表。

除了 Node.js 会在stream期间自动创建的缓冲区之外，还可以创建和操作自己的缓冲区。

## 二、Buffer使用
**主要方法**
1. **Buffer.from(initialization)** It initializes the buffer with given data.
2. **Buffer.alloc(size)** It creates a buffer and allocates size to it.
3. `buf.write(data)` It writes the data on the buffer.
4. `buf.toString()` It read data from the buffer and returned it.
5. `buf.toJSON()` 
6. `Buffer.isBuffer(object)` It checks whether the object is a buffer or not.
7. `buf.length` It returns the length of the buffer.
8. `buf.copy(targetBuffer[, targetStart[, sourceStart[, sourceEnd]]])` It copies data from one `buf` to targetBuffer.
9. `buf.compare(otherBuffer)`  返回一个数字，表示 **buf** 在 **otherBuffer** 之前(<0)，之后(>0)或相同(eq 0)。
10. `buf.equals(otherBuffer)` 
11. `buf.slice(start = 0, end=buffer.length)` It returns the subsection of data stored in a buffer.
12. `Buffer.concat([buffer1,buffer2])` It concatenates two buffers. `Buffer.concat(list[, totalLength])`

> Buffer 的特点
> - **固定大小：** 创建 Buffer 时，需要指定其大小，一旦创建，大小不可改变。
> - **索引访问：** Buffer 的内容可以通过索引访问，类似于数组。
> - **编码解码：** Buffer 可以将字符串编码为二进制数据，也可以将二进制数据解码为字符串。


```js
import { Buffer } from 'node:buffer';

// Creates a zero-filled Buffer of length 10.
const buf1 = Buffer.alloc(10);

// Creates a Buffer of length 10,
// filled with bytes which all have the value `1`.
const buf2 = Buffer.alloc(10, 1);

// Creates an uninitialized buffer of length 10.
// This is faster than calling Buffer.alloc() but the returned
// Buffer instance might contain old data that needs to be
// overwritten using fill(), write(), or other functions that fill the Buffer's
// contents.
const buf3 = Buffer.allocUnsafe(10);

// Creates a Buffer containing the bytes [1, 2, 3].
const buf4 = Buffer.from([1, 2, 3]);

// Creates a Buffer containing the bytes [1, 1, 1, 1] – the entries
// are all truncated using `(value & 255)` to fit into the range 0–255.
const buf5 = Buffer.from([257, 257.5, -255, '1']);

// Creates a Buffer containing the UTF-8-encoded bytes for the string 'tést':
// [0x74, 0xc3, 0xa9, 0x73, 0x74] (in hexadecimal notation)
// [116, 195, 169, 115, 116] (in decimal notation)
const buf6 = Buffer.from('tést');

// Creates a Buffer containing the Latin-1 bytes [0x74, 0xe9, 0x73, 0x74].
const buf7 = Buffer.from('tést', 'latin1');
```

Once your buffer has been created, you can start interacting with it
```js
buf1.toJSON() // { type: 'Buffer', data: [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] } // an empty buffer
```

```js
buf1.length // 10
```

```js
// Write to a buffer
buf1.write("Buffer really rocks!") 
```

```js
// Decode a buffer
buf1.toString(); // Buffer rea
```


## 三、扩展
### ProtoBuf
详见[[ProtoBuf]]


## Reference
1. [Node.js Buffer API](https://nodejs.org/docs/latest-v18.x/api/buffer.html)
2. [Do you want a better understanding of Buffer in Node.js? Check this out](https://www.freecodecamp.org/news/do-you-want-a-better-understanding-of-buffer-in-node-js-check-this-out-2e29de2968e8/)
3. [protocol-buffers for Node.js](https://www.npmjs.com/package/protocol-buffers)
4. [protobuf](https://github.com/protocolbuffers/protobuf)

