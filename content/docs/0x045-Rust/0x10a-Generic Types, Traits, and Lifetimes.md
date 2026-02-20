
#Rust

Review
1. 2024-03-23 16:40
2. 2024-06-29 10:43

## 一、Introduction

Every reference in Rust has a _lifetime_, which is the scope for which that reference is valid. Most of the time, lifetimes are implicit and inferred, just like most of the time, types are inferred.

The main aim of lifetimes is to prevent _dangling references_, which cause a program to reference data other than the data it’s intended to reference.


```rust
struct Point<T, U> {
    x: T,
    y: U,
}

fn main() {
    let both_integer = Point { x: 5, y: 10 };
    let both_float = Point { x: 1.0, y: 4.0 };
    let integer_and_float = Point { x: 5, y: 4.0 };
}
```

```rust
enum Option<T> {
    Some(T),
    None,
}
```

```rust
enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

```rust
struct Point<T> {
    x: T,
    y: T,
}

impl<T> Point<T> {
    fn x(&self) -> &T {
        &self.x
    }
}

fn main() {
    let p = Point { x: 5, y: 10 };

    println!("p.x = {}", p.x());
}
```

```rust
impl Point<f32> {
    fn distance_from_origin(&self) -> f32 {
        (self.x.powi(2) + self.y.powi(2)).sqrt()
    }
}
```


## Summary
We covered a lot in this chapter! Now that you know about generic type parameters, traits and trait bounds, and generic lifetime parameters, you’re ready to write code without repetition that works in many different situations. **Generic type** parameters let you apply the *code* to different types. **Traits** and **trait bounds** ensure that even though the types are generic, they’ll have the behavior the code needs. You learned how to use **lifetime** annotations to ensure that this flexible code won’t have any dangling references. And all of this analysis happens at compile time, which doesn’t affect runtime performance!

```rust
let mut a = String::from("ok")
```



## Reference
https://doc.rust-lang.org/book/ch10-03-lifetime-syntax.html
