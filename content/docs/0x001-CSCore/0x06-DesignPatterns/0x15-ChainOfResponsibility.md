
Review
1. 2024-09-17 16:18

> [!Summary]
> 

## 一、Introduction
责任链模式是一种行为设计模式， 允许你将请求沿着处理者链进行发送。收到请求后， 每个处理者均可对请求进行处理， 或将其传递给链上的下个处理者。

The **chain of responsibility pattern** is a behavioral design pattern that allows you to pass a request along a chain of objects until one of them handles it. This pattern is useful when you have multiple objects that can handle a request, and you want to avoid coupling the sender of the request to the receiver.

使用场景：
- 多条件流程判断：权限控制
- ERP 系统流程审批：总经理、人事经理、项目经理
- Java 过滤器的底层实现 Filter

```ts
interface RequestHandler {
  handleRequest(request: Request): void;
}

abstract class AbstractRequestHandler implements RequestHandler {
  private nextHandler: RequestHandler | null = null;

  setNextHandler(handler: RequestHandler): void {
    this.nextHandler = handler;
  }

  handleRequest(request: Request): void {
    if (this.nextHandler !== null) {
      this.nextHandler.handleRequest(request);
    }
  }
}

class ConcreteHandler1 extends AbstractRequestHandler {
  handleRequest(request: Request): void {
    if (request.type === "Type1") {
      console.log("Handled by ConcreteHandler1");
    } else {
      super.handleRequest(request);
    }
  }
}

class ConcreteHandler2 extends AbstractRequestHandler {
  handleRequest(request: Request): void {
    if (request.type === "Type2") {
      console.log("Handled by ConcreteHandler2");
    } else {
      super.handleRequest(request);
    }
  }
}

// Client code
const handler1 = new ConcreteHandler1();
const handler2 = new ConcreteHandler2();

handler1.setNextHandler(handler2);

const request1 = { type: "Type1" };
const request2 = { type: "Type2" };
const request3 = { type: "Type3" };

handler1.handleRequest(request1);
handler1.handleRequest(request2);
handler1.handleRequest(request3);
```


## Reference

