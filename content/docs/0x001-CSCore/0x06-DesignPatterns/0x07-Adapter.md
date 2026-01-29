
#Structural 

Review
1. 2024-09-16 19:26

> [!Summary]
> 

## 一、Introduction
The Adapter Pattern is a structural design pattern that allows incompatible interfaces to work together. It provides a bridge between two incompatible classes by wrapping one class in another, making it compatible with the client class.

适配器模式是一种结构型设计模式，用于使原本不兼容的接口能够一起工作。它通常涉及到一个客户端使用一个期望的特定接口，而另一个类或组件提供了一个不同的接口。适配器模式通过创建一个中间层（适配器），将一个类的接口转换成客户端期望的另一个接口。

**特点：**
- 接口转换：适配器模式提供了将一个类的接口转换成另一种接口的方式。
- 兼容性：解决了接口不兼容的问题，使得原本不能一起工作的类可以协同工作。

**应用场景：**
- **不同系统的集成：** 当需要将两个使用不同接口的系统集成时，可以使用适配器模式。
- **第三方库的集成：** 当使用一个第三方库，但其接口与现有系统不兼容时，可以通过适配器模式进行集成。
- **硬件设备控制：** 在硬件设备控制领域，不同的设备可能有不同的控制接口，适配器模式可以用来统一这些接口。
- **新旧系统迁移：** 在新旧系统迁移过程中，旧系统中的组件可能需要适配新系统的接口。
- **模块化设计：** 在模块化设计中，适配器模式可以用来连接不同模块，即使它们的接口不兼容。

**Structure of the Adapter Pattern**
1. **Target:** Defines the specific interface the client expects.
2. **Adaptee:** Defines the existing interface that needs to be adapted.
3. **Adapter:** Implements the Target interface and adapts the Adaptee interface to the Target interface.

```ts
interface Duck {
  quack(): void;
  fly(): void;
}

class MallardDuck implements Duck {
  quack() {
    console.log("Quack");
  }

  fly() {
    console.log("Flying high");
  }
}

interface Turkey {
  gobble(): void;
  fly(): void;
}

class WildTurkey implements Turkey {
  gobble() {
    console.log("Gobble gobble");
  }

  fly() {
    console.log("I can fly a short distance");
  }
}

class TurkeyAdapter implements Duck {
  private turkey: Turkey;

  constructor(turkey: Turkey) {
    this.turkey = turkey;
  }

  quack() {
    this.turkey.gobble();
  }

  fly() {
    for (let i = 0; i < 5; i++) {
      this.turkey.fly();
    }
  }
}

// Usage
const mallardDuck = new MallardDuck();
mallardDuck.quack();
mallardDuck.fly();

const wildTurkey = new WildTurkey();
const turkeyAdapter = new TurkeyAdapter(wildTurkey);
turkeyAdapter.quack();
turkeyAdapter.fly();
```


## Reference

