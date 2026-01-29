
Review
1. 2021/02/08
2. 2024-09-08 09:59

> [!Summary]
> 

## 一、Introduction
MVC 通过分离 Model、View 和 Controller 的方式来组织代码结构。

其中 View 负责页面的显示逻辑，

Model 负责存储页面的业务数据，以及对相应数据的操作。

并且 View 和 Model 应用了观察者模式，当 Model 层发生改变的时候它会通知有关 View 层更新页面。

Controller 层是 View 层和 Model 层的纽带，它主要负责用户与应用的响应操作，当用户与页面产生交互的时候，Controller 中的事件触发器就开始工作了，通过调用 Model 层，来完成对 Model 的修改，然后 Model 层再去通知 View 层更新。


## Reference

