
Review
1. 2024-09-17 07:48

> [!Summary]
> **Benefits of the Facade Pattern**
> 
> - **Simplified Interface:** The facade provides a simpler interface to the subsystem, making it easier to use.
> - **Reduced Coupling:** The facade decouples the client code from the subsystem, making it easier to maintain and extend.
> - **Improved Reusability:** The facade can be reused in different parts of the application.
> - **Encapsulation:** The facade hides the complexity of the subsystem from the client code.

## 一、Introduction
Facade （外观）模式是一种结构型设计模式，它提供了一个简化接口，用于访问一个或多个复杂子系统。Facade 模式通过隐藏系统的复杂性，提供了一个更简单和一致的接口，使客户端更容易使用。Facade 模式的目标是简化接口，隐藏复杂性，并提供一个更方便的入口点。这有助于降低系统之间的耦合度，并提高代码的可维护性。

The facade pattern is a structural design pattern that provides a simplified interface to a complex subsystem. It hides the complexities of the subsystem and presents a unified interface to clients. This can make it easier to use the subsystem and reduce coupling between the subsystem and its clients.


```ts
interface Subsystem {
  operation1(): void;
  operation2(): void;
}

class Subsystem1 implements Subsystem {
  operation1(): void {
    console.log("Subsystem1: Operation1");
  }

  operation2(): void {
    console.log("Subsystem1: Operation2");
  }
}

class Subsystem2 implements Subsystem {
  operation1(): void {
    console.log("Subsystem2: Operation1");
  }

  operation2(): void {
    console.log("Subsystem2: Operation2");
  }
}

class Facade {
  private subsystem1: Subsystem;
  private subsystem2: Subsystem;

  constructor() {
    this.subsystem1 = new Subsystem1();
    this.subsystem2 = new Subsystem2();
  }

  operationA(): void {
    console.log("Facade: OperationA");
    this.subsystem1.operation1();
    this.subsystem2.operation1();
  }

  operationB(): void {
    console.log("Facade: OperationB");
    this.subsystem2.operation2();
    this.subsystem1.operation2();
  }
}

// Client code
const facade = new Facade();
facade.operationA();
facade.operationB();
```


## Reference

