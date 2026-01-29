
Review
1. 2023-03-25 23:03

## 一、Introduction

1. 用户基本信息表
2. 主题表
3. 文章表
4. 书籍表
5. 电影表
6. 音乐表
7. TODO表
8. 时间线维度
9. Popular维度


**用户基本信息表**

```sql
CREATE TABLE `user` (
  `id` varchar(36) NOT NULL COMMENT 'userid',
  `username` varchar(50) DEFAULT NULL COMMENT 'account name, used to login',
  `nickname` varchar(50) DEFAULT NULL COMMENT 'used to display',
  `realname` varchar(50) DEFAULT NULL,
  `avatar` varchar(200) DEFAULT NULL,
  `age` tinyint(3) unsigned DEFAULT NULL,
  `gender` tinyint(2) unsigned DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL COMMENT '账号状态，是否被封禁了等',
  `phone` varchar(20) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `create_time` timestamp NOT NULL DEFAULT current_timestamp(),
  `update_time` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `oauth_type` varchar(50) DEFAULT NULL COMMENT '授权类型，包括weibo, qq, weixin等',
  `oauth_id` varchar(255) DEFAULT NULL,
  `unionid` varchar(255) DEFAULT NULL,
  `credential` varchar(255) DEFAULT NULL COMMENT '授权的token等认证信息',
  `login_ip` varchar(50) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `remark` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `phone` (`phone`),
  KEY `create_time_username_idx` (`create_time`,`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci COMMENT='用户基本信息表';
```


```sql
CREATE TABLE `post` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL DEFAULT 'no',
  `description` varchar(255) NOT NULL DEFAULT 'no',
  `create_time` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `update_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `status` tinyint(4) NOT NULL DEFAULT 0 COMMENT '阅读状态，0-未开始，1-进行中，2-已完成',
  `post_author` varchar(100) NOT NULL DEFAULT 'no',
  `post_author_avatar` varchar(255) DEFAULT NULL,
  `post_link` varchar(255) NOT NULL DEFAULT '',
  `post_cover_image_link` varchar(255) DEFAULT NULL,
  `post_content` longtext DEFAULT NULL,
  `post_publish_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `user_id` varchar(36) NOT NULL DEFAULT '' COMMENT 'user_id',
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='blog/post/文章表';
```


```sql
CREATE TABLE `tag` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `create_time` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
```


```sql
CREATE TABLE `post_tag` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `post_id` bigint(20) DEFAULT NULL,
  `tag_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
```



## Reference
1. [21个MySQL表设计的经验准则](https://www.longkui.site/mysql/21mysql/5018/)
