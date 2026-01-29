
Review
1. 2022-12-07
2. 2024-01-14
3. 2024-07-25 07:50

> [!本文摘要]
> `this` 指向
> - In an object method, `this` refers to the object
> - Alone, `this` refers to the global object
> - In a function, `this` refers to the global object
> - In a function, in strict mode, `this` is undefined
> - In an event handler, `this` refers to the element that received the event
> - Methods like call(), apply(), and bind() can refer `this` to any object
> 
> Others
> - `this` is not a variable. It is a keyword. You cannot change the value of `this`.
> - Please note that arrow functions are special: they have no `this`. When `this` is accessed inside an arrow function, it is taken from outside.
> - 每个函数的 this 是在调用时(运行时)被绑定的，完全取决于函数的调用位置。this 的绑定和函数声明的位置没有任何关系，只取决于函数的调用方式。this 在任何情况下都不指向函数的词法作用域。
> - 当一个函数被调用时，会创建一个**执行上下文**。这个执行上下文会包含函数在哪里被调用(调用栈)、函数的调用方法、传入的参数等信息。this 就是执行上下文的其中一个属性，会在函数执行的过程中用到。
> - JavaScript 语言和宿主环境中许多新的内置函数，都提供了一 个可选的参数，通常被称为“上下文”(context)，其作用和 bind(..) 一样，确保你的回调 函数使用指定的 this。



> **四条规则来判断 this 的绑定对象。** 
> 1. new绑定：由new调用?绑定到新创建的对象或者return的对象。
> 2. 显式绑定：由call或者apply(或者bind)调用?绑定到指定的对象。
> 3. 隐私绑定：由上下文对象调用?绑定到那个上下文对象。
> 4. 默认绑定：在严格模式下绑定到undefined，否则绑定到全局对象。 
> 
> 硬绑定：显式绑定的变种，创建一个包裹函数，在函数内部手动调用call/apply等，函数外部在被调用call/apply就不会被生效了。其实就是bind()的实现。
> 
> 如果你把 null 或者 undefined 作为 this 的绑定对象传入 call、apply 或者 bind，这些值在调用时会被忽略，实际应用的是默认绑定规则。如果函数并不关心 this 的话，你仍然需要传入一个占位值，这时 **_null_** 可能是一个不错的选择。创建一个“DMZ”(demilitarized zone，非军事区)对象——它就是一个空的非委托的对象（Object.create(null)）会更加安全，无任何副作用。
> 
> 总是使用 null 来忽略 this 绑定可能产生一些副作用。如果某个函数确实使用了 this(比如第三方库中的一个函数)，那默认绑定规则会把 this 绑定到全局对象(在浏览器中这个对象是 window)，这将导致不可预知的后果(比如修改全局对象)。 
> 
> 对于默认绑定来说，决定 this 绑定对象的并不是调用位置是否处于严格模式，而是函数体是否处于严格模式。如果函数体处于严格模式，this 会被绑定到 undefined，否则 this 会被绑定到全局对象。


> When we write our code using objects to represent entities, that’s called [object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming), in short: “OOP”.

## 一、Introduction
`This` refers to an object, but it depends on how or where it is being invoked. It also has some differences between strict mode and non-strict mode.

In JavaScript, the **this** keyword refers to the object that is currently being executed. It is a dynamic value that changes depending on how a function is called. The value of **this** is determined by the context in which the function is called, and it can be different each time the function is invoked.

### In regular function
```js
function sayHello() {
  console.log(`Hello, ${this.name}!`);
}

sayHello(); // Output: "Hello, undefined!"
```

### `this` in methods
> The value of `this` is the **first** object “before dot”, the one used to call the method.

```js
let user = {
  name: "John",
  age: 30,

  sayHi() {
    // "this" is the "current object"
    alert(this.name);
  }

};

user.sayHi(); // John, this refer before sayHi -> user
```

```js
let user = { name: "John" };
let admin = { name: "Admin" };

function sayHi() {
  alert( this.name );
}

// use the same function in two objects
user.f = sayHi;
admin.f = sayHi;

// these calls have different this
// "this" inside the function is the object "before the dot"
user.f(); // John  (this == user)
admin.f(); // Admin  (this == admin)

admin['f'](); // Admin (dot or square brackets access the method – doesn't matter)
```

### Arrow functions have no “this”
Arrow functions are special: they don’t have their “own” `this`. If we reference `this` from such a function, it’s taken from the **outer “normal” function**.

```js
var firstName: "AAA",

let user = {
  firstName: "Ilya",
  sayHi() {
    let arrow = () => console.log(this.firstName);
    arrow();
  }
};

user.sayHi(); // Ilya
```

```js
var greeting = 'hi';

const obj = {
  greeting: 'hey',

  fo() {
    const greeting = 'hola';

    const fo2 = function () {
      const greeting = 'hello';

      const arrowFo = () => {
        console.log(this.greeting);
      };

      arrowFo();
    };
    fo2();
  },
};

obj.fo(); //logs: hi
```

```js
var greeting = 'hi';

const obj = {
  greeting: 'hey',

  fo() {
    const greeting = 'hola';

    this.fo2 = function () {
      const greeting = 'hello';

      const arrowFo = () => {
        console.log(this.greeting);
      };

      arrowFo();
    };
    this.fo2();
  },
};

obj.fo(); //logs: hey
```

### In a `constructor` function
```js
function Person(name) {
  this.name = name;
  this.sayHello = function() {
    console.log(`Hello, ${this.name}!`);
  }
}

const person = new Person('John Doe');
person.sayHello(); // Output: "Hello, John Doe!"
```

### In event handlers
In HTML event handlers, `this` refers to the HTML element that received the event:
```html
<button onclick="this.style.display='none'">  
  Click to Remove Me!  
</button>
```


### Function Borrowing
Function borrowing allows us to use the methods of one object on a different object without having to make a copy of that method and maintain it in two separate places. It is accomplished through the use of `.call()`, `.apply()`, or `.bind()`, all of which exist to explicitly set this on the method we are borrowing.

## Reference
[mdn this](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
[The JS This keyword](https://www.w3schools.com/js/js_this.asp)
[Object methods, "this"](https://javascript.info/object-methods)
[Function Borrowing in JavaScript](https://medium.com/@ensallee/function-borrowing-in-javascript-4bd671e9d7b4)

