
Review
1. 2023-10-07 23:03
2. 2024-10-03


> [!Summary]
> - `exports` 是 `module.exports` 的引用。直接修改 `exports` 对象会影响 `module.exports`。但是，如果将 `exports` 重新赋值，则会覆盖 `module.exports`，因此一般建议直接使用 `module.exports`。


## 一、Introduction
We split our code into different files to maintain, organize and reuse code whenever possible. A module system allows us to split and include code and import code written by other developers whenever required. In simple terms, **a module is nothing but a JavaScript file**.

However, starting with version 13.2.0, Node.js has stable support of ES modules.

In Node.js, **Modules** are the blocks of encapsulated code that communicate with an external application on the basis of their related functionality. Modules can be a single file or a collection of multiple files/folders. The reason programmers are heavily reliant on modules is because of their reusability as well as the ability to break down a complex piece of code into manageable chunks. 

**Modules are of three types:**
- Core Modules
- local Modules
- Third-party Modules

**Core Modules:** Node.js has many built-in modules that are part of the platform and come with Node.js installation. These modules can be loaded into the program by using the **required** function.

**Local Modules:** Unlike built-in and external modules, local modules are created locally in your Node.js application. 

**Third-party modules:** Third-party modules are modules that are available online using the Node Package Manager(NPM). These modules can be installed in the project folder or globally. Some of the popular third-party modules are Mongoose, express, angular, and React.

## Comparing CommonJS modules and ES modules syntax
CommonJS module

```js
module.exports.add = function(a, b) {
	return a + b;
} 

module.exports.subtract = function(a, b) {
	return a - b;
}
```

```js
const {add, subtract} = require('./util')

console.log(add(5, 5)) // 10
console.log(subtract(10, 5)) // 5
```

Notice that the `exports` object references the `module.exports`:
```js
console.log(module.exports === exports); // true
```


```js
const add = (a,b)=>{
    return a + b
}

// 默认导出
module.exports = add
```

```js
//------ Main File[main.js] ----

const add = require('./calculate') //name of the desired file
const result = add(2,4)
console.log(result); //Output : 6
```

> [!Important]
> When you use the `require()` function to include a module multiple times, the `require()` function evaluates the module once only at the first call and puts it in a cache.
> 
> From the subsequent calls, the `require()` function uses the exports object from the cache instead of executing the module again.

Before Node.js executes a module, it wraps all the code inside that module with a function wrapper which looks like the following:

```js
(function(exports, require, module, __filename, __dirname) {
    // Module code
});
```


On the other hand, library authors can also simply enable ES modules in a Node.js package by changing the file extensions from `.js` to `.mjs.`

```js
// util.mjs

export function add(a, b) {
    return a + b;
}

export function subtract(a, b) {
    return a - b;
}
```

```js
// app.mjs

import {add, subtract} from './util.mjs'

console.log(add(5, 5)) // 10
console.log(subtract(10, 5)) // 5
```

Another way to enable ES modules in your project can be done by adding a `"type: module"` field inside the nearest `package.json` file (the same folder as the package you’re making):

```json
{
  "name": "my-library",
  "version": "1.0.0",
  "type": "module"
}
```

In this case, all code in that package will be treated as ES modules and the `import`/`export` statements should be used instead of `require()`.

## Pros and cons of using ES modules and CommonJS modules in Node.js

> [!info]
> ES modules are the standard for JavaScript, while CommonJS is the default in Node.js

> [!Warning]
> Older Node.js versions don’t support ES modules

While ES modules have become the standard module format in JavaScript, developers should consider that older versions of Node.js lack support (specifically Node.js v9 and under).

We can build a library that supports both `import` and `require()`, allowing us solve the issue of incompatibility.

```txt
my-node-library
├── lib/
│   ├── browser-lib.js (iife format)
│   ├── module-a.js  (commonjs format)
│   ├── module-a.mjs  (es6 module format)
│   └── private/
│       ├── module-b.js
│       └── module-b.mjs
├── package.json
└── …
```

> [!info]
> CommonJS loads modules synchronously, ES modules are asynchronous


