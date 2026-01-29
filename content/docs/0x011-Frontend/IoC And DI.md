
Review
1. 2023-08-08 07:03

> 概念知识：控制反转、依赖注入、依赖倒置
> 技术知识：装饰器 Decorator、反射 Reflect
> `TSyringe` 的定义：Token、Provider <https://github.com/microsoft/tsyringe#injection-token>

## 一、Introduction
### 控制反转(IoC)

**控制反转**（Inversion of Control，缩写为 **IoC**）是一种设计原则，通过反转程序逻辑来降低代码之间的耦合性。

**控制反转容器**（IoC 容器）是某一种具体的工具或者框架，用来执行从内部程序反转出来的代码逻辑，从而提高代码的复用性和可读性。我们常常用到的 DI 工具，就扮演了 IoC 容器的角色，连接着所有的对象和其依赖。

### 依赖注入(DI)

依赖注入是**控制反转**的一种**具体的实现**，通过放弃程序内部对象声明创建的控制，由外部去创建并注入依赖的对象。

依赖注入的方法主要是以下四种：

1. 基于接口。实现特定接口以供外部容器注入所依赖类型的对象。
2. 基于 set 方法。实现特定属性的 public set 方法，来让外部容器调用传入所依赖类型的对象。
3. 基于构造函数。实现特定参数的构造函数，在新建对象时传入所依赖类型的对象。
4. 基于注解，在私有变量前加类似 “@Inject” 的注解，让工具或者框架能够分析依赖，自动注入依赖。

通常前端实现的是3、4方法。


#### 使用 DI 工具的不足：

- 无法控制的生命周期，因为对象的实例化在 IoC 里面，所以对象什么时候创建出来并不完全由当前程序说了算。所以这要求我们在使用工具或者框架之前，需要非常了解其中的原理，最好是读过里面的源码。
- 当依赖出错的时候，比较难定位到是哪个在出错。因为依赖是注入进来的，所以当依赖出错的时候只能通过经验去分析，或者现场 debug 住，一点点进行深入调试，才能知道是哪个地方的内容出错了。这对 Debug 能力，或者项目的整体把控能力要求很高。
- 代码无法连贯阅读。如果是依赖实现，你从入口一直往下，就能看到整个代码执行树；而如果是依赖抽象，具体的实现和实现之间的连接关系是分开的，通常需要文档才能够看到项目全貌。

#### 流行的DI工具
- [`InversifyJS`](https://github.com/inversify/InversifyJS): 能力强大的，依赖注入的工具，比较严格的依赖抽象的执行方式；虽然严格的申明很好，但是写起来很重复和啰嗦。
- [`TSyringe`](https://github.com/microsoft/tsyringe): 简单易用，继承自 angular 的抽象定义，比较值得学习。

### 依赖倒置

软件设计模式六大原则之一，依赖倒置原则，英文缩写 **DIP**，全称 Dependence Inversion Principle。

高层模块不应该依赖低层模块，两者都应该依赖其抽象；抽象不应该依赖细节，细节应该依赖抽象。


## Reference
1. [终于搞懂 IoC 和 DI](https://mp.weixin.qq.com/s/f1RlijQCYBVi3_ZPSQFOVw)
2. [Inversion of Control Containers and the Dependency Injection pattern](https://martinfowler.com/articles/injection.html)
3. [Github DI topics](https://github.com/topics/dependency-injection?l=typescript)
