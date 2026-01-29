
Review
1. 2024-07-24 08:21

## 一、Introduction
> **Note:** JavaScript only hoists declarations, not initializations.

JavaScript **Hoisting** refers to the process whereby the interpreter appears to move the **_declaration_** of **functions**, **variables**, **classes**, or **imports** to the top of their [scope](https://developer.mozilla.org/en-US/docs/Glossary/Scope), prior to execution of the code.

1. `Value hoisting`: Being able to use a variable's value in its scope before the line it is declared.  **Function declarations**, `import` declarations
2. `Declaration hoisting`: Being able to reference a variable in its scope before the line it is declared, without throwing a [`ReferenceError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError), but the value is always [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined).  `var` declaration
3. `暂时性死区`:The declaration of the variable causes behavior changes in its scope before the line in which it is declared. `let`, `const`, `class` declarations
4. The side effects of a declaration are produced before evaluating the rest of the code that contains it. `import` declarations

**Features of Hoisting**
- Declarations are hoisted, not initializations.
- Allows calling functions before their declarations.
- All variable and function declarations are processed before any code execution.
- Undeclared variables are implicitly created as global variables when assigned a value.

```js
// Hoisting
function codeHoist() {
    a = 10;
    let b = 50;
}
codeHoist();

console.log(a); // 10
console.log(b); // ReferenceError : b is not defined
```

```js
console.log(name); // ReferenceError: Cannot access 'name' before initialization
let name = 'Mukul Latiyan';
```

```js
fun(); // Calling before declaration

function fun() { // Declaring
  console.log("Function is hoisted");
}
```

```js
fun() // Calling the expression
// output: TypeError: fun is not a function

var fun = () =>{ // Declaring
    let name = 'Mukul Latiyan';
    console.log(name);
}
```

```js
new MyClass(); // ReferenceError: Cannot access 'MyClass' before initialization

class MyClass {}
```

> Unlike function declarations, class declarations are not [hoisted](https://developer.mozilla.org/en-US/docs/Glossary/Hoisting) (or, in some interpretations, hoisted but with the temporal dead zone restriction), which means you cannot use a class before it is declared.

### Import declarations are hoisted
Import declarations are [hoisted](https://developer.mozilla.org/en-US/docs/Glossary/Hoisting). In this case, it means that the imported values are available in the module's code even before the place that declares them, and that the imported module's side effects are produced before the rest of the module's code starts running.

```js
// …
const myCanvas = new Canvas("myCanvas", document.body, 480, 320);
myCanvas.create();
import { Canvas } from "./modules/canvas.js";
myCanvas.createReportList();
// …

```

`import`声明的提升特性:
1. import声明会被提升到模块的顶部。
2. import声明的提升是完全的,即声明和初始化都会被提升。
3. 在模块中,所有import语句都会在其他代码执行之前被解析和执行。

## Reference
JavaScript Hoisting <https://www.geeksforgeeks.org/javascript-hoisting/>

