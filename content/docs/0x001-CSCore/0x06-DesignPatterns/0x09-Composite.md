#Structural 

Review
1. 2024-09-16 21:57

> [!Summary]
> 

## 一、Introduction
组合模式是一种结构型设计模式，它允许你将对象组合成**树状结构**，以表示“部分-整体”的层次结构。这种模式使得用户可以一致地对待单个对象和对象组合。

The composite pattern is a structural design pattern that allows you to treat groups of objects uniformly as individual objects. This is particularly useful when you have a hierarchical structure of objects and you want to perform the same operation on both individual objects and groups of objects.

```ts
interface Component {
  operation(): void;
}

class Leaf implements Component {
  constructor(public name: string) {}

  operation(): void {
    console.log(`Leaf: ${this.name}`);
  }
}

class Composite implements Component {
  private children: Component[] = [];

  add(component: Component): void {
    this.children.push(component);
  }

  remove(component: Component): void {
    const index = this.children.indexOf(component);
    if (index !== -1) {
      this.children.splice(index, 1);
    }
  }

  getChild(index: number): Component {
    return this.children[index];
  }

  operation(): void {
    console.log("Composite:");
    for (const child of this.children) {
      child.operation();
    }
  }
}

// Create individual leaves
const leaf1 = new Leaf("Leaf 1");
const leaf2 = new Leaf("Leaf 2");

// Create composite components
const composite1 = new Composite();
const composite2 = new Composite();

// Add leaves to composites
composite1.add(leaf1);
composite1.add(leaf2);
composite2.add(composite1);

// Perform operations on individual leaves and composite components
leaf1.operation();
leaf2.operation();
composite1.operation();
composite2.operation();
```

## Reference

