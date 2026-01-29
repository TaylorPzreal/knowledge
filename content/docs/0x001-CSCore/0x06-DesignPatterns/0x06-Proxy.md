#Structural

Review
1. 2024-09-16 17:15

> [!Summary]
> 

## 一、Introduction
代理模式是一种结构型设计模式，它为其他对象提供一种代理以控制对这个对象的访问。代理模式在客户端和目标对象之间起到中介的作用，从而使客户端不能直接访问目标对象，而必须通过代理对象来访问。

**核心思想：**
- **代理对象:** 代表目标对象，并控制对目标对象的访问。
- **目标对象:** 真正执行业务逻辑的对象。
- **客户端:** 通过代理对象来访问目标对象。

为什么要使用代理模式？
- **远程代理:** 为一个位于不同地址的对象提供一个本地代理，从而隐藏一个对象存在于不同地址的事实。
- **虚拟代理:** 创建一个大型对象的代理，从而减少内存的开销。
- **保护代理:** 控制对原始对象的访问，用于保护对象。
- **智能引用:** 当一个对象被使用时，执行一些额外的操作，如计数、日志、访问控制等。

代理模式的结构
- **Subject（抽象主题角色）:** 定义了真实主题和代理对象共有的接口。
- **RealSubject（真实主题角色）:** 真正的业务对象，包含了具体的业务逻辑。
- **Proxy（代理角色）:** 代理对象，持有对真实主题对象的引用，并提供与真实主题相同的接口

```ts
interface Subject {
  request(): void;
}

class RealSubject implements Subject {
  request() {
    console.log('真实对象处理请求');
  }
}

class Proxy implements Subject {
  private realSubject: RealSubject;

  constructor(realSubject: RealSubject) {
    this.realSubject = realSubject;
  }

  request() {
    // 在请求前做一些处理
    console.log('代理预处理');
    this.realSubject.request();
    // 在请求后做一些处理
    console.log('代理后处理');
  }
}

// 使用示例
const realSubject = new RealSubject();
const proxy = new Proxy(realSubject);
proxy.request();
```



## Reference

