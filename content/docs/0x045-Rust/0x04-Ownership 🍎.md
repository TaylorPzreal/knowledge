
Review
1. 2024-03-07 23:29
2. 2024-06-22 21:32

> Ownership 是 Rust 最独特和核心的特性，它让 Rust 能够在没有垃圾回收器的情况下保证内存安全。所有权有三个规则：
> 
> - **每个值都有一个所有者。** (Each value has an owner.)
> - **一次只有一个所有者。** (There can only be one owner at a time.)
> - **当所有者离开作用域时，值会被丢弃。** (When the owner goes out of scope, the value will be dropped.)
> 
> 理解所有权对于避免数据竞争和内存泄漏至关重要。
## 一、Introduction
***Ownership*** is Rust’s most unique feature and has deep implications for the rest of the language. It enables Rust to make memory safety guarantees without needing a garbage collector, so it’s important to understand how ownership works.

_Ownership_ is a set of rules that govern how a Rust program manages memory. All programs have to manage the way they use a computer’s memory while running. Memory is managed through a system of ownership with a set of rules that the compiler checks. If any of the rules are violated, the program won’t compile. None of the features of ownership will slow down your program while it’s running.

Once you understand ownership, you won’t need to think about the stack and the heap very often, but knowing that ***the main purpose of ownership is to manage heap data*** can help explain why it works the way it does.

Each value in Rust has its own designated owner and there can be *only one owner for a value at a time*. When the owner goes out of scope, the value would be automatically dropped. 

The three main facets of ownership include `ownership rules`, `borrowing` and `slices`. Ownership rules play a key role in system performance and prevention of issues like null or dangling references. `Borrowing` is a mechanism where we allow something to reference a value without taking ownership. Finally, `slices` are a data type that does not have ownership and helps in making a reference to a portion of a collection.

The ownership of a variable follows the same pattern every time: assigning a value to another variable moves it. When a variable that includes data on the heap goes out of scope, the value will be cleaned up by `drop` unless ownership of the data has been moved to another variable.

### Ownership Rules
- Each value in Rust has an _owner_.
- There can only be one owner at a time.
- When the owner goes out of scope, the value will be dropped.

Rust takes a different path: the memory is automatically returned once the variable that owns it goes out of scope.

```rust
{
    let s = String::from("hello"); // s is valid from this point forward
    // do stuff with s
}                                  
// this scope is now over, and s is no
// longer valid
```

There is a natural point at which we can return the memory our `String` needs to the allocator: when `s` goes out of scope. When a variable goes out of scope, Rust calls a special function for us. This function is called [`drop`](https://doc.rust-lang.org/std/ops/trait.Drop.html#tymethod.drop), and it’s where the author of `String` can put the code to return the memory. Rust calls `drop` automatically at the closing curly bracket.

#### `move`
```rust
let s1 = String::from("hello");
let s2 = s1;
```

the concept of copying the pointer, length, and capacity without copying the data probably sounds like making a shallow copy. But because Rust also invalidates the first variable, instead of being called a shallow copy, it’s known as a _move_. In this example, we would say that `s1` was _moved_ into `s2`.

That solves our problem! With only `s2` valid, when it goes out of scope it alone will free the memory, and we’re done.

If we _do_ want to deeply copy the heap data of the `String`, not just the stack data, we can use a common method called `clone`.

```rust
let s1 = String::from("hello");
let s2 = s1.clone();
```


#### `copy`

The reason is that types such as integers that have a known size at compile time are stored entirely on the stack, so copies of the actual values are quick to make. That means there’s no reason we would want to prevent `x` from being valid after we create the variable `y`. In other words, there’s no difference between deep and shallow copying here, so calling `clone` wouldn’t do anything different from the usual shallow copying, and we can leave it out.

As a general rule, any group of simple scalar values can implement `Copy`, and nothing that requires allocation or is some form of resource can implement `Copy`.

Here are some of the types that implement `Copy`:
- All the integer types, such as `u32`.
- The Boolean type, `bool`, with values `true` and `false`.
- All the floating-point types, such as `f64`.
- The character type, `char`.
- Tuples, if they only contain types that also implement `Copy`. For example, `(i32, i32)` implements `Copy`, but `(i32, String)` does not.

The mechanics of passing a value to a function are similar to those when assigning a value to a variable. Passing a variable to a function will move or copy, just as assignment does.

```rust
fn main() {
    let s = String::from("hello");  // s comes into scope

    takes_ownership(s);             // s's value moves into the function...
                                    // ... and so is no longer valid here

    let x = 5;                      // x comes into scope

    makes_copy(x);                  // x would move into the function,
                                    // but i32 is Copy, so it's okay to still
                                    // use x afterward

} // Here, x goes out of scope, then s. But because s's value was moved, nothing
  // special happens.

fn takes_ownership(some_string: String) { // some_string comes into scope
    println!("{}", some_string);
} // Here, some_string goes out of scope and `drop` is called. The backing
  // memory is freed.

fn makes_copy(some_integer: i32) { // some_integer comes into scope
    println!("{}", some_integer);
} // Here, some_integer goes out of scope. Nothing special happens.
```




## Reference
1. <https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html>
