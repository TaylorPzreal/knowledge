
Review
1. 2024-06-26 08:40

## 一、Introduction
 The data these collections point to is stored on the **heap**, which means the amount of data does not need to be known at compile time and can grow or shrink as the program runs.
 - A _vector_ allows you to store a variable number of values next to each other.
- A _string_ is a collection of characters. We’ve mentioned the `String` type previously, but in this chapter we’ll talk about it in depth.
- A _hash map_ allows you to associate a value with a particular key. It’s a particular implementation of the more general data structure called a _map_.

### Vectors
Vectors allow you to store more than one value in a single data structure that puts all the values next to each other in memory. Vectors can only store values of the same type. They are useful when you have a list of items, such as the lines of text in a file or the prices of items in a shopping cart.

```rust
let v: Vec<i32> = Vec::new();

// Rust conveniently provides the `vec!` macro, which will create a new vector that holds the values you give it.
let v = vec![1, 2, 3];
```

```rust
let mut v = Vec::new();

    v.push(5);
    v.push(6);
    v.push(7);
    v.push(8);
```


reference a value stored in a vector: via indexing or using the `get` method
```rust
    let v = vec![1, 2, 3, 4, 5];

    let third: &i32 = &v[2];
    println!("The third element is {third}");

    let third: Option<&i32> = v.get(2);
    match third {
        Some(third) => println!("The third element is {third}"),
        None => println!("There is no third element."),
    }
```

To access each element in a vector in turn, we would iterate through all of the elements rather than use indices to access one at a time.
```rust
    let v = vec![100, 32, 57];
    for i in &v {
        println!("{i}");
    }

```

We can also iterate over mutable references to each element in a mutable vector in order to make changes to all the elements.
```rust
    let mut v = vec![100, 32, 57];
    for i in &mut v {
        *i += 50;
    }

```

To change the value that the **mutable** reference refers to, we have to use the `*` dereference operator to get to the value in `i` before we can use the `+=` operator. We’ll talk more about the dereference operator in the [“Following the Pointer to the Value with the Dereference Operator”](https://doc.rust-lang.org/book/ch15-02-deref.html#following-the-pointer-to-the-value-with-the-dereference-operator) section of Chapter 15.


Defining an `enum` to store values of different types in one vector
```rust
    enum SpreadsheetCell {
        Int(i32),
        Float(f64),
        Text(String),
    }

    let row = vec![
        SpreadsheetCell::Int(3),
        SpreadsheetCell::Text(String::from("blue")),
        SpreadsheetCell::Float(10.12),
    ];
```


> If you don’t know the exhaustive set of types a program will get at runtime to store in a vector, the enum technique won’t work. Instead, you can use a trait object.




## Reference

