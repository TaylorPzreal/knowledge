
#NodeJS #cmd #CLI 

Review
1. 2023-03-19 07:17
2. 2024-08-16

## 一、Introduction
用户方便开发CMD工具。

> Command Line Applications are applications that can be run from the command line. They are also called CLI (Command Line Interface) applications. Users can interact with clients entirely by terminal commands.


## 二、Configuration
### 2.1: Environment variables
Environment variables allow us to manage the configuration of our applications separately from our codebase. Separating configurations makes it easier for our application to be deployed in different environments.

> 1. The variables are written in **uppercase** letters (e.g. PORT).
> 2. The `.env` file _should never_ be committed to the source code repository. We must place the file into the `.gitignore` file.


1. `process.env`
2. `dotenv`
3. `dotenvx`

#### `process.env`
In Node.js, `process.env` is a global variable that is injected during runtime. It is a view of the state of the system environment variables. When we set an environment variable, it is loaded into `process.env` during runtime and can later be accessed.

#### `dotenv`
`dotenv` is a zero-dependency module that loads environment variables from a `.env` file into `process.env`. Storing configuration in the environment separate from code is based on The Twelve-Factor App methodology.

```sh
npm i dotenv
```

```.env
# This is a comment
S3_BUCKET="YOURS3BUCKET"
SECRET_KEY="YOURSECRETKEYGOESHERE"
PRIVATE_KEY="-----BEGIN RSA PRIVATE KEY-----
...
Kh9NV...
...
-----END RSA PRIVATE KEY-----"
```

```js
const dotenv = require('dotenv')
const result = dotenv.config()

if (result.error) {
  throw result.error
}

console.log(result.parsed)
console.log(process.env.S3_BUCKET)
```

preload `dotenv`
We can use the `--require` (`-r`) command line option to preload dotenv. By doing this, we do not need to require and load dotenv in the application.
```sh
node -r dotenv/config preload.js
```

Basic parsing engine rules:
- `BASIC=basic` becomes `{BASIC: 'basic'}`
- empty lines are skipped
- lines beginning with `#` are treated as comments
- `#` marks the beginning of a comment (unless when the value is wrapped in quotes)
- empty values become empty strings (`EMPTY=` becomes `{EMPTY: ''}`)
- inner quotes are maintained (think JSON) (`JSON={"foo": "bar"}` becomes `{JSON:"{\"foo\": \"bar\"}"`)
- whitespace is removed from both ends of unquoted values (`FOO= some value`  becomes `{FOO: 'some value'}`)
- single and double quoted values are escaped (`SINGLE_QUOTE='quoted'` becomes `{SINGLE_QUOTE: "quoted"}`)
- single and double quoted values maintain whitespace from both ends (`FOO=" some value "` becomes `{FOO: ' some value '}`)
- backticks are supported (`` BACKTICK_KEY=`This has 'single' and "double" quotes inside of it.` ``)
- double quoted values expand new lines (`MULTILINE="new\nline"` becomes
```txt
{MULTILINE: 'new
line'}
```

#### use .env demo
- HTTP port
- database connection string
- location of static files
- endpoints of external services

### 2.2: 参数处理
1. `commander.js`
2. `process.argv`


#### `commander.js`
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


### 2.3: Prompts
1. `process.stdin`
2. `Readline` <https://nodejs.org/docs/latest/api/readline.html> 
3. `Inquirer` <https://github.com/SBoudrias/Inquirer.js>
4. `enquirer` <https://github.com/enquirer/enquirer>
5. `prompts`  <https://github.com/terkelg/prompts>

The `process.stdin` property returns a stream connected to stdin (fd 0). It is a net.Socket (which is a Duplex stream) unless fd 0 refers to a file, in which case it is a Readable stream.

```js
console.log('请输入数据');
process.stdin.on('data', (chunk) => {
  const input = chunk.toString();
  console.log(`You typed: ${input}`);
});
```

```js
const fs = require('fs');
const process = require('process');

const readStream = fs.createReadStream('input.txt');
readStream.pipe(process.stdin);

process.stdin.on('data', (chunk) => {
  console.log(`Read from file: ${chunk}`);
});
```


```js
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('What is your name? ', (answer) => {
  console.log(`Hello, ${answer}!`);
  rl.close();
});
```

### 2.4: Print
1. `stdout` / `stderr`
2. `chalk`
3. `figlet` <https://github.com/patorjk/figlet.js> 
4. `cliprogress` <https://github.com/npkgz/cli-progress> 
5. `console.table` 

#### `cli-progress`
easy to use progress-bar for command-line/terminal applications
https://github.com/npkgz/cli-progress

```sh
yarn add cli-progress
```

**Features**
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

#### console colors
1. Chalk <https://github.com/chalk/chalk>
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


### 2.5: watch files change
1. `fs.watch()` 
2. watcher
3. nodemon
4. chokidar <https://github.com/paulmillr/chokidar> 



## Reference
<https://github.com/motdotla/dotenv#readme>
<https://zetcode.com/javascript/dotenv/>
<https://www.knowledgehut.com/blog/web-development/node-environment-variables>
[# How To Handle Command-line Arguments in Node.js Scripts](https://www.digitalocean.com/community/tutorials/nodejs-command-line-arguments-node-scripts)

