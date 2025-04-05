---
title: "Bash"
# weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# Bash Shell

Review

1. 2019/09/04
2. 2020/02/29

第一个流行的Shell是有Steven Bourne开发的，为感激他的奉献，命名为BourneShell（sh）。
bash是Bourne shell的增强版本，也是机遇GNU的架构下发展出来的，称为Bourne Again SHell（bash）。

Bash shell功能

- 历史命令
- 命令与文件补全功能
- 命令别名设置功能
- 任务管理、前台、后台控制：（job control、foreground、background）
- 程序化脚本（shell script）
- 通配符（Wildcard）

## 基础命令

查询命令是否为 bash shell 内置命令：`type`

```bash
type ls
type cd
```

## 变量

- 环境变量，通常以大写字符表示，自定义变量驼峰命名即可
- 变量的使用 `$var`, or `${var}`
- 变量与变量内容以一个等号来连接，等号两边不能直接接空格
- 双引号内的变量会动态取值，单引号不能注入变量值。
- 执行一串命令，需要执行其他额外命令来提供信息，可通过 `command` or $(command)
- 如：`version=$(uname -r)`
- 若变量需要在其他子程序执行，则需要以export来是变量变成环境变量。子进程不会继承父进程的自定义变量。
- 取消变量的方法为使用 `unset`

### 环境变量相关命令

- `env` 用于观察环境变量
- `set` 用于观察所有变量（环境变量+自定义变量）
- `export` 展示所有的环境变量

### 特殊变量

- `$?` 上个执行命令的返回值
  - 成功执行返回0
  - 执行错误返回非0值
- `$$` 当前Shell的进程ID
- `$0` 当前脚本的名称
- `$1-$9` 脚本的参数
- `$#` 传递给脚本的参数个数
- `$*` 所有参数作为一个字符串
- `$@` 所有参数作为独立的字符串

### 变量操作

```bash
# 变量声明
declare -i number=42
declare -r readonly_var="constant"

# 设置为整数
typeset -i var=5+3    # var=8
declare -i var=5+3     # 效果相同

# 只读变量
typeset -r PI=3.14
declare -r PI=3.14     # 等效操作

# 大小写转换
typeset -u UPSTR="hello"  # UPSTR="HELLO"
declare -l LOWSTR="WORLD" # LOWSTR="world"

# 变量替换
${var:-default}  # 如果var未设置，使用default
${var:=default}  # 如果var未设置，设置var为default
${var:+value}    # 如果var已设置，使用value
${var:?message}  # 如果var未设置，显示错误信息

# 字符串操作
${#var}          # 字符串长度
${var:start:len} # 子字符串
${var#pattern}   # 删除最短匹配前缀
${var##pattern}  # 删除最长匹配前缀
${var%pattern}   # 删除最短匹配后缀
${var%%pattern}  # 删除最长匹配后缀
```

## 历史命令

- `history` 查看历史命令
- `!number` 执行第number条命令
- `!command` 向前查找开头为command的命令并执行
- `!!` 执行上一个历史命令
- `!$` 上一个命令的最后一个参数
- `!^` 上一个命令的第一个参数
- `!*` 上一个命令的所有参数

## 配置文件

- `/etc/profile` 系统整体的设置
- `~/.bash_profile` 用户登录时执行
- `~/.bashrc` 每次打开新终端时执行
- `~/.bash_logout` 退出登录时执行

使用 `source` 或 `.` 命令重新加载配置文件：

```bash
source ~/.bashrc
# 或
. ~/.bashrc
```

## 通配符

- `*` 匹配任意多个字符
- `?` 匹配单个字符
- `[]` 匹配指定范围内的字符
- `[!]` 匹配不在指定范围内的字符
- `{}` 生成多个匹配项

## 正则表达式

- `[:alnum:]` `[0-9A-Za-z]`  # 字母和数字
- `[:alpha:]` `[a-zA-Z]`     # 字母
- `[:blank:]` 空格键，Tab键
- `[:space:]` 任何会产生空白的字符，包括空格键、【Tab】、CR等
- `[:cntrl:]` 控制按键，CR, LF, Tab, Del
- `[:digit:]` `[0-9]`        # 数字
- `[:graph:]` 可打印的非空白字符
- `[:lower:]` `[a-z]`        # 小写字母
- `[:upper:]` `[A-Z]`        # 大写字母
- `[:print:]` 可打印字符，包括空格
- `[:punct:]` 标点符号
- `[:xdigit:]` `[0-9A-Fa-f]` # 十六进制数字

示例

```sh
sed -i '' 's/\t/[[:space:]]{2}/g' nginx.conf
```

## 重定向

- `>` 输出重定向（覆盖）
- `>>` 输出重定向（追加）
- `<` 输入重定向
- `2>` 错误输出重定向
- `&>` 标准输出和错误输出重定向
- `|` 管道，将前一个命令的输出作为后一个命令的输入

## 进程控制

- `&` 后台运行
- `jobs` 查看后台任务
- `fg` 将后台任务调到前台
- `bg` 继续运行后台任务
- `Ctrl+Z` 暂停当前任务
- `Ctrl+C` 终止当前任务

## 常用快捷键

- `Ctrl+A` 移动到行首
- `Ctrl+E` 移动到行尾
- `Ctrl+U` 删除到行首
- `Ctrl+K` 删除到行尾
- `Ctrl+R` 搜索历史命令
- `Ctrl+L` 清屏
- `Ctrl+D` 退出终端
- `Tab` 命令补全
- `Ctrl+B` 向后移动一个字符
- `Ctrl+F` 向前移动一个字符

## 调试技巧

```bash
# 启用调试模式
set -x
# 禁用调试模式
set +x

# 检查脚本语法
bash -n script.sh

# 跟踪脚本执行
bash -v script.sh
```

## 最佳实践

1. 使用引号保护变量和字符串
2. 使用 `[[ ]]` 进行条件测试
3. 使用 `set -e` 在出错时立即退出
4. 使用 `set -u` 检查未定义变量
5. 使用 `set -o pipefail` 检查管道命令的失败
6. 使用函数组织代码
7. 添加适当的注释
8. 使用有意义的变量名
9. 处理错误情况
10. 使用 `trap` 处理信号
