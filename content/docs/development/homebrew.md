---
title: "Homebrew"
# weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# Homebrew Quick Start

## Review

1. 2020/02/11
2. 2021/04/02
3. 2021/08/01
4. 2023/10/29
5. 2025/03/15


> !Caution
> macOS 低版本系统（Version 12.7.6），已不支持更新了。--2025


## Homebrew

https://brew.sh/ 
https://github.com/Homebrew/brew
The missing package manager for macOS (or Linux)


## 安装配置（2025/03/16）

参考 <https://mirrors.tuna.tsinghua.edu.cn/help/homebrew/>

配置 `.zshrc`

```
export HOMEBREW_API_DOMAIN="https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles/api"
export HOMEBREW_BOTTLE_DOMAIN="https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles"
export HOMEBREW_BREW_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git"
export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git"
export HOMEBREW_PIP_INDEX_URL="https://pypi.tuna.tsinghua.edu.cn/simple"
```

执行命令安装
```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

add Homebrew's location to your $PATH in your `.bash_profile` or `.zshrc` file.
```
export PATH="/usr/local/bin:$PATH"
```


brew 常用命令
```sh
brew update
brew upgrade
# 自检程序，如果有问题自检试试
brew doctor 
brew search xxx-pkg
brew install xxx-pkg
brew remove xxx-pkg
```

查看全部安装路径
```sh
brew list
```

查看指定软件安装路径
```sh
brew list xxx-pkg
```

```sh
brew install --cask xxx
```

不要使用：`brew cask install xxx`；会报错：Error: Unknown command: cask


## 自建 homebrew formula cookbook
```sh
brew search formula_name
```

```sh
brew create formula_name
```

```sh
brew tap repName/projectName url
```

```sh
brew install formulaname
```

```sh
brew untap repName/projectName
```

```sh
brew uninstall formulaname
```


// 如果tap有新的更新，可以执行下面命令
```sh
brew update
brew upgrade formulaname
brew cleanup formulaname
brew remove formulaname
```

```sh
brew create https://*.tar.gz
```

brew也有自己的守护进程
```sh
brew services list
brew services start/stop/restart
```

## Reference

1. 国内5步安装Homebrew：https://blog.csdn.net/u010458765/article/details/104730037
2. 一个命令安装：https://zhuanlan.zhihu.com/p/111014448
3. Homebrew清华镜像 https://mirrors.tuna.tsinghua.edu.cn/help/homebrew/ 
4. 分步安装可参考这里：https://www.raydbg.com/2019/Homebrew-Update-Slow/
5. https://zhuanlan.zhihu.com/p/35696075
6. https://docs.brew.sh/
7. https://vanwollingen.nl/distributing-private-tools-through-homebrew-d046761fb3a1
8. https://github.com/Homebrew/brew/blob/master/docs/Formula-Cookbook.md
9. https://docs.brew.sh/How-to-Create-and-Maintain-a-Tap
10. https://engineering.innovid.com/distributing-command-line-tools-with-homebrew-d03e795cadc8
