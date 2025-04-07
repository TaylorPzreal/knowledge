---
title: "Rsync"
# weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# Rsync 命令指南

Review

1. 2021/04/25
2. 2024/11/10

Rsync (Remote Sync) 是一个在 Linux/Unix 系统中广泛使用的文件同步和传输工具。它能够高效地在本地和远程系统之间同步文件和目录，支持增量传输，是系统管理员和开发者的得力工具。

Rsync (Remote Sync) is a most commonly used command for copying and synchronizing files and directories remotely as well as locally in Linux/Unix systems. With the help of rsync command you can copy and synchronize your data remotely and locally across directories, across disks and networks, perform data backups and mirroring between two Linux machines.

## 主要特性

* 高效的文件同步：仅传输源和目标之间的差异部分
* 支持远程和本地同步
* 保留文件属性：权限、所有者、时间戳等
* 支持压缩传输，节省带宽
* 支持断点续传
* 支持排除/包含特定文件
* 支持删除目标端多余文件

Features

* It efficiently copies and sync files to or from a remote system.
* Supports copying links, devices, owners, groups and permissions.
* It’s faster than scp (Secure Copy) because rsync uses remote-update protocol which allows to transfer just the differences between two sets of files. First time, it copies the whole content of a file or a directory from source to destination but from next time, it copies only the changed blocks and bytes to the destination.
* Rsync consumes less bandwidth as it uses compression and decompression method while sending and receiving data both ends.

## 基本语法

```bash
rsync [选项] 源文件 目标文件
```

## 常用选项

| 选项         | 说明                         |
| ------------ | ---------------------------- |
| -a           | 归档模式，相当于 -rlptgoD    |
| -v           | 显示详细输出                 |
| -z           | 传输时压缩数据               |
| -h           | 以人类可读格式显示数字       |
| -e           | 指定远程 shell（通常为 ssh） |
| -r           | 递归复制目录                 |
| `--progress` | 显示传输进度                 |
| `--delete`   | 删除目标端多余文件           |
| `--exclude`  | 排除特定文件或目录           |
| `--include`  | 包含特定文件或目录           |
| -P           | 显示进度并支持断点续传       |

> 归档模式 (archive mode), archive mode allows copying files recursively and it also preserves symbolic links, file permissions, user & group ownerships and timestamps.

## 实用示例

### 1. 本地文件同步

```bash
# 同步单个文件
rsync -vzh a.txt b.txt

# 同步目录
rsync -avzh source_directory/ destination_directory/
```

### 2. 远程同步

```bash
# 本地到远程
rsync -avzh local_directory/ user@remote_host:/path/to/destination/

# 远程到本地
rsync -avzh user@remote_host:/path/to/source/ local_directory/
```

### 3. 使用 SSH 同步

```bash
# 本地到远程（使用 SSH）
rsync -avzhe ssh backup.tar user@remote_host:/backups/

# 远程到本地（使用 SSH）
rsync -avzhe ssh user@remote_host:/path/to/file /local/path/
```

### 4. 选择性同步

```bash
# 只同步特定文件
rsync -avze ssh --include '*.txt' --exclude '*' user@remote_host:/source/ /destination/

# 排除特定文件
rsync -avz --exclude '*.log' source/ destination/
```

### 5. 删除目标端多余文件

```bash
# 同步时删除目标端多余文件
rsync -avz --delete source/ destination/
```

### 6. 使用自定义 SSH 密钥

```bash
rsync -avzh --delete -e 'ssh -i ~/.ssh/custom_key' source/ user@remote_host:/destination/
```

## 性能优化

* 使用 `-z` 选项进行压缩传输
* 使用 `--bwlimit` 限制带宽使用
* 使用 `--partial` 支持断点续传
* 使用 `--progress` 显示传输进度

## 注意事项

1. 源路径末尾的斜杠 `/` 会影响同步行为：
   * 带斜杠：同步目录内容
   * 不带斜杠：同步整个目录

2. 使用 `--delete` 选项时要特别小心，确保不会误删重要文件

3. 建议在重要操作前先使用 `-n` 或 `--dry-run` 选项进行模拟运行

## 相关工具

* `scp` - 安全文件传输
* `sftp` - 安全文件传输协议
* `rz/sz` - 通过串口传输文件

## 参考资源

* [Rsync 官方文档](https://rsync.samba.org/documentation.html)
* [Linux 文件同步指南](https://www.tecmint.com/rsync-local-remote-file-synchronization-commands/)
