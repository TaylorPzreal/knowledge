
Review
1. 2024-09-17 16:51

> [!Summary]
> 

## 一、Introduction
The **visitor pattern** is a behavioral design pattern that allows you to define new operations on existing object structures without modifying the classes of those objects. This pattern is useful when you need to perform different operations on objects of different types within a hierarchy, and you want to avoid modifying the classes of those objects.

```ts
interface Visitor {
  visitShape(shape: Shape): void;
  visitCircle(circle: Circle): void;
  visitSquare(square: Square): void;
}

interface Shape {
  accept(visitor: Visitor): void;
}

class Circle implements Shape {
  private radius: number;

  constructor(radius: number) {
    this.radius = radius;
  }

  accept(visitor: Visitor): void {
    visitor.visitCircle(this);
  }
}

class Square implements Shape {
  private side: number;

  constructor(side: number) {
    this.side = side;
  }

  accept(visitor: Visitor): void {
    visitor.visitSquare(this);
  }
}

class AreaCalculatorVisitor implements Visitor {
  private area: number = 0;

  visitShape(shape: Shape): void {}

  visitCircle(circle: Circle): void {
    this.area += Math.PI * circle.radius * circle.radius;
  }

  visitSquare(square: Square): void {
    this.area += square.side * square.side;
  }

  getArea(): number {
    return this.area;
  }
}

// Client code
const circle = new Circle(10);
const square = new Square(5);

const calculator = new AreaCalculatorVisitor();
circle.accept(calculator);
square.accept(calculator);

console.log("Total area:", calculator.getArea());
```

## Reference

