
Review
1. 2024-09-17 08:06

> [!Summary]
> 

## 一、Introduction
中介者模式（Mediator Pattern）是一种行为型设计模式，它定义了一个对象，该对象封装了一组对象之间的交互方式。中介者使对象之间不直接相互通信，而是通过中介者对象进行通信，从而降低了对象之间的耦合度。中介者模式适用于需要将多个对象解耦并通过一个中心点进行通信的场景。这可以减少对象之间的直接关联，提高系统的可维护性。

The **mediator pattern** (中介者模式) is a behavioral design pattern that promotes loose coupling between objects by defining an object that encapsulates how a set of objects interact. This mediator can simplify communication between objects, making the system more flexible and easier to maintain.

```ts
interface ChatRoom {
  register(user: User): void;
  sendMessage(sender: User, message: string): void;
}

class ConcreteChatRoom implements ChatRoom {
  private users: User[] = [];

  register(user: User): void {
    this.users.push(user);
  }

  sendMessage(sender: User, message: string): void {
    for (const user of this.users) {
      if (user !== sender) {
        user.receiveMessage(sender, message);
      }
    }
  }
}

class User {
  private chatRoom: ChatRoom;
  private name: string;

  constructor(chatRoom: ChatRoom, name: string) {
    this.chatRoom = chatRoom;
    this.name = name;
    this.chatRoom.register(this);
  }

  sendMessage(message: string): void {
    this.chatRoom.sendMessage(this, message);
  }

  receiveMessage(sender: User, message: string): void {
    console.log(`${sender.name}: ${message}`);
  }
}

// Client code
const chatRoom = new ConcreteChatRoom();
const user1 = new User(chatRoom, "User 1");
const user2 = new User(chatRoom, "User 2");

user1.sendMessage("Hello, User 2!");
user2.sendMessage("Hi, User 1!");
```


## Reference

