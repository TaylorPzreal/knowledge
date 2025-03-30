---
title: "Rechange Git History User"
date: 2025-03-30T20:43:27+08:00
tags: 
 - Git
 - Shell
categories: Development
# bookComments: false
# bookSearchExclude: false
---

# 修改GIT History提交的姓名和邮箱

```sh
#!/bin/sh
git filter-branch --env-filter '
OLD_EMAIL="旧邮箱@example.com"
CORRECT_NAME="新姓名"
CORRECT_EMAIL="新邮箱@example.com"
if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]; then
    export GIT_COMMITTER_NAME="$CORRECT_NAME"
    export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
fi
if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]; then
    export GIT_AUTHOR_NAME="$CORRECT_NAME"
    export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
fi
' --tag-name-filter cat -- --branches --tags
```

替换脚本中的 `OLD_EMAIL`、`CORRECT_NAME` 和 `CORRECT_EMAIL` 为实际值

```sh
chmod +x email.sh && ./email.sh
git push --force --all
```
