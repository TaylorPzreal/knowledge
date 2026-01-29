
Review
1. 2024-10-03 07:39

> [!Summary]
> **I/O** stands for **Input/Output**. It refers to the process of transferring data between a computer system and an external device or network.

## 一、Introduction
> - **File System Operations:** Understand how Node.js performs non-blocking file I/O operations.
> - **Network I/O:** Learn about the non-blocking nature of network operations in Node.js.


## File system
```js
const fs = require('fs');

const buffer = Buffer.alloc(1024); // 创建一个 1024 字节的缓冲区

fs.open('myFile.txt', 'r', (err, fd) => {
    if (err) throw err;

    fs.read(fd, buffer, 0, buffer.length, 0, (err, bytesRead) => {
        if (err) throw err;

        // 将读取到的数据转换为字符串
        const data = buffer.toString('utf8', 0, bytesRead);
        console.log(data);

        // 关闭文件描述符
        fs.close(fd, (err) => {
            if (err) throw err;
        });
    });
});
```

##### File Descriptor
**文件描述符**（File Descriptor）是一个非负整数，它在操作系统中用来标识一个打开的文件。你可以把它想象成一个“门牌号”，每个打开的文件都有一个唯一的描述符，操作系统通过这个号码来找到并操作对应文件。
- **`fs.open('', '', (err, fd)=>{})`：** 打开文件时，返回一个文件描述符。
- **`fs.read(fd)`、`fs.write(fd,)`：** 使用文件描述符进行读写操作。
- **`fs.close(fd)`：** 关闭文件，释放文件描述符。


##### File system (`fs`) flags 优势
详见 [File system flags](https://nodejs.org/docs/latest/api/fs.html#file-system-flags) 
- **精细化控制文件操作：** flags 提供了对文件操作的精细控制，可以根据不同的需求选择不同的打开方式，从而避免不必要的数据覆盖或丢失。
- **提高性能：** 对于频繁的文件操作，合理使用 flags 可以优化性能。例如，使用 `'a'` 方式追加写入，可以避免每次写入都重新定位文件指针。
- **确保数据完整性：** 在某些场景下，需要保证文件数据的完整性，flags 可以帮助我们实现这一目标。例如，使用 `'wx'` 或 `'ax'` 可以避免覆盖已存在的文件。

###### 常用的 flags
- **'r'**: 以==只读==方式打开文件。如果文件不存在，则产生错误。
- **'r+'**: 以==读写==方式打开文件。文件指针位于*文件开头*。如果文件不存在，则产生错误。
- **'w'**: 以==写==方式打开文件。如果文件存在则截断文件；如果文件不存在则创建新文件。
- **'w+'**: 以==读写==方式打开文件。如果文件存在则截断文件；如果文件不存在则创建新文件。
- **'a'**: 以==追加==方式打开文件。如果文件不存在则创建新文件。
- **'a+'**: 以读写方式打开文件。如果文件不存在则创建新文件。文件指针位于*文件末尾*。
- `'a'`: Open file for appending. The file is created if it does not exist.
- `'ax'`: Like `'a'` but fails if the path exists.

`fs.open('filepath', 'flags', cb)` 

```js
const fs = require('fs');

// 以追加方式写入数据
fs.writeFile('myFile.txt', 'Hello, world!', { flag: 'a' }, (err) => {
  if (err) throw err;
  console.log('Data written to file');
});

// 以读写方式打开文件，并从文件开头读取数据
fs.open('myFile.txt', 'r+', (err, fd) => {
  if (err) throw err;
  // ... 读取操作
  fs.close(fd, (err) => {
    if (err) throw err;
  });
});
```

###### 具体场景选择 flags 的原则
- **是否覆盖已有数据：** 如果不想覆盖已有数据，使用 `'a'`、`'ax'` 等追加方式。
- **是否需要读写：** 如果既要读取又要写入，使用 `'r+'`、`'w+'`、`'a+'` 等读写方式。
- **文件是否存在时的处理：** 如果文件不存在，需要创建新文件，可以使用 `'wx'`、`'ax'` 等方式；如果文件存在，需要报错，可以使用 `'x'` 方式。
- **性能优化：** 对于频繁的写入操作，使用 `'a'` 方式可以提高性能。

```js
const fs = require('node:fs');
const path = require('node:path');

fs.open(path.resolve(__dirname, 'myFile.txt'), 'r+', (err, fd) => {
  if (err) throw err;

  // 从第0个字节开始读取10个字节
  const buffer = Buffer.alloc(10);
  const offset = 0;

  fs.read(fd, buffer, 0, 10, offset, (err, bytesRead) => {
    if (err) throw err;
    console.log(buffer.toString());

    // 在第50个字节处写入新数据
    const data = Buffer.from('new data');
    fs.write(fd, data, 0, data.length, 0, (err, written) => {
      if (err) throw err;
    });
  });
});

```

##### `fs.stat()` usage
The `fs.stat(filepath)` method returns an object that contains information about the file, such as the file size, creation date, and modified date.


## Reference

