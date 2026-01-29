
Review
1. 2022/04/13
2. 2023/07/29
3. 2023-07-29 07:43

## 一、Introduction


## 二、日志相关组件

### Popular libs
- pm2-logrotate
- [winston](https://github.com/winstonjs/winston) ⭐️⭐️⭐️⭐️⭐️
	- winston-common-scribe
	- winston-common-sentry
	- winston-daily-rotate-file
- [debug](https://github.com/debug-js/debug) ⭐️⭐️⭐️⭐️⭐️ with [supports-color@~8](https://www.npmjs.com/package/supports-color/v/8.1.1)
- [Bunyan](https://github.com/trentm/node-bunyan) 
- [Pino](https://github.com/pinojs/pino) 
- [Roarr](https://github.com/gajus/roarr) 
- [Loglevel](https://github.com/pimterry/loglevel) 
- [Npmlog](https://github.com/npm/npmlog) 
- [Bole](https://github.com/rvagg/bole)

```sh
pnpm add debug supports-color@~8
```

```json
{
  "scripts": {
    "dev": "export DEBUG=* &&  node index.js"
  }
}
```


## Reference
1. [nodejs-logging-libraries](https://www.highlight.io/blog/nodejs-logging-libraries)
2. [5 Best Node.js Logging Libraries](https://www.highlight.io/blog/nodejs-logging-libraries)
