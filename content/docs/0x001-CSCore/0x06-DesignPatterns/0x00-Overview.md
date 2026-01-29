
#设计模式 #DesignPattern

Review
1. 2019/03/04
2. 2023-08-05 22:24
3. 2023/12/09
4. 2024-09-16
5. 2026-01-09


> [!Summary]
> 设计模式是在软件设计中反复出现的问题的解决方案。它们是经过验证的、可重用的代码设计经验，能够解决特定类型的问题。这些模式帮助开发者更有效地组织和设计代码，**提高可维护性、可扩展性，降低代码耦合**。
> 
> **直观极简设计模式介绍**
> <https://refactoring.guru/design-patterns/typescript>
> 目前全球范围内做得最好的设计模式学习网站，每一个模式都配有非常形象的**插图**、通俗易懂的**比喻**（生活实例）、类图以及详细的实现步骤。
> 
> <https://www.patterns.dev/>
> 由 Chrome 团队成员和知名开发者维护，专注于现代 Web 开发。除了设计模式，还有很多框架的设计模式。
> 
> Books
> 《设计模式之蝉》
> 《JavaScript设计模式》
> 《设计模式：可复用面向对象软件的基础》

## 一、Introduction
设计模式无外乎对面对对象编程的三大特性:
封装，继承，多态的应用；以此达到保证程序扩展性和低耦合的目的。

设计模式是写出高质量代码的“方法“，是需要程序员必须熟练掌握的技能之一。

**为什么要用设计模式？**
设计模式是前人总结的经验
- 设计模式可以提高代码的可重用性
- 设计模式可以增强系统的可维护性
- 设计模式可以增强代码的可扩展性
- 设计模式可以提高系统的可阅读性。

## 二、设计模式的设计原则
***SOLID***
1. **单一职责原则**(Single Responsibility Principle)：一个程序只做好一件事
2. **开闭原则**(OpenClosed)：一个软件实体如类、模块、函数，应该**对扩展开放，对修改关闭**
3. **里氏替换原则**(Liskov Substitution)：所有引用基类的地方必须能够透明的使用其子类的对象，子类能覆盖父类，父类能出现的地方子类就能出现
4. **接口隔离原则**(Interface Segregation)：客户端不应该依赖它不需要的接口；接口尽可能小，保持接口的单一独立；
5. **依赖倒置原则**(Dependency Inversion)：面向接口编程，依赖于抽象而不依赖于具体，使用方只关注接口而不关注具体类的实现。高层模块不应该依赖低层模块，两者都应该依赖于抽象。抽象不应该依赖于细节，细节应该依赖于抽象。

其他原则
1. **迪米特原则**：一个对象应该对其他对象有较少的了解，即类间解耦
2. **不要自我重复**（Don't repeat yourself）
3. **组合优先继承**（Composite over inheritance）：通过组合集成的两个组件是松耦合关系，通过props来约束。但是有继承关系的两个组件是强耦合关系，对父组件的修改可能会导致子组件的未预期的结果。

迪米特法则又称 "最少知道原则" ， 它的定义是 "只与你的朋友交谈，不与陌生人说话"， 这句话的含义是如果两个软件实体或服务之间无需直接通信，那么就不应当发生直接的相互调用，可以通过第三方实体或服务进行转发通信。 其目的是为了降低系统的耦合度。


## 三、设计模式分类
1. 发布订阅模式
2. 观察者模式
3. 单例模式
4. 工厂模式
5. 装饰模式
6. 策略模式
7. 代理模式

经常提及的设计有23种，这23中设计模式按照其特点可依此分为**创建型**，**结构型**，**行为型**

Design patterns can be categorized into three main groups:
1. **Creational Patterns:** These patterns focus on object creation mechanisms, trying to create objects in a manner suitable for the situation. They abstract the instantiation process, making it more flexible and independent of the system.
2. **Structural Patterns:** Structural patterns deal with object composition, forming relationships between objects to create larger, more complex structures. They help to define how objects and classes can be combined to form new structures and provide new functionality.
3. **Behavioral Patterns:** Behavioral patterns are concerned with communication between objects, defining how they interact and distribute responsibilities. These patterns help you design systems where objects collaborate in a more flexible and efficient manner.


### 3.1 创建型 (Creational Patterns)
创建型模式是用来**创建对象**的模式，抽象了实例化的过程，帮助一个系统独立于其他关联对象的创建、组合和表示方式。

1. 工厂模式（**Factory Method Pattern**）Defines an interface for creating an object but lets subclasses alter the type of objects that will be created.
2. 抽象工厂模式（**Abstract Factory Pattern**）Provides an interface for creating families of related or dependent objects without specifying their concrete classes.
3. 建造者模式（**Builder Pattern**）Separates the construction of a complex object from its representation, allowing the same construction process to create different representations.
4. 原型模式（**Prototype Pattern**）Creates new objects by copying an existing object, known as the prototype.
5. 单例模式（Singleton Pattern）Ensures that a class has only one instance and provides a global point of access to that instance.
6. **Object Pool Pattern** Manages a pool of reusable objects to minimize the overhead of object creation and destruction.

### 3.2 结构型 (Structural Patterns)
结构型模式讨论的是类和对象的结构,它采用继承机制来组合接口或实现(类结构型模式),或通过组合一些对象实现新的功能(对象结构型模式)。这些结构型模式在某些方面具有很大的相似性,但侧重点各有不同。

1. 代理模式(**Proxy Pattern**)
2. 装饰模式（**Decorator Pattern**）
3. 适配器模式（**Adapter Pattern**）
4. 组合模式（**Composite Pattern**）
5. 桥梁模式（**Bridge Pattern**）
6. 外观模式
7. 享元模式

### 3.3 行为型 (Architectural/Behavioral Patterns)
行为型设计模式关注的是对象的行为即对象的方法,用来解决对象之间的依赖和联系问题。

1. 模板方法模式
2. 命令模式（**Command Pattern**）
3. 责任链模式（**Chain of Responsibility Pattern**）
4. 策略模式（**Strategy Pattern**）
5. 迭代器模式
6. 中介者模式
7. 观察者模式（**Observer Pattern**）
8. 备忘录模式
9. 访问者模式（**Visitor Pattern**）
10. 状态模式（**State Pattern**）
11. 解释器模式

## Reference
1. [OOP Design Patterns in Javascript](https://dev.to/alexmercedcoder/oop-design-patterns-in-javascript-3i98)
2. [如何理解这6种常见设计模式？](https://yqh.aliyun.com/detail/20033)
3. [JS Design Patterns: A Comprehensive Guide](https://dev.to/topefasasi/js-design-patterns-a-comprehensive-guide-h3m)
4. [JavaScript Design Patterns](https://www.digitalocean.com/community/tutorial-series/javascript-design-patterns)
5. [掘金-JavaScript 23 种设计模式ES6](https://juejin.cn/post/6844904032826294286)
6. [WX-架构与设计模式的六大原则](https://mp.weixin.qq.com/s/vpVjLN3ZVj0jUhOuRsQHwQ)
