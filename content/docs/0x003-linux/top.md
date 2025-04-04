---
title: "Top"
# weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# Linux System Monitoring Commands

Review

1. 2020/04/15

This guide covers essential Linux system monitoring commands for analyzing system performance and resource usage.

## 1. top - Process Activity Monitor

`top`（Time of Process）is a real-time system monitor that displays system summary information and a list of processes currently being managed by the Linux kernel.

### Basic Usage

```bash
top
```

![top](images/top-demo.png)

### Key Metrics

- **CPU Usage**:
  - `%us`: User space CPU usage (without nice scheduling)
  - `%sy`: System space CPU usage (kernel processes)
  - `%ni`: User space CPU usage with nice scheduling
  - `%id`: Idle CPU
  - `%wa`: CPU waiting for I/O operations
  - `%hi`: Hardware interrupt handling
  - `%si`: Software interrupt handling
  - `%st`: CPU stolen by virtual machine

- **Memory Usage**:
  - `Mem`: Physical memory usage
  - `Swap`: Swap space usage

### Interactive Commands

- `P`: Sort by CPU usage
- `M`: Sort by memory usage
- `N`: Sort by process ID
- `k`: Kill a process
- `q`: Quit top
- `1`: Toggle CPU core display

## 2. free - Memory Usage

`free` displays the total amount of free and used physical and swap memory in the system.

```sh
brew install procps
```

### Basic Usage

```bash
free -h  # Human readable format
free -m  # Display in megabytes
```

### Key Metrics

- `total`: Total installed memory
- `used`: Used memory
- `free`: Unused memory
- `shared`: Memory used by tmpfs
- `buff/cache`: Memory used by buffers and cache
- `available`: Memory available for new applications

## 3. vmstat - Virtual Memory Statistics

`vmstat` reports information about processes, memory, paging, block IO, traps, and CPU activity.

### Basic Usage

```bash
vmstat 1  # Update every second

# for macOS
vm_stat -c 5 1
```

### Key Metrics

- **Procs**:
  - `r`: Running processes
  - `b`: Blocked processes
- **Memory**:
  - `swpd`: Used swap space
  - `free`: Free memory
  - `buff`: Buffer memory
  - `cache`: Cache memory
- **Swap**:
  - `si`: Swap in
  - `so`: Swap out
- **IO**:
  - `bi`: Blocks in
  - `bo`: Blocks out
- **System**:
  - `in`: Interrupts per second
  - `cs`: Context switches per second
- **CPU**:
  - `us`: User time
  - `sy`: System time
  - `id`: Idle time
  - `wa`: I/O wait time
  - `st`: Stolen time

get free memory

```sh
vm_stat | perl -ne '/page size of (\d+)/ and $size=$1; /Pages free:\s+(\d+)/ and printf("Free Memory: %.2f MB\n", $1*$size/1048576)'
```

## 4. pmap - Process Memory Map

`pmap` reports the memory map of a process, showing the memory usage of each segment.

```sh
brew install pmap
```

### Basic Usage

```bash
pmap -x <PID>  # Detailed memory map
pmap -d <PID>  # Display device format
```

### Example

```bash
# View memory usage of process with PID 5647
pmap -d 5647
```

### Key Information

- Address space
- Permissions
- Offset
- Device
- Mapping name
- Size
- RSS (Resident Set Size)
- Dirty pages
- Referenced pages
- Anonymous pages

## Best Practices

1. **Regular Monitoring**:
   - Use `top` for real-time monitoring
   - Schedule regular checks with `vmstat`
   - Monitor memory usage with `free`

2. **Troubleshooting**:
   - High CPU usage: Check `top` for process details
   - Memory issues: Use `free` and `pmap`
   - I/O bottlenecks: Monitor with `vmstat`

3. **Performance Optimization**:
   - Identify memory-hungry processes with `pmap`
   - Track system resource trends
   - Monitor swap usage to prevent performance degradation

Remember to run these commands with appropriate permissions (usually as root or with sudo) for complete system information.
