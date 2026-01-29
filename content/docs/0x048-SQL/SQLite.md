
Review
1. 2023-08-18 23:34

## 一、Introduction
[SQLite](https://www.sqlite.org/index.html) is a software library that provides a relational database management system. It is used in many applications, including mobile apps, web browsers, and desktop software. 

SQLite is a popular relational database management system (RDBMS) that is widely used in small to medium-sized applications. It is a self-contained, serverless, zero-configuration, transactional SQL database engine that is embedded into the end program. This means that SQLite does not require a separate server process or system to operate, making it an ideal choice for applications that require a lightweight, low-maintenance database solution. SQLite is also open-source and free to use, making it a popular choice for developers and organizations on a budget.


## 二、Basic Usage


```sh
# shell interactive
sqlite3

# start a database
sqlite3 test.db

# exit
.exit

# create table
create table tableName (colName);

# inset a record
insert into tableName values (1);

# search
select * from tableName;

# 
.schema
```

SQLite supports several data types, including:
1. **NULL** represents a missing or unknown value.
2. **INTEGER** represents a signed integer value.
3. **REAL** represents a floating-point value.
4. **TEXT** represents a text string.
5. **BLOB** represents a binary data value.


```sql
CREATE TABLE my_table (
  id INTEGER PRIMARY KEY,
  name TEXT,
  age INTEGER,
  height REAL,
  photo BLOB
);
```


## Reference

