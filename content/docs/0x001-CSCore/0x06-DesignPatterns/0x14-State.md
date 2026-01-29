
Review
1. 2024-09-17 16:43

> [!Summary]
> 

## 一、Introduction
The **state pattern** is a behavioral design pattern that allows an object to *alter its behavior when its internal state changes*. This pattern is useful when you have an object that can exist in multiple states, and the behavior of the object should change depending on its current state.

```ts
interface State {
  handle(context: Context): void;
}

class ConcreteStateA implements State {
  handle(context: Context): void {
    console.log("State A");
    context.setState(new ConcreteStateB());
  }
}

class ConcreteStateB implements State {
  handle(context: Context): void {
    console.log("State B");
    context.setState(new ConcreteStateA());
  }
}

class Context {
  private state: State;

  constructor(state: State) {
    this.state = state;
  }

  request(): void {
    this.state.handle(this);
  }

  setState(state: State): void {
    this.state = state;
  }
}

// Client code
const context = new Context(new ConcreteStateA());
context.request();
context.request();
context.request();
```

## Reference

