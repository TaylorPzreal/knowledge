---
title: "Sed"
# weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# Sed (Stream Editor)

Review

1. 2019/12/25

Sed is a powerful stream editor that can perform basic text transformations on an input stream (a file or input from a pipeline). It is commonly used for text substitution, deletion, insertion, and other text manipulations.

## Basic Usage

```bash
sed [options] 'command' file
```

### Common Options

- `-n`: Suppress automatic printing of pattern space
- `-e`: Add the script to the commands to be executed
- `-f`: Add the contents of script-file to the commands to be executed
- `-i`: Edit files in place (make backup if extension supplied)
- `-r`: Use extended regular expressions

## Basic Commands

### Substitution (s)

```bash
# Basic substitution
sed 's/old/new/' file.txt

# Global substitution (replace all occurrences)
sed 's/old/new/g' file.txt

# Case-insensitive substitution
sed 's/old/new/i' file.txt

# Replace only the 2nd occurrence on each line
sed 's/old/new/2' file.txt
```

### Deletion (d)

```bash
# Delete lines containing pattern
sed '/pattern/d' file.txt

# Delete lines 1-5
sed '1,5d' file.txt

# Delete last line
sed '$d' file.txt
```

### Printing (p)

```bash
# Print only lines matching pattern
sed -n '/pattern/p' file.txt

# Print lines 1-5
sed -n '1,5p' file.txt
```

### Insertion and Appending

```bash
# Insert text before line 4
sed '4i\This is inserted text' file.txt

# Append text after line 4
sed '4a\This is appended text' file.txt
```

## Advanced Usage

### Multiple Commands

```bash
# Using -e for multiple commands
sed -e 's/old/new/' -e 's/another/other/' file.txt

# Using semicolon to separate commands
sed 's/old/new/; s/another/other/' file.txt
```

### Address Ranges

```bash
# Apply command to lines 1-5
sed '1,5s/old/new/' file.txt

# Apply command from line 10 to end
sed '10,$s/old/new/' file.txt

# Apply command to lines matching pattern
sed '/pattern/s/old/new/' file.txt
```

### Hold Space and Pattern Space

```bash
# Swap pattern space and hold space
sed 'x' file.txt

# Copy hold space to pattern space
sed 'g' file.txt

# Append pattern space to hold space
sed 'H' file.txt
```

## Common Patterns

### Remove Empty Lines

```bash
sed '/^$/d' file.txt
```

### Remove Leading/Trailing Whitespace

```bash
# Remove leading whitespace
sed 's/^[ \t]*//' file.txt

# Remove trailing whitespace
sed 's/[ \t]*$//' file.txt
```

### Convert DOS Line Endings to Unix

```bash
sed 's/\r$//' file.txt
```

### Extract Specific Lines

```bash
# Extract lines 5-10
sed -n '5,10p' file.txt

# Extract lines containing pattern
sed -n '/pattern/p' file.txt
```

## macOS Specific Notes

On macOS, when using the `-i` option to edit files in place, you must specify an empty string as the backup extension:

```bash
sed -i '' 's/old/new/' file.txt
```

## Best Practices

1. Always test sed commands with `-n` and `p` first to see what will be affected
2. Use `-i` with caution, especially on macOS
3. When using regular expressions, consider using `-r` for extended regex support
4. For complex transformations, consider using a sed script file with `-f`
5. When working with large files, be mindful of performance implications

## Common Pitfalls

1. Forgetting to escape special characters in patterns
2. Not understanding the difference between `g` and `i` flags
3. Misusing address ranges
4. Not properly handling newlines in patterns
5. Forgetting macOS requires empty string for `-i` option

## Reference

- [GNU Sed Manual](https://www.gnu.org/software/sed/manual/sed.html)
- [Sed Tutorial](http://www.grymoire.com/Unix/Sed.html)
- [Sed Examples](https://www.geeksforgeeks.org/sed-command-in-linux-unix-with-examples/)
- [Sed Single vs Double Quotes](https://superuser.com/questions/1311023/sed-command-in-single-quotes-works-but-it-doesnt-using-double-quotes)
- [30分钟掌握SED](https://juejin.im/entry/586360f3570c3500695501d6#toc_29)
- [Sed Video Tutorial](https://www.youtube.com/watch?v=QaGhpqRll_k)
