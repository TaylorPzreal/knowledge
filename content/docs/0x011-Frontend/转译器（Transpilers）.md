

Review
1. 2023-02-27 06:30

## 一、Introduction

1. Babel
2. Traceur
3. Typescript
4. [wuzzle](https://github.com/host1-tech/wuzzle)
5. SWC

### wuzzle
1.  For compilers with webpack embedded for compilation (like [create-react-app](https://github.com/facebook/create-react-app), [vue-cli](https://github.com/vuejs/vue-cli), [next](https://github.com/vercel/next.js), [nuxt](https://github.com/nuxt/nuxt.js), etc), wuzzle provides the ability of modifying their internally used webpack configs.
2.  For JS runners with their own methods of compilation (like [jest](https://github.com/facebook/jest), [mocha](https://github.com/mochajs/mocha), the bare [node](https://github.com/nodejs/node), etc), wuzzle can hook up compatible webpack based compilation as replacements.
3.  For file transpilation, wuzzle provides a webpack based transpiler.
4.  For setup process, wuzzle opts in easily.
5.  For modification on webpack configs, wuzzle provides a unified entry, a dry-run mode, and well-tested modification utilities.


## Reference
1. [Wuzzle，进行基于 webpack 的 JS 转译](https://mp.weixin.qq.com/s/pbgfYuYb_n_sjeS-SnHxXg)
