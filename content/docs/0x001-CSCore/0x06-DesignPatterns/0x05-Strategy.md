
Review
1. 2024-09-16 17:08

> [!Summary]
> 策略模式的应用场景
> - **不同的排序算法：** 快速排序、冒泡排序、插入排序等。
> - **不同的支付方式：** 支付宝支付、微信支付、银行卡支付等。
> - **不同的压缩算法：** `gzip`、`zip`、`bzip2`等。
> - **不同的验证规则：** 邮箱验证、手机号验证、身份证验证等。


## 一、Introduction
**策略模式**是一种行为型设计模式，它定义了一系列算法，并将每个算法封装起来，使它们可以相互替换。策略模式使得算法可以在不影响到客户端的情况下发生变化。

**核心思想：**
- **封装算法：** 将不同的算法封装到不同的类中，每个类代表一种具体的策略。
- **策略接口：** 定义一个统一的接口，所有策略类都实现这个接口。
- **上下文：** 持有一个策略对象的引用，并通过委托的方式调用策略的方法。


为什么要使用策略模式？
- **提高代码可维护性：** 将算法从主逻辑中分离，使得代码更清晰，更容易维护。
- **增强代码灵活性和可扩展性：** 可以动态地切换算法，而无需修改客户端代码。
- **避免使用条件语句：** 通过策略模式，可以避免使用大量的条件语句来选择不同的算法。

```ts
interface Strategy {
  execute(): void;
}

class ConcreteStrategyA implements Strategy {
  execute() {
    console.log('执行算法A');
  }
}

class ConcreteStrategyB implements Strategy {
  execute() {
    console.log('执行算法B');
  }
}

class Context {
  private strategy: Strategy;

  constructor(strategy: Strategy) {
    this.strategy = strategy;
  }

  public request() {
    this.strategy.execute();
  }
}

// 使用示例
const strategyA = new ConcreteStrategyA();
const strategyB = new ConcreteStrategyB();

const context = new Context(strategyA);
context.request();  // 输出：执行算法A

context.strategy = strategyB;
context.request();  // 输出：执行算法B
```


## Reference

