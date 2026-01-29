
Review
1. 2024-07-21 22:48

## 一、Introduction
In TypeScript, namespaces are used to organize and share code across multiple files. Namespaces allow you to group related functionality into a single unit and prevent naming conflicts.

```ts
// myNamespace.ts
namespace MyNamespace {
  export function doSomething() {
    console.log('Doing something...');
  }
}

// main.ts
/// <reference path="myNamespace.ts" />
MyNamespace.doSomething(); // Output: "Doing something..."
```

In TypeScript, modules are used to organize and reuse code. There are two types of modules in TypeScript:
- Internal
- External

**Internal modules** are used to organize code within a file and are also referred to as *namespaces*. They are defined using the “namespace” keyword.

**External modules** are used to organize code across multiple files. They are defined using the “export” keyword in one file and the “import” keyword in another file. External modules in TypeScript follow the *CommonJS* or *ES modules* standards.


### Ambient Modules
Ambient modules in TypeScript are used to declare external modules or third-party libraries in a TypeScript program. Ambient modules provide type information for modules that have no TypeScript declarations, but are available in the global scope.


```ts
// myModule.d.ts
declare module 'my-module' {
  export function doSomething(): void;
}

// main.ts
import * as myModule from 'my-module';
myModule.doSomething();
```


### Namespace Augmentation
In TypeScript, namespace augmentation is a way to extend or modify existing namespaces. This is useful when you want to add new functionality to existing namespaces or to fix missing or incorrect declarations in third-party libraries.


```ts
// myModule.d.ts
declare namespace MyModule {
  export interface MyModule {
    newFunction(): void;
  }
}

// main.ts
/// <reference path="myModule.d.ts" />
namespace MyModule {
  export class MyModule {
    public newFunction() {
      console.log('I am a new function in MyModule!');
    }
  }
}

const obj = new MyModule.MyModule();
obj.newFunction(); // Output: "I am a new function in MyModule!"
```

### Global Augmentation
In TypeScript, global augmentation is a way to add declarations to the global scope. This is useful when you want to add new functionality to existing libraries or to augment the built-in types in TypeScript.

```ts
// myModule.d.ts
declare namespace NodeJS {
  interface Global {
    myGlobalFunction(): void;
  }
}

// main.ts
global.myGlobalFunction = function () {
  console.log('I am a global function!');
};

myGlobalFunction(); // Output: "I am a global function!"
```



## Reference
Namespaces <https://www.typescriptlang.org/docs/handbook/namespaces.html> 
Namespaces and Modules <https://www.typescriptlang.org/docs/handbook/namespaces-and-modules.html> 

