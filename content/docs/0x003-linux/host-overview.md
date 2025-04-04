---
title: "Host Overview"
# weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# 主机规划与磁盘分区

Review

1. 2019/08/03

## 系统组件概述

各个组件或设备在Linux下面都是一个文件，这种设计理念使得Linux系统具有高度的统一性和灵活性。

## 硬件选择指南

如何挑选计算机硬件？

- 游戏机/工作机的考虑，游戏机要求更高
- 性能/价格比与性能/消耗的瓦数比的考虑，主流级产品一般比新产品更适合，省电也很重要
- 支持度的考虑，硬件开发商是否提供了适当的驱动程序
- 内存需求：建议至少8GB，对于开发或虚拟化环境建议16GB以上
- CPU选择：多核心处理器更适合多任务处理，建议至少4核心
- 显卡选择：对于普通办公，集成显卡足够；对于图形工作或游戏，需要独立显卡

## 存储系统

### 磁盘阵列（RAID）

磁盘阵列（RAID）是利用硬件技术将数个硬盘整合成为一个大硬盘的方法，操作系统只会看到最后被整合起来的大硬盘。

常见的RAID级别：

- RAID 0：条带化，提高性能，无冗余
- RAID 1：镜像，提供数据冗余
- RAID 5：分布式奇偶校验，平衡性能和冗余
- RAID 10：RAID 1+0，结合镜像和条带化

### 分区表格式

1. MBR（MS-DOS）分区表（Master Boot Record）
   - 最大支持2TB磁盘
   - 最多4个主分区
   - 可以通过扩展分区创建更多逻辑分区

2. GPT（GUID Partition Table）
   - 支持超过2TB的磁盘
   - 最多支持128个分区
   - 提供更好的数据完整性保护
   - 与UEFI固件配合使用

### 磁盘结构

![linux-Cluster](images/linux-Cluster.png)

![linux-Spindle](images/linux-Spindle.png)

磁盘结构详解：

- 扇区（Sector）：磁盘的最小物理存储单位，通常为512字节或4K字节
- 磁道（Track）：同一盘片上的同心圆
- 柱面（Cylinder）：所有盘片的同一磁道组成的圆柱体
- 簇（Cluster）：文件系统分配空间的最小单位，由多个扇区组成

### MBR结构

第一个扇区（512字节）包含：

- 主引导记录（446字节）：存储启动程序
- 分区表（64字节）：记录硬盘分区状态
- 结束标志（2字节）：0x55AA

由于分区表所在的区块仅有64字节，因此仅能有4组记录区，每组记录了该区段的起始于结束的柱面号码。

### 文件系统选择

常见的Linux文件系统：

- ext4：最常用的Linux文件系统，稳定可靠
- XFS：高性能文件系统，适合大文件处理
- Btrfs：新一代文件系统，支持快照和压缩
- ZFS：企业级文件系统，提供高级功能

## 系统启动

### 启动方式

1. BIOS（Basic Input Output System）
   - 传统启动方式
   - 使用MBR分区表
   - 启动过程较慢

2. UEFI（Unified extensible Firmware Interface）
   - 现代启动方式
   - 支持GPT分区表
   - 启动速度更快
   - 提供安全启动功能

### 启动流程

1. BIOS/UEFI初始化
2. 加载引导程序（如GRUB）
3. 加载内核
4. 初始化系统服务
5. 启动用户空间

## 系统要求

### 最小系统要求

- CPU：1GHz处理器
- 内存：2GB RAM
- 存储：20GB可用空间
- 显卡：支持1024x768分辨率

### 推荐系统要求

- CPU：2GHz双核处理器
- 内存：4GB RAM
- 存储：40GB可用空间
- 显卡：支持1920x1080分辨率

## Reference

- Linux对笔记本电脑的支持 <https://linux-laptop.net/>
- Linux对打印机的支持 <https://wiki.linuxfoundation.org/openprinting/start>
- Linux硬件兼容性数据库 <https://linux-hardware.org/>
- Linux文件系统文档 <https://www.kernel.org/doc/html/latest/filesystems/index.html>
