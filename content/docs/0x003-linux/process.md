---
title: "Process"
# weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# 进程管理控制

Review

1. 2020/03/20

## 进程查看

### 基本进程查看

```bash
ps aux | grep redis    # 查看特定进程
ps -ef                 # 查看所有进程
ps -ef | grep java     # 查看 Java 进程
```

### 端口相关

```bash
netstat -anp tcp | grep 6379   # 查看端口占用情况
lsof -i :8080                  # 查看端口属于哪个程序
lsof -i tcp:8080              # 查看 TCP 端口 8080 的使用情况
```

### 进程详细信息

```bash
top                          # 实时查看进程状态
htop                         # 交互式进程查看器（需要安装）
btop
pstree                       # 以树状图显示进程
```

#### htop demo

```sh
brew install htop
```

![htop](images/htop-demo.png)

#### btop demo

```sh
brew install btop
```

![btop](images/btop-demo.png)

## 进程管理

### 终止进程

```bash
kill -9 PID                  # 强制终止进程
kill -15 PID                 # 优雅终止进程
pkill process_name           # 通过进程名终止
killall process_name         # 终止所有同名进程
```

### 进程信号

常用的信号值：

- `-1` (SIGHUP): 重新加载配置
- `-2` (SIGINT): 中断进程（Ctrl+C）
- `-9` (SIGKILL): 强制终止进程
- `-15` (SIGTERM): 正常终止进程
- `-19` (SIGSTOP): 暂停进程
- `-18` (SIGCONT): 继续运行暂停的进程

### 进程优先级

```bash
nice -n 10 command           # 以较低优先级运行命令
renice 10 -p PID            # 修改运行中进程的优先级
```

## 后台进程管理

### 后台运行

```bash
command &                   # 在后台运行命令
nohup command &             # 在后台运行命令，且不受终端关闭影响
```

### 作业控制

```bash
jobs                        # 查看后台作业
fg %n                       # 将后台作业 n 切换到前台
bg %n                       # 将暂停的作业 n 切换到后台
```

## 进程监控

### 系统资源监控

```bash
vmstat 1                    # 查看系统资源使用情况
vm_stat 1                   # for macOS
iostat 1                    # 查看磁盘 I/O 情况
free -h                     # 查看内存使用情况
```

### 进程资源使用

```bash
pidstat -p PID 1            # 监控特定进程的资源使用
strace -p PID               # 跟踪进程的系统调用
```

## 进程监控工具推荐

### 基础工具

- `pidof` - 查找指定程序名的进程 ID
- `pkill` - 通过进程名终止进程
- `kill` - 通过进程 ID 终止进程

### 系统监控工具

1. `top` - 经典的实时系统监控工具
2. `htop` - 交互式进程查看器，提供彩色界面和更多功能
3. `btop` - 现代化的系统资源监控工具，支持主题定制
4. `bashtop` - 基于 Bash 的系统监控工具，轻量级
5. `bpytop` - Python 实现的系统监控工具，功能丰富
6. `glances` - 跨平台的系统监控工具，支持多种输出格式

### 工具特点对比

| 工具名称 | 语言 | 特点 | 安装方式 |
|---------|------|------|----------|
| htop | C | 交互式界面，支持鼠标操作 | `brew install htop` |
| btop | C++ | 现代化界面，支持主题 | `brew install btop` |
| bashtop | Bash | 轻量级，纯 Bash 实现 | <https://github.com/aristocratos/bashtop> |
| bpytop | Python | 功能丰富，支持插件 | `brew install bpytop` |
| glances | Python | 跨平台，支持多种输出 | `brew install glances` |

## 实用技巧

1. 查找占用 CPU 最高的进程：

```bash
ps aux | sort -k3nr | head -n 10
```

2. 查找占用内存最高的进程：

```bash
ps aux | sort -k4nr | head -n 10
```

3. 查看进程的线程数：

```bash
ps -T -p PID
```

4. 查看进程打开的文件：

```bash
lsof -p PID
```

## 参考资料

- [Linux 进程管理](http://wuchong.me/blog/2014/07/24/linux-process-manage/)
- [Linux 进程管理详解](https://www.cnblogs.com/peida/archive/2012/12/19/2824418.html)
- <https://www.freecodecamp.org/news/the-best-linux-tutorials/>
- <https://guide.freecodecamp.org/linux>
- Command Line Crash Course <https://www.youtube.com/watch?v=yz7nYlnXLfE>

+
