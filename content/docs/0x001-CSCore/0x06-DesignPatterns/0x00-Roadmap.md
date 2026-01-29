
#设计模式 #DesignPattern

Review
1. 2019/03/04
2. 2023-08-05 22:24
3. 2023/12/09

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

## 二、设计模式的6大设计原则
1、单一职责原则
2、里氏替换原则:所有引用基类的地方必须能够透明的使用其子类的对象;
3、依赖倒置原则:面向接口编程
4、接口隔离原则:客户端不应该依赖它不需要的接口;接口尽可能小
5、迪米特原则:一个对象应该对其他对象有较少的了解,即类间解耦
6、开闭原则:一个软件实体如类,模块,函数,应该对扩展开放,对修改关闭。

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


### 3.1 创建型
创建型模式是用来**创建对象**的模式，抽象了实例化的过程，帮助一个系统独立于其他关联对象的创建、组合和表示方式。

1. 工厂模式（**Factory Method Pattern**）Defines an interface for creating an object but lets subclasses alter the type of objects that will be created.
2. 抽象工厂模式（**Abstract Factory Pattern**）Provides an interface for creating families of related or dependent objects without specifying their concrete classes.
3. 建造者模式（**Builder Pattern**）Separates the construction of a complex object from its representation, allowing the same construction process to create different representations.
4. 原型模式（**Prototype Pattern**）Creates new objects by copying an existing object, known as the prototype.
5. 单例模式（Singleton Pattern）Ensures that a class has only one instance and provides a global point of access to that instance.
6. **Object Pool Pattern** Manages a pool of reusable objects to minimize the overhead of object creation and destruction.

### 3.2 结构型
结构型模式讨论的是类和对象的结构,它采用继承机制来组合接口或实现(类结构型模式),或通过组合一些对象实现新的功能(对象结构型模式)。这些结构型模式在某些方面具有很大的相似性,但侧重点各有不同。

1. 代理模式(**Proxy Pattern**)
2. 装饰模式（**Decorator Pattern**）
3. 适配器模式（**Adapter Pattern**）
4. 组合模式（**Composite Pattern**）
5. 桥梁模式（**Bridge Pattern**）
6. 外观模式
7. 享元模式

### 3.3 行为型
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
