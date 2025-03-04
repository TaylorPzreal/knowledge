+++
title = 'Zsh Overview'
date = 2024-04-13T14:44:23+08:00
draft = false
+++

## 一、Introduction
Zsh is a shell designed for interactive use, although it is also a powerful scripting language. Many of the useful features of **_bash_**, **_ksh_**, and **_tcsh_** were incorporated into zsh; many original features were added.

## 二、Configuration
1.  zsh
2.  ohmyzsh, zsh-autosuggestions, zsh-syntax-highlighting

[install zsh](https://github.com/ohmyzsh/ohmyzsh/wiki/Installing-ZSH)
```sh
# For Fedora
sudo dnf install zsh

# For Ubuntu
apt install zsh

# For macOS
brew install zsh

# For CentOS
sudo yum update && sudo yum -y install zsh
```

Make it your default shell: `chsh -s $(which zsh)` or use `sudo lchsh $USER` if you are on Fedora. Or `chsh -s /bin/zsh` .

[install ohmyzsh](https://ohmyz.sh/#install)
```sh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

config plugins
zsh-autosuggestions plugin
```sh
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
```

zsh-syntax-highlighting
```sh
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

config `.zshrc`
```Properties
# config theme
ZSH_THEME="afowler"

plugins=(git zsh-autosuggestions zsh-syntax-highlighting z)
```

after configured, exec
`source .zshrc`

[more plugins](https://github.com/ohmyzsh/ohmyzsh/wiki/Plugins)


## Reference
1. [Zsh](https://www.zsh.org/)
