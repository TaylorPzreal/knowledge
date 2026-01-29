#Archive 

Review
1. 2023-02-25 07:31

## 一、Introduction
A version/environment manager is essential if you work with different Node.js.

**基本功能需求**
1. 支持切换不同node版本
2. 进入依赖不同node版本的项目中，支持自动切换node版本
3. 项目依赖的其他全局CLI（如tsc、yarn等），支持自动切换版本
4. 支持配置文件 `.node-version` 、`.nvmrc`
5. 支持自动补全（completions）
6. 支持跨平台（macOS, Linux, Windows）
7. 支持不同Shell(Bash, ZSH, Fish, Elvish)


**Popular Libraries**
1. [NVM](https://github.com/nvm-sh/nvm)
2. [N](https://github.com/tj/n)
3. [FNM](https://github.com/Schniz/fnm) 【次推荐】
4. [Volta](https://github.com/volta-cli/volta) 【推荐】
5. [Asdf](https://github.com/asdf-vm/asdf)
6. [nvs](https://github.com/jasongin/nvs)
7. [nodeenv](https://github.com/ekalinin/nodeenv)
8. [nave](https://github.com/isaacs/nave)

## 二、详细介绍
### 2.1、NVM
NVM支持同时安装多个Node版本，然后使用的时候可以在不同版本之间手动切换。

常用命令
```sh
nvm install 16.6.2 # install Node.js v16.6.2
nvm use 16.5.0 # switch to version 16.5.0 on the current shell instance
nvm alias default 16.6.2 # set the default version for new shell instances
nvm ls-remote # list all available versions
nvm ls # list all installed versions
nvm # view nvm usage information
```

使用 `NVM` 通过操作系统的包管理器安装 Node.js 的一个**优势是能够在不提升权限的情况下全局安装 npm 包**。 这意味着不再需要在命令前添加前缀以使用 sudo 全局安装软件包。 全局包的范围限定为当前 Node.js 版本并安装到  `$HOME/.nvm/versions/node/<version>/bin/` 。 **当您切换到不同的 Node.js 版本时，这会导致无法访问它们**。 为了解决这个问题，NVM 提供了一种在安装不同版本时迁移全局包的方法。

NVM 的功能非常出色，但它也有一些缺点。 例如
1. 它只支持符合 POSIX 标准的 shell，例如 bash 或 zsh，让流行的 Fish shell 用户望而却步。 
2. 也缺乏对 Windows 的支持，除非你使用 Windows 子系统 for Linux (WSL) 或像 Cygwin 这样的项目。 
3. 还观察到 NVM 将 shell 初始化减慢了几毫秒，这在某些系统上可能会很明显。 

#### Installation on macOS
```sh
# Step 1 – Remove existing Node Versions
brew uninstall --ignore-dependencies node 
brew uninstall --force node 

# Step 2 – Install NVM on macOS
brew update 
brew install nvm 
mkdir ~/.nvm 

# and, add below lines to ~/.bash_profile ( or ~/.zshrc for macOS Catalina or later)
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && source "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/etc/bash_completion.d/nvm" ] && . "$NVM_DIR/etc/bash_completion.d/nvm"  # This loads nvm bash_completion

# Next, load the variable to the current shell environment. From the next login, it will automatically loaded.
source ~/.bash_profile

# Step 3 – Install Node.js with NVM
nvm ls-remote 
nvm install node     _## Installing Latest version_ 
nvm install 14       _## Installing Node.js 14.X version_ 
nvm ls 

# If you have installed multiple versions on your system, you can set any version as the default version any time. To set the node 14.X as default version, simply use:
nvm use 14

# To set a default Node version to be used in any new shell, use the alias 'default':
nvm alias default node@14
```

#### Calling `nvm use` automatically in a directory with a `.nvmrc` file
Put this into your `$HOME/.zshrc` to call `nvm use` automatically whenever you enter a directory that contains an `.nvmrc` file with a string telling nvm which node to `use`:
```sh
# place this after nvm initialization!
autoload -U add-zsh-hook
load-nvmrc() {
  local nvmrc_path="$(nvm_find_nvmrc)"

  if [ -n "$nvmrc_path" ]; then
    local nvmrc_node_version=$(nvm version "$(cat "${nvmrc_path}")")

    if [ "$nvmrc_node_version" = "N/A" ]; then
      nvm install
    elif [ "$nvmrc_node_version" != "$(nvm version)" ]; then
      nvm use
    fi
  elif [ -n "$(PWD=$OLDPWD nvm_find_nvmrc)" ] && [ "$(nvm version)" != "$(nvm version default)" ]; then
    echo "Reverting to nvm default version"
    nvm use default
  fi
}
add-zsh-hook chpwd load-nvmrc
load-nvmrc
```

#### Uninstalling/Removal
```sh
rm -rf "$NVM_DIR"
```

Edit `~/.bashrc` (or other shell resource config) and remove the lines below:
```sh
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
[[ -r $NVM_DIR/bash_completion ]] && \. $NVM_DIR/bash_completion
```


### 2.2、N
`N` 是一个 node.js 模块。
它的**工作原理**是将特定版本的预构建二进制文件下载（和缓存）到 `/usr/local` 内的 `n/versions/node` 目录，然后将其安装到 `/usr/local/bin` 目录，这会覆盖存在的任何现有版本。 请注意，在使用 n 安装 Node.js 版本时，您可能需要使用 sudo 以避免权限错误。 项目的 README 文档中提供了一些避免对 n 和 npm 全局安装使用 sudo 的指南。

与 NVM 相比，n 管理 Node.js 版本的方法的主要优势在于，当您在不同版本的 Node 之间切换时，全局 npm 包不会受到影响。 另一方面，NVM 允许您通过其 nvm use 命令在不同的终端中使用不同的 Node.js 版本，而 n 则不能。 一旦您切换到不同的 Node.js 版本，更改就会在整个系统范围内反映出来。 您可以通过使用 n use 子命令调用特定的 Node.js 二进制文件而不切换到该版本来解决这个问题。 这在执行一次性脚本时会派上用场。

### 2.3、FNM
Fast Node Manager(FNM) 是一个用 `Rust` 编写的跨平台 Node.js 版本管理器，声称==比 NVM 快 40 倍==，同时提供大部分相同的功能。 与其前身不同，也许是由于其 Rust 起源，它同时**支持 Windows (Powershell) 和 Fish shell**，使其适合更广泛的用户。

FNM 在 `$HOME/.fnm/node-versions` 目录中安装 Node.js 二进制文件，并在 shell 启动时将它们符号链接到` /tmp/fnm_multishells` 目录中，以便您可以在每个 shell 中使用不同的 Node.js 版本。

#### 2.3.1、Features
1. 🌎 Cross-platform support (macOS, Windows, Linux)
2. ✨ Single file, easy installation, instant startup
3. 🚀 Built with speed in mind
4. 📂 Works with `.node-version` and `.nvmrc` files

#### 2.3.2、Installation
```sh
# Using a script(macOS/Linux)
curl -fsSL https://fnm.vercel.app/install | bash

# HomeBrew
brew install fnm

# Scoop
scoop install fnm
```

#### 2.3.3、本地配置
##### Completions（补全提示）
```sh
fnm completions --shell zsh
```

##### Zsh
Add the following to your `.zshrc` profile:
```sh
eval "$(fnm env --use-on-cd --node-dist-mirror https://npm.taobao.org/dist)"
```

1. ==更改目录时自动切换 Node.js 版本。==
2. 指定==国内Node镜像==，国外的镜像访问失败

默认国外镜像站点：<https://nodejs.org/dist>

#### 2.3.4、常用命令
```sh
fnm --version
fnm -h
fnm ls-remote # list remote Node.js versions
fnm install 16.5.0 # install a specific version
fnm use 14.17.5 # switch Node.js version
fnm ls # list installed versions
fnm default <version> # set a default version
fnm env # 列出所有的环境变量
```
[More cmd](https://github.com/Schniz/fnm/blob/master/docs/commands.md)

项目工程配置如下，这样每次进入该代码目录，会自动切换为相应的Node版本。
```
node --version > .node-version
```

Remove
```sh
brew uninstall fnm
```

### 2.4、VOLTA
The Hassle-Free JavaScript Tool Manager. Based on Rust.

Volta 的主要价值主张是它可以根据项目的 `package.json` 文件跟踪所需的确切包版本来管理==整个 JavaScript 工具链==。 在幕后，Volta 使用垫片路由到工具的正确版本，并使用适当的 Node.js 引擎执行它。

每个工具的二进制文件都下载到 Unix 系统上用户主目录中的 `.volta/bin` 目录。使用 Volta 安装包后，您将能够直接在终端中运行它，就像您通过 npm 全局安装它一样。 当你换一个项目有相同的包作为依赖时，Volta 会自动无缝切换到本地安装的版本以保证兼容性。

#### Features
-   Speed ⚡
-   Seamless, per-project version switching
-   Cross-platform support, including Windows and all Unix shells
-   Support for multiple package managers
-   Stable tool installation—no reinstalling on every Node upgrade!
-   Extensibility hooks for site-specific customization

#### Installation
Try it out!
```sh
# install Volta
curl https://get.volta.sh | bash
```


#### Configuration
由于默认使用的是国外源，访问会失败，需要设置为国内源。
默认情况下，Volta 从公共资源和注册表（https://nodejs.org、https://yarnpkg.com、https://www.npmjs.com）获取 Node、npm 和 Yarn。

可以通过 `hooks` 进行自定义配置。
Hooks specified in the Volta directory (`~/.volta/hooks.json` on Linux/MacOS) will apply across the entire system.

Hooks specified in a .volta subdirectory of a project (`<PROJECT ROOT>/.volta/hooks.json`) will only apply within that project. `<PROJECT ROOT>` here is defined as the location of the package.json for that project.

`hook.json` example: 目前仅支持配置 `yarn`, `node`, `npm` 3种工具。
```json
{
  "node": {
    "index": {
      "bin": "/usr/local/node-lookup"
    },
    "latest": {
      "prefix": "http://example.com/node/"
    },
    "distro": {
      "template": "http://example.com/{{os}}/{{arch}}/node-{{version}}.tar.gz"
    }
  },
  "npm": {
    "index": {
      "prefix": "http://example.com/npm/"
    },
    "latest": {
      "bin": "~/npm-latest"
    },
    "distro": {
      "template": "http://example.com/npm/npm-{{version}}.tgz"
    }
  },
  "yarn": {
    "index": {
      "template": "http://example.com/yarn/{{os}}/{{arch}}/yarn-{{version}}.tgz"
    },
    "latest": {
      "prefix": "http://example.com/yarnpkg/"
    },
    "distro": {
      "bin": "~/yarn-distro"
    }
  }
}

```

##### 每个工具都有3个操作，每个操作都可以应用一个hook
-   `index` Represents the URL used to determine the list of versions that are available to download for that tool. The response when accessing that URL must match the format of the public indexes for the selected tool. 用于确定该工具可供下载的版本列表的 URL。
-   `latest` Represents the URL used to determine the latest version of that tool. For `node`, the response should be in the same format as `index`, making sure that the latest version is the first element in the list. For `yarn`, the response should be the raw version number string and nothing else. 用于确定该工具的最新版本的 URL。
-   `distro` Represents the URL that is used to download the tool binaries. 表示用于下载工具二进制文件的 URL。

##### Hook types
prefix Hooks
`prefix Hooks` 是一个简单的 URL 替换。 URL 将使用指定的前缀构建，后跟该操作的公共文件名。 例如，使用上面的 `hooks.json`，我们有一个前缀钩子指定用于确定最新的 yarn 版本。 默认情况下，Volta 会通过向 https://yarnpkg.com/latest-version 发出请求来获取最新版本。 使用钩子，Volta 会尝试访问 http://example.com/yarnpkg/latest-version，将 latest-version 附加到 http://example.com/yarnpkg/ 的指定前缀上。

template Hooks
`template Hooks` 允许您为 URL 指定模板，其中包含将被替换的通配符。 可用的通配符是：
- {{os}} 将被 darwin、linux 或 win 取代，具体取决于操作系统。
- {{arch}} 将被 x86 或 x64 取代，具体取决于系统的架构。
- {{version}}（仅适用于发行版操作）将替换为 Volta 尝试下载的工具的特定版本。
- {{filename}} 将替换为 Volta 从公共注册表下载的文件的文件名。
- {{ext}}（仅适用于发行版操作）将替换为 Volta 希望下载的文件扩展名。

bin Hooks
`bin Hooks` 是一个通用的钩子，它将调用外部脚本来确定 URL。 该值是将被调用的可执行脚本的路径，URL 将从该脚本的标准输出中读取。 脚本的 stderr 将显示给用户，因此如果需要，它可用于显示进度条或等待微调器。 如果脚本的路径是相对的，那么它将相对于指定它的 hooks.json 文件进行解析。 在此上下文中，相对路径表示路径在 Linux/MacOS 上以 ./ 或 ../ 开头。 最后，对于发行版操作hooks，请求的工具版本将作为第一个参数传递给该脚本。

因此，本地的 `~/.volta/hooks.json` 配置如下：
```json
{
  "node": {
    "index": {
      "prefix": "https://npmmirror.com/mirrors/node/"
    },
    "distro": {
      "template": "https://npmmirror.com/mirrors/node/v{{version}}/{{filename}}"
    }
  },
  "npm": {
    "index": {
      "prefix": "https://registry.npmmirror.com/"
    },
    "distro": {
      "template": "https://registry.npmmirror.com/npm/-/{{filename}}"
    }
  },
  "pnpm": {
    "index": {
      "prefix": "https://registry.npmmirror.com/"
    },
    "distro": {
      "template": "https://registry.npmmirror.com/pnpm/-/{{filename}}"
    }
  },
  "yarn": {
    "latest": {
      "prefix": "https://classic.yarnpkg.com/"
    },
    "distro": {
      "template": "https://mirrors.aliyun.com/macports/distfiles/yarn/{{filename}}"
    }
  }
}
```

#### Usage
```sh
# install Node
volta install node

# start using Node
node

volta install yarn@1.22.11
# success: installed and set yarn@1.22.11 as default

volta install jest
# success: installed jest@27.0.6 with executables: jest

volta install typescript
# success: installed typescript@4.3.5 with executables: tsc, tsserver

volta install node@latest
# success: installed and set node@16.7.0 (with npm@7.20.3) as default
```

```sh
$ tsc --version
# Version 4.3.5

$ cd node_project
$ cat package.json | grep 'typescript'
  "typescript": "^4.0.8",

$ tsc --version
# Version 4.0.8
```

If you want to guarantee that a specific Node.js version is used against a project, you can use Volta to specify the desired version through its `pin` subcommand:
```sh
$ volta pin node@14.17.5
# success: pinned node@14.17.5 (with npm@6.14.14) in package.json
```

This adds the following entry to the project's `package.json` file:
```json
"volta": {
  "node": "14.17.5"
}
```

有了上面的配置，任何使用 Volta 的人在 cd 进入项目目录时都会自动获得 package.json 文件中指定的正确 Node.js 版本。 如果本地没有对应的Node.js版本，会直接下载安装。

#### Uninstallation
```sh
rm -rf ~/.volta
```

Edit your shell profile scripts to remove the two lines that mention Volta. 

#### 它是如何工作的？
Volta 不使用任何花哨的操作系统功能或特定于 shell 的挂钩。 它建立在简单、经过验证的垫片(shims)方法之上。

每当您使用 Volta 安装工具时，它都会向您的 **PATH** 添加一个垫片，充当智能（且快速）路由器到正确版本的工具，并使用正确的Node引擎运行它。

Volta 易于安装，没有外部依赖项，因为它作为单个快速本机可执行文件内置在 Rust 中。

### 2.5、Asdf
<https://github.com/asdf-vm/asdf>
> asdf is a CLI tool that can manage multiple language runtime versions on a per-project basis. It is like `gvm`, `nvm`, `rbenv` & `pyenv` (and more) all in one! Simply install your language's plugin!

Asdf 并不特定于 Node.js 生态系统。 它是一种用于在每个项目的基础上管理多个语言运行时版本的工具，旨在取代特定于语言的环境管理器，例如 nvm、rbenv 和 pyenv。 如果您使用多种语言开发应用程序并且需要一种更有效的方法来管理每种语言的环境，而不是使用多个不相关的工具，那么 Asdf 可能是您的正确选择。

Asdf 仅支持 Linux 和 macOS，因此您无法在 Windows 上使用它，除非通过 WSL。

为 Asdf 安装 Node.js 插件所需的命令：
```sh
asdf plugin add nodejs https://github.com/asdf-vm/asdf-nodejs.git
```

安装指定版本
```sh
asdf install nodejs latest
```

设置默认的 Node.js 版本：
```sh
asdf global nodejs latest
```

This will add the following line to the `$HOME/.tool-versions` file:
```sh
$ cat ~/.tool-versions
nodejs 16.7.0

$ which node
/home/<user>/.asdf/shims/node
```

```sh
asdf install nodejs <version>

asdf local nodejs <version>
```

Asdf 也理解 `.nvmrc` 和 `.node-version`，因此从其他环境管理器迁移应该是一件轻而易举的事。 您需要将以下行添加到 `$HOME/.asdfrc` 文件中，以确保 Asdf 可以从这两个文件中读取：
```txt
legacy_version_file = yes
```


## Reference
1. <https://www.honeybadger.io/blog/node-environment-managers/>
2. [Install nvm on macOS](https://tecadmin.net/install-nvm-macos-with-homebrew/)

