
**Review**
1.  2020/04/06
2.  2023/02/18

## 一、简介
一种用于 API 的==查询语言，是一个规范==

GraphQL 既是一种==用于 API 的查询语言也是一个满足你数据查询的运行时==。 GraphQL 对你的 API 中的数据提供了一套易于理解的完整描述，使得客户端能够准确地获得它需要的数据，而且没有任何冗余，也让 API 更容易地随着时间推移而演进，还能用于构建强大的开发者工具。

### API服务对比：GraphQL vs RESTful
**RESTful**
1.  简单易懂
2.  快速搭建
3.  在数据聚合方面有很大的劣势

**GraphQL**
1.  专注数据聚合，需要什么就返回什么


### 框架
**Server**
- [apollo-server](https://github.com/apollographql/apollo-server)  ⭐️⭐️⭐️
- [GraphQL.js](https://github.com/graphql/graphql-js)  ⭐️⭐️⭐️⭐️⭐️
- [express-graphql](https://github.com/graphql/express-graphql) 
- [koa-graphql](https://www.npmjs.com/package/koa-graphql) 
- [graphql-helix](https://github.com/contra/graphql-helix) 
- [graphql-yoga](https://github.com/dotansimha/graphql-yoga) ⭐️⭐️⭐️⭐️⭐️

**Client**
- [apollo-client](https://github.com/apollographql/apollo-client)
- apollo-server-express
- [Relay](https://github.com/facebook/relay)
- [graphql-request](https://github.com/prisma-labs/graphql-request)
- [amplify-js](https://github.com/aws-amplify/amplify-js)
- [lokka](https://github.com/kadirahq/lokka)
- [nanogql](https://github.com/choojs/nanographql)
- [gq-loader](https://github.com/Houfeng/gq-loader)
- [grafoo](https://github.com/grafoojs/grafoo)
- [urql](https://github.com/FormidableLabs/urql)
- [graphql-hooks](https://github.com/nearform/graphql-hooks)
- [graphqurl](https://github.com/hasura/graphqurl)


### 最佳实践
1.  GraphQL 通常通过单入口来提供 HTTP 服务的完整功能
2.  压缩：Accept-Encoding: gzip
3.  无版本控制
4.  分页
5.  缓存


## **Reference**
1. [https://graphql.cn/](https://graphql.cn/)
2. [https://graphql.org/](https://graphql.org/)
3. [https://www.graphql.com/](https://www.graphql.com/)
4. [Getting Started with GraphQL.js](https://graphql.org/graphql-js/)
