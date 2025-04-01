---
title: "NPX"
# weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# Node Package Execute - NPX

- npx 是一个 npm 包执行器。它自 npm `v5.2.0` 版本开始内置，无需单独安装。
- npx 主要目的是更方便地执行 Node.js 包提供的命令行工具，特别是那些你不想全局安装或只想偶尔使用的工具。

## 核心功能与工作方式

执行包命令: `npx <command> [args...]`
查找逻辑:
1. 首先检查当前项目 node_modules/.bin 目录下是否存在该命令。如果存在，则直接执行本地版本。
2. 如果本地不存在，检查环境变量 PATH 中是否存在该命令（即全局安装的包）。如果存在，则执行全局版本。
3. 如果本地和全局都没有找到，npx 会临时从 npm 仓库下载对应的包，执行其指定的二进制文件（通常在包的 `package.json` 的 `bin` 字段定义），执行完毕后通常不会将包保留在本地（除非有缓存机制）。

执行特定版本: `npx <package-name>@<version> <command>` 可以执行指定版本的包命令。


## 主要优势

- 避免全局安装污染: 对于只需要运行一次或偶尔使用的工具（如项目脚手架 create-react-app），无需使用 `npm install -g` 全局安装，避免污染全局环境和潜在的版本冲突。
- 使用最新版本: 默认情况下，如果需要临时下载，npx 会下载最新稳定版的包来执行，确保你使用的是最新的功能或修复。
- 方便执行本地依赖: 无需配置 `npm scripts` 或写冗长的路径 (`./node_modules/.bin/<command>`)，可以直接通过 `npx <command>` 执行项目本地安装的工具（例如 `npx jest` 运行测试）。
- 测试和试用: 可以方便地试用不同的 npm 包或其不同版本提供的命令，而无需在本地或全局安装它们。


## 开发一个 npx 命令

### 配置 `package.josn`，增加 `bin` 配置

```json
{
  "name": "xxx-package",
  "version": "1.0.0",
  "main": "dist/index.js",
  "bin": {
    "xxx-command": "./dist/index.js"  // 指向编译后的 JS 文件
  },
  "scripts": {
    "build": "tsc && chmod 755 build/index.js",
    "prepublishOnly": "npm run build" // 发布前自动构建
  },
  "files": ["dist"], // 确保发布时包含 dist 目录
  "devDependencies": {
    "typescript": "^5.0.0"
  }
}
```

### 配置源文件

`src/index.ts`

```ts
#!/usr/bin/env node
// 一定要有上面这一行。Shebang 告诉系统用 Node.js 执行此脚本。不加该行解析执行可能失败

import fs from 'fs';

// 示例：读取文件并打印内容
function main() {
  const filePath = process.argv[2]; // 获取命令行参数
  if (!filePath) {
    console.error('请提供文件路径');
    process.exit(1);
  }

  try {
    const content = fs.readFileSync(filePath, 'utf-8');
    console.log(content);
  } catch (error) {
    console.error('读取文件失败:', error.message);
  }
}

main();
```

### config `tsconfig.json`

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "Node16",
    "moduleResolution": "Node16",
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": [
    "src/**/*"
  ],
  "exclude": [
    "node_modules"
  ]
}
```

### 本地测试

```sh
npm run build
```

```sh
# 方法 1：全局安装测试
npm install -g .          # 全局安装你的包
xxx-command ./test.txt   # 执行命令

# 方法 2：使用 npx 直接测试
npx xxx-command ./test.txt
```

### 发布后测试

```sh
npx -y -p xxx-package xxx-command any-file.txt
```

## 关键点

- Shebang 行：`#!/usr/bin/env node` 必须放在 CLI 入口文件的第一行，确保用 Node 执行
- 文件权限：需要手动配置 `chmod +x` 权限，否则执行时会缺少权限
