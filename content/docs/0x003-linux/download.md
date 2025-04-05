---
title: "Download"
# weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---


## 常用下载工具

Review

1. 2019/02/15
2. 2023/08/12
3. 2024/11/10

### 1. aria2c

aria2c 是一个轻量级的多协议和多源命令行下载工具，支持 HTTP/HTTPS、FTP、SFTP、BitTorrent 和 Metalink。

```bash
# 基本下载
aria2c http://example.com/file.zip

# 多线程下载
aria2c -s 16 http://example.com/file.zip

# 断点续传
aria2c -c http://example.com/file.zip
```

### 2. curl

curl 是一个强大的命令行工具，用于传输数据，支持多种协议。

```bash
# 基本下载
curl -O http://example.com/file.zip

# 显示进度条
curl -# -O http://example.com/file.zip

# 断点续传
curl -C - -O http://example.com/file.zip
```

### 3. wget

wget 是一个简单可靠的命令行下载工具，支持 HTTP、HTTPS 和 FTP。

```bash
# 基本下载
wget http://example.com/file.zip

# 后台下载
wget -b http://example.com/file.zip

# 断点续传
wget -c http://example.com/file.zip
```

### 4. axel

axel 是一个轻量级的下载加速器，支持多线程下载。

```bash
# 基本下载
axel http://example.com/file.zip

# 指定线程数
axel -n 10 http://example.com/file.zip
```

### 5. lftp

lftp 是一个功能强大的文件传输程序，支持多种协议。

```bash
# 基本下载
lftp -c "get http://example.com/file.zip"

# 镜像下载
lftp -c "mirror http://example.com/directory"
```

### 6. rsync

rsync 是一个快速、多功能的文件复制工具，特别适合大文件和目录的同步。

```bash
# 基本同步
rsync -avz source/ destination/

# 远程同步
rsync -avz user@remote:/path/to/source/ /path/to/destination/
```

### 7. scp

scp 用于在本地和远程系统之间安全地复制文件。

```bash
# 下载文件
scp user@remote:/path/to/file /local/path

# 上传文件
scp /local/path/file user@remote:/path/to/destination
```

## 选择建议

- 对于大文件下载：推荐使用 `aria2c` 或 `axel`，支持多线程下载
- 对于简单下载：使用 `wget` 或 `curl`，操作简单直观
- 对于文件同步：使用 `rsync`
- 对于安全传输：使用 `scp` 或 `lftp`
