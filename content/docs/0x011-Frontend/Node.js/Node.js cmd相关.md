
Review
1. 2023-03-19 07:17

## 一、Introduction
用户方便开发CMD工具。


## 二、相关库
### 2.1, commander.js
The complete solution for [node.js](http://nodejs.org/) command-line interfaces.
https://github.com/tj/commander.js

```sh
npm install commander
```

Usage
```js
const { program } = require('commander');

program
  .option('--first')
  .option('-s, --separator <char>');

program.parse();

const options = program.opts();
const limit = options.first ? 1 : undefined;
console.log(program.args[0].split(options.separator, limit));
```


### 2.2, cli-progress
easy to use progress-bar for command-line/terminal applications
https://github.com/npkgz/cli-progress

```sh
yarn add cli-progress
```

#### Features
-   **Simple**, **Robust** and **Easy** to use
-   Full customizable output format (various placeholders are available)
-   Single progressbar mode
-   Multi progessbar mode
-   Custom Bar Characters
-   FPS limiter
-   ETA calculation based on elapsed time
-   Custom Tokens to display additional data (payload) within the bar
-   TTY and NOTTY mode
-   No callbacks required - designed as pure, external controlled UI widget
-   Works in Asynchronous and Synchronous tasks
-   Preset/Theme support
-   Custom bar formatters (via callback)
-   Logging during multibar operation

```js
const cliProgress = require('cli-progress');

// note: you have to install this dependency manually since it's not required by cli-progress
const colors = require('ansi-colors');

// create new progress bar
const b1 = new cliProgress.SingleBar({
    format: 'CLI Progress |' + colors.cyan('{bar}') + '| {percentage}% || {value}/{total} Chunks || Speed: {speed}',
    barCompleteChar: '\u2588',
    barIncompleteChar: '\u2591',
    hideCursor: true
});

// initialize the bar - defining payload token "speed" with the default value "N/A"
b1.start(200, 0, {
    speed: "N/A"
});

// update values
b1.increment();
b1.update(20);

// stop the bar
b1.stop();
```

### 2.3, console color
1. Chalk
2. colors
3. clc-color

自定义
```js
const Color = {
  Reset: "\x1b[0m",
  Bright: "\x1b[1m",
  Dim: "\x1b[2m",
  Underscore: "\x1b[4m",
  Blink: "\x1b[5m",
  Reverse: "\x1b[7m",
  Hidden: "\x1b[8m",
  
  FgBlack: "\x1b[30m",
  FgRed: "\x1b[31m",
  FgGreen: "\x1b[32m",
  FgYellow: "\x1b[33m",
  FgBlue: "\x1b[34m",
  FgMagenta: "\x1b[35m",
  FgCyan: "\x1b[36m",
  FgWhite: "\x1b[37m",
  FgGray: "\x1b[90m",
  
  BgBlack: "\x1b[40m",
  BgRed: "\x1b[41m",
  BgGreen: "\x1b[42m",
  BgYellow: "\x1b[43m",
  BgBlue: "\x1b[44m",
  BgMagenta: "\x1b[45m",
  BgCyan: "\x1b[46m",
  BgWhite: "\x1b[47m"
  BgGray: "\x1b[100m",
}
```

```js

```

## Reference

