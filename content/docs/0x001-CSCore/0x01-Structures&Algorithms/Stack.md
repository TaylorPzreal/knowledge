
Review
1. 2024-09-11 07:02

> [!Summary]
> 

## 一、Introduction


##### 最小栈
```ts
class MinStack {
  private stack: number[];
  private sortStack: number[];

  constructor() {
    this.stack = [];
    this.sortStack = [Infinity];
  }

  push(x: number): void {
    this.stack.push(x);
    this.sortStack.push(Math.min(x, this.getMin()));
  }

  // 删除堆栈顶部的元素
  pop(): void {
    this.stack.pop();
    this.sortStack.pop();
  }

  // 获取堆栈顶部的元素
  top(): number {
    return this.stack[this.stack.length - 1];
  }

  // 获取堆栈中的最小元素。
  getMin(): number {
    return this.sortStack[this.sortStack.length - 1];
  }
}

```


### LeetCode 习题
1. [x] 20. 有效的括号 ✅ 2024-10-07
2. [x] 155. 最小栈 ✅ 2024-10-07
3. [x] 394. 字符串解码 #Medium ✅ 2024-10-08
4. [x] 739. 每日温度 ✅ 2024-10-08





## Reference

