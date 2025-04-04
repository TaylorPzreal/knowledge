---
title: "Awk"
# weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# AWK

Review

1. 2020/01/01
2. 2022/04/12

## 简介

Awk 是一种强大的文本处理语言，由 Alfred Aho、Peter Weinberger 和 Brian Kernighan 开发（AWK 即取自他们姓氏的首字母）。它特别适合处理结构化文本数据，如日志文件、CSV 文件等。

Awk 的主要特点：

- 逐行处理文本数据
- 自动将每行分割成字段
- 支持模式匹配和动作执行
- 内置变量和函数
- 支持算术和字符串操作
- 支持条件语句和循环

## 基本语法

```sh
awk [选项] '模式 {动作}' 输入文件
```

### 常用选项

- `-F`：指定字段分隔符
- `-v`：定义变量
- `-f`：从文件读取 awk 程序

## 内置变量

| 变量 | 描述 |
|------|------|
| `$0` | 整行内容 |
| `$1-$n` | 第 n 个字段 |
| `NF` | 当前行的字段总数 |
| `NR` | 当前处理的行号 |
| `FS` | 输入字段分隔符（默认空格） |
| `OFS` | 输出字段分隔符（默认空格） |
| `RS` | 输入记录分隔符（默认换行符） |
| `ORS` | 输出记录分隔符（默认换行符） |
| `FILENAME` | 当前处理的文件名 |
| `FNR` | 当前文件中的行号 |

## 常用函数

### 字符串函数

- `length(str)`：返回字符串长度
- `substr(str, start, length)`：返回子字符串
- `tolower(str)`：转换为小写
- `toupper(str)`：转换为大写
- `split(str, arr, sep)`：分割字符串到数组
- `gsub(regex, replacement, str)`：全局替换

### 数学函数

- `sin(x)`：正弦
- `cos(x)`：余弦
- `sqrt(x)`：平方根
- `rand()`：随机数
- `int(x)`：取整

## 实用示例

### 示例数据

`employee.txt`

```txt
ajay manager account 45000
sunil clerk account 25000
varun manager sales 50000
amit manager account 47000
tarun peon sales 15000
deepak clerk sales 23000
sunil peon sales 13000
satvik director purchase 80000
```

### 基础操作

1. 打印所有行

```sh
awk '{print}' employee.txt
```

2. 打印匹配模式的行

```sh
awk '/manager/ {print}' employee.txt
```

3. 打印特定字段

```sh
awk '{print $1,$4}' employee.txt  # 打印第1和第4个字段
```

4. 添加行号

```sh
awk '{print NR,$0}' employee.txt
```

5. 打印指定行范围

```sh
awk 'NR==3, NR==6 {print NR,$0}' employee.txt
```

### 进阶操作

1. 条件过滤

```sh
awk '$3 == "account" {print}' employee.txt  # 打印部门为account的行
awk '$4 > 40000 {print}' employee.txt      # 打印工资大于40000的行
```

2. 计算统计

```sh
awk '{sum += $4} END {print "Total Salary:", sum}' employee.txt  # 计算总工资
awk '{count[$3]++} END {for (dept in count) print dept, count[dept]}' employee.txt  # 统计各部门人数
```

3. 格式化输出

```sh
awk '{printf "%-10s %-10s %-10s %10d\n", $1, $2, $3, $4}' employee.txt
```

4. 使用自定义分隔符

```sh
awk -F':' '{print $1}' /etc/passwd  # 使用冒号作为分隔符
```

5. 使用变量

```sh
awk -v min_salary=30000 '$4 > min_salary {print}' employee.txt
```

## 实际应用场景

1. 日志分析

```sh
# 统计HTTP状态码
awk '{count[$9]++} END {for (code in count) print code, count[code]}' access.log
```

2. CSV处理

```sh
# 计算CSV文件特定列的总和
awk -F',' '{sum += $3} END {print sum}' data.csv
```

3. 系统监控

```sh
# 监控CPU使用率
ps aux | awk 'NR>1 {sum += $3} END {print sum}'
```

4. 文本转换

```sh
# 将空格分隔的文件转换为CSV
awk '{print $1","$2","$3","$4}' employee.txt > employee.csv
```

## 最佳实践

1. 使用单引号包裹 awk 程序，避免 shell 解释特殊字符
2. 对于复杂的 awk 程序，建议使用 `-f` 选项从文件读取
3. 使用 `BEGIN` 和 `END` 块进行初始化和清理
4. 合理使用内置变量和函数
5. 注意字段分隔符的设置

## 参考资源

1. [GNU Awk User's Guide](https://www.gnu.org/software/gawk/manual/gawk.html)
2. [Awk Tutorial](https://www.tutorialspoint.com/awk/index.htm)
3. [Awk One-Liners](https://www.pement.org/awk/awk1line.txt)
4. [Built-in Variables](https://www.thegeekstuff.com/2010/01/8-powerful-awk-built-in-variables-fs-ofs-rs-ors-nr-nf-filename-fnr/)
