
Review
1. 2024-03-06 23:16

## 一、Introduction
Functions are prevalent in Rust code. Rust code uses _snake case_ as the conventional style for function and variable names, in which all letters are lowercase and underscores separate words.

```rust
fn main() {
    println!("Hello, world!");
    another_function(5);
}

fn another_function(x: i32) {
    println!("Another function.{}", x);
}
```

We can define functions to have _parameters_, which are special variables that are part of a function’s signature. When a function has parameters, you can provide it with concrete values for those parameters. Technically, the ==concrete values== are called _arguments_, but in casual conversation, people tend to use the words _parameter_ and _argument_ interchangeably for either the variables in a function’s definition or the concrete values passed in when you call a function.

Rust is an expression-based language, this is an important distinction to understand.
- **Statements** are instructions that perform some action and do not return a value.
- **Expressions** evaluate to a resultant value.

The `6` in the statement `let y = 6;` is an expression that evaluates to the value `6`. Calling a function is an expression. Calling a macro is an expression. A new scope block created with curly brackets is an expression, for example:

```rust
fn main() {
    let y = {
        let x = 3;
        x + 1
    };
    println!("The value of y is: {y}");
}
```

Expressions do not include ending semicolons. If you add a semicolon to the end of an expression, you turn it into a statement, and it will then not return a value. Keep this in mind as you explore function return values and expressions next.

Functions can return values to the code that calls them. We don’t name return values, but we must declare their type after an arrow (`->`). In Rust, the return value of the function is synonymous with ==the value of the final expression== in the block of the body of a function.


## Reference
1. <https://doc.rust-lang.org/book/ch03-03-how-functions-work.html>


