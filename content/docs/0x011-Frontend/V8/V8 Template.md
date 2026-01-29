
Review
1. 2024-10-04 10:20

> [!Summary]
> 

## 一、Introduction
**V8 模板** 是 V8 JavaScript 引擎中一个重要的概念，它为 JavaScript 函数和对象提供了一种蓝图。简单来说，模板定义了 JavaScript 对象的结构和行为，以及函数的执行方式。

### V8 模板的两种类型
1. FunctionTemplate
2. ObjectTemplate

**FunctionTemplate：**
- **作用：** 定义函数的结构，包括函数的参数、返回值类型、以及函数体内的逻辑。
- **用途：**
    - 将 C++ 函数包装成 JavaScript 函数，让 JavaScript 代码可以调用 C++ 编写的原生函数。
    - 在 C++ 中创建 JavaScript 函数。


**ObjectTemplate：**
- **作用：** 定义对象的结构，包括对象的属性、方法、以及原型。
- **用途：**
    - 创建 JavaScript 对象的实例。
    - 为对象添加自定义属性和方法。

###### V8 模板的用途
- **扩展 JavaScript：** 通过创建自定义的 FunctionTemplate 和 ObjectTemplate，可以为 JavaScript 添加新的功能和对象。
- **实现 JavaScript 和 C++ 的互操作：** V8 模板可以将 C++ 函数和对象暴露给 JavaScript，同时也可以从 JavaScript 调用 C++ 代码。
- **提高性能：** 通过使用 V8 模板，可以优化 JavaScript 代码的执行效率。

###### V8 模板的工作原理
V8 引擎在执行 JavaScript 代码时，会根据模板来创建相应的 JavaScript 对象和函数。模板中定义的属性和方法会被映射到 JavaScript 对象上，从而实现自定义的 JavaScript 对象。



## Reference

