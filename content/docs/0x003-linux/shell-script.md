---
title: "Shell Script"
# weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# Shell script

Review
1. 2019/12/25
2. 2020/04/16
3. 2024/06/20

## 脚本头部规范

```sh
#!/bin/bash
set -euo pipefail
trap "echo 'error: Script failed: see failed command above'" ERR
```

## 添加颜色输出

```sh
echo -e "\e[COLORmSample Text\e[0m"
```

| **Option** | **Description**                            |
| ---------- | ------------------------------------------ |
| `-e`       | Enable interpretation of backslash escapes |
| `\e[`      | Begin the color modifications              |
| `COLORm`   | Color Code + ‘m’ at the end                |
| `\e[0m`    | End the color modifications                |

```sh
$ echo -e "\e[31mRed Text\e[0m"
```

```sh
# info=\e[0;36m
# warning=\e[;33m
# success=\e[0;32m
# error=\e[0;31m
# nc=\e[0m
```

- [https://stackoverflow.com/questions/5947742/how-to-change-the-output-color-of-echo-in-linux](https://stackoverflow.com/questions/5947742/how-to-change-the-output-color-of-echo-in-linux)
- [https://www.shellhacks.com/bash-colors/](https://www.shellhacks.com/bash-colors/)

## 查找双字节文字

```sh
perl -ane '{ if(m/[[:^ascii:]]/) { print  } }
```

## Reference
1. [https://github.com/wangdoc/bash-tutorial](https://github.com/wangdoc/bash-tutorial)
2. [https://github.com/jlevy/the-art-of-command-line/blob/master/README-zh.md](https://github.com/jlevy/the-art-of-command-line/blob/master/README-zh.md) 
3. [https://devhints.io/bash](https://devhints.io/bash) 
4. Shellcheck [https://github.com/koalaman/shellcheck](https://github.com/koalaman/shellcheck) 
5. awesome shell [https://github.com/alebcay/awesome-shell](https://github.com/alebcay/awesome-shell) 
6. Filenames and Pathnames in Shell: How to do it Correctly [https://dwheeler.com/essays/filenames-in-shell.html](https://dwheeler.com/essays/filenames-in-shell.html)
