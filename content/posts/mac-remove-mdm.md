---
title: "macOS Remove MDM"
date: 2025-03-29T12:05:02+08:00
tags: 'macOS'
categories: 'development'
# bookComments: false
# bookSearchExclude: false
---

# 禁用 macOS 上的远程管理（MDM）

在Mac上，远程管理系统可以方便地进行各种管理任务，但有时需要将其移除，特别是在设备更换所有权或将设备从企业使用转为个人使用的情况下。

MDM 是一种技术，允许组织远程配置、管理和保护其拥有的设备，包括强制执行安全策略、部署应用程序和进行故障排除 。另一种形式的远程管理是 Apple 远程桌面，它与 MDM 不同，允许直接控制和观察屏幕 。当用户从公司回购这些曾经受管理的 MacBook 时，这些远程管理功能可能会仍然存在，从而限制用户对设备的完全控制。因此，移除所有形式的远程管理对于希望获得设备完全自主权的用户来说至关重要。

## 检查

### 检查 MDM 注册状态

如果设备未通过 Apple 的设备注册计划（DEP）注册，并且没有 MDM 注册，则可能会显示“Error fetching Device Enrollment configuration: Client is not DEP enabled.” 。如果设备已注册到 MDM，则此命令可能会显示相关的配置信息，包括 MDM 服务器的详细信息 。

```sh
sudo profiles show -type enrollment
```

![show type](images/macos-show-type-a.png)

> 此命令可以返回不同的状态，例如“No MDM enrollment”（未进行 MDM 注册）、“MDM enrolled”（已进行 MDM 注册）、“DEP Enrolled”（已进行 DEP 注册）等 。

```sh
profiles status -type enrollment
```

![status type](images/macos-show-type-b.png)


## 配置

当标准的 MDM 描述文件移除方法无效时，通常是因为设备受到了更高级别的管理，例如设备监管或通过 Apple 的设备注册计划（DEP）、Apple 商务管理（ABM）或 Apple 校园教务管理（ASM）进行的注册。

### 步骤1：备份重要数据

自己备份重要的数据

### 步骤2：禁用系统完整性保护 (SIP)

系统完整性保护（SIP）是 macOS 的一项功能，限制了 root 用户帐户在 Mac 操作系统的受保护部分可以执行的操作。禁用 SIP 对于删除某些类型的远程管理软件至关重要，这些软件会深度安装在系统中。

> 警告： 禁用系统完整性保护（SIP）会降低系统的安全性，并可能导致系统不稳定 。用户应仅在尝试移除 MDM 描述文件时临时禁用 SIP，并在完成后立即重新启用。

1. 重启Mac并按住 `Command + R` 进入恢复模式
2. 从实用工具菜单中打开终端并输入 `csrutil disable`
3. 重启 Mac 以应用更改

### 步骤3：移除 MDM 配置文件

```sh
cd /var/db/ConfigurationProfiles
sudo rm -rf *
sudo mkdir Settings
sudo touch Settings/.profilesAreInstalled
```

### 步骤4：修改 hosts 文件以阻止重新注册

```sh
sudo vim /etc/hosts
```

增加如下配置

```
0.0.0.0 iprofiles.apple.com
0.0.0.0 mdmenrollment.apple.com
0.0.0.0 deviceenrollment.apple.com
```

```sh
sudo dscacheutil -flushcache
```

### 步骤5：Enable SIP

1. 重启进入恢复模式 `Command + R`
2. 打开终端并通过输入 `csrutil enable` 来启用 SIP
3. 重启Mac完成安全设置


## 参考

- [如何在Mac上禁用远程管理](https://tsplus.net/zh/remote-access/blog/how-to-get-rid-of-remote-management-on-mac/)
- [请问Mac系统 弹窗显示：设备注册“Google LLC”可自动配置您的Mac。该如何取消？](https://www.zhihu.com/question/342191141/answer/1255561508)
