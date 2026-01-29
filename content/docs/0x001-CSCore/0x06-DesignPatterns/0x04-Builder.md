
Review
1. 2024-09-16 16:44

> [!Summary]
> 适用于逐步构建一个复杂对象

## 一、Introduction
**构造器**模式分“步骤”创建对象。通常我们通过不同的函数和方法向对象添加属性和方法。

Builder 模式是一种创建型设计模式，它将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示。换句话说，就是将一个复杂对象的构建过程封装起来，使得客户端不需要知道其内部的具体构造细节。

为什么使用 Builder 模式？
- **复杂对象构建:** 当一个对象有很多属性，并且这些属性之间存在复杂的依赖关系时，使用构造函数来创建对象会变得非常繁琐。
- **逐步构建:** Builder 模式允许你逐步构建一个复杂对象，而不是一次性提供所有的参数。
- **表示分离:** 将对象的构建过程与表示分离，使得你可以创建不同表示的相同类型对象。

```ts
interface Product {
  part1: string;
  part2: number;
  // ... 其他部件
}

interface Builder {
  buildPart1(part1: string): void;
  buildPart2(part2: number): void;
  // ... 其他构建方法
  getProduct(): Product;
}

class ConcreteBuilder implements Builder {
  private product: Product = { part1: '', part2: 0 };

  buildPart1(part1: string): void {
    this.product.part1 = part1;
  }

  buildPart2(part2: number): void {
    this.product.part2 = part2;
  }

  getProduct(): Product {
    return this.product;
  }
}

class Director {
  constructor(private builder: Builder) {}

  construct(): Product {
    this.builder.buildPart1('part1');
    this.builder.buildPart2(2);
    // ... 其他构建步骤
    return this.builder.getProduct();
  }
}

// 使用示例
const builder = new ConcreteBuilder();
const director = new Director(builder);
const product = director.construct();
console.log(product);
```

## Reference

