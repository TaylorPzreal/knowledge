
Review
1. 2022/01/08
2.  2023/02/05
3. 2023-02-20 06:51

## 一、Introduction


## 二、Popular Node Frameworks
1. Express.js [https://github.com/expressjs/express](https://github.com/expressjs/express)
2. Koa.js ⭐️⭐️⭐️⭐️⭐️ [https://github.com/koajs/koa](https://github.com/koajs/koa)
3. Next.js(React) [https://github.com/vercel/next.js](https://github.com/vercel/next.js)
4. Nestjs(Angular) [https://github.com/nestjs/nest](https://github.com/nestjs/nest)
5. Nuxt.js(Vue) [https://github.com/nuxt/nuxt.js](https://github.com/nuxt/nuxt.js)
6. Remix(React) [https://github.com/remix-run/remix](https://github.com/remix-run/remix)
7. Meteor.js [https://github.com/meteor/meteor](https://github.com/meteor/meteor)
8. Sails.js [https://github.com/balderdashy/sails](https://github.com/balderdashy/sails)
9. Fastify [https://github.com/fastify/fastify](https://github.com/fastify/fastify)
10. Egg.js [https://github.com/eggjs/egg](https://github.com/eggjs/egg)
11. UmiJS [https://umijs.org/](https://umijs.org/)
12. Astro
13. Eleventy
14. SvelteKit
15. Docusaurus
16. Connect
17. Hapi <https://github.com/hapijs/hapi> 
18. Typetron https://github.com/typetron/typetron
19. Amplication https://github.com/amplication/amplication 
20. Elysia(Bun)  https://github.com/elysiajs/elysia
21. Hono(Bun) <https://github.com/honojs/hono> 
22. Baojs(Bun)
23. Fast(Deno)
24. Restify
25. Hyper Express https://github.com/kartikk221/hyper-express
26. RedwoodJS(React) https://redwoodjs.com/


## 三、详细功能梳理
### 3.1、Express.js
**中间件：洋葱模型**

**Features**
-   Robust routing
-   Focus on high performance
-   Super-high test coverage
-   HTTP helpers (redirection, caching, etc)
-   View system supporting 14+ template engines
-   Content negotiation
-   Executable for generating applications quickly

### 3.2、Koa.js
==Koa.js as the next level Node.js framework.==
==**解决Express洋葱模型缺陷**==

Koa是由**Express**背后的团队设计的**新Web框架**，旨在成为Web应用程序和API的更小，更具表现力，更强大的基础。通过利用async函数，Koa 允许以同步方式实现异步逻辑，并增强错误处理能力。Koa 在其核心中没有捆绑任何中间件，它提供了一套优雅的方法，使编写服务器变得快速而愉快。

中间件支持 **async function** and **common function**

核心功能：
1.  比Express更极致的request/response简化
	- `ctx.request`
	- `ctx.status = 200`
	- `ctx.body = 'ok'`
2.  精简内核，所有额外功能都移到中间件里面实现

Koa更强大优雅，可定制性更高。

示例
```js
const Koa = require('koa');
const app = new Koa();

app.use(async ctx => {
  ctx.body = 'Hello World';
});

app.listen(3000);
```

**Pros of Koa.js**
**1.** Koa increases interoperability and robustness while still making middleware creation more fun.
**2.** Koa is extremely light with just 550 lines of code.
**3.** ES6 generators will tidy up the code and make it more manageable by removing the chaos created by all those callbacks.
**4.** It provides a very good user experience.
**5.** Cleaner, more readable async code.
**6.** No callback hell

**Cons of Koa.js**
**1.** The open source community is relatively small.
**2.** Not compatible with Express-style middleware.
**3.** Koa makes use of generators that are incompatible with all other Node.js framework middleware.

**Koa常用中间件**
 1. koa-mount（优先使用koa-router） [https://github.com/koajs/mount](https://github.com/koajs/mount) 
 2. koa-router [https://github.com/koajs/router](https://github.com/koajs/router) 
 3. koa-static [https://github.com/koajs/static](https://github.com/koajs/static) 
 4. koa-session [https://github.com/koajs/session](https://github.com/koajs/session) 
 5. koa-cors [https://github.com/koajs/cors](https://github.com/koajs/cors) 
 6. nodemon [https://nodemon.io/](https://nodemon.io/) 
1. pg(postgres)
2. sequelize
3. mongoose
4. prisma
5. node-cache

**body parser**
1. koa-body [Github](https://github.com/koajs/koa-body) ⭐️⭐️⭐️⭐️⭐️
2. co-body [Github](https://github.com/cojs/co-body)
3. koa-bodyparser [Github](https://github.com/koajs/bodyparser)
4. @koa/multer support `multipart/form-data` 

```sh
yarn add koa-router koa-body
```

**How is Koa different from Express?**
- No callback hell
- Absence of boilerplate codes
- Better overall user experience
- Better error handling using try/catch
- Koa depends less on middleware
- Koa is more modular
- Routing is not available, unlike Express.
- Proper Stream handling

### 3.3、Next.js


### 3.4、Remix
Build Better Websites. Create modern, resilient user experiences with web fundamentals.


### 3.5、Hono
https://github.com/honojs/hono
Hono - _**means flame🔥 in Japanese**_ - is a small, simple, and ultrafast web framework built on Web Standards. It works on any JavaScript runtime: Cloudflare Workers, Fastly Compute, Deno, Bun, Vercel, AWS Lambda, Lambda@Edge, and Node.js.

#### Features
- **Ultrafast** 🚀 - The router `RegExpRouter` is really fast. Not using linear loops. Fast.
- **Lightweight** 🪶 - The `hono/tiny` preset is under 12kB. Hono has zero dependencies and uses only the Web Standard API.
- **Multi-runtime** 🌍 - Works on Cloudflare Workers, Fastly Compute, Deno, Bun, AWS Lambda, Lambda@Edge, or Node.js. The same code runs on all platforms.
- **Batteries Included** 🔋 - Hono has built-in middleware, custom middleware, and third-party middleware. Batteries included.
- **Delightful DX** 😃 - Super clean APIs. First-class TypeScript support. Now, we've got "Types".

## Reference
1. [2022年值得使用的Node.js框架](https://developer.51cto.com/article/709634.html)
2. [bun-http-framework-benchmark](https://github.com/SaltyAom/bun-http-framework-benchmark)
3. [nodejs frameworks threads](https://npmtrends.com/express-vs-fastify-vs-hapi-vs-hyper-express-vs-koa-vs-nanoexpress-vs-restify)