- Dynamic `import()` is supported in both CommonJS and ES modules. It can be used to include ES module files from CommonJS code
- ECMAScript 6 also provides that modules can be loaded from a URL, while CommonJS is limited to relative and absolute file paths. [This new improvement](https://nodejs.org/api/esm.html#esm_https_loader) not only makes loading more complicated, but also slow
- Sources that are in formats Node.js doesn’t understand can be converted into JavaScript. More details can be found [here](https://nodejs.org/api/esm.html#esm_transpiler_loader)
- Support for [extensionless main entry points](https://github.com/WICG/import-maps#extension-less-imports) in ESM has been dropped
- [proposal-import-meta](https://github.com/tc39/proposal-import-meta) provides the absolute URL of the current ES module file. It is currently a stage 4 proposal in the TC39 spec
- Dynamic imports can be used to import both ES and CommonJS modules. In CommonJS modules it can be used to load ES modules. Note that it returns a promise
- A file extension must be provided when using the `import` keyword. Directory indexes (e.g., `'./database/index.js'`) must be fully specified
- Dual CommonJS and ESM are now possible with the use of [conditional exports.](https://nodejs.org/api/esm.html#esm_conditional_exports) Now, Node.js can run ES module entry points, and a package can contain both CommonJS and ESM entry points
- From version 14.13.1, ESM added support for using `node: URLs` to load Node.js built-in modules, allowing built-in modules to be referenced by valid absolute URL strings

Readers should also note that there are still some known differences between ESM and commonJS modules. For example, native modules are not currently supported with ESM imports. Also, the ES module loader has its own kind of caching system and does not rely on `require.cache` found in the commonJS parlance.

Others include the unavailability of `__filename` or `__dirname` found in the commonJS module system. ESM provides other ways of replicating this behavior with the use of `import.meta.url`.

> In all, ECMAScript modules are the future of JavaScript.


## NodeJS Core Modules
1. `http` 
2. `path` 
3. `util` 
4. `fs` 
5. `url` 
6. `querystring` 
7. `stream` 
8. `zlib` 
9. `crypto` 
10. `net` TCP/IP Network
11. `os` 
12. `child_process` 
13. `events` 


##### `url` module
```js
const url = require('node:url');
const sourceUrl = 'https://user:pass@sub.example.com:8080/p/a/t/h?query=string#hash';
const purl = url.parse(sourceUrl);
```

```txt
┌────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                              href                                              │
├──────────┬──┬─────────────────────┬────────────────────────┬───────────────────────────┬───────┤
│ protocol │  │        auth         │          host          │           path            │ hash  │
│          │  │                     ├─────────────────┬──────┼──────────┬────────────────┤       │
│          │  │                     │    hostname     │ port │ pathname │     search     │       │
│          │  │                     │                 │      │          ├─┬──────────────┤       │
│          │  │                     │                 │      │          │ │    query     │       │
"  https:   //    user   :   pass   @ sub.example.com : 8080   /p/a/t/h  ?  query=string   #hash "
│          │  │          │          │    hostname     │ port │          │                │       │
│          │  │          │          ├─────────────────┴──────┤          │                │       │
│ protocol │  │ username │ password │          host          │          │                │       │
├──────────┴──┼──────────┴──────────┼────────────────────────┤          │                │       │
│   origin    │                     │         origin         │ pathname │     search     │ hash  │
├─────────────┴─────────────────────┴────────────────────────┴──────────┴────────────────┴───────┤
│                                              href                                              │
└────────────────────────────────────────────────────────────────────────────────────────────────┘
(All spaces in the "" line should be ignored. They are purely for formatting.)
```


## Reference
1. [CommonJS vs. ES modules](https://blog.logrocket.com/commonjs-vs-es-modules-node-js/)
2. [How Modular Programming Works in Node.js](https://www.freecodecamp.org/news/modular-programming-nodejs-npm-modules/)
3. [Using ES modules in Node.js](https://blog.logrocket.com/es-modules-in-node-today/#commonjsmodulesystem)
4. [CommonJS modules](https://nodejs.org/api/modules.html#modules-commonjs-modules)
5. [Node.js Modules](https://www.javascripttutorial.net/nodejs-tutorial/nodejs-modules/)
6. [CommonJS vs. ES Modules: Modules and Imports in NodeJS](https://reflectoring.io/nodejs-modules-imports/)
7. [JavaScript Module Systems Showdown: CommonJS vs AMD vs ES2015](https://auth0.com/blog/javascript-module-systems-showdown/) 

