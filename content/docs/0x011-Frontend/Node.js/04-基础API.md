
Review
1. 2023/02/16
2. 2023-02-25 16:23
3. 2024-08-15

## 一、Introduction


## 二、重要API
1. `__filename` 当前脚本文件路径. The `__filename` in Node returns the filename of the executed code. It gives the **absolute path** of the code file.
2. `__dirname` 当前脚本文件夹路径. The `__dirname` in a node script returns the path of the folder where the current JavaScript file resides. It gives the **absolute path** of the code file.
3. `process.cwd()` The `process.cwd()` method returns the current working directory of the Node.js process

setTimeout
setInterval
setImmediate

**process**
1.  argv
2.  env
3.  stdin
4.  stdout
5.  exit

```js
process.stdin.on('data', e => {

})
```


## Paths
```js
const path = require('node:path');

const notes = '/users/joe/notes.txt';

path.dirname(notes); // /users/joe
path.basename(notes); // notes.txt
path.extname(notes); // .txt

path.basename(notes, path.extname(notes)); // notes, get the file name without the extension by specifying a second argument to `basename`

```

- `dirname`: gets the parent folder of a file
- `basename`: gets the filename part
- `extname`: gets the file extension

`path.resolve` vs `path.join` vs `path.normalize`
1) `path.resolve` creates the absolute path of a relative path.
The method creates absolute path **from right to left** until an absolute path is constructed.

For example:
```javascript
path.resolve('joe.txt'); // '/Users/joe/joe.txt' if run from my home folder
path.resolve('tmp', 'joe.txt'); // '/Users/joe/tmp/joe.txt' if run from my home folder
path.resolve('/etc', 'joe.txt'); // '/etc/joe.txt'

path.resolve('/a', 'b', 'c');     //    C:\a\b\c
path.resolve('/a', '/b', 'c');    //    C:\b\c
path.resolve('/a', '/b', '/c');   //    C:\c
```

If absolute path is not generated, the method using current working directory:
```js
path.resolve('a', 'b', 'c');     //    C:\{current_working_directory}\a\b\c
```

2) `path.join` joins all path and the normalize the result
For example:
```javascript
const name = 'joe';
path.join('/', 'users', name, 'notes.txt'); // '/users/joe/notes.txt'
path.join('/a', '/b', '/c');   //   /a/b/c
path.join('/a', '/b', 'c');    //   \a\b\c
path.join('/a', 'b', 'c');     //   \a\b\c
path.join('a', 'b', 'c');      //   a\b\c
```

3) `path.normalize()` is another useful function, that will try and calculate the actual path, when it contains relative specifiers like `.` or `..`, or double slashes:

```js
path.normalize('/users/joe/..//test.txt'); // '/users/test.txt'
```


`path.relative(from, to)`
The `path.relative()` method returns the relative path from `from` to `to` based on the current working directory. If `from` and `to` each resolve to the same path (after calling `path.resolve()` on each), a zero-length string is returned.

If a zero-length string is passed as `from` or `to`, the current working directory will be used instead of the zero-length strings.

```js
path.relative('/data/orandea/test/aaa', '/data/orandea/impl/bbb');
// Returns: '../../impl/bbb'
```



`path.isAbsolute(path)`

- `path.format(pathObject)` => String 
- `path.parse(path)` => Object, returns an object whose properties represent significant elements of the `path`.

`path.delimiter` Provides the platform-specific path delimiter:
- `;` for Windows
- `:` for POSIX


## `FS Module`
File System or fs module is a built in module in Node that enables interacting with the file system using JavaScript.

- `fs.appendFile()` The `fs.appendFile()` method appends specified content to a file. If the file does not exist, the file will be created:
- `fs.open()` 
- `fs.writeFile()` The `fs.writeFile()` method replaces the specified file and content if it exists. If the file does not exist, a new file, containing the specified content, will be created.

The `fs.open()` method takes a "flag" as the second argument, if the flag is "w" for "writing", the specified file is opened for writing. If the file does not exist, an empty file is created:
```js
var fs = require('fs');  

fs.open('mynewfile2.txt', 'w', function (err, file) {  
  if (err) throw err;  
  console.log('Saved!');  
});
```


```js
var fs = require('fs');  
  
fs.appendFile('mynewfile1.txt', ' This is my text.', function (err) {  
  if (err) throw err;  
  console.log('Updated!');  
})
```

To delete a file with the File System module,  use the `fs.unlink()` method.
To rename a file with the File System module,  use the `fs.rename()` method.


1. `fs-extra` <https://github.com/jprichardson/node-fs-extra>
2. `globby` <https://github.com/sindresorhus/globby>
3. `glob` <https://github.com/isaacs/node-glob>
4. `chokidar` <https://github.com/paulmillr/chokidar>


**Chokidar**
Node.js `fs.watch`:
- Doesn't report filenames on MacOS.
- Doesn't report events at all when using editors like Sublime on MacOS.
- Often reports events twice.
- Emits most changes as `rename`.
- Does not provide an easy way to recursively watch file trees.
- Does not support recursive watching on Linux.

Node.js `fs.watchFile`:
- Almost as bad at event handling.
- Also does not provide any recursive watching.
- Results in high CPU utilization.

Chokidar resolves these problems.

## Reference
<https://nodejs.org/en/learn/manipulating-files/nodejs-file-paths>
<https://nodejs.org/api/path.html>
<https://nodejs.org/api/fs.html>
<https://www.w3schools.com/nodejs/nodejs_filesystem.asp>

