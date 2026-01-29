
Review
1. 2021/03/04
2. 2023/02/05
3. 2023-03-12 13:46
4. 2024-07-21

## 一、Introduction
### Primitive Types
1. Number
2. Boolean
3. String
4. Symbol
5. Null
6. Undefined
7. BigInt

### Object Types
1. Interface
2. Class
3. Enum
4. Array
5. Tuple

### Other Types
- Any
- Unknown
- Void
- Never
- Union
- Intersection
- Type aliases
- Type Assertions

### Useful Operators
1. `in`
2. `keyof`
3. `typeof`
4. `extends`


## 二、最佳实践
### 2.1: Strict Type Checking
严格的类型检查就是要确保变量的类型与您期望的类型相匹配。通过将一些TS的静默错误更改为抛出错误，消除了TS的一些静默错误，能更加有效保障代码运行的安全；提高编译器效率，增加运行速度；禁止一些可能在ECMAScript未来版本中定义的语法。

`tsconfig.json`
```json
{
	"compilerOptions": {
		"strict": true
	}
}
```

确定默认值：使用最新的 **??** 运算符或者最好是在参数级别定义返回值。?? 与 || 不同，它只返回 null 或 undefined，而不是所有 falsy 值。

### 2.2: Type Inference（类型推断）
类型推断是 TypeScript 编译器根据分配给它的值自动确定变量类型的能力。但请记住，类型推断不是魔杖，有时最好明确类型，尤其是在处理复杂类型或要确保使用特定类型时。
下面这条语句，可以推断出是字符串类型。
```ts
let name = "John";
```

强制告诉编译器它无法推断的类型使用 `as SomeOtherType;`
```ts
products as Product[];
```

### 2.3: Linters
Linters are tools that can help you to write better code by enforcing a set of rules and guidelines.

