---
title: "Disk"
# weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# 磁盘空间管理

Review

1. 2020/03/20

## 基本概念

在Linux系统中，磁盘空间管理是系统管理员的重要任务之一。主要涉及两个核心命令：`du` (disk usage) 和 `df` (disk filesystem)。

## du 命令详解

`du` 命令用于显示目录或文件所占用的磁盘空间。

### 常用选项

* `-h`：以人类可读的格式显示（如 K、M、G）
* `-s`：只显示总计大小
* `-a`：显示所有文件和目录的大小
* `-c`：显示总计并显示总计大小
* `--max-depth=N`：显示目录层级深度

### 常用命令示例

* `du -sh [目录名]`：显示目录的总大小
* `du -sm [目录名]`：以MB为单位显示目录大小
* `du -h [目录名]`：显示目录下所有文件和子目录的大小
* `du -sh *`：显示当前目录下所有文件和目录的大小
* `du -h --max-depth=1`：显示当前目录下第一级子目录的大小，简写为 `du -h -d 1`

## df 命令详解

`df` 命令用于显示文件系统的磁盘空间使用情况。

### 常用选项

* `-h`：以人类可读的格式显示
* `-l`：只显示本地文件系统
* `-T`：显示文件系统类型
* `-i`：显示inode使用情况

### 常用命令示例

* `df -h`：显示所有文件系统的使用情况
* `df -hl`：显示本地文件系统的使用情况
* `df -hT`：显示文件系统类型和使用情况
* `df -hi`：显示inode使用情况

## 其他实用命令

### 查找大文件

* `find /path/to/directory -type f -size +100M`：查找大于100M的文件
* `find /path/to/directory -type f -size +1G -exec ls -lh {} \;`：查找大于1G的文件并显示详细信息

### 清理磁盘空间

* `rm -rf /path/to/directory/*`：删除目录下所有文件
* `find /path/to/directory -type f -name "*.log" -mtime +30 -delete`：删除30天前的日志文件

## 注意事项

1. `du` 和 `df` 的区别：
   * `du` 是面向文件的命令，只计算被文件占用的空间
   * `df` 是基于文件系统总体来计算，包括文件系统metadata占用的空间

2. 磁盘空间不足时：
   * 使用 `df -h` 查看哪个分区空间不足
   * 使用 `du -sh *` 找出占用空间大的目录
   * 使用 `find` 命令定位大文件
   * 清理不必要的文件或日志

3. 定期检查磁盘空间使用情况，避免系统因磁盘空间不足而出现问题。
