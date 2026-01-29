
Review
1. 2024-07-21 17:24

## 一、Introduction
A class in TypeScript is defined using the class keyword, followed by the name of the class. The class definition can include fields (also known as properties or attributes), methods (functions), and a constructor.

```ts
class Animal {
  name: string;
  constructor(name: string) {
    this.name = name;
  }

  makeSound(): void {
    console.log(`${this.name} is making a sound`);
  }
}

const dog = new Animal('Dog');
dog.makeSound(); // Output: Dog is making a sound
```

### Constructor
In TypeScript, constructor parameters can be declared with access modifiers (e.g. `public`, `private`, `protected`) and/or type annotations. The parameters are then automatically assigned to properties of the same name within the constructor, and can be accessed within the class.

```ts
class Example {
  constructor(private name: string, public age: number) {}
}
```

In this example, the constructor has two parameters: name and age. name has a private access modifier, so it can only be accessed within the Example class. age has a public access modifier, so it can be accessed from outside the class as well.

In TypeScript, you can achieve constructor overloading by using multiple constructor definitions with different parameter lists in a single class.

```ts
class Point {
  // Overloads
  constructor(x: number, y: string);
  constructor(s: string);

  constructor(xs: any, y?: any) {
    // TBD
  }
}
```

> Note that, similar to function overloading, we only have one implementation of the consructor and it’s the only the signature that is overloaded.


 There are three access modifiers in TypeScript:
- `public:` This is the default access modifier. Properties and methods declared as public can be accessed from anywhere, both inside and outside the class.
- `private:` Properties and methods declared as private can only be accessed within the same class. They are not accessible from outside the class.
- `protected:` Properties and methods declared as protected can be accessed within the class and its subclasses. They are not accessible from outside the class and its subclasses.


Abstract classes in TypeScript are classes that cannot be instantiated on their own and must be subclassed by other classes. Abstract classes provide a blueprint for other classes and can have abstract methods, which are methods without a body and must be overridden by the subclass. These classes are useful for defining a common interface or basic functionality that other classes can inherit and build upon.

```ts
abstract class Animal {
  abstract makeSound(): void;

  move(): void {
    console.log('moving...');
  }
}

class Dog extends Animal {
  makeSound(): void {
    console.log('bark');
  }
}
```


Inheritance refers to a mechanism where a subclass inherits properties and methods from its parent class. This allows a subclass to reuse the code and behavior of its parent class while also adding or modifying its own behavior. In TypeScript, inheritance is achieved using the `extends` keyword.

Polymorphism refers to the ability of an object to take on many forms. This allows objects of different classes to be treated as objects of a common class, as long as they share a common interface or inheritance hierarchy. In TypeScript, polymorphism is achieved through method overriding and method overloading.

```ts
class Animal {
  makeSound(): void {
    console.log('Making animal sound');
  }
}

class Dog extends Animal {
  makeSound(): void {
    console.log('Bark');
  }
}

class Cat extends Animal {
  makeSound(): void {
    console.log('Meow');
  }
}

let animal: Animal;

animal = new Dog();
animal.makeSound(); // Output: Bark

animal = new Cat();
animal.makeSound(); // Output: Meow
```

In TypeScript, method overriding is a mechanism where a subclass provides a new implementation for a method that is already defined in its parent class. This allows the subclass to inherit the behavior of the parent class, but change its behavior to fit its own needs.

To override a method in TypeScript the signature of the method in the subclass must match exactly with the signature of the method in the parent class.


## Reference

