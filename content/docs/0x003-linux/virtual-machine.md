---
title: "Virtual Machine"
# weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# Linux 虚拟机解决方案

Review

1. 2020/11/07

## 1. 常见虚拟机方案

### 桌面级解决方案

- VirtualBox
- VMWare
- Hvper-V
- Vagrant

### 服务器级解决方案

- openVZ
- XenServer
- ESX
- Ken
- KVM（推荐）
- Docker
- vsf
- VPS

## 2. KVM 虚拟机配置

KVM(Kernel-based Virtual Machine)

### 2.1 系统准备

下载 CentOS 7 镜像：

```bash
wget https://mirrors.tuna.tsinghua.edu.cn/centos/7.8.2003/isos/x86_64/CentOS-7-x86_64-Minimal-2003.iso
wget https://mirrors.tuna.tsinghua.edu.cn/centos/7.8.2003/isos/x86_64/sha256sum.txt
```

### 2.2 创建虚拟机

#### Master 节点配置

```bash
virt-install \
--virt-type=kvm \
--name centos7-master \
--ram 8192 \
--vcpus=4 \
--os-variant=centos7.0 \
--cdrom=/var/lib/libvirt/boot/CentOS-7-x86_64-Minimal-2003.iso \
--network=bridge=br0,model=virtio \
--graphics vnc \
--disk path=/var/lib/libvirt/images/centos7-master.qcow2,size=40,bus=virtio,format=qcow2
```

#### Node 节点配置

```bash
virt-install \
--virt-type=kvm \
--name centos7-node \
--ram 8192 \
--vcpus=4 \
--os-variant=centos7.0 \
--cdrom=/var/lib/libvirt/boot/CentOS-7-x86_64-Minimal-2003.iso \
--network=bridge=br0,model=virtio \
--graphics vnc \
--disk path=/var/lib/libvirt/images/centos7-node.qcow2,size=40,bus=virtio,format=qcow2
```

## 3. VNC 远程连接配置

VNC (Virtual Network Computing)

### 3.1 获取 VNC 端口

```bash
virsh dumpxml centos7 | grep vnc
```

输出示例：

```xml
<graphics type='vnc' port='5901' autoport='yes' listen='127.0.0.1'>
```

### 3.2 建立 SSH 隧道

Please note down the port value (i.e. 5901). You need to use an SSH client to setup tunnel and a VNC client to access the remote vnc server. Type the following SSH port forwarding command from your `client/desktop/macbook` pro system:

```bash
ssh taylorpzreal@192.168.0.104 -L 5901:127.0.0.1:5901
```

### 3.3 使用 VNC 客户端连接

- 地址：127.0.0.1
- 端口：5901

## 4. 网络配置

### 4.1 添加网络接口

#### 虚拟机关机状态下

```bash
virsh attach-interface vm1 bridge br0 --model virtio --config
```

#### 虚拟机开机状态下

```bash
virsh attach-interface vm2 bridge br0 --model virtio --current
```

### 4.2 持久化网络配置

```bash
cd /etc/libvirt/qemu
virsh dumpxml vm2 > vm2.xml
```

## 5. 参考资料

- [KVM 中文维基](https://wiki.archlinux.org/index.php/KVM_(简体中文))
- [KVM FAQ](http://www.linux-kvm.org/page/FAQ#What_is_the_difference_between_kvm_and_Xen.3F)
- [KVM - Fix Missing Default Network](https://blog.programster.org/kvm-missing-default-network)
- [How to install KVM on CentOS 7 / RHEL 7 Headless Server](https://www.cyberciti.biz/faq/how-to-install-kvm-on-centos-7-rhel-7-headless-server/)
- [KVM 官方网站](https://www.linux-kvm.org/page/Main_Page)
- [VNC Viewer 下载](https://www.realvnc.com/en/connect/download/viewer/macos/)
