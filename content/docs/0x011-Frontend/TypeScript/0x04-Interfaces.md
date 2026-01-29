
Review
1. 2024-07-21 16:37

## 一、Introduction
Interfaces in TypeScript provide a way to define a contract for a type, which includes a set of properties, methods, and events. It’s used to enforce a structure for an object, class, or function argument.

```ts
interface User {
  name: string;
  age: number;
}

const user: User = {
  name: 'John Doe',
  age: 30,
};
```

> **Types** are used to create a new named type based on an existing type or to combine existing types into a new type.
> **Interfaces**, on the other hand, are used to describe the structure of objects and classes.


In TypeScript, you can extend an interface by creating a new interface that inherits from the original interface using the “extends” keyword.

```ts
interface Shape {
  width: number;
  height: number;
}

interface Square extends Shape {
  sideLength: number;
}

let square: Square = {
  width: 10,
  height: 10,
  sideLength: 10,
};
```




## Reference

