---
title: "Install Git by Sourcecode"
# weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# 源码安装 Git

Review

1. 2020/11/17

## 环境要求

- CentOS 7 或更高版本
- 具有 sudo 权限的用户
- 至少 10GB 可用磁盘空间
- 稳定的网络连接

## 安装步骤

### 1. 安装必要的依赖包

```bash
# 安装开发工具组
sudo yum -y groupinstall "Development Tools"

# 安装其他必要的依赖包
sudo yum -y install zlib-devel perl-ExtUtils-MakeMaker asciidoc xmlto openssl-devel
```

### 2. 下载并解压 Git 源码

```bash
# 下载 Git 源码包
wget https://www.kernel.org/pub/software/scm/git/git-2.29.2.tar.gz

# 解压源码包
tar -zxvf git-2.29.2.tar.gz
cd git-2.29.2
```

### 3. 编译安装 Git

```bash
# 配置安装路径
./configure --prefix=/usr/local/git

# 编译并安装
make && make install
```

### 4. 配置环境变量

```bash
# 添加 Git 到系统 PATH
echo 'export PATH="/usr/local/git/bin:$PATH"' >> ~/.bashrc

# 使环境变量生效
source ~/.bashrc
```

### 5. 验证安装

```bash
# 检查 Git 版本
git --version
```

### 6. 清理安装文件

```bash
# 删除源码包和解压目录
rm -rf git-2.29.2.tar.gz git-2.29.2
```

## 注意事项

1. 确保系统已安装所有必要的依赖包，否则编译过程可能会失败
2. 如果遇到权限问题，请使用 sudo 命令
3. 安装完成后，建议重启终端或执行 `source ~/.bashrc` 使环境变量生效
4. 如果需要在其他用户下使用 Git，需要将环境变量配置添加到 `/etc/profile` 文件中

## 常见问题

1. 如果编译失败，请检查是否安装了所有必要的依赖包
2. 如果 `git` 命令无法识别，请检查环境变量是否正确配置
3. 如果遇到 SSL 相关错误，请确保 openssl-devel 已正确安装

## 参考链接

- [CentOS7安装最新git教程](https://blog.csdn.net/Juladoe/article/details/76170193)
- [IUS (第三方安装centos)](https://ius.io/)
- [Git 官方文档](https://git-scm.com/doc)
