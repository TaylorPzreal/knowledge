
Review
1. 2024-03-06 22:31
2. 2024-06-22 22:50

## 一、Introduction

### Scalar Types
A _scalar_ type represents a single value. Rust has four primary scalar types: **integers**, **floating-point numbers**, **Booleans**, and **characters**. 

#### Integer Types
An _integer_ is a number without a fractional component.  integer types default to `i32`.

| Length  | Signed  | Unsigned |
| ------- | ------- | -------- |
| 8-bit   | `i8`    | `u8`     |
| 16-bit  | `i16`   | `u16`    |
| 32-bit  | `i32`   | `u32`    |
| 64-bit  | `i64`   | `u64`    |
| 128-bit | `i128`  | `u128`   |
| arch    | `isize` | `usize`  |
Each signed variant can store numbers from -(2n - 1) to 2n - 1 - 1 inclusive, where _n_ is the number of bits that variant uses. So an `i8` can store numbers from -(27) to 27 - 1, which equals -128 to 127.
Unsigned variants can store numbers from 0 to 2n - 1, so a `u8` can store numbers from 0 to 28 - 1, which equals 0 to 255.


Note that number literals that can be multiple numeric types allow a type suffix, such as `57u8`, to designate the type. Number literals can also use `_` as a visual separator to make the number easier to read, such as `1_000`, which will have the same value as if you had specified `1000`.

| Number literals  | Example       |
| ---------------- | ------------- |
| Decimal          | `98_222`      |
| Hex              | `0xff`        |
| Octal            | `0o77`        |
| Binary           | `0b1111_0000` |
| Byte (`u8` only) | `b'A'`        |

#### Floating-Point Types
Rust also has two primitive types for _floating-point numbers_, which are numbers with decimal points. Rust’s floating-point types are `f32` and `f64`, which are *32 bits* and *64 bits* in size, respectively. The default type is `f64` because on modern CPUs, it’s roughly the same speed as `f32` but is capable of more precision. **All floating-point types are signed**.

Floating-point numbers are represented according to the `IEEE-754` standard. The `f32` type is a single-precision float, and `f64` has double precision.

#### The Boolean Type
As in most other programming languages, a Boolean type in Rust has two possible values: `true` and `false`. Booleans are *one byte* in size. The Boolean type in Rust is specified using `bool`.

#### The Character Type

Rust’s `char` type is the language’s most primitive alphabetic type.

Note that we specify `char` literals with **single quotes**, as opposed to `string` literals, which use **double quotes**. Rust’s `char` type is *four bytes* (`u32`) in size and represents a **Unicode Scalar Value**, which means it can represent a lot more than just ASCII.

Accented letters, Chinese/Japanese/Korean ideographs, emoji, and zero width spaces are all valid `char` Types in Rust.

### Compound Types
_Compound types_ can group multiple values into one type. Rust has two primitive compound types: **tuples** and **arrays**.

#### The Tuple Type

A _tuple_ is a general way of grouping together a number of values with a variety of types into one compound type. Tuples have a fixed length: once declared, they cannot grow or shrink in size.

We create a tuple by writing a comma-separated list of values inside parentheses. Each position in the tuple has a type, and the types of the different values in the tuple don’t have to be the same.

```rust
fn main() {
    let tup: (i32, f64, u8) = (500, 6.4, 1);
}
```

```rust
fn main() {
    let tup = (500, 6.4, 1);

	// destructuring
    let (x, y, z) = tup;

    println!("The value of y is: {y}");

	// We can also access a tuple element directly by 
	// using a period (`.`) followed by the index of the value 
	// we want to access.
	let five_hundred = tup.0;
}
```


#### The Array Type

Another way to have a collection of multiple values is with an _array_. Unlike a tuple, every element of an array must have the same type. Unlike arrays in some other languages, arrays in Rust have a fixed length.

Arrays are useful when you want your data allocated on the stack rather than the heap or when you want to ensure you always have a fixed number of elements. An array isn’t as flexible as the vector type, though. A _vector_ is a similar collection type provided by the standard library that _is_ allowed to grow or shrink in size. If you’re unsure whether to use an array or a vector, chances are you should use a vector.

However, arrays are more useful when you know the number of elements will not need to change.

You write an array’s type using square brackets with the type of each element, a semicolon, and then the number of elements in the array, like so:

```rust
let a: [i32; 5] = [1, 2, 3, 4, 5];
```

Here, `i32` is the type of each element. After the semicolon, the number `5` indicates the array contains five elements.

You can also initialize an array to contain the same value for each element by specifying the initial value, followed by a semicolon, and then the length of the array in square brackets, as shown here:
```rust
let a = [3; 5];
```

The array named `a` will contain `5` elements that will all be set to the value `3` initially.


> [!重要]
> These types are of a known size, can be stored on the ***stack*** and popped off the stack when their scope is over, and can be quickly and trivially copied to make a new, independent instance if another part of code needs to use the same value in a different scope.


## Reference
1. <https://doc.rust-lang.org/book/ch03-02-data-types.html>
