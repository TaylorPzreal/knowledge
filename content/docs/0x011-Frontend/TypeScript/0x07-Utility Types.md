
Review
1. 2024-07-21 21:19

## 一、Introduction
1. `Awaited<Type>` This type is meant to model operations like await in async functions, or the `.then()` method on Promises - specifically, the way that they recursively unwrap Promises.
2. `Partial<Type>`: makes all properties of a type optional.
3. `Required<Type>`: Constructs a type consisting of all properties of `Type` set to required. The opposite of `Partial`.
4. `Readonly<Type>`: makes all properties of a type read-only.
5. **`Record<Keys, Type>`**: `Record` constructs an object type whose property keys are `Keys` and whose property values are `Type`. This utility can be used to map the properties of a type to another type.
6. `Pick<Type, Keys>`: allows you to pick specific properties from a type.
7. `Omit<Type, Keys>`: allows you to omit specific properties from a type.
8. **`Exclude<UnionType, ExcludedMembers>`**: Constructs a type by excluding from `UnionType` all union members that are assignable to `ExcludedMembers`. **creates a type that is the set difference of A and B**.  ***差集***
9. **`Extract<Type, Union>`** Extract constructs a type by extracting from `Type` all union members that are assignable to `Union`. ***交集***
10. `NonNullable<Type>` Non-Nullable constructs a type by excluding `null` and `undefined` from Type.
11. `Parameters<Type>` Parameters constructs a tuple type from the types used in the parameters of a function type `Type`.
12. `ConstructorParameters<Type>` Constructs a tuple or array type from the types of a constructor function type. It produces a tuple type with all the parameter types (or the type `never` if `Type` is not a function).
13. `ReturnType` Return type constructs a type consisting of the return type of function Type.
14. `InstanceType` This type constructs a type consisting of the instance type of a constructor function in Type.
15. `NoInfer<Type>` Blocks inferences to the contained type. Other than blocking inferences, `NoInfer<Type>` is identical to `Type`.
16. `ThisParameterType<Type>` Extracts the type of the [this](https://www.typescriptlang.org/docs/handbook/functions.html#this-parameters) parameter for a function type, or `unknown` if the function type has no `this` parameter.
17. `OmitThisParameter<Type>` Removes the [`this`](https://www.typescriptlang.org/docs/handbook/functions.html#this-parameters) parameter from `Type`. If `Type` has no explicitly declared `this` parameter, the result is simply `Type`. Otherwise, a new function type with no `this` parameter is created from `Type`. Generics are erased and only the last overload signature is propagated into the new function type.
18. `ThisType<Type>` This utility does not return a transformed type. Instead, it serves as a marker for a contextual [`this`](https://www.typescriptlang.org/docs/handbook/functions.html#this) type. Note that the [`noImplicitThis`](https://www.typescriptlang.org/tsconfig#noImplicitThis) flag must be enabled to use this utility.
19. `Uppercase<StringType>`
20. `Lowercase<StringType>`
21. `Capitalize<StringType>`
22. `Uncapitalize<StringType>`


```ts
interface User {
  name: string;
  age: number;
  email: string;
}
```

### `Partial<Type>`
```ts
Partial<User>
```


```ts
Pick<User, 'name' | 'age'>
```

```ts
Omit<User, 'age' | 'email'>
```

```ts
Readonly<User>
```

```ts
interface CatInfo {
  age: number;
  breed: string;
}

type CatName = 'miffy' | 'boris' | 'mordred';

const cats: Record<CatName, CatInfo> = {
  miffy: { age: 10, breed: 'Persian' },
  boris: { age: 5, breed: 'Maine Coon' },
  mordred: { age: 16, breed: 'British Shorthair' },
};
```

### `Exclude`
```ts
type T0 = Exclude<'a' | 'b' | 'c', 'a'>; // "b" | "c"
type T1 = Exclude<'a' | 'b' | 'c', 'a' | 'b'>; // "c"
type T2 = Exclude<string | number | (() => void), Function>; // string | number

type Shape =
| { kind: "circle"; radius: number }
| { kind: "square"; x: number }
| { kind: "triangle"; x: number; y: number };

type T3 = Exclude<Shape, { kind: "circle" }>
```


```ts
type T0 = Extract<'a' | 'b' | 'c', 'a' | 'f'>;
//    ^ = type T0 = "a"
```

```ts
type T0 = NonNullable<string | number | undefined>;
// type T0 = string | number

type T1 = NonNullable<string[] | null | undefined>;
// type T1 = string[]
```

### `Parameters`
```ts
type T0 = Parameters<() => string>;
// type T0 = []

type T1 = Parameters<(s: string) => void>;
// type T1 = [s: string]

type T2 = Parameters<<T>(arg: T) => T>;
// type T2 = [arg: unknown]

declare function f1(arg: { a: number; b: string }): void;
type T3 = Parameters<typeof f1>;
// type T3 = [arg: {
//     a: number;
//     b: string;
// }]

type T4 = Parameters<any>;
// type T4 = unknown[]

type T5 = Parameters<never>;
// type T5 = never

type T6 = Parameters<string>;
// ^ Type 'string' does not satisfy the constraint '(...args: any) => any'.

type T7 = Parameters<Function>;
// ^ Type 'Function' does not satisfy the constraint '(...args: any) => any'.
```

### `ConstructorParameters<Type>`
```ts
type T0 = ConstructorParameters<ErrorConstructor>;
// type T0 = [message?: string]

type T1 = ConstructorParameters<FunctionConstructor>;
// type T1 = string[]

type T2 = ConstructorParameters<RegExpConstructor>;
// type T2 = [pattern: string | RegExp, flags?: string]

class C {
constructor(a: number, b: string) {}
}

type T3 = ConstructorParameters<typeof C>;
// type T3 = [a: number, b: string]

type T4 = ConstructorParameters<any>;
// type T4 = unknown[]

type T5 = ConstructorParameters<Function>;
// type T5 = never
```


### `ReturnType<Type>`
```ts
type T0 = ReturnType<() => string>;
// type T0 = string

type T1 = ReturnType<(s: string) => void>;
// type T1 = void

type T2 = ReturnType<<T>() => T>;
// type T2 = unknown

type T3 = ReturnType<<T extends U, U extends number[]>() => T>;
// type T3 = number[]

declare function f1(): { a: number; b: string };
type T4 = ReturnType<typeof f1>;
// type T4 = {
//     a: number;
//     b: string;
// }

type T5 = ReturnType<any>;
// type T5 = any

type T6 = ReturnType<never>;
// type T6 = never

type T7 = ReturnType<string>;
// ^ Type 'string' does not satisfy the constraint '(...args: any) => any'.

type T8 = ReturnType<Function>;
// ^ Type 'Function' does not satisfy the constraint '(...args: any) => any'.
```


### `InstanceType<Type>`
```ts
class C {
  x = 0;
  y = 0;
}

type T0 = InstanceType<typeof C>;
// type T0 = C

type T1 = InstanceType<any>;
// type T1 = any

type T2 = InstanceType<never>;
// type T2 = never

type T3 = InstanceType<string>;
// ^ Type 'string' does not satisfy the constraint 'abstract new (...args: any) => any'.

type T4 = InstanceType<Function>;
// ^ Type 'Function' does not satisfy the constraint 'abstract new (...args: any) => any'.
```

```ts
type A = Awaited<Promise<string>>;
// type A = string

type B = Awaited<Promise<Promise<number>>>;
// type B = number

type C = Awaited<boolean | Promise<number>>;
// type C = number | boolean
```


### `NoInfer<Type>`
```ts
function createStreetLight<C extends string>(
	colors: C[],
	defaultColor?: NoInfer<C>,
) {
	// ...
}

createStreetLight(["red", "yellow", "green"], "red"); // OK
createStreetLight(["red", "yellow", "green"], "blue"); // Error
```


### `ThisParameterType<Type>`
```ts
function toHex(this: Number) {
	return this.toString(16);
}

function numberToString(n: ThisParameterType<typeof toHex>) {
	return toHex.apply(n);
}
```



```ts
type LowercaseGreeting = "hello, world";
type Greeting = Capitalize<LowercaseGreeting>;
// type Greeting = "Hello, world"
```


```ts
type UppercaseGreeting = "HELLO WORLD";
type UncomfortableGreeting = Uncapitalize<UppercaseGreeting>;
// type UncomfortableGreeting = "hELLO WORLD"
```

## Reference
1. Utility Types <https://www.typescriptlang.org/docs/handbook/utility-types.html> 

