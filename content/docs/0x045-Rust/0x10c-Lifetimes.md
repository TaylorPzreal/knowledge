
Review
1. 2024-07-05 22:41

> 生命周期是 Rust 编译器用来确保所有 Borrowing 都有效的一种机制。它们指定了一个引用有效的作用域。
> 
> - **生命周期省略 (Lifetime Elision):** 很多时候，编译器可以推断出生命周期，你不需要显式地写出来。
> - **显式生命周期注解 (Explicit Lifetime Annotations):** 在某些复杂情况下，你需要手动注解生命周期，尤其是在函数签名中。例如：`fn foo<'a>(x: &'a i32, y: &'a i32) -> &'a i32`。

## 一、Introduction
Lifetimes are another kind of generic that we’ve already been using. Rather than ensuring that a type has the behavior we want, lifetimes ensure that references are valid as long as we need them to be.

**Every reference in Rust has a _lifetime_**, which is the scope for which that reference is valid. Most of the time, lifetimes are implicit and inferred, just like most of the time, types are inferred. We must only annotate types when multiple types are possible. In a similar way, we must annotate lifetimes when the lifetimes of references could be related in a few different ways. Rust requires us to annotate the relationships using generic lifetime parameters to ensure the actual references used at runtime will definitely be valid.

Lifetime annotations don’t change how long any of the references live. Rather, they describe the relationships of the lifetimes of multiple references to each other without affecting the lifetimes. Just as functions can accept any type when the signature specifies a generic type parameter, functions can accept references with any lifetime by specifying a generic lifetime parameter.

Lifetimes on function or method parameters are called _input lifetimes_, and lifetimes on return values are called _output lifetimes_.

Lifetime annotations have a slightly unusual syntax: the names of lifetime parameters must start with an apostrophe (`'`) and are usually all lowercase and very short, like generic types. Most people use the name `'a` for the first lifetime annotation. We place lifetime parameter annotations after the `&` of a reference, using a space to separate the annotation from the reference’s type.


```rust
&i32        // a reference
&'a i32     // a reference with an explicit lifetime
&'a mut i32 // a mutable reference with an explicit lifetime
```

> One lifetime annotation by itself doesn’t have much meaning, because the annotations are meant to tell Rust how generic lifetime parameters of multiple references relate to each other.


The `longest` function definition specifying that all the references in the signature must have the same lifetime `'a`
```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```


> When returning a reference from a function, the lifetime parameter for the return type needs to match the lifetime parameter for one of the parameters. 
> 
> Ultimately, lifetime syntax is about connecting the lifetimes of various parameters and return values of functions. Once they’re connected, Rust has enough information to allow memory-safe operations and disallow operations that would create dangling pointers or otherwise violate memory safety.



### Lifetime Annotations in Struct Definitions

So far, the structs we’ve defined all hold owned types. We can define structs to hold **references**, but in that case we would need to add a lifetime annotation on every reference in the struct’s definition.

```rust
struct ImportantExcerpt<'a> {
    part: &'a str,
}

fn main() {
    let novel = String::from("Call me Ishmael. Some years ago...");
    let first_sentence = novel.split('.').next().expect("Could not find a '.'");
    let i = ImportantExcerpt {
        part: first_sentence,
    };
}
```


```rust
impl<'a> ImportantExcerpt<'a> {
    fn level(&self) -> i32 {
        3
    }
    
    fn announce_and_return_part(&self, announcement: &str) -> &str {
        println!("Attention please: {announcement}");
        self.part
    }
}
```


All string literals have the `'static` lifetime, which we can annotate as follows:
```rust
let s: &'static str = "I have a static lifetime.";

```

> The text of this string is stored directly in the program’s binary, which is always available. Therefore, the lifetime of all string literals is `'static`.


```rust
use std::fmt::Display;

fn longest_with_an_announcement<'a, T>(
    x: &'a str,
    y: &'a str,
    ann: T,
) -> &'a str
where
    T: Display,
{
    println!("Announcement! {ann}");
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```



## Reference

