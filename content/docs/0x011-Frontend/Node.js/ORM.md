
Review
1. 2022/08/20
2. 2023-02-22 08:11

## 一、Introduction
> **Object–relational mapping** (**ORM**, **O/RM**, and **O/R mapping tool**) in computer science is a programming technique for converting data between a relational database and the heap of an object-oriented programming language. This creates, in effect, a virtual object database that can be used from within the programming language.


## 二、Popular ORM
1.  **TypeORM** [https://github.com/typeorm/typeorm](https://github.com/typeorm/typeorm) 
2.  **Prisma** [https://github.com/prisma/prisma](https://github.com/prisma/prisma) 
3.  Sequelize [https://github.com/sequelize/sequelize](https://github.com/sequelize/sequelize) 
4.  Objection.js [https://github.com/Vincit/objection.js](https://github.com/Vincit/objection.js) 
5.  bookshelf.js [https://github.com/bookshelf/bookshelf](https://github.com/bookshelf/bookshelf) 
6.  **Drizzle** ORM https://github.com/drizzle-team/drizzle-orm 
7. @moccacoders/node-obremap
8. node-querybuilder
9. fxsql
10. Mikro-ORM https://github.com/mikro-orm/mikro-orm

### 2.1、TypeORM
[https://github.com/typeorm/typeorm](https://github.com/typeorm/typeorm) 

TypeORM is an [ORM](https://en.wikipedia.org/wiki/Object-relational_mapping) that can run in NodeJS, Browser, Cordova, PhoneGap, Ionic, React Native, NativeScript, Expo, and Electron platforms and can be used with TypeScript and JavaScript (ES5, ES6, ES7, ES8). Its goal is to always support the latest JavaScript features and provide additional features that help you to develop any kind of application that uses databases - from small applications with a few tables to large scale enterprise applications with multiple databases.

TypeORM supports both [Active Record](https://github.com/typeorm/typeorm/blob/master/docs/active-record-data-mapper.md#what-is-the-active-record-pattern) and [Data Mapper](https://github.com/typeorm/typeorm/blob/master/docs/active-record-data-mapper.md#what-is-the-data-mapper-pattern) patterns, unlike all other JavaScript ORMs currently in existence, which means you can write high quality, loosely coupled, scalable, maintainable applications the most productive way.

TypeORM is highly influenced by other ORMs, such as [Hibernate](http://hibernate.org/orm/), [Doctrine](http://www.doctrine-project.org/) and [Entity Framework](https://www.asp.net/entity-framework).

```sh
npm install typeorm --save
npm install reflect-metadata --save
npm install @types/node --save-dev
npm install mysql --save # pg, sqlite3, mssql, sql.js oracledb, @sap/hana-client, hdb-pool, @google-cloud/spanner, mongodb
```

```js
// import at app.ts
import "reflect-metadata"
```

##### TypeScript configuration

Also, make sure you are using TypeScript version **4.5** or higher, and you have enabled the following settings in `tsconfig.json`:

```js
import { Entity, PrimaryGeneratedColumn, Column } from "typeorm"

@Entity()
export class User {
    @PrimaryGeneratedColumn()
    id: number

    @Column()
    firstName: string

    @Column()
    lastName: string

    @Column()
    age: number
}
```

```js
const userRepository = MyDataSource.getRepository(User)

const user = new User()
user.firstName = "Timber"
user.lastName = "Saw"
user.age = 25
await userRepository.save(user)

const allUsers = await userRepository.find()
const firstUser = await userRepository.findOneBy({
    id: 1,
}) // find by id
const timber = await userRepository.findOneBy({
    firstName: "Timber",
    lastName: "Saw",
}) // find by firstName and lastName

await userRepository.remove(timber)
```


### 2.2、Sequelize
Sequelize is a modern TypeScript and Node.js ORM for Postgres, MySQL, MariaDB, SQLite and SQL Server, and more. Featuring solid transaction support, relations, eager and lazy loading, read replication and more.

[https://sequelize.org/](https://sequelize.org/)

### 2.3、Prisma
Prisma unlocks a new level of **developer experience** when working with databases thanks to its intuitive data model, automated migrations, type-safety & auto-completion.

### 2.4、Drizzle ORM
Drizzle ORM 是用于 SQL 数据库的 TypeScript ORM，在设计时考虑到了最大的类型安全性。 它带有用于自动生成 SQL 迁移的 drizzle-kit CLI 伴侣。 Drizzle ORM 是一个库，而不是一个框架。 它始终作为任何级别的选择加入解决方案。

ORM 的主要哲学是“如果你知道 SQL，你就知道 Drizzle ORM”。 我们==尽可能遵循类似 SQL 的语法==，==强类型化并在编译时失败==，而不是在运行时。




## 三、TypeORM vs Prisma

While Prisma and TypeORM solve similar problems, they work in very different ways.

**TypeORM** is a traditional ORM which maps _tables_ to _model classes_. These model classes can be used to generate SQL migrations. Instances of the model classes then provide an interface for CRUD queries to an application at runtime.

**Prisma** is a new kind of ORM that mitigates many problems of traditional ORMs, such as bloated model instances, mixing business with storage logic, lack of type-safety or unpredictable queries caused e.g. by lazy loading.

It uses the [Prisma schema](https://www.prisma.io/docs/concepts/components/prisma-schema) to define application models in a declarative way. Prisma Migrate then allows to generate SQL migrations from the Prisma schema and executes them against the database. CRUD queries are provided by Prisma Client, a lightweight and entirely type-safe database client for Node.js and TypeScript.



## Reference
1. [Top 6 ORMs for Modern Node.js App Development](https://amplication.com/blog/top-6-orms-for-modern-nodejs-app-development)
