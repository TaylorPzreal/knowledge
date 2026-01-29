

Review
1. 2024-07-17 07:38

## 一、Introduction
Macros in Rust are a way to define reusable chunks of code. They’re similar to functions in that they can accept input and produce output, but macros have a few key differences and advantages. With macros, you can write code that writes other code, which is known as metaprogramming. In comparison to functions, macros are more flexible and can accept a variety of different inputs. Macros are defined using the `macro_rules!` keyword and they use a different syntax than regular Rust functions. When you define a macro, you specify the code that should be inserted at compile time. The compiler then replaces all calls to the macro with the expanded macro code.


- **声明宏 (Declarative Macros - `macro_rules!`)**: 最常见的宏类型，基于模式匹配。
- **过程宏 (Procedural Macros):** 更高级，用于派生宏、属性宏和函数式宏。

## Reference

