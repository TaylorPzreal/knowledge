
Review
1. 2024-07-09 06:47

## 一、Introduction

1. `assert`
2. `assert_eq`
3. `assert_ne`
4. `should_panic`


```rust
pub fn add(left: usize, right: usize) -> usize {
    left + right
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = add(2, 2);
        assert_eq!(result, 4);
    }
}
```

> For now, let’s focus solely on the `it_works()` function. Note the `#[test]` annotation: this attribute indicates this is a test function, so the test runner knows to treat this function as a test. We might also have non-test functions in the `tests` module to help set up common scenarios or perform common operations, so we always need to indicate which functions are tests.


A common way to verify functionality is to test for equality between the result of the code under test and the value you expect the code to return. You could do this using the `assert!` macro and passing it an expression using the `==` operator. However, this is such a common test that the standard library provides a pair of macros—`assert_eq!` and `assert_ne!`—to perform this test more conveniently. These macros compare two arguments for equality or inequality, respectively. They’ll also print the two values if the assertion fails, which makes it easier to see _why_ the test failed; conversely, the `assert!` macro only indicates that it got a `false` value for the `==` expression, without printing the values that led to the `false` value.


Under the surface, the `assert_eq!` and `assert_ne!` macros use the operators `==` and `!=`, respectively. When the assertions fail, these macros print their arguments using debug formatting, which means the values being compared must implement the `PartialEq` and `Debug` traits. All primitive types and most of the standard library types implement these traits. For structs and enums that you define yourself, you’ll need to implement `PartialEq` to assert equality of those types. You’ll also need to implement `Debug` to print the values when the assertion fails. Because both traits are derivable traits, as mentioned in Listing 5-12 in Chapter 5, this is usually as straightforward as adding the `#[derive(PartialEq, Debug)]` annotation to your struct or enum definition. See Appendix C, [“Derivable Traits,”](https://doc.rust-lang.org/book/appendix-03-derivable-traits.html) for more details about these and other derivable traits.


### Adding Custom Failure Messages
```rust
    #[test]
    fn greeting_contains_name() {
        let result = greeting("Carol");
        assert!(
            result.contains("Carol"),
            "Greeting did not contain name, value was `{}`",
            result
        );
    }

```


We do this by adding the attribute `should_panic` to our test function. The test passes if the code inside the function panics; the test fails if the code inside the function doesn’t panic.

```rust
pub struct Guess {
    value: i32,
}

impl Guess {
    pub fn new(value: i32) -> Guess {
        if value < 1 || value > 100 {
            panic!("Guess value must be between 1 and 100, got {value}.");
        }

        Guess { value }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    #[should_panic]
    fn greater_than_100() {
        Guess::new(200);
    }
}
```

We place the `#[should_panic]` attribute after the `#[test]` attribute and before the test function it applies to.

Tests that use `should_panic` can be imprecise. A `should_panic` test would pass even if the test panics for a different reason from the one we were expecting. To make `should_panic` tests more precise, we can add an optional `expected` parameter to the `should_panic` attribute. The test harness will make sure that the failure message contains the provided text.

```rust
// --snip--

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    #[should_panic(expected = "less than or equal to 100")]
    fn greater_than_100() {
        Guess::new(200);
    }
}
```


```rust
#[cfg(test)]
mod tests {
    #[test]
    fn it_works() -> Result<(), String> {
        if 2 + 2 == 4 {
            Ok(())
        } else {
            Err(String::from("two plus two does not equal four"))
        }
    }
}
```


 _Unit tests_ are small and more focused, testing one module in isolation at a time, and can test private interfaces. 
 _Integration tests_ are entirely external to your library and use your code in the same way any other external code would, using only the public interface and potentially exercising multiple modules per test.

The `#[cfg(test)]` annotation on the tests module tells Rust to compile and run the test code only when you run `cargo test`, not when you run `cargo build`.

The attribute `cfg` stands for _configuration_ and tells Rust that the following item should only be included given a certain configuration option. In this case, the configuration option is `test`, which is provided by Rust for compiling and running tests.

Regardless of which testing ideology you adhere to, Rust’s privacy rules do allow you to test private functions.
```rust
pub fn add_two(a: i32) -> i32 {
    internal_adder(a, 2)
}

fn internal_adder(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn internal() {
        assert_eq!(4, internal_adder(2, 2));
    }
}
```


Their purpose is to test whether many parts of your library work together correctly. Units of code that work correctly on their own could have problems when integrated, so test coverage of the integrated code is important as well. To create integration tests, you first need a _tests_ directory.

```txt
adder
├── Cargo.lock
├── Cargo.toml
├── src
│   └── lib.rs
└── tests
    └── integration_test.rs

```

Filename: `tests/integration_test.rs`
```rust
use adder::add_two;

#[test]
fn it_adds_two() {
    assert_eq!(4, add_two(2));
}
```


Cargo treats the `tests` directory specially and compiles files in this directory only when we run `cargo test`.

To run all the tests in a particular integration test file, use the `--test` argument of `cargo test` followed by the name of the file:
```sh
cargo test --test integration_test
```

To avoid having `common` appear in the test output, instead of creating _tests/common.rs_, we’ll create _tests/common/mod.rs_. The project directory now looks like this:
```txt
├── Cargo.lock
├── Cargo.toml
├── src
│   └── lib.rs
└── tests
    ├── common
    │   └── mod.rs
    └── integration_test.rs

```

This is the older naming convention that Rust also understands. Naming the file this way tells Rust not to treat the `common` module as an integration test file. Files in subdirectories of the _tests_ directory don’t get compiled as separate crates or have sections in the test output.

Filename: tests/integration_test.rs
```rust
use adder;

mod common;

#[test]
fn it_adds_two() {
    common::setup();
    assert_eq!(4, adder::add_two(2));
}
```

> If our project is a binary crate that only contains a _src/main.rs_ file and doesn’t have a _src/lib.rs_ file, we can’t create integration tests in the _tests_ directory and bring functions defined in the _src/main.rs_ file into scope with a `use` statement. Only library crates expose functions that other crates can use; binary crates are meant to be run on their own.

This is one of the reasons Rust projects that provide a binary have a straightforward _src/main.rs_ file that calls logic that lives in the _src/lib.rs_ file. Using that structure, integration tests _can_ test the library crate with `use` to make the important functionality available. If the important functionality works, the small amount of code in the _src/main.rs_ file will work as well, and that small amount of code doesn’t need to be tested.

## Reference

