
#OS 

**Review**
1. 2022/11/14
2. 2023/05/28
3. 2023/07/25

## 安装


## 环境配置
### SSH
```sh
sudo dnf install -y openssh-server

sudo systemctl start sshd.service

sudo systemctl enable sshd.service
```

### 关闭防火墙
```sh
sudo systemctl stop firewalld.service

sudo systemctl disable firewalld.service
```

### 配置远程登录
```sh
# 将本机的公钥复制到要登录的远程主机的 ~/.ssh/authorized_keys 文件中
ssh-copy-id taylorpzreal@myhost.com

# 远程主机配置相关文件权限
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys

# 重启两边的ssh服务
sudo systemctl restart sshd
```

## 安装驱动和Cuda

Drivers
refer [https://linuxhint.com/install-nvidia-drivers-on-fedora-35/](https://linuxhint.com/install-nvidia-drivers-on-fedora-35/)

```sh
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm


sudo dnf update 
sudo dnf install akmod-nvidia xorg-x11-drv-nvidia-cuda


sudo reboot

# 查看GPU使用情况
nvidia-smi
```




```sh
sudo dnf install cuda-devel cuda-libs cuda-tools
```


### Detect Nvidia Card

lspci | grep VGA

`output: 02:00.0 VGA compatible controller: NVIDIA Corporation TU116 [GeForce GTX 1660 Ti] (rev a1)`


### Install Nvidia Drivers
```sh
sudo reboot
```

**Question**
`Could not load dynamic library 'libcudart.so.11.0';`

**Install cuda**
```sh

```



**Vim**
```sh
sudo dnf install -y vim
```  

**zsh**
```sh
sudo dnf install -y zsh

sh -c "$(wget https://ghproxy.com/https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"

git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

sudo dnf install -y util-linux-user

chsh -s /usr/bin/zsh
```


**Docker**
[https://docs.docker.com/engine/install/fedora/](https://docs.docker.com/engine/install/fedora/)


**Rust & Cargo**
```sh
curl https://sh.rustup.rs -sSf | sh
```


**进入睡眠状态**
```sh
sudo systemctl suspend
```