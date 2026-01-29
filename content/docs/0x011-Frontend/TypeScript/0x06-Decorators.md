
Review
1. 2024-07-21 20:30

#Stage3

## 一、Introduction
Decorators are an upcoming ECMAScript feature that allow us to customize classes and their members in a reusable way.

Decorators are a feature of TypeScript that allow you to modify the behavior of a class, property, method, or parameter. They are a way to add additional functionality to existing code, and they can be used for a wide range of tasks, including logging, performance optimization, and validation.

Decorators provide a way to add both annotations and a meta-programming syntax for class declarations and members.

```ts
function log(
  target: Object,
  propertyKey: string | symbol,
  descriptor: PropertyDescriptor
) {
  const originalMethod = descriptor.value;

  descriptor.value = function (...args: any[]) {
    console.log(`Calling ${propertyKey} with arguments: ${args}`);
    return originalMethod.apply(this, args);
  };

  return descriptor;
}

class Calculator {
  @log
  add(a: number, b: number): number {
    return a + b;
  }
}

const calculator = new Calculator();
calculator.add(1, 2);
// Output: Calling add with arguments: 1,2
// Output: 3
```


## Reference
Decorators <https://www.typescriptlang.org/docs/handbook/decorators.html> 
