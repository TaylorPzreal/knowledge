---
title: "Upgrade Kernel"
# weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# 升级 Linux Kernel 版本

Review

1. 2021/06/26

本文档介绍如何在 CentOS 7.x 系统上升级内核版本。

## 环境要求

- CentOS 7.x 操作系统
- root 或具有 sudo 权限的用户

## 当前内核版本检查

首先检查当前系统的内核版本：

```bash
uname -msr
```

输出示例：

```txt
Linux 3.10.0-1127.19.1.el7.x86_64 x86_64
```

## 升级步骤

### 1. 更新系统仓库

```bash
yum -y update
```

### 2. 启用 ELRepo 仓库

ELRepo 是一个提供最新稳定版 Linux 内核的仓库。

```bash
# 导入 ELRepo 的 GPG 密钥
rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org

# 安装 ELRepo 仓库
rpm -Uvh https://www.elrepo.org/elrepo-release-7.0-3.el7.elrepo.noarch.rpm
```

### 3. 查看可用内核版本

```bash
yum list available --disablerepo='*' --enablerepo=elrepo-kernel
```

> **注意**: 从 2021/06/26 开始，ELRepo 仓库不再提供 4.x 版本的内核，最低版本为 5.4.128-1.el7.elrepo。

### 4. 安装新内核

安装长期支持版本（LTS）的内核：

```bash
yum --enablerepo=elrepo-kernel install -y kernel-lt
```

### 5. 设置默认启动内核

```bash
grub2-set-default 0
```

### 6. 重启系统

```bash
sync
reboot
```

## 清理旧内核

升级完成后，可以移除旧的内核版本：

```bash
# 查看已安装的内核
rpm -qa | grep kernel

# 查看当前使用的内核
uname -r

# 移除指定的旧内核（替换为实际的内核版本号）
yum remove kernel-lt-4.4.241-1.el7.elrepo.x86_64
```

## 自动化脚本

以下是一个自动化升级内核的脚本：

```bash
#!/bin/bash

# 显示当前内核版本
uname -msr

# 更新系统
yum -y update

# 配置 ELRepo 仓库
rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
rpm -Uvh https://www.elrepo.org/elrepo-release-7.0-3.el7.elrepo.noarch.rpm

# 安装新内核
yum list available --disablerepo='*' --enablerepo=elrepo-kernel
yum --enablerepo=elrepo-kernel install -y kernel-lt

# 设置默认启动内核
grub2-set-default 0

# 同步数据到磁盘
sync
```

## 注意事项

1. 升级内核前请确保系统已备份
2. 建议在测试环境中先进行升级测试
3. 升级后如遇到问题，可以通过 GRUB 菜单选择旧内核启动
4. 某些特定的硬件驱动可能需要重新编译

## 参考链接

- [How to Upgrade Kernel in CentOS](https://phoenixnap.com/kb/how-to-upgrade-kernel-centos)
- [How to compile and install Linux Kernel from source code](https://www.cyberciti.biz/tips/compiling-linux-kernel-26.html)
