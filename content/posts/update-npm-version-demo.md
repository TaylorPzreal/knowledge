---
title: "Update npm Version Demo"
date: 2019-12-23
tags: 
 - npm
 - nodejs
categories: frontend
# bookComments: false
# bookSearchExclude: false
---

2019/12/23

```sh
#!/bin/bash

dir=$1

cd $dir;
git checkout release/aaa
git pull
branch=`git rev-parse --abbrev-ref HEAD`
echo "\ncurrent branch is: $branch\n"

if [[ $branch != 'release/aaa' ]]; then
    echo "Your branch is not exist."
    exit 1;
fi

# update version
echo '---------------update version-----------------'
cVersion=`awk -F'"' '/"version":/{print $4}' package.json`
cPatch=`echo "$cVersion" | grep -E -o '[[:digit:]]+$'`
nPatch=$(($cPatch+1))
nVersion=`echo "$cVersion" | sed -E "s/[[:digit:]]+$/$nPatch/"`

echo "change version $cPatch to $nPatch"
echo "current version is: : $cVersion"
echo "next version is: $nVersion"
echo ''


# replacde package.json package-lock.json
echo '----------replace package version-------------'
sed -i '' "/\"version\"/s/$cVersion/$nVersion/" package.json
sed -i '' "1,/\"version\"/s/$cVersion/$nVersion/" package-lock.json

# diff
echo '************git diff code************'
git diff | cat
echo '\n'

# add, commit, push
echo "git add -> commit -> push code."
git add package.json package-lock.json
git commit -m 'chore: update version'
git push

echo "done."

```
