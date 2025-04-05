---
title: "Command"
# weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# Linux Command Reference

Review

1. 2019/11/30
2. 2023/03/15

## Shell Basics

### Shell Information

```bash
# Check current shell
echo $SHELL
echo $0
env | grep SHELL
ps
```

### Command Information

```bash
type    # Show how a command name is interpreted
which   # Show which executable will be used
man     # Display manual pages
apropos # Search manual pages
info    # Display info pages
whatis  # Display one-line manual page descriptions
alias   # Create command aliases
```

## File Operations

### Text Processing

```bash
# View file contents
cat file.txt
head file.txt    # Show first lines
tail file.txt    # Show last lines
less file.txt    # Interactive file viewer

# Text manipulation
cut             # Cut sections from each line
tr              # Translate or delete characters
sort            # Sort lines of text
uniq            # Report or omit repeated lines
wc              # Print line, word, and byte counts
grep            # Print lines matching a pattern
```

### File Compression

```bash
# Basic tar operations
tar -czf archive.tar.gz file1 file2    # Create compressed archive
tar -tzf archive.tar.gz                # List archive contents
tar -xvzf archive.tar.gz               # Extract archive

# Tar with progress (Linux)
tar cf - /folder | pv -s $(du -sb /folder | awk '{print $1}') | gzip > archive.tar.gz

# Tar with progress (macOS)
tar cf - /folder | pv -s $(($(du -sk /folder | awk '{print $1}') * 1024)) | gzip > archive.tar.gz
```

### File Transfer

```bash
cp -r sourceFolder targetFolder        # Copy directory recursively
cp source dest                         # Copy file
scp sourceFile user@host:remotePath    # Secure copy to remote host
rsync -av source/ dest/                # Efficient file synchronization
```

## System Information

### Process Management

```bash
ps              # Display process status
top             # Display and update sorted process information
jobs            # List jobs
bg              # Run job in background
fg              # Run job in foreground
kill            # Send signal to process
killall         # Kill processes by name
shutdown        # Shutdown or restart system
```

### System Information

```bash
env             # Display environment variables
printenv        # Print environment variables
clear           # Clear terminal screen
history         # Display command history
dmesg           # Display kernel messages
```

## User and Permission Management

```bash
id              # Display user identity
chmod           # Change file mode
umask           # Set default file permissions
su              # Switch user
sudo            # Execute command as superuser
chown           # Change file owner
chgrp           # Change file group
passwd          # Change user password
chsh            # Change login shell
echo $SHELL     # show current shell
```

## Date and Time

```bash
# Get yesterday's date
date -d "yesterday 13:00" '+%Y-%m-%d'

# Format date
date '+%Y-%m-%d %H:%M:%S'
```

## macOS Specific Commands

```txt
sips -s format [image type] [file name] --out [output file]
```

```bash
# Convert image format
sips -s format jpeg input.png --out output.jpg
```

## Shell Scripting Tips

### Loops

```bash
# Number range
for i in {1..10}
do
    echo $i
done

# Conditional statements
echo "One for ${1:-you}, one for me."
```

### Best Practices

- In bash, prefer `[[` over `[` for string comparisons
- For arithmetic operations, use `((` instead of `[[`
- Use `set -e` in scripts to exit on error
- Use `set -u` to treat unset variables as errors
- Quote variables to prevent word splitting

## Text Processing Examples

### Merge Multiple Lines

```bash
# Using tr
cat file.txt | tr '\n' ','

# Using awk
cat file.txt | awk 'BEGIN{ORS=","}{print}'

# Using xargs and sed
cat file.txt | xargs | sed 's/ /,/g'
```

### Create File from Standard Input

```bash
cat > test.txt
# Type content
# Press Ctrl+D to finish
```

## 参考

1. 命令行的艺术：<https://github.com/jlevy/the-art-of-command-line/blob/master/README-zh.md>
2. The Bash Hackers wiki: <https://wiki.bash-hackers.org/>
3. Shell Style Guide: <https://google.github.io/styleguide/shell.xml>
4. Bash Programming - Introduction How To: <http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO.html#toc>
5. Advanced Bash-Scripting Guide: <http://www.tldp.org/LDP/abs/html/>
6. Perl tutorial: <https://www.youtube.com/watch?v=WEghIXs8F6c>
7. The bash guide: <https://guide.bash.academy/>
8. The Bash Hackers Wiki: <https://wiki.bash-hackers.org/>
9. Bash scripting cheatsheet: <https://devhints.io/bash>
10. Bash Completion：<https://iridakos.com/programming/2018/03/01/bash-programmable-completion-tutorial>
11. Bash cheatsheet: <https://devhints.io/bash>
12. Linux Basics <https://dev.to/rudrakshi99/linux-basics-2onj>