[ESLint](https://eslint.org/), that can help you to enforce a consistent code style and catch potential errors.

### 2.4: Interfaces
Interfaces also make it easier to refactor your code, by ensuring that all the places where a certain type is used are updated at once.
```ts
interface User {  
	name: string;  
	age: number;  
}

let user: User = {name: "John", age: 25};
```

### 2.5: Type Aliases
TypeScript allows you to create custom types using a feature called type aliases. The main difference between features type alias and interfaceis that ==type alias creates a new name for the type==, whereas ==interface creates a new name for the shape of the object==.

```ts
type Point = { x: number, y: number };  
let point: Point = { x: 0, y: 0 };
```

Type aliases can also be used to create complex types, such as a **union type（联合类型）** or an **intersection type（交叉类型）**.
交叉类型是将多个类型合并为一个类型。

```ts
type User = { name: string, age: number };  
type Admin = { name: string, age: number, privileges: string[] };  
type SuperUser = User & Admin;
```

### 2.6: Tuples
Tuples（元组）是一种表示具有不同类型的**固定数组长度**的方法。 它们允许您表达具有特定顺序和类型的值的集合。

```ts
let point: [number, number] = [1, 2];
let [x, y] = point;  
console.log(x, y);
```

### 2.7: any
Sometimes, we may not have all the information about a variable’s type, but still need to use it in our code. In such cases, we can utilize the `any` type. But, like any powerful tool, the use of `any` should be used with caution and purpose.

One best practice when using `any` is to limit its usage to specific cases where the type is truly unknown, such as when working with **third-party libraries** or **dynamically generated data**.

Another best practice is to ==avoid using `any` in function return types and function arguments==, as it can weaken the type safety of your code. Instead, you can use a type that is more specific or use a type that is more general like `unknown` or `object` that still provide some level of type safety.

### 2.8: unknow 
`unknown` is the type-safe counterpart of any. Anything is assignable to `unknown`, but `unknown` isn’t assignable to anything but itself and `any` without a type assertion or a control flow based narrowing. 

Unlike `any`, when you use the `unknown` type, TypeScript will not allow you to perform any operation on a value unless you first check its type. This can help you to catch type errors at compile-time, instead of at runtime.

在所有我们不确定类型的情况下，我们都应该使用unknown。

```ts
function printValue(value: unknown) {  
	if (typeof value === "string") {  
		console.log(value);  
	} else {  
		console.log("Not a string");  
	}
}
```

### 2.9: never
In TypeScript, `never` is a special type that represents values that will never occur. ==It’s used to indicate that a function will not return normally, but will instead throw an error.== This is a great way to indicate to other developers (and the compiler) that a function can’t be used in certain ways, this can help to catch potential bugs.

```ts
function divide(numerator: number, denominator: number): number | never {  
	if (denominator === 0) {  
		throw new Error("Cannot divide by zero");  
	}
	return numerator / denominator;  
}
```

never类型是任何类型的子类型，也可以赋值给任何类型；然而，没有类型是never的子类型或可以赋值给never类型（除了never本身之外）。 即使 any也不可以赋值给never。

```ts
// 返回never的函数必须存在无法达到的终点
function error(message: string): never {
    throw new Error(message);
}

// 推断的返回值类型为never
function fail() {
    return error("Something failed");
}
```

### 2.10: `keyof` operator
The `keyof` operator is a powerful feature of TypeScript that allows you to create a type that represents the keys of an object. It can be used to make it clear which properties are allowed for an object.

```ts
interface User {  
	name: string;  
	age: number;  
}
type UserKeys = keyof User; // "name" | "age"
```

You can also use the `keyof` operator to create more type-safe functions that take an object and a key as arguments:

```ts
interface User {
  name: string;
  age: number;
}

function getValue<T, K extends keyof T>(obj: T, key: K) {
  return obj[key];
}

let user: User = { name: "John", age: 30 };
console.log(getValue(user, 'age')); // "John"
console.log(getValue(user, "gender")); // Error: Argument of type '"gender"' is not assignable to parameter of type '"name" | "age"'.
```

### 2.11: Enums
Enums, short for enumerations, are a way to define a set of named constants in TypeScript. They can be used to create a more readable and maintainable code, by giving a meaningful name to a set of related values.

```ts
enum OrderStatus {  
 Pending,  
 Processing,  
 Shipped,  
 Delivered = 'deliverd',  
 Cancelled = 5,
}  
let orderStatus: OrderStatus = OrderStatus.Pending;
```

Enums can also have a custom set of numeric values or strings.

1.  默认情况下，**从0开始为元素编号**
2.  可以手动指定成员的数值
3.  一个便利：由枚举值可得到枚举的名称

### 2.12: Namespaces
==`Namespaces` are a way to organize your code and prevent naming collisions.== They allow you to create a container for your code, where you can define variables, classes, functions, and interfaces.

For example, you can use a namespace to group all the code related to a specific feature:

```ts
namespace OrderModule {
  export class Order { /* … */ }
  export function cancelOrder(order: Order) { /* … */ }
  export function processOrder(order: Order) { /* … */ }
}

let order = new OrderModule.Order();
OrderModule.cancelOrder(order);
```

### 2.13: Utility Types
Utility types are a **built-in** feature of TypeScript that provide a set of predefined types to help you write better type-safe code. They allow you to perform common type operations and manipulate types in a more convenient way.

For example, you can use the `Pick` utility type to extract a subset of properties from an object type:

```ts
type User = { name: string, age: number, email: string };  
type UserInfo = Pick<User, "name" | "email">;
```

- Pick: `Pick<Persion, 'id' | 'name'>`
- Omit: `Omit<Persion, 'id' | 'name'`
- Exclude: remove properties from an object type
- Partial: make all properties of a type optional

```ts
type User = { name: string, age: number, email: string };  
type UserWithoutAge = Exclude<User, "age">;

type User = { name: string, age: number, email: string };  
type PartialUser = Partial<User>;
```

```ts
// 实现Pick
type Pick<T, K extends keyof T> = { [P in K]: T[P] }

type ArrowFn<T> = (arg: T) => T

// 实现Readonly
type MyReadonly<T> = { readonly [P in keyof T]: T[P] }
```

### 2.14: Readonly and ReadonlyArray
When working with data in TypeScript, you might want to make sure that certain values can’t be changed. And that’s where `Readonly` and `ReadonlyArray` come in.

The `Readonly` keyword is used to make properties of an object read-only, meaning they can’t be modified after they are created. This can be useful when working with configuration or constant values, for example.

```ts
interface Point {
  x: number;
  y: number;
}
let point: Readonly<Point> = { x: 0, y: 0 };
point.x = 1; // TypeScript will raise an error because "point.x" is read-only
```

The `ReadonlyArray` is similar to `Readonly` but for arrays. It makes an array read-only, and it can’t be modified after it’s created.

```ts
let numbers: ReadonlyArray<number> = [1, 2, 3];
numbers.push(4); // TypeScript will raise an error because "numbers" is read-only
```


### 2.15: Type Guards（类型保护）
Type guards are a powerful tool that can help you to narrow down the type of a variable based on certain conditions.

```ts
function isNumber(x: any): x is number {
  return typeof x === "number";
}
let value = 3;
if (isNumber(value)) {
  value.toFixed(2); // TypeScript knows that "value" is a number because of the type guard
}
```

Type guards can be used with the equality operator (`===`, `!==`, `==`, `!=` 
), `in` operator, the `typeof` operator and the `instanceof` operator.

```ts
function move(animal: Fish | Bird) {
	if ("swim" in animal) {
		return animal.swim();
	}
	return animal.fly();
}
```

 In JavaScript `x instanceof Foo` checks whether the _prototype chain_ of `x` contains `Foo.prototype`.

```ts
function logValue(x: Date | string) {
	if (x instanceof Date) {
		console.log(x.toUTCString());
	} else {
		console.log(x.toUpperCase());
	}
}
```

In JavaScript, we can use any expression in conditionals, `&&`s, `||`s, `if` statements, Boolean negations (`!`), and more.
Values like
- `0`
- `NaN`
- `""` (the empty string)
- `0n` (the `bigint` version of zero)
- `null`
- `undefined`
- `false`
- `-0`

Type predicates
```ts
function isString(value: unknown): value is string {
  return typeof value === 'string';
}

function example(x: unknown) {
  if (isString(x)) {
    // We can now call any 'string' method on 'x'.
    x.toUpperCase();
  } else {
    console.log(x);
  }
}
```

### 2.16: Generics（泛型）
Generics allow you to write a single function, `class` or `interface` that can work with multiple types, without having to write separate implementations for each type.

```ts
function createArray<T>(length: number, value: T): Array<T> {
  let result: T[] = [];
  for (let i = 0; i < length; i++) {
    result[i] = value;
  }
  return result;
}
let names = createArray<string>(3, "Bob");
let numbers = createArray<number>(3, 0);
```

### 2.17:   `infer` keyword
The `infer` keyword is a powerful feature of TypeScript that allows you to extract the type of a variable in a type.

For example, you can use the `infer` keyword to create a more precise type for a function that returns an array of a specific type:

```ts
type ArrayType<T> = T extends (infer U)[] ? U : never;
type MyArray = ArrayType<string[]>; // MyArray is of type string
```

You can also use the `infer` keyword to create more precise types for a function that returns an object with a specific property:

```ts
type ObjectType<T> = T extends { [key: string]: infer U } ? U : never;
type MyObject = ObjectType<{ name: string, age: number }>; // MyObject is of type {name:string, age: number}
```

### 2.18: Conditional Types（条件类型）
Conditional types let you to express more complex type relationships. They allow you to create new types based on the conditions of other types.

For example, you can use a conditional type to extract the return type of a function:
```ts
type FnReturnType<T> = T extends (...args: any[]) => infer R ? R : any;
type R1 = FnReturnType<() => string>; // string
type R2 = FnReturnType<() => void>; // void
```

You can also use conditional types to extract the properties of an object type that meet a certain condition:
```ts
type PickProperties<T, U> = { [K in keyof T]: T[K] extends U ? K : never }[keyof T];
type P1 = PickProperties<{ a: number, b: string, c: boolean }, string | number>; // "a" | "b"
```

### 2.19: Mapped Types（映射类型）
映射类型是一种基于现有类型创建新类型的方法。 它们允许您通过对现有类型的属性应用一组操作来创建新类型。

For example, you can use a mapped type to create a new type that represents the readonly version of an existing type:
```ts
type Readonly<T> = { readonly [P in keyof T]: T[P] };
let obj: { a: number, b: string } = { a: 1, b: "hello" };
let readonlyObj: Readonly<typeof obj> = { a: 1, b: "hello" };
```

You can also use a mapped type to create a new type that represents the optional version of an existing type:
```ts
type Optional<T> = { [P in keyof T]?: T[P] };  
let obj: { a: number, b: string } = { a: 1, b: "hello" };  
let optionalObj: Optional<typeof obj> = { a: 1 };
```

映射类型可以以不同的方式使用：创建新类型，添加或删除现有类型的属性，或更改现有类型的属性类型。

### 2.20: Decorators（装饰器）
Decorators（装饰器）是一种使用简单语法向类、方法或属性添加附加功能的方法。 它们是一种在不修改类实现的情况下增强类行为的方法。

```ts
function logMethod(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
  let originalMethod = descriptor.value;
  descriptor.value = function (...args: any[]) {
    console.log(`Calling ${propertyKey} with args: ${JSON.stringify(args)}`);
    let result = originalMethod.apply(this, args);
    console.log(`Called ${propertyKey}, result: ${result}`);
    return result;
  }
}
class Calculator {
  @logMethod
  add(x: number, y: number): number {
    return x + y;
  }
}
```

您还可以使用装饰器将元数据添加到可以在运行时使用的类、方法或属性。
```ts
function setApiPath(path: string) {
  return function (target: any) {
    target.prototype.apiPath = path;
  }
}

@setApiPath("/users")
class UserService {
  // …
}
console.log(new UserService().apiPath); // "/users"
```

### 2.21: 可选属性
清楚地表达，模型哪些组合存在，哪些不存在
1.  将属性定义为**可选**而不是**划分类型**更容易并且生成的代码更少。它还需要对正在开发的产品有充分的了解，并且可以在对产品的假设发生变化时限制代码的使用。
2.  类型系统的最大好处是它们可以用**编译时检查**代替运行时检查。通过更多的快速输入，可以在编译时检查可能被忽视的错误。

**使用一个完整的描述性类型名称作为泛型参数**
```ts
interface Product {
	id: string;
	type: 'react' | 'vue';
}

interface ReactProduct extends Product {
	type: 'react';
	reactVersion: '16';
}

interface VueProduct extends Product {
	type: 'vue',
	vueVersion: '3';
}
```


### 2.22: Void
`void` represents the return value of functions which don’t return a value. It’s the inferred type any time a function doesn’t have any `return` statements, or doesn’t return any explicit value from those return statements.


### 2.23: Type Compatibility
TypeScript uses structural typing to determine type compatibility. This means that two types are considered compatible if they have the same structure, regardless of their names.

```ts
interface Point {
  x: number;
  y: number;
}

let p1: Point = { x: 10, y: 20 };
let p2: { x: number; y: number } = p1;

console.log(p2.x); // Output: 10
```


### 2.24: `as const` Assertion
`any` is a special type in TypeScript that represents a value of any type. When a value is declared with the any type, the compiler will not perform any type checks or type inference on that value.

Type assertions (`as [type]`) are a way to override the default static type-checking behavior and tell the compiler that you know more about the type of a particular expression than it does.

`as const` is a type assertion in TypeScript that allows you to assert that an expression has a specific type, and that its value should be treated as a read-only value.

```
const colors = ['red', 'green', 'blue'] as const;

// colors is now of type readonly ['red', 'green', 'blue']
```


### 2.25: Non Null Assertion
The non-null assertion operator (`!`) is a type assertion in TypeScript that allows you to tell the compiler that a value will never be null or undefined.

```ts
let nameLength = name!.length;
```

However, it’s important to be careful when using the non-null assertion operator, as it can lead to runtime errors if the value is actually `null` or `undefined`.


### 2.26: Satisfies keyword
TypeScript developers are often faced with a dilemma: we want to ensure that some expression matches some type, but also want to keep the most specific type of that expression for inference purposes.

The `satisfies` operator lets us validate that the type of an expression matches some type, without changing the resulting type of that expression. As an example, we could use `satisfies` to validate that all the properties of palette are compatible with `string | number[]`:

```ts
type Colors = 'red' | 'green' | 'blue';
type RGB = [red: number, green: number, blue: number];

const palette = {
  red: [255, 0, 0],
  green: '#00ff00',
  bleu: [0, 0, 255],
  //  ~~~~ The typo is now caught!
} satisfies Record<Colors, string | RGB>;

// Both of these methods are still accessible!
const redComponent = palette.red.at(0);
const greenNormalized = palette.green.toUpperCase();
```

### 2.27: Function Overloading
Function Overloading in TypeScript allows multiple functions with the same name but with different parameters to be defined. The correct function to call is determined based on the number, type, and order of the arguments passed to the function at runtime.

```ts
function add(a: number, b: number): number;
function add(a: string, b: string): string;

function add(a: any, b: any): any {
  return a + b;
}

console.log(add(1, 2)); // 3
console.log(add('Hello', ' World')); // "Hello World"
```



## Reference
1. [Mastering TypeScript: 20 Best Practices for Improved Code Quality](https://itnext.io/mastering-typescript-21-best-practices-for-improved-code-quality-2f7615e1fdc3)
2. [TS部分泛型的使用和实现](https://zhuanlan.zhihu.com/p/40311981)

