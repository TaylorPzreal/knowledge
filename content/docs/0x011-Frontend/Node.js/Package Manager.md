#包管理器  #packagemanager


Review
1. 2023/01/03
2. 2023/02/05
3. 2023-02-25 08:55
4. 2024-10-03

## 一、Introduction
NPM stands for Node Package Manager, responsible for managing all the packages and modules for Node.js.


## 二、Popular managers
1. NPM
2. Yarn@1、Yarn@4.x
3. PNPM@7、PNPM@10.x
4. Bun

### 2.1、Corepack
Corepack 是一个零运行时依赖的 Node.js 脚本，充当 **Node.js** 项目和在开发过程中使用的**包管理器**之间的桥梁。 实际上，Corepack 将允许您使用 **Yarn** 和 **pnpm** 而无需安装它们 - 就像当前 npm 发生的情况一样，默认情况下由 Node.js 提供。

#### 安装
==Corepack 默认随 Node.js 14.19.0 和 16.9.0安装，可以直接使用==。不是此版本的Node.js可以通过下面命令安装。
```sh
npm install -g corepack

# OR for macOS
brew install corepack
```

#### 启用
注意⚠️：使用Corepack之前需要将yarn, pnpm卸载掉才会生效。
```sh
corepack enable
```

#### 切换版本
```sh
corepack prepare pnpm@x.y.z --activate

# OR
corepack prepare pnpm@latest --activate
```

#### 禁用
```sh
corepack disable
```


### 2.2、Feature Comparison
| Feature                     | pnpm                            | Yarn                | npm                   |
| --------------------------- | ------------------------------- | ------------------- | --------------------- |
| Workspace support           | ✔️                               | ✔️                   | ✔️                     |
| Isolated node_modules       | ✔️ - The default                 | ✔️                   | ✔️                     |
| Hoisted node_modules        | ✔️                               | ✔️                   | ✔️ - The default       |
| Autoinstalling peers        | ✔️ - Via auto-install-peers=true | ❌                   | ✔️                     |
| Plug'n'Play                 | ✔️                               | ✔️ - The default     | ❌                     |
| Zero-Installs               | ❌                               | ✔️                   | ❌                     |
| Patching dependencies       | ✔️                               | ✔️                   | ❌                     |
| Managing Node.js versions   | ✔️                               | ❌                   | ❌                     |
| Has a lockfile              | ✔️ - pnpm-lock.yaml              | ✔️ - yarn.lock       | ✔️ - package-lock.json |
| Overrides support           | ✔️                               | ✔️ - Via resolutions | ✔️                     |
| Content-addressable storage | ✔️                               | ❌                   | ❌                     |
| Dynamic package execution   | ✔️ - Via pnpm dlx                | ✔️ - Via yarn dlx    | ✔️ - Via npx           |
| Side-effects cache          | ✔️                               | ❌                   | ❌                     |
| Listing licenses            | ✔️ - Via pnpm licenses list      | ✔️ - Via a plugin    | ❌                     |



## 三、NPM
npm作为node官方的包管理工具

**npm@^2 的问题**
1.  依赖包重复安装，同一个依赖被引用n次，就会被下载n次
2.  依赖层级过多（依赖地狱）不利于维护查找
3.  模块实例无法共享


## 四、Yarn
yarn的出现则是为了解决npm带来的诸多问题，虽然yarn提高了依赖包的安装速度与使用体验


