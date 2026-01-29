#Structural 

Review
1. 2024-09-16 19:00

> [!Summary]
> The Decorator Pattern is a structural design pattern that allows you to add new responsibilities to objects dynamically without altering their structure. It provides a flexible way to extend the functionality of objects at runtime.

## 一、Introduction
装饰者模式是一种结构型设计模式，允许用户在不修改对象自身的基础上，通过添加装饰者对象来动态地给对象添加额外的职责或功能。

**特点：**
- 动态扩展：可以在运行时动态地给对象添加职责。
- 透明性：装饰者模式不改变对象的接口，因此对客户端来说是透明的。
- 灵活性：可以多个装饰者组合使用，为对象添加多个职责。

**优点：**
- 增加对象的职责是动态的、可撤销的。
- 可以用多个装饰者包装一个对象，添加多个职责。
- 装饰者和对象可以独立变化，不会相互耦合。

**缺点：**
- 过度使用装饰者模式可能会使系统变得复杂，难以理解。
- 可能会引起多层装饰者调用，影响性能。

**应用场景：**
- **日志记录：** 在不修改原有对象的基础上，添加日志记录功能。
- **安全控制：** 为对象添加访问控制，如权限检查。
- **性能监控：** 为对象的方法添加性能监控功能，以分析性能瓶颈。

```ts
interface Beverage {
  getDescription(): string;
  cost(): number;
}

class Espresso implements Beverage {
  getDescription(): string {
    return 'Espresso';
  }

  cost(): number {
    return 1.99;
  }
}

abstract class CondimentDecorator implements Beverage {
  protected beverage: Beverage;

  constructor(beverage: Beverage) {
    this.beverage = beverage;
  }

  getDescription(): string {
    return this.beverage.getDescription();
  }

  abstract cost(): number;
}

class Mocha extends CondimentDecorator {
  cost(): number {
    return this.beverage.cost() + 0.20;
  }

  getDescription(): string {
    return this.beverage.getDescription() + ', Mocha';
  }
}

class Soy extends CondimentDecorator {
  cost(): number {
    return this.beverage.cost() + 0.15;
  }

  getDescription(): string {
    return this.beverage.getDescription() + ', Soy';
  }
}

// Usage
const espresso = new Espresso();
console.log(espresso.getDescription() + ' $' + espresso.cost());

const mochaEspresso = new Mocha(espresso);
console.log(mochaEspresso.getDescription() + ' $' + mochaEspresso.cost());

const soyMochaEspresso = new Soy(mochaEspresso);
console.log(soyMochaEspresso.getDescription() + ' $' + soyMochaEspresso.cost());
```


ES Decorator
```ts
function Injectable() {
  return function (target: any) {
    target.isInjectable = true;
  };
}

@Injectable()
class MyService {
  // ...
}
```


## Reference
[[装饰器]]

