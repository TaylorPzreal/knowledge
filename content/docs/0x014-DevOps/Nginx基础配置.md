
**Review**
1. 2019/08/29
2. 2020/03/15
3. 2020/07/15
4. 2023-03-18 09:51

## 一、Introduction



## 二、Installation 


## 三、Configuration

### 基础配置
```Properties
user                            root;
worker_processes                1;

events {
  worker_connections            10240;
}

http {
  log_format                    '$remote_addr - $remote_user [$time_local] ' '"$request" $status $body_bytes_sent ' '"$http_referer" "$http_user_agent"';
  include                       mime.types;
  default_type                  application/octet-stream;
  sendfile                      on;
  #autoindex                    on;
  #autoindex_exact_size         off;
  autoindex_localtime           on;
  keepalive_timeout             65;
  gzip                          on;
  gzip_disable                  "msie6";
  gzip_min_length               100;
  gzip_buffers                  4 16k;
  gzip_comp_level               1;
  gzip_types                  text/plain application/x-javascript text/css application/xml text/javascript application/x-httpd-php image/jpeg image/gif image/png;
  gzip_types                    "*";
  gzip_vary                     off;
  server_tokens                 off;
  client_max_body_size          200m;

  server {
    listen                      80 default_server;
    server_name                 _;
    return                      403 /www/403/index.html;
  }

  include                       ../serve/*.conf;
}
```

### 隐藏 Nginx 版本信息
```Properties
http {
  server_tokens         off;
}
```

### 禁止ip直接访问80端口
```Properties
server {
  listen                80 default;
  server_name           _;
  return                500;
}
```

### 配置 web 服务
```Properties
server {
  # 项目启动端口
  listen            80;
  # 域名（localhost）
  server_name       _;
  # 禁止 iframe 嵌套
  add_header        X-Frame-Options SAMEORIGIN;
  
  # 访问地址 根路径配置
  location / {
    # 项目目录
    root 	    html;
    # 默认读取文件
    index           index.html;
    # 配置 history 模式的刷新空白
    try_files       $uri $uri/ /index.html;
  }
  
  # 后缀匹配，解决静态资源找不到问题
  location ~* \.(gif|jpg|jpeg|png|css|js|ico)$ { 
    root           html/static/;
  }
  
  # 图片防盗链
  location ~/static/.*\.(jpg|jpeg|png|gif|webp)$ {
    root              html;
    valid_referers    *.deeruby.com;
    if ($invalid_referer) {
      return          403;
    }
  }
  
  # 访问限制
  location /static {
    root               html;
    # allow 允许
    allow              39.xxx.xxx.xxx;
    # deny  拒绝
    deny               all;
  }
}
```

### PC端和移动端使用不同的项目文件映射
```Properties
server {
  location / {
    root /home/static/pc;
    if ($http_user_agent ~* '(mobile|android|iphone|ipad|phone)') {
      root /home/static/mobile;
    }
    index index.html;
  }
}
```

### 配置负载均衡
```Properties
upstream my_upstream {
  server                http://localhost:9001 weight=1;
  server                http://localhost:9002 weight=2;
  server                http://localhost:9003 backup;
}

server {
  listen                9000;
  server_name           test.com;

  location / {
    proxy_pass          http://my_upstream;
    proxy_set_header    Host $http_host;
    proxy_set_header    X-Real-IP $remote_addr;
    proxy_set_header    X-Forwarded-For $proxy_add_x_forwarded_for;
  }
}
```

#### proxy_pass模块常用指令
1. `proxy_pass`：指定需要反向代理的服务器地址，可以是一个upstream池
2. `proxy_next_upstream`：如果后端服务器不可用的话自动将请求转发到另一台服务器，默认为on，还可以设置为timeout或者http状态码
3. `proxy_method`：修改用户的method请求
4. `proxy_http_version`：修改用户的http协议版本
5. `proxy_set_header`：修改用户header头部，如客户端真实IP信息，常用选项
6. `proxy_set_body`：修改用户包体信息
7. `proxy_send_timeout`：默认60S
8. `proxy_connect_timeout`：默认60S，Nginx与后端服务器连接超时时间


### SSL 配置 HTTPS
```Properties
server {
  listen                      80;
  server_name                 www.xxx.com;
  # 将 http 重定向转移到 https
  return 301 https://$server_name$request_uri;
}

server {
  listen                      443 ssl;
  server_name                 www.xxx.com;
  ssl_certificate             /etc/nginx/ssl/www.xxx.com.pem;
  ssl_certificate_key         /etc/nginx/ssl/www.xxx.com.key;
  ssl_session_timeout         10m;
  ssl_ciphers                 ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
  ssl_protocols               TLSv1 TLSv1.1 TLSv1.2;
  ssl_prefer_server_ciphers   on;
  
  location / {
    root                    /project/xxx;
    index                   index.html index.htm index.md;
    try_files               $uri $uri/ /index.html;
  }
}
```


### Nginx 限制下载速率
**写在http段内**
limit_conn_zone $binary_remote_addr zone=perip:10m;
limit_conn_zone $server_name zone=perserver:10m;

**写在server段内**
limit_conn perip 10;
limit_conn perserver 100;
limit_rate_after 100M;
limit_rate 10k;

-   limit_conn_zone定义一个限制连接的桶；
-   $binary_remote_addr表示根据客户端IP作为key来计算连接数；
-   zone=addr声明这个桶的名称；
-   limit_conn执行限制连接数，后面的addr就是调用前面配置的桶。


## Reference
1. https://mp.weixin.qq.com/s/Nh-ysv7k7j3bd2HDMTv7Bw
2. [10 Tips for 10x Application Performance](https://www.nginx.com/blog/10-tips-for-10x-application-performance/)
3. [Nginx入门教程](https://xuexb.github.io/learn-nginx/)
4. [https://www.xiaoz.me/archives/12516](https://www.xiaoz.me/archives/12516)

