
Review
1. 2021/03/09
2. 2023/02/05
2. 2023-03-18 18:31

## 一、Introduction
动态类型的自由性经常导致错误，这不仅降低了开发人员的效率，而且由于添加新代码行的开销增加而使开发变得很费劲。

因此，由于缺乏类型和编译时错误检查，JavaScript 对于组织和大型代码库中的服务器端代码来说是一个糟糕的选择。

**TypeScript** 由 Microsoft 开发和维护（2012年10月发布），是一种**面向对象**的开源编程语言。它是 JavaScript 的超集，包含可选类型。此外，它还可以编译为纯 JavaScript。

TypeScript主要应用场景是开发==大型复杂应用程序==。

**其他相似语言**
- CoffeeScript
- PureScript


## 二、TypeScript 特性
### Language Features（语言特性）
-   命名空间
-   接口
-   空检查
-   泛型
-   访问修饰符


### 优势
- 支持面向对象的编程概念
- TypeScript 是一种同时支持 **动态类型** 和 **静态类型** 的编程语言。它提供类、可见性范围、命名空间、继承、联合、接口和许多其他特性。此外，还提供注释、变量、语句、表达式、模块和函数。
- 向后兼容（Compatibility）：TypeScript 支持旧的和新的附加功能，但是它兼容所有版本的 JavaScript，例如 ES7 和 ES12。它可以将 ES7 中的完整代码编译回 ES5，反之亦然。这确保了平稳过渡和语言可移植性。
- 静态类型（Static Typing）：静态类型意味着开发人员必须声明变量类型。静态类型可以帮助开发者及早检测错误、更快地完成代码等。
- 显著改善开发者体验
- 易于维护
- 易于迭代，极大提高生产力
-   可以使用静态类型和注释
-   支持面向对象的特性，例如接口、继承和类
-   支持 ES6 (ECMAScript)，它为处理对象和继承提供了更简单的语法
-   全功能 IDE 支持
-   可以避免隐藏的错误，例如经典的 “未定义” 不是函数
-   易于重构代码而不会显著破坏它
-   在大规模、复杂的系统中定位更容易

### 不足
1.  性能问题：由于 TypeScript 是自实现的，而且这种实现非常复杂，它的类型系统本身可以算是一种迷你编程语言，这导致**类型检查**的速度极其缓慢。**type checking is one of the slowest parts of their workflow**
2.  自身存在的缺陷：比如 allowJs 配置选项、any 类型和 intersection 类型，其类型系统根本无法保证代码的类型安全


## 三、TypeScript VS JavaScript 
简而言之，TypeScript 是一种面向对象的编程语言，而 JavaScript 是一种脚本语言。因此，TypeScript 通过 ES6 特性提供接口和模块；另一方面，JavaScript 不提供此类功能。

**TypeScript**
- 编译时类型检查：使用 Vanilla JavaScript，类型验证在运行时执行。然而，这会增加运行时开销，这可以通过进行编译时验证来避免。
- 大型项目或多个开发人员：TypeScript 可以在大型项目或许多开发人员一起工作时无缝运行。
- 易于使用新库或框架：假设，如果你正在使用 React 进行开发并且不熟悉它的 API，你可以获得 语法提示来帮助你识别和导航新界面。但是，它们都提供类型定义

**JavaScript**  
- 小项目：对于代码较少的小型项目，TypeScript 可能有点矫枉过正。
- 框架支持：如果 TypeScript 不支持您选择的框架 – 例如 EmberJS，那么您可能无法利用它的功能。
- 构建工具：要生成能运行的最终 JavaScript，TypeScript 需要有一个构建的步骤。不过，在不使用任何构建工具的情况下开发 JavaScript 应用正变得越来越少。
- 测试工作流程：如果您优秀的 JavaScript 开发人员已经在使用测试驱动开发，那么切换到 TypeScript 的好处可能不足以证明迁移成本是合理的。

**JavaScript** 不适合大型复杂应用程序。它旨在为一个应用程序只编写几百行代码。
以下是 JavaScript 提供的一些独特功能：
-   灵活、动态和跨平台
-   它可以用于客户端和服务器端
-   轻量化解读
-   所有浏览器都支持
-   弱类型
-   即时编译


## Reference
1. [TypeScript与JavaScript：你应该知道的区别](https://mp.weixin.qq.com/s/X_bOnloQ4zTFixnpQMlHaA)
2. [TypeScript Type Challenges](https://github.com/type-challenges/type-challenges)
