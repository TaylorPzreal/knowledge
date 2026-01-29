
Review
1. 2024-09-17 16:15

> [!Summary]
> 

## 一、Introduction
The **flyweight pattern** is a structural design pattern that reduces memory usage by *sharing common objects*. This pattern is particularly useful when you have a large number of similar objects that differ only in a few attributes.

```ts
interface Shape {
  draw(x: number, y: number): void;
}

class Circle implements Shape {
  private radius: number;

  constructor(radius: number) {
    this.radius = radius;
  }

  draw(x: number, y: number): void {
    console.log(`Drawing a circle with radius ${this.radius} at (${x}, ${y})`);
  }
}

class CircleFactory {
  private circles: Map<number, Circle> = new Map();

  getCircle(radius: number): Circle {
    if (!this.circles.has(radius)) {
      this.circles.set(radius, new Circle(radius));
    }
    return this.circles.get(radius);
  }
}

// Client code
const circleFactory = new CircleFactory();

const circle1 = circleFactory.getCircle(10);
const circle2 = circleFactory.getCircle(10);
const circle3 = circleFactory.getCircle(20);

circle1.draw(100, 100);
circle2.draw(200, 200);
circle3.draw(300, 300);
```




## Reference

