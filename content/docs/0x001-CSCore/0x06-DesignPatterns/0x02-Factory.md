
#DesignPattern 

Review
1. 2023-12-09 18:23
2. 2024-09-16

## 一、Introduction
1. 简单工厂（Simple Factory）
2. 工厂方法（Factory Method）
3. 抽象工厂（Abstract Factory）


### 1: Simple Factory
简单工厂模式，又叫静态工厂方法（Static Factory Method），由一个工厂对象决定创建某一种产品对象类的实例。主要用来创建同一类对象。

- **特点:**
    - 结构简单，易于理解。
    - 工厂类集中了创建对象的逻辑，降低了客户端代码的复杂度。
- **缺点:**
    - 工厂类职责过重，违反了单一职责原则。
    - 扩展性较差，每增加一个新产品，都需要修改工厂类。
- **适用场景:**
    - 产品种类较少，且变化不大。
    - 对系统性能要求不高。

```js
const SimpleyFactory = function (type) {
  switch (type) {
    case 'alert':
      return new AlertType();
    case 'confirm':
      return new ConfirmType();
    default:
      return new DefaultType();
  }
};
```

```js
function createBook(name, time) {
  const o = new Object();
  o.name = name;
  o.time = time;
  o.type = 'tech';
  o.getName = function() {
    return this.name;
  }

  return o;
}
```


### 2: Factory Method
工厂模式（Factory Pattern）是一种创建模式，它提供用于创建对象的接口，由子类决定创建的对象的类型。 它封装了对象创建过程，使其更加灵活并与客户端代码解耦。

> 理念是将实际创建对象工作推迟到子类中

- **特点:**
    - 更好地遵循开闭原则，可以方便地增加新的产品。
    - 将创建对象的职责委托给子类，降低了耦合度。
- **缺点:**
    - 相比简单工厂，结构稍复杂。
- **适用场景:**
    - 一个类不知道它需要创建哪种对象。
    - 一个类希望其子类指定创建的对象。
    - 将一个类的实例化延迟到子类。

```js
// Product class
class Product {
  constructor(name) {
    this.name = name;
  }
}

// Factory for creating products
class ProductFactoryA  {
  createProduct(name) {
    return new Product(name);
  }
}

class ProductFactoryB extends Product {
  createProduct(name) {
    return new ProductFactoryB(name);
  }
}

// Usage
const factory = new ProductFactoryA();
const productA = factory.createProduct('Product A');
const productB = factory.createProduct('Product B');

console.log(productA.name); // Output: 'Product A'
console.log(productB.name); // Output: 'Product B'

```


### 3: Abstract Factory Pattern
**抽象工厂**允许在不指定具体类的情况下生成一系列相关的对象。当你想要创建仅共享某些属性和方法的对象时，抽象工厂模式就可以派上用场。

```js
// Abstract Product classes
class Button {
  render() {}
}

class Checkbox {
  render() {}
}

// Concrete Product classes
class MacButton extends Button {
  render() {
    return 'Render Mac button';
  }
}

class MacCheckbox extends Checkbox {
  render() {
    return 'Render Mac checkbox';
  }
}

class WindowsButton extends Button {
  render() {
    return 'Render Windows button';
  }
}

class WindowsCheckbox extends Checkbox {
  render() {
    return 'Render Windows checkbox';
  }
}

// Abstract Factory interface
class GUIFactory {
  createButton() {}
  createCheckbox() {}
}

// Concrete Factories
class MacFactory extends GUIFactory {
  createButton() {
    return new MacButton();
  }

  createCheckbox() {
    return new MacCheckbox();
  }
}

class WindowsFactory extends GUIFactory {
  createButton() {
    return new WindowsButton();
  }

  createCheckbox() {
    return new WindowsCheckbox();
  }
}

// Usage
function createUI(factory) {
  const button = factory.createButton();
  const checkbox = factory.createCheckbox();

  return { button, checkbox };
}

const macUI = createUI(new MacFactory());
console.log(macUI.button.render()); // Output: 'Render Mac button'
console.log(macUI.checkbox.render()); // Output: 'Render Mac checkbox'

const windowsUI = createUI(new WindowsFactory());
console.log(windowsUI.button.render()); // Output: 'Render Windows button'
console.log(windowsUI.checkbox.render()); // Output: 'Render Windows checkbox'
```


### When to Use Which Pattern
- **Use the Factory Pattern** when you want to encapsulate the object creation process and provide a simple interface for creating objects with different implementations.
- **Use the Abstract Factory** Pattern when you need to create families of related or dependent objects that must work together. It helps ensure that the created objects are compatible and cohesive.


## Reference

