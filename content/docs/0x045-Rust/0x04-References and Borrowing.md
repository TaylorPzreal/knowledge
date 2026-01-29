
Review
1. 2024-03-09 08:44
2. 2024-06-23 09:00

> 当你不想转移所有权，但又需要访问数据时，可以使用借用。借用允许你引用（reference）数据而不拥有它。
> 
> - **不可变引用 (Immutable References):** 你可以有多个不可变引用同时存在，它们只允许读取数据。
> - **可变引用 (Mutable References):** 在任何给定时间，你只能有一个可变引用。它允许修改数据。
> 
> **借用规则：**
> 
> - **在任何给定时间，你要么拥有一个可变引用，要么拥有任意数量的不可变引用。** (At any given time, you can either have one mutable reference or any number of immutable references.)
> - **引用总是有效的。** (References must always be valid.)
> 
> 这个规则防止了数据竞争（Data Races）。

## 一、Introduction
A _reference_ is like a ***pointer*** in that it’s an address we can follow to access the data stored at that address; that data is owned by some other variable. **Unlike a pointer, a reference is guaranteed to point to a valid value of a particular type for the life of that reference.**

![](./assets/c0dd476fb2fa_dab9804e.svg)

```rust
fn main() {
    let s1 = String::from("hello");

    let len = calculate_length(&s1);

    println!("The length of '{}' is {}.", s1, len);
}

fn calculate_length(s: &String) -> usize {
    s.len()
}
```

> [!Dereferencing]
> 注意：与使用 `&` 进行引用，相反的是取消引用，它是通过取消引用操作符 `*` 来实现的。


The `&s1` syntax lets us create a reference that _refers_ to the value of `s1` but does not own it. Because it does not own it, the value it points to will not be dropped when the reference stops being used.

Likewise, the signature of the function uses `&` to indicate that the type of the parameter `s` is a reference.

We call the action of creating a reference ==_borrowing_==. As in real life, if a person owns something, you can borrow it from them. When you’re done, you have to give it back. You don’t own it.

In Rust, “***borrowing***” is a technique which allows you to access the data of a particular value while the owner retains control. There are two types of borrowing: **mutable** and **immutable**. Immutable borrowing means an owner can fondly permit several read-only borrows of a value at the same time as long as the value doesn’t change. On the other hand, mutable borrowing allows only a single borrower at a time who can potentially modify the value. This practice is essential in maintaining the concept of ownership without violating any of its rules and avoiding the problem of dangling references.

A mutable reference

```rust
fn main() {
    let mut s = String::from("hello");
    change(&mut s);
}

fn change(some_string: &mut String) {
    some_string.push_str(", world");
}
```

Mutable references have one big **restriction**: ==if you have a mutable reference to a value, you can have no other references to that value==. This code that attempts to create two mutable references to `s` will fail:
```rust
    let mut s = String::from("hello");

    let r1 = &mut s;
    let r2 = &mut s;

    println!("{}, {}", r1, r2);

```

The benefit of having this restriction is that Rust can prevent data races at compile time. A ***data race*** is similar to a race condition and happens when these three behaviors occur:
- Two or more pointers access the same data at the same time.
- At least one of the pointers is being used to write to the data.
- There’s no mechanism being used to synchronize access to the data.

Data races cause undefined behavior and can be difficult to diagnose and fix when you’re trying to track them down at runtime; Rust prevents this problem by refusing to compile code with data races!

Whew! ==We also cannot have a mutable reference while we have an immutable one to the same value==.

Note that a reference’s scope starts from where it is introduced and continues through the last time that reference is used. For instance, this code will compile because the last usage of the immutable references, the `println!`, occurs before the mutable reference is introduced:

```rust
let mut s = String::from("hello");

let r1 = &s; // no problem
let r2 = &s; // no problem
println!("{} and {}", r1, r2);
    // variables r1 and r2 will not be used after this point

let r3 = &mut s; // no problem
println!("{}", r3);
```

The scopes of the immutable references `r1` and `r2` end after the `println!` where they are last used, which is before the mutable reference `r3` is created. These scopes don’t overlap, so this code is allowed: the compiler can tell that the reference is no longer being used at a point before the end of the scope.


Let’s recap what we’ve discussed about references:
- At any given time, you can have _either_ one mutable reference _or_ any number of immutable references.
- References must always be valid.

### String Slices
_Slices_ let you reference a contiguous sequence of elements in a [collection](https://doc.rust-lang.org/book/ch08-00-common-collections.html) rather than the whole collection. A **slice** is a kind of **reference**, so it does not have ownership.

A _string slice_ is a reference to part of a `String`, and it looks like this:
```rust
let s = String::from("hello world");

let hello = &s[0..5];
let world = &s[6..11];
```

Rather than a reference to the entire `String`, `hello` is a reference to a portion of the `String`, specified in the extra `[0..5]` bit. We create slices using a range within brackets by specifying `[starting_index..ending_index]`, where `starting_index` is the first position in the slice and `ending_index` is one more than the last position in the slice. Internally, the slice data structure stores the starting position and the length of the slice, which corresponds to `ending_index` minus `starting_index`. So, in the case of `let world = &s[6..11];`, `world` would be a slice that contains a pointer to the byte at index 6 of `s` with a length value of `5`.

![](./assets/f102ea48c13c_5757a8ce.svg)
> Note: String slice range indices must occur at valid UTF-8 character boundaries. If you attempt to create a string slice in the middle of a multibyte character, your program will exit with an error. For the purposes of introducing string slices, we are assuming ASCII only in this section; a more thorough discussion of UTF-8 handling is in the [“Storing UTF-8 Encoded Text with Strings”](https://doc.rust-lang.org/book/ch08-02-strings.html#storing-utf-8-encoded-text-with-strings) section of Chapter 8.



## Reference
1. <https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html>
