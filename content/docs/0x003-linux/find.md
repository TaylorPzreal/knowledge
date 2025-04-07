---
title: "Find"
# weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# Find

Review

1. 2019/12/24
2. 2025/04/06

`find` 是一个强大的文件搜索工具，可以根据各种条件查找文件。

## 基本用法

```sh
# 在当前目录及其子目录中查找文件
find .

# 在指定目录中查找文件
find /path/to/directory

# 按文件名查找
find . -name "*.txt"

# 按文件类型查找
find . -type f  # 查找普通文件
find . -type d  # 查找目录
find . -type l  # 查找符号链接
```

## 高级用法

### 排除目录

```sh
# 排除单个目录
find . -path ./dir1 -prune -o -print

# 排除多个目录
find . -type d \( -path dir1 -o -path dir2 -o -path dir3 \) -prune -o -print

# 排除隐藏目录
find . -type d -name ".*" -prune -o -print
```

### 按时间查找

```sh
# 查找最近修改的文件（24小时内）
find . -mtime -1

# 查找超过7天未修改的文件
find . -mtime +7

# 查找最近访问的文件（24小时内）
find . -atime -1
```

### 按大小查找

```sh
# 查找大于10MB的文件
find . -size +10M

# 查找小于1KB的文件
find . -size -1k

# 查找空文件
find . -empty
```

### 执行操作

```sh
# 删除找到的文件
find . -name "*.tmp" -delete

# 对找到的文件执行命令
# 对找到的所有 .txt 文件执行 cat 命令
# find . -name "*.txt" 找到当前目录及子目录下所有 .txt 文件
# -exec cat {} \; 对每个找到的文件执行 cat 命令
# {} 会被替换为找到的文件名
# \; 表示命令结束
find . -name "*.txt" -exec cat {} \;

# 使用 xargs 处理找到的文件
find . -name "*.log" | xargs rm

# 
find . -type d -ipath "node_modules" | xargs rm -rf
```

### 权限相关

```sh
# 查找可执行文件
find . -type f -executable

# 查找具有特定权限的文件
find . -type f -perm 644

# 查找属于特定用户的文件
find . -user username
```

## 实用技巧

1. 使用 `-maxdepth` 限制搜索深度：

   ```sh
   find . -maxdepth 2 -name "*.txt"
   ```

2. 使用 `-iname` 进行不区分大小写的搜索：

   ```sh
   find . -iname "*.jpg"
   ```

3. 组合多个条件：

   ```sh
   find . -type f -name "*.txt" -size +1M -mtime -7
   ```

## 参考

- [How to exclude a directory in find command](https://stackoverflow.com/questions/4210042/how-to-exclude-a-directory-in-find-command)
- [GNU find manual](https://www.gnu.org/software/findutils/manual/html_node/find_html/index.html)
