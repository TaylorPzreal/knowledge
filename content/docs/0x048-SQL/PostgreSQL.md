
#SQL

Review
1. 2023-04-07 17:14

## 一、Introduction


## 二、Installation

### 2.1: Installing on Fedora37

```sh
sudo dnf update
sudo dnf install postgresql-server postgresql-contrib
```

### 2.2: Configuration
```sh
sudo systemctl enable postgresql
sudo postgresql-setup --initdb --unit postgresql
sudo systemctl start postgresql
```

修改默认密码
```sh
sudo -u postgres psql
```

```psql
postgres=# \password postgres
```

```psql
CREATE DATABASE my_project OWNER postgres;
```

### 2.3: 配置允许远程访问
The postgresql server is using two main configuration files
-   `/var/lib/pgsql/data/postgresql.conf`
-   `/var/lib/pgsql/data/pg_hba.conf`

#### 配置 `pg_hba.conf`

```
```sh
sudo vim /var/lib/pgsql/data/pg_hba.conf
```

将下面的内容
```Properties
# IPv4 local connections:
host    all             all             127.0.0.1/32            ident
# IPv6 local connections:
host    all             all             ::1/128                 ident
```

替换为
```Properties
# IPv4 local connections:
host    all             all             0.0.0.0/0              md5
# IPv6 local connections:
host    all             all             ::1/128                md5
```

#### 配置 `postgresql.conf`

```sh
sudo vim /var/lib/pgsql/data/postgresql.conf
```

将下面内容
```Properties
listen_addresses = 'localhost'          # what IP address(es) to listen on;
```

替换为
```Properties
listen_addresses = '*'          # what IP address(es) to listen on;
```

#### 配置防火墙

```sh
sudo firewall-cmd --permanent --add-port=5432/tcp
```

```sh
sudo systemctl restart postgresql.service
```

### 远程访问
通过客户端软件访问即可。



## Reference
1. [Fedora Databases PostgreSQL](https://docs.fedoraproject.org/en-US/quick-docs/postgresql/) 
2. [Prisma PostgreSQL database](https://www.prisma.io/dataguide/postgresql/setting-up-a-local-postgresql-database) 

