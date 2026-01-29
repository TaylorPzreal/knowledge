
Review
1. 2024-07-21 16:00

## 一、Introduction
1. **Union Types** in TypeScript allow you to specify multiple possible types for a single variable or parameter. Union operator `|`
2. An **intersection type** creates a new type by combining multiple existing types. The new type has all features of the existing types. Intersection Operator `&`
3. `keyof` Operator: The `keyof` operator in TypeScript is used to get the union of keys from an object type.


The union operator `|` is used to combine two or more types into a single type that represents all the possible types.

```ts
type stringOrNumber = string | number;
let value: stringOrNumber = 'hello';

value = 42;
```

The intersection operator `&` is used to intersect two or more types into a single type that represents the properties of all the types.

```ts
interface A {
  a: string;
}

interface B {
  b: number;
}

type AB = A & B;
let value: AB = { a: 'hello', b: 42 };
```


```ts
interface User {
  name: string;
  age: number;
  location: string;
}

type UserKeys = keyof User; // "name" | "age" | "location"
const key: UserKeys = 'name';
```


## Generics
Generics in TypeScript are a way to write code that can work with multiple data types, instead of being limited to a single data type. Generics allow you to write functions, classes, and interfaces that take one or more type parameters, which act as placeholders for the actual data types that will be used when the function, class, or interface is used.
A generic type is defined using angle brackets `<T>` and can be used as a placeholder for a specific data type.

```ts
function identity<T>(arg: T): T {
  return arg;
}

let output = identity<string>('Hello'); // type of output will be 'string'
```


```ts
class GenericNumber<T> {
  zeroValue: T;
  add: (x: T, y: T) => T;
}

let myGenericNumber = new GenericNumber<number>();
myGenericNumber.zeroValue = 0;
myGenericNumber.add = function (x, y) {
  return x + y;
};
```

Generic constraints in TypeScript allow you to specify the requirements for the type parameters used in a generic type. These constraints ensure that the type parameter used in a generic type meets certain requirements.
Constraints are specified using the `extends` keyword, followed by the type that the type parameter must extend or implement.

```ts
interface Lengthwise {
  length: number;
}

function loggingIdentity<T extends Lengthwise>(arg: T): T {
  // Now we know it has a .length property, so no more error
  console.log(arg.length);

  return arg;
}

loggingIdentity(3); // Error, number doesn't have a .length property
loggingIdentity({ length: 10, value: 3 }); // OK
```



## Reference

