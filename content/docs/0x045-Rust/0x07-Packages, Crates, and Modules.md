
Review
1. 2024-06-24 23:11

## 一、Introduction
 _module system_, include:
- **Packages:** A Cargo feature that lets you build, test, and share crates
- **Crates:** A tree of modules that produces a library or executable (binary). It is the smallest unit of compilation in Rust.
- **Modules** and **use:** Let you control the organization, scope, and privacy of paths
- **Paths:** A way of naming an item, such as a struct, function, or module
- **Workspaces**: For very large projects comprising a set of interrelated packages that evolve together


## Packages and Crates
A _crate_ is the smallest amount of code that the Rust compiler considers at a time. Crates can contain modules, and the modules may be defined in other files that get compiled with the crate.

A crate can come in one of two forms: a binary crate or a library crate. _Binary crates_ are programs you can compile to an executable that you can run, such as a command-line program or a server.

A crate can come in one of two forms: a binary crate or a library crate. _Binary crates_ are programs you can compile to an executable that you can run, such as a command-line program or a server. Each must have a function called `main` that defines what happens when the executable runs.

_Library crates_ don’t have a `main` function, and they don’t compile to an executable. Instead, they define functionality intended to be shared with multiple projects.

Most of the time when Rustaceans say “crate”, they mean library crate, and they use “crate” interchangeably with the general programming concept of a “library".

A _package_ is a bundle of one or more crates that provides a set of functionality. A package contains a _Cargo.toml_ file that describes how to build those crates. Cargo is actually a package that contains the binary crate for the command-line tool you’ve been using to build your code. The Cargo package also contains a library crate that the binary crate depends on. Other projects can depend on the Cargo library crate to use the same logic the Cargo command-line tool uses.

**A package can contain as many binary crates as you like, but at most only one library crate. A package must contain at least one crate, whether that’s a library or binary crate.**

```sh
# for library
cargo new restaurant --lib

# for binary
cargo new restaurant
```

Cargo follows a convention that _src/main.rs_ is the crate root of a binary crate with the same name as the package. Likewise, Cargo knows that if the package directory contains _src/lib.rs_, the package contains a library crate with the same name as the package, and _src/lib.rs_ is its crate root. Cargo passes the crate root files to `rustc` to build the library or binary.

A package can have multiple binary crates by placing files in the _src/bin_ directory: each file will be a separate binary crate.

## Modules


Modules can also hold definitions for other items, such as structs, enums, constants, traits, and functions.

By using modules, we can group related definitions together and name why they’re related.

Filename: src/lib.rs
```rust
mod front_of_house {
    mod hosting {
        fn add_to_waitlist() {}

        fn seat_at_table() {}
    }

    mod serving {
        fn take_order() {}

        fn serve_order() {}

        fn take_payment() {}
    }
}
```

_module tree_
```txt
crate
 └── front_of_house
     ├── hosting
     │   ├── add_to_waitlist
     │   └── seat_at_table
     └── serving
         ├── take_order
         ├── serve_order
         └── take_payment
```

Notice that the entire module tree is rooted under the implicit module named `crate`.

## Paths
To show Rust where to find an item in a module tree, we use a path in the same way we use a path when navigating a filesystem.

A path can take two forms:
- An _absolute path_ is the full path starting from a **crate** root; for code from an external crate, the absolute path begins with the `crate name`, and for code from the current crate, it starts with the literal `crate`.
- A _relative path_ starts from the current module and uses `self`, `super`, or an identifier in the current module.

Both absolute and relative paths are followed by one or more identifiers separated by double colons (`::`).

In Rust, all items (functions, methods, structs, enums, modules, and constants) are private to parent modules by default. If you want to make an item like a function or struct private, you put it in a module.

Items in a parent module can’t use the private items inside child modules, but items in child modules can use the items in their ancestor modules.

Rust chose to have the module system function this way so that hiding inner implementation details is the default. That way, you know which parts of the inner code you can change without breaking outer code. However, Rust does give you the option to expose inner parts of child modules’ code to outer ancestor modules by using the `pub` keyword to make an item public.

The `pub` keyword on a module only lets code in its ancestor modules refer to it, not access its inner code. Because modules are containers, there’s not much we can do by only making the module public; we need to go further and choose to make one or more of the items within the module public as well.

