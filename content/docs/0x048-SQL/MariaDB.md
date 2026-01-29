

Review
1. 2023-03-25 12:20

## 一、Introduction


## 二、Installation MariaDB

### Installing MariaDB on Fedora37

```sh
sudo dnf update
sudo dnf install mariadb-server
```

### Configuring MariaDB
```sh
sudo systemctl enable mariadb
sudo systemctl start mariadb
```

```sh
sudo mariadb-secure-installation
```


### 配置允许远程访问
```sh
mariadb -u root -p
```

```sh
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '123456' WITH GRANT OPTION;

flush privileges;
```

### 远程访问
通过客户端软件访问即可。



## Reference
1. https://docs.fedoraproject.org/en-US/quick-docs/installing-mysql-mariadb/
