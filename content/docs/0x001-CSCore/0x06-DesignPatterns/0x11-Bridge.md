#Structural 

Review
1. 2024-09-17 07:54

> [!Summary]
> 

## 一、Introduction
The bridge pattern is a structural design pattern that *decouples an abstraction from its implementation*, allowing them to vary independently. This pattern is particularly useful when you have a class hierarchy that needs to be independent from the implementation details of its subclasses.

```ts
interface Shape {
  draw(): void;
}

class Circle implements Shape {
  private color: Color;

  constructor(color: Color) {
    this.color = color;
  }

  draw(): void {
    console.log(`Drawing a circle in ${this.color.getColor()}`);
  }
}

class Square implements Shape {
  private color: Color;

  constructor(color: Color) {
    this.color = color;
  }

  draw(): void {
    console.log(`Drawing a square in ${this.color.getColor()}`);
  }
}

interface Color {
  getColor(): string;
}

class Red implements Color {
  getColor(): string {
    return "red";
  }
}

class Blue implements Color {
  getColor(): string {
    return "blue";
  }
}

// Client code
const redCircle = new Circle(new Red());
redCircle.draw();

const blueSquare = new Square(new Blue());
blueSquare.draw();
```

## Reference