## 五、pnpm
Yarn依旧没有解决npm的依赖重复安装等致命问题。
[Motivation](https://pnpm.io/motivation)
1. 节约磁盘空间并提升安装速度
2. 创建非扁平化的 `node_modules` 文件夹
![](./assets/61e1d464a17b_9bd22530.jpeg)

![](./assets/c511869733cc_d2637570.jpeg)

### 常用命令
```sh
# install deps
pnpm install

# add new package
pnpm add <pkg>

# exec scripts command
pnpm <cmd>
```


## 六、版本管理
问题：很多Package依赖了相同的Library的不同版本，可能低版本有问题，需要升级，但是Package一般不容易改成依赖一个相同的版本，这里可能是Package不在维护等原因，所以可以通过 `resolutions` 方案结局。

yarn/npm配置 `resolutions` 按需下载版本依赖包

**Yarn配置**
`package.json` 配置
```json
{
	"resolutions": {
		"d3": "3.0.0"
	}
}
```

重新 `yarn install` 即可；

**NPM配置**
`package.json` 配置同上；
然后在 package.json 中的 `scripts` 中新增一行：
```json
{
	"scripts": {
		"preinstall": "npx force-resolutions"
	}
}
```

然后删除 `node_modules`，执行 `npm install` 即可；


下面2个npm包都可以处理
1.  force-resolutions [https://www.npmjs.com/package/force-resolutions](https://www.npmjs.com/package/force-resolutions) 
2.  npm-force-resolutions [https://www.npmjs.com/package/npm-force-resolutions](https://www.npmjs.com/package/npm-force-resolutions) 

**验证**
`package-lock.json`
查看所有直接依赖和间接依赖都变成了新的版本。

`yarn.lock`
查看所有依赖的版本都指向了同一个版本。

## 七、国内镜像源配置
```sh
npm set registry https://registry.npm.taobao.org
npm set disturl https://npm.taobao.org/dist
npm set sass_binary_site https://npm.taobao.org/mirrors/node-sass
npm set electron_mirror https://npm.taobao.org/mirrors/electron/
npm set puppeteer_download_host https://storage.googleapis.com.cnpmjs.org
npm set chromedriver_cdnurl https://npm.taobao.org/mirrors/chromedriver
npm set operadriver_cdnurl https://npm.taobao.org/mirrors/operadriver
npm set phantomjs_cdnurl https://npm.taobao.org/mirrors/phantomjs
npm set selenium_cdnurl https://npm.taobao.org/mirrors/selenium
npm set node_inspector_cdnurl https://npm.taobao.org/mirrors/node-inspector
npm set fse_binary_host_mirror https://npm.taobao.org/mirrors/fsevents
npm set SQLITE3_BINARY_SITE https://npm.taobao.org/mirrors/sqlite3
npm set node_sqlite3_binary_host_mirror https://npm.taobao.org/mirrors
npm set PYTHON_MIRROR https://npm.taobao.org/mirrors/python
npm set grpc-node-binary-host-mirror https://npm.taobao.org/mirrors/grpc
npm cache clean --force
```


```
yarn config set registry https://registry.npm.taobao.org
yarn config set disturl https://npm.taobao.org/dist
yarn config set sass_binary_site https://npm.taobao.org/mirrors/node-sass
yarn config set electron_mirror https://npm.taobao.org/mirrors/electron/
yarn config set puppeteer_download_host https://storage.googleapis.com.cnpmjs.org
yarn config set chromedriver_cdnurl https://npm.taobao.org/mirrors/chromedriver
yarn config set operadriver_cdnurl https://npm.taobao.org/mirrors/operadriver
yarn config set phantomjs_cdnurl https://npm.taobao.org/mirrors/phantomjs
yarn config set selenium_cdnurl https://npm.taobao.org/mirrors/selenium
yarn config set node_inspector_cdnurl https://npm.taobao.org/mirrors/node-inspector
yarn config set fse_binary_host_mirror https://npm.taobao.org/mirrors/fsevents
yarn config set SQLITE3_BINARY_SITE https://npm.taobao.org/mirrors/sqlite3
yarn config set PYTHON_MIRROR https://npm.taobao.org/mirrors/python
yarn config set grpc-node-binary-host-mirror https://npm.taobao.org/mirrors/grpc
yarn cache clean --force
```


## 八、`node_modules` 排查优化

Node Modules Inspector 是 Vue 团队成员的又一力作，它不仅填补了前端依赖管理领域的一个空白，更为开发者提供了一个强大的工具。无论是初学者还是资深开发者，都可以通过这个工具更好地理解和优化项目的依赖关系。如果你还在为 node_modules 的复杂性而烦恼，不妨试试这个神器，它可能会成为你开发流程中不可或缺的一部分！
Node Modules Inspector Github 地址：<https://github.com/antfu/node-modules-inspectorNode>
Modules Inspector 在线体验地址：<https://node-modules.dev/>


## Reference
1.  [https://blog.csdn.net/cxwtsh123/article/details/123134278](https://blog.csdn.net/cxwtsh123/article/details/123134278) 
2. [pnpm](https://pnpm.io/)
3. [corepack](https://github.com/nodejs/corepack)