> [! 最佳实践]
> Best Practices for Packages with a Binary and a Library
> 
> We mentioned a package can contain both a _src/main.rs_ binary crate root as well as a _src/lib.rs_ library crate root, and both crates will have the package name by default. Typically, packages with this pattern of containing both a library and a binary crate will have just enough code in the binary crate to start an executable that calls code within the library crate. This lets other projects benefit from most of the functionality that the package provides, because the library crate’s code can be shared.
> 
> The module tree should be defined in _src/lib.rs_. Then, any public items can be used in the binary crate by starting paths with the name of the package. The binary crate becomes a user of the library crate just like a completely external crate would use the library crate: it can only use the public API. This helps you design a good API; not only are you the author, you’re also a client!


```rust
mod back_of_house {
    pub struct Breakfast {
        pub toast: String,
        seasonal_fruit: String,
    }

    impl Breakfast {
        pub fn summer(toast: &str) -> Breakfast {
            Breakfast {
                toast: String::from(toast),
                seasonal_fruit: String::from("peaches"),
            }
        }
    }
}

pub fn eat_at_restaurant() {
    // Order a breakfast in the summer with Rye toast
    let mut meal = back_of_house::Breakfast::summer("Rye");
    // Change our mind about what bread we'd like
    meal.toast = String::from("Wheat");
    println!("I'd like {} toast please", meal.toast);
}
```


```rust
mod back_of_house {
    pub enum Appetizer {
        Soup,
        Salad,
    }
}

pub fn eat_at_restaurant() {
    let order1 = back_of_house::Appetizer::Soup;
    let order2 = back_of_house::Appetizer::Salad;
}
```


```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

use crate::front_of_house::hosting;

pub fn eat_at_restaurant() {
    hosting::add_to_waitlist();
}
```

> [!Important]
> Note that `use` only creates the shortcut for the particular scope in which the `use` occurs.

Bringing the function’s parent module into scope with `use` means we have to specify the parent module when calling the function. Specifying the parent module when calling the function makes it clear that the function isn’t locally defined while still minimizing repetition of the full path.

On the other hand, when bringing in structs, enums, and other items with `use`, it’s idiomatic to specify the full path.

Renaming one of the two `Result` types using `as`.
```rust
use std::fmt::Result;
use std::io::Result as IoResult;

fn function1() -> Result {
    // --snip--
}

fn function2() -> IoResult<()> {
    // --snip--
}
```

### Re-exporting Names with `pub use`

When we bring a name into scope with the `use` keyword, the name available in the new scope is private. To enable the code that calls our code to refer to that name as if it had been defined in that code’s scope, we can combine `pub` and `use`. This technique is called _re-exporting_ because we’re bringing an item into scope but also making that item available for others to bring into their scope.


```rust
use std::io;
use std::io::Write;
```
=>
```rust
use std::io::{self, Write};
use std::collections::*; // Be careful when using the glob operator! Glob can make it harder to tell what names are in scope and where a name used in your program was defined.
```


### Separating Modules into Different Files

`src/front_of_house.rs`
```rust
pub mod hosting {
    pub fn add_to_waitlist() {}
}
```


`src/lib.rs`
```rust
mod front_of_house;

pub use crate::front_of_house::hosting;

pub fn eat_at_restaurant() {
    hosting::add_to_waitlist();
}
```


> [!warning]
> Note that you only need to load a file using a `mod` declaration _once_ in your module tree. Once the compiler knows the file is part of the project (and knows where in the module tree the code resides because of where you’ve put the `mod` statement), other files in your project should refer to the loaded file’s code using a path to where it was declared



## Workspace
Cargo offers a feature called _workspaces_ that can help manage multiple related packages that are developed in tandem.

A _workspace_ is a set of packages that share the same _Cargo.lock_ and output directory.
Notice that the workspace has only one _Cargo.lock_ file at the top level, rather than having a _Cargo.lock_ in each crate’s directory.

Cargo doesn’t assume that crates in a workspace will depend on each other, so we need to be explicit about the dependency relationships.


top level `Cargo.toml`
```toml
[workspace]

members = [
    "adder",
    "add_one",
]
```

```txt
├── Cargo.lock
├── Cargo.toml
├── add_one
│   ├── Cargo.toml
│   └── src
│       └── lib.rs
├── adder
│   ├── Cargo.toml
│   └── src
│       └── main.rs
└── target
```


The top-level _Cargo.lock_ now contains information about the dependency of `add_one` on `rand`. However, even though `rand` is used somewhere in the workspace, we can’t use it in other crates in the workspace unless we add `rand` to their _Cargo.toml_ files as well.

If you publish the crates in the workspace to [crates.io](https://crates.io/), each crate in the workspace will need to be published separately. Like `cargo test`, we can publish a particular crate in our workspace by using the `-p` flag and specifying the name of the crate we want to publish.

## Reference

