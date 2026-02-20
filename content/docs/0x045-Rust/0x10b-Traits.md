
Review
1. 2024-06-29 22:52


> Trait 定义了某些类型可以共享的功能，类似于其他语言中的接口

## 一、Introduction
> Trait是Rust中实现多态和代码重用的核心机制。它们提供了一种灵活且强大的方式来定义共享行为，同时保持了Rust的性能和安全性。通过Trait，你可以编写更加通用和可扩展的代码，同时利用Rust的类型系统来确保正确性。

A _trait_ defines functionality a particular type has and can share with other types. We can use traits to define shared behavior in an abstract way. We can use _trait bounds_ to specify that a generic type can be any type that has certain behavior.

> Note: Traits are similar to a feature often called _interfaces_ in other languages, although with some differences.

A type’s behavior consists of the methods we can call on that type. Different types share the same behavior if we can call the same methods on all of those types. Trait definitions are a way to group method signatures together to define a set of behaviors necessary to accomplish some purpose.

The `trait` def is created using the `trait` keyword followed by its name and the set of methods it includes enclosed in curly brackets.

```rust
trait Printable {
    fn print(&self);
}

struct Book {
    title: String,
    author: String,
}

impl Printable for Book {
    fn print(&self) {
        println!("{} by {}", self.title, self.author);
    }
}
```

Traits in Rust define behaviors that are shared among different data types. Implementing traits for data types is a great way to group method signatures together and define a set of behaviors your types require. Essentially, anything with a certain `trait` applied to it will “inherit” the behavior of that trait’s methods, but this is not the same thing as inheritance found in object-oriented programming languages.

Traits are abstract; it’s not possible to create instances of traits. However, we can define pointers of trait types, and these can hold any data type that implements the `trait`. A `trait` is **implemented** for something else with the syntax `impl TraitAbc for Xyz {...}`, which can be a concrete type or another trait.

### Implementing a Trait on a Type


```rust
trait Drawable {
    fn draw(&self);
}

trait Resizable {
    fn resize(&mut self, width: u32, height: u32);
}

struct Rectangle {
    width: u32,
    height: u32,
}

impl Drawable for Rectangle {
    fn draw(&self) {
        println!("Drawing a rectangle of {}x{}", self.width, self.height);
    }
}

impl Resizable for Rectangle {
    fn resize(&mut self, width: u32, height: u32) {
        self.width = width;
        self.height = height;
    }
}

struct Circle {
    radius: u32,
}

impl Drawable for Circle {
    fn draw(&self) {
        println!("Drawing a circle with radius {}", self.radius);
    }
}

fn draw_shape(shape: &impl Drawable) {
    shape.draw();
}

fn main() {
    let mut rect = Rectangle { width: 10, height: 20 };
    let circle = Circle { radius: 5 };

    draw_shape(&rect);
    draw_shape(&circle);

    rect.resize(15, 25);
    draw_shape(&rect);
}
```


## 常用 Trait 速览

| Trait | 用途 |
|-------|------|
| `Clone` | `.clone()` 显式复制；可多次调用。 |
| `Copy` | 按位复制，赋值时自动复制不 move；为 marker，依赖 `Clone`。整数、bool、char、仅含 Copy 的 tuple 等实现 Copy。 |
| `Send` | 类型可安全地传到其他线程（所有权转移）。 |
| `Sync` | `&T` 可安全在线程间共享；`T: Sync` 等价于 `&T: Send`。 |
| `Default` | `T::default()` 或 `Default::default()` 提供默认值。 |
| `From` / `Into` | 类型转换；实现 `From` 则 `Into` 自动生成。 |
| `Debug` / `Display` | 格式化输出；`{:?}` 与 `{}`，前者可派生。 |

## Trait Bounds
Trait Bounds in Rust is a way of specifying that a generic must satisfy a certain trait. Essentially, a trait bound says something like: “T must support the following behavior”. In other words, they allow you to use generic type parameters in your function definitions to specify that the function can accept any type as a parameter, as long as that type implements a certain trait. For instance, `T: Display` would constitute a trait bound, requiring the generic `T` to implement the `Display` trait.


## Reference

