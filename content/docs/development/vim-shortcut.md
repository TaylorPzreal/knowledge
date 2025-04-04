---
title: "Vim Shortcut"
# weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# Vim Shortcut Key

Review
1. 2019/08/16

## Editor
- emacs
- vi
- nano
- vim

vim环境设置文件 `~/.vimrc`
vim记录文件(曾经做过的操作记录) `~/.viminfo`

## vim 按键说明

命令模式可用功能的按键说明，光标移动、复制粘贴、查找替换

Ctrl + f 向下移动一页
Ctrl + b 向上移动一页
Ctrl + d 向下移动半页
Ctrl + u 向上移动半页

+ 光标移动到非空格符下一行
- 光标移动到非空格符上一行

`n<space>` 向右移动n个字符

H 移动到屏幕最上方那一行的第一个字符
M 移动到屏幕中央那一行的第一个字符
L 移动到屏幕最下方那一行的第一个字符
G 移动到最后一行
nG 移动到指定行
`n<Enter>` 向下移动n行

```vim
:n1,n2s/word1/word2/gc g -- global c -- confirm
```

nx 向后删除n个字符
nX 向前删除n个字符
ndd 删除（剪切）本行已向下共n行 , d1G, dG, d0, d^, d$, 

nyy 复制光标所在的向下n行 y1G, yG, y0, y^, y$
p将已复制的数据在光标下一行粘贴
P将已复制的数据在光标上一行粘贴

J将光标所在行与下一行的数据结合成一行

u 回复前一个操作
Ctrl + r 重构上一个操作

c重复删除多个数据，例如向下删除10行，【10cj】

I 目前所在行第一个非空个字符插入
A 目前所在行最后一个字符插入

ZZ 若文件没有修改，则不保存退出，若文件已经修改过，则保存后退出。

`:w [filename]` 另存为
`:r [filename]` 读入另一个文件的数据，将数据加载到光标所在行后面
`:n1, n2 w [filename]` n1 - n2 行保存为filename这个文件
`:! command` 暂时退出vim到命令式下执行command命令。

v 字符选择
V 行选择
Ctrl + v 矩形选择

vim file1 file2 file3 …
:n 编辑下一个
:N 编辑上一个
:files 列出所有开启文件

`:sp [filename]` filename可有可无，如果想要在新窗口启动另一个文件就加入文件名，否则在另一个窗口出现的是本文件
Ctrl + w + j 下一个窗口
Ctrl + w + k 上一个窗口
Ctrl + w + q or :close退出此窗口

关键词补全功能
ctrl + x -> ctrl + n 当前 文件内容文字 作为关键词 
ctrl + x -> ctrl + f 当前目录 文件名 作为关键词
ctrl + x -> ctrl + o 以扩展名作为语法补充，以vim内置的关键词予以补齐

## Reference

https://www.vim.org/
