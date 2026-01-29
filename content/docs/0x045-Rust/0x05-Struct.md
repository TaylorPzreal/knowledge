
Review
1. 2024-03-10 07:48
2. 2024-06-23 13:42

> 结构体是自定义数据类型的方式，可以将多个相关数据组合在一起。

## 一、Introduction
A _struct_, or _structure_, is a custom data type that lets you package together and name multiple related values that make up a meaningful group. If you’re familiar with an object-oriented language, a _struct_ is like an object’s data attributes.

There are three types of `struct` in Rust: classic ‘C’ structs, tuple structs, and unit structs.
- **Classic ‘C’ structs** are named-field structs and are the most commonly used.
- **Tuple structs**, while not being common, are useful when you want to couple together just a few data points that don’t need field names.
- **Unit structs** are useful in situations where you want to implement a **trait** on some type, but don’t have any data that you want to store in the type itself.

 In Rust, all items (functions, methods, structs, enums, modules, and constants) are private to parent modules by default. If you want to make an item like a function or struct private, you put it in a module.

Items in a parent module can’t use the private items inside child modules, but items in child modules can use the items in their ancestor modules. This is because child modules wrap and hide their implementation details, but the child modules can see the context in which they’re defined.

```rust
struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}


fn main() {
    let mut user1 = User {
        active: true,
        username: String::from("someusername123"),
        email: String::from("someone@example.com"),
        sign_in_count: 1,
    };
	
	user1.email = String::from("anotheremail@example.com");
	
	let user2 = User {
		email: String::from("another@example.com"),
		..user1
	};
}

fn build_user(email: String, username: String) -> User {
    User {
        active: true,
        username,
        email,
        sign_in_count: 1,
    }
}
```

Note that the entire instance must be mutable; Rust doesn’t allow us to mark only certain fields as mutable.

The `..user1` must come last to specify that any remaining fields should get their values from the corresponding fields in `user1`, but we can choose to specify values for as many fields as we want in any order, regardless of the order of the fields in the struct’s definition.


### Tuple structs
Rust also supports structs that look similar to tuples, called _**tuple structs**_. Tuple structs have the added meaning the struct name provides but don’t have names associated with their fields; rather, they just have the types of the fields. **Tuple structs are useful when you want to give the whole tuple a name and make the tuple a different type from other tuples**, and when naming each field as in a regular struct would be verbose or redundant.

```rust
struct Color(i32, i32, i32);
struct Point(i32, i32, i32);

fn main() {
    let black = Color(0, 0, 0);
    let origin = Point(0, 0, 0);
}
```

Note that the `black` and `origin` values are different types because they’re instances of different tuple structs. Each struct you define is its own type, even though the fields within the struct might have the same types.

Otherwise, tuple struct instances are similar to tuples in that you can destructure them into their individual pieces, and you can use a `.` followed by the index to access an individual value.

An example
```rust
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!(
        "The area of the rectangle is {} square pixels.",
        area(&rect1)
    );
}

fn area(rectangle: &Rectangle) -> u32 {
    rectangle.width * rectangle.height
}
```


#### Unit-Like Structs Without Any Fields
You can also define structs that don’t have any fields! These are called _unit-like structs_ because they behave similarly to `()`, the unit type that we mentioned in [“The Tuple Type”](https://doc.rust-lang.org/book/ch03-02-data-types.html#the-tuple-type) section. **Unit-like structs can be useful when you need to implement a trait on some type but don’t have any data that you want to store in the type itself.** Here’s an example of declaring and instantiating a unit struct named `AlwaysEqual`:

```rust
struct AlwaysEqual;

fn main() {
    let subject = AlwaysEqual;
}
```

To define `AlwaysEqual`, we use the `struct` keyword, the name we want, and then a semicolon. No need for curly brackets or parentheses! Then we can get an instance of `AlwaysEqual` in the `subject` variable in a similar way: using the name we defined, without any curly brackets or parentheses.

### Method Syntax
> 可以在 `impl` 块中为结构体定义关联函数和方法。

_Methods_ are similar to functions: we declare them with the `fn` keyword and a name, they can have parameters and a return value, and they contain some code that’s run when the method is called from somewhere else. Unlike functions, methods are defined within the context of a struct (or an enum or a trait object, which we cover in [Chapter 6](https://doc.rust-lang.org/book/ch06-00-enums.html) and [Chapter 17](https://doc.rust-lang.org/book/ch17-02-trait-objects.html), respectively), and their first parameter is always `self`, which represents the instance of the struct the method is being called on.

The `&self` is actually short for `self: &Self`. Within an `impl` block, the type `Self` is an alias for the type that the `impl` block is for. Methods must have a parameter named `self` of type `Self` for their first parameter, so Rust lets you abbreviate this with only the name `self` in the first parameter spot. Note that we still need to use the `&` in front of the `self` shorthand to indicate that this method borrows the `Self` instance, just as we did in `rectangle: &Rectangle`.

If we wanted to change the instance that we’ve called the method on as part of what the method does, we’d use `&mut self` as the first parameter.

> Note that we can choose to give a method the same name as one of the struct’s fields.

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }

    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}


fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!(
        "The area of the rectangle is {} square pixels.",
        rect1.area()
    );
}
```

> _automatic referencing and dereferencing_
> when you call a method with `object.something()`, Rust automatically adds in `&`, `&mut`, or `*` so `object` matches the signature of the method. In other words, the following are the same:

```rust
p1.distance(&p2);
(&p1).distance(&p2);
```


### Associated Functions
All functions defined within an `impl` block are called _associated functions_ because they’re associated with the type named after the `impl`. We can define associated functions that don’t have `self` as their first parameter (and thus are not methods) because they don’t need an instance of the type to work with. We’ve already used one function like this: the `String::from` function that’s defined on the `String` type.

Associated functions that aren’t methods are often used for constructors that will return a new instance of the struct. These are often called `new`, but `new` isn’t a special name and isn’t built into the language.


```rust
impl Rectangle {
    fn square(size: u32) -> Self {
        Self {
            width: size,
            height: size,
        }
    }
}


fn main() {
	let sq = Rectangle::square(3);
}
```



## Reference
1. <https://doc.rust-lang.org/book/ch05-03-method-syntax.html>

