
Review
1. 2024-07-21 21:42

## 一、Introduction
- Intersection Types
- Union Types
- Type Aliases
- Conditional Types
- Index Types
- Mapped Types
- Type Guards



### Conditional Types
Conditional types in TypeScript are a way to select a type based on a condition. They allow you to write a type that dynamically chooses a type based on the types of its inputs. Conditional types are declared using a combination of the `infer` keyword and a type that tests a condition and selects a type based on the result of the test.

```ts
type Extends<T, U> = T extends U ? T : U;

type A = Extends<string, any>; // type A is 'string'
type B = Extends<any, string>; // type B is 'string'
```

### Literal Types
Literal types in TypeScript are a way to specify a value exactly, rather than just a type. Literal types can be used to enforce that a value must be of a specific type and a specific value. Literal types are created by using a literal value, such as a string, number, or boolean, as a type.

```ts
type Age = 42;

let age: Age = 42; // ok
let age: Age = 43; // error
```


### Template Literal Types
Template literal types in TypeScript are a way to manipulate string values as types. They allow you to create a type based on the result of string manipulation or concatenation. Template literal types are created using the backtick (“) character and string manipulation expressions within the type.

```ts
type Name = `Mr. ${string}`;

let name: Name = `Mr. Smith`;  // ok
let name: Name = `Mrs. Smith`;  // error
```

### Recursive Types
Recursive types in TypeScript are a way to define a type that references itself. Recursive types are used to define complex data structures, such as trees or linked lists, where a value can contain one or more values of the same type.

```ts
type LinkedList<T> = {
  value: T;
  next: LinkedList<T> | null;
};

let list: LinkedList<number> = {
  value: 1,
  next: { value: 2, next: { value: 3, next: null } },
};
```


### Mapped Types
Mapped types in TypeScript are a way to create a new type based on an existing type, where each property of the existing type is transformed in some way. Mapped types are declared using a combination of the `keyof` operator and a type that maps each property of the existing type to a new property type.

```ts
type Readonly<T> = {
  readonly [P in keyof T]: T[P];
};

let obj = { x: 10, y: 20 };
let readonlyObj: Readonly<typeof obj> = obj;
```



## Reference

