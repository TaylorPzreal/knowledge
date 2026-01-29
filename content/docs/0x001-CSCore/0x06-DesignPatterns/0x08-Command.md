#Behavioral 

Review
1. 2024-09-16 19:42

> [!Summary]
> 

## 一、Introduction
命令模式是一种行为设计模式，它将一个请求或操作封装为一个对象。这种模式可以解耦请求的发送者和接收者，让它们不直接交互，而是通过命令对象来间接进行通信。

The Command Pattern is a behavioral design pattern that encapsulates a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.

**When to Use the Command Pattern**
- When you want to parameterize objects with different requests.
- When you need to queue or log requests.
- When you need to support undoable operations.
- When you want to decouple the object that invokes the operation from the one that knows how to perform it.

**Structure of the Command Pattern**
1. **Command:** Defines the interface for executing an operation.
2. **ConcreteCommand:** Implements the Command interface and specifies the operation to be executed.
3. **Receiver:** Knows how to perform the operations.
4. **Invoker:** Invokes the command object.


```ts
interface Command {
  execute(): void;
}

class Light {
  on() {
    console.log("Light turned on");
  }

  off() {
    console.log("Light turned off");
  }
}

class LightOnCommand implements Command {
  private light: Light;

  constructor(light: Light) {
    this.light = light;
  }

  execute() {
    this.light.on();
  }
}

class LightOffCommand implements Command {
  private light: Light;

  constructor(light: Light) {
    this.light = light;
  }

  execute() {
    this.light.off();
  }
}

class RemoteControl {
  private slots: Command[];

  constructor() {
    this.slots = [];
  }

  setCommand(slot: number, command: Command) {
    this.slots[slot] = command;
  }

  buttonPressed(slot: number) {
    this.slots[slot].execute();
  }
}

// Usage
const remoteControl = new RemoteControl();
const livingRoomLight = new Light();

const lightOnCommand = new LightOnCommand(livingRoomLight);
const lightOffCommand = new LightOffCommand(livingRoomLight);

remoteControl.setCommand(0, lightOnCommand);
remoteControl.setCommand(1, lightOffCommand);

remoteControl.buttonPressed(0);
remoteControl.buttonPressed(1);
```


## Reference

