---
tags:
  - Rust
---
#Rust 

**Review**
1. 2021/09/05
2. 2024/03/02
3. 2024/06/11
4. 2025-06-14

- Rust <https://www.rust-lang.org/> 
- Rust Roadmap <https://roadmap.sh/rust>
- Rust GitHub <https://github.com/rust-lang/rust>
- Rust Development Roadmap <https://serokell.io/blog/rust-development>
- Rust by example <https://github.com/rust-lang/rust-by-example>
- The Rust Programming Language <https://doc.rust-lang.org/stable/book/>
- Rust Reference <https://doc.rust-lang.org/reference/index.html>
- Rust std <https://doc.rust-lang.org/std/index.html>
- Rust API Guidelines <https://rust-lang.github.io/api-guidelines/about.html>
- Comprehensive Rust by Google <https://github.com/google/comprehensive-rust>
- [Lerna X in Y minutes => Rust](https://learnxinyminutes.com/docs/rust/) 
- Crate Registry <https://crates.io/>
- [Into_rust()](http://intorust.com/) "Screencasts for learning Rust."
- [Rustlings](https://github.com/carols10cents/rustlings) "Small exercises to get you used to reading and writing Rust code."
- [100 exercises to learn rust](https://github.com/mainmatter/100-exercises-to-learn-rust) 
- Tour of Rust <https://tourofrust.com/> 
- The [Rust User Forum](http://users.rust-lang.org/) answers questions of all levels
- Rust REPL <https://github.com/evcxr/evcxr/blob/main/evcxr_repl/README.md>
- Rust Cargo Book <https://doc.rust-lang.org/cargo/index.html>
- [crates.io](https://crates.io/)
- [Docs.rs](https://docs.rs/)
- License List <https://spdx.org/licenses/>

## Overview
Rust is a modern system programming language focused on **performance**, **safety**, and **concurrency**. It accomplishes these goals without having a garbage collector, making it a useful language for a number of use cases other languages aren’t good at. **Its syntax is similar to C++**, but Rust offers better memory safety while maintaining high performance.

Rust is an _ahead-of-time compiled_ language, meaning you can compile a program and give the executable to someone else, and they can run it even without having Rust installed.

Rust is an expression-based language, this is an important distinction to understand.

In Rust, memory safety is accomplished through a system of **ownership** with a set of rules that the compiler checks at compile time.

**Important features**
1. Ownership & Reference
2. Lifetime
3. Traits
4. Macro

## 一、Environment Setup
**Tools**
1. Cargo：Cargo is Rust’s build system and package manager.
2. rustup：是Rust的安装和工具链管理工具，使用rustup安装Rust；
3. wasm-bindgen: 提供了JS和Rust类型之间的桥梁，它允许JS使用字符串调用Rust API，或者使用Rust函数来捕获JS异常。wasm-bindgen 的核心是促进 javascript 和 Rust 之间使用 wasm 进行通信。它允许开发者直接使用 Rust 的结构体、javascript的类、字符串等类型，而不仅仅是 wasm 支持的整数或浮点数类型。
4. wsm-pack: wasm-pack 由 Rust / Wasm 工作组开发维护，是现在最为活跃的 WebAssembly 应用开发工具。wasm-pack 支持将代码打包成 npm 模块，并且附带 Webpack 插件（wasm-pack-plugin），借助它，我们可以轻松的将 Rust 与已有的 JavaScript 应用结合。
5. wasm32-unknown-unknown: 通过 rustup 的 target 命令可以指定编译的目标平台，也就是编译后的程序在哪种操作系统上运行。wasm-pack 使用 wasm32-unknown-unknown 目标编译代码。


```sh
# install rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# update installed Rustup
rustup update

# Rust local doc
rustup doc

rustup --version

cargo --version

rustc --version
```


**Cargo配置国内源**
https://rsproxy.cn/
步骤1：设置 Rustup 镜像， 修改配置 `~/.zshrc` or `~/.bashrc`
```
export RUSTUP_DIST_SERVER="https://rsproxy.cn"
export RUSTUP_UPDATE_ROOT="https://rsproxy.cn/rustup"
```

步骤2：设置 crates.io 镜像， 修改配置 `~/.cargo/config`，已支持git协议和sparse协议，>=1.68 版本建议使用 ==sparse-index==，速度更快。
```
[source.crates-io]
replace-with = 'rsproxy-sparse'
[source.rsproxy]
registry = "https://rsproxy.cn/crates.io-index"
[source.rsproxy-sparse]
registry = "sparse+https://rsproxy.cn/index/"
[registries.rsproxy]
index = "https://rsproxy.cn/crates.io-index"
[net]
git-fetch-with-cli = true
```


`cargo` account is Github
```sh
cargo login
```

## 二、Development
```sh
# create new project
cargo new project_name

cargo new --lib project_name // for Rust lib project

# add new deps
cargo add ferris-says

# build your project
cargo build # for test, -> target/debug/**
cargo build --release  # for production, -> target/release/**

# 检测: build a project without producing a binary to check for errors
cargo check

# build and run your project in one step
cargo run

# test your project
cargo test

# publish a library to [crates.io](http://crates.io)
cargo publish

# deprecating versions from crates.io
cargo yank --vers 1.0.1

# undo a yank and allow projects to start depending on a version again:
cargo yank --vers 1.0.1 --undo

# build documentation for your project
cargo doc

# build documentation provided by all your dependencies locally and open it in your browser.
cargo doc --open
```

编译
```sh
rustc --version

# 编译生成二进制文件
rustc -o output_filename input_filename.rs

# 执行二进制文件
./output_filename

# 编译生成库文件
rustc --crate-type lib input_filename.rs
```

_Documentation comment_, that will generate HTML documentation. The HTML displays the contents of documentation comments for public API items intended for programmers interested in knowing how to _use_ your crate as opposed to how your crate is _implemented_.

Documentation comments use three slashes, `///`, instead of two and support Markdown notation for formatting the text. Place documentation comments just before the item they’re documenting.

```rust
/// Adds one to the number given.
///
/// # Examples
///
/// ```
/// let arg = 5;
/// let answer = my_crate::add_one(arg);
///
/// assert_eq!(6, answer);
/// ```
pub fn add_one(x: i32) -> i32 {
    x + 1
}
```

The `cargo install` command allows you to install and use binary crates locally. This isn’t intended to replace system packages; it’s meant to be a convenient way for Rust developers to install tools that others have shared on [crates.io](https://crates.io/).
All binaries installed with `cargo install` are stored in the installation root’s _bin_ folder(_$HOME/.cargo/bin_).

```sh
cargo install ripgrep
```

Cargo is designed so you can extend it with new subcommands without having to modify Cargo. If a binary in your `$PATH` is named `cargo-something`, you can run it as if it was a Cargo subcommand by running `cargo something`. Custom commands like this are also listed when you run `cargo --list`.

IDEs
1. VSCode
2. RustRover
3. Zed
4. Cursor

## 三、CLI 开发
```sh
cargo new projectName
```

[clap](https://github.com/clap-rs/clap) 
`clap` is a command line argument parser for Rust. It is used for managing and parsing command line arguments and subcommands for your application. `clap` allows you to set the name, version, author, about info, and other global settings of your application.

[structopt](https://github.com/TeXitoi/structopt) 
`StructOpt` is a third-party library in Rust designed to parse command-line arguments by defining a struct. It brings together the capabilities of `clap` for command-line parsing with Rust’s powerful type system. With `StructOpt`, you can define a struct for your command-line program where each field represents a flag, switch, option, or positional argument. This allows a highly declarative and expressive means of handling command-line inputs, including automatic help message generation, strongly-typed values, default values, validators, and more.

[Termion](https://github.com/redox-os/termion) 
`Termion` is a pure Rust, bindless library for low-level handling, manipulating and reading information about terminals. This provides a full-featured solution for cross-terminal compatibility, allowing for features such as color support, input handling, and other terminal specific features.

[arguments](https://crates.io/crates/arguments)
The package provides a parser for command-line arguments.

[args](https://crates.io/crates/args)
A dead simple implementation of command line argument parsing and validation built on top of the [getopts](https://crates.io/crates/getopts) crate.

[colorous](https://crates.io/crates/colorous)
Professional color schemes ported from d3-scale-chromatic.

[serde](https://crates.io/crates/serde)
A generic serialization/deserialization framework


## 四、GUI开发
“GUI Dev” or Graphical User Interface Development is a significant aspect of software development which focuses on creating visually engaging and intuitive user interfaces.

1. **Tauri** <https://github.com/tauri-apps/tauri> Build smaller, faster, and more secure desktop applications with a web frontend.
2. **Iced** <https://github.com/iced-rs/iced> A cross-platform GUI library for Rust focused on simplicity and type-safety. Inspired by [Elm](https://elm-lang.org/).
3. Dioxus <https://github.com/dioxuslabs/dioxus>
4. **Druid** <https://github.com/linebender/druid> A data-first Rust-native UI design toolkit. Similar to **React**.
5. conrod
6. relm/gtk-rs/gtk+3/[gtk4-rs](https://github.com/gtk-rs/gtk4-rs) 
7. Xilem <https://github.com/linebender/xilem>
8. Slint <https://github.com/slint-ui/slint> 
9. egui
10. azul <https://github.com/fschutt/azul> 
11. GPUI https://www.gpui.rs/

GPUI 生态
1. GPUI Component https://github.com/longbridge/gpui-component?tab=readme-ov-file
2. Wry (Cross-platform WebView library in Rust for Tauri.) https://github.com/tauri-apps/wry



## 五、Backend Development
Frameworks
1. **Rocket** <https://github.com/rwf2/Rocket> 
2. **Actix Web** <https://github.com/actix/actix-web> 
3. Axum <https://github.com/tokio-rs/axum> 
4. Warp <https://github.com/seanmonstar/warp> 
5. **yew** <https://github.com/yewstack/yew> Rust / Wasm framework for creating reliable and efficient web applications
6. gotham
7. Leptos
8. Salvo
9. ntex
10. loco
11. Tide
12. Tuono <https://github.com/tuono-labs/tuono> Tuono is a full-stack web framework for building React applications using Rust as the backend with a strong focus on usability and performance.

**Pingora (Cloudflare开源)**
https://github.com/cloudflare/pingora
- **定位**：替代Nginx的代理框架，专注安全与高性能3。
- **优势**：
	- 日均处理万亿级请求，资源消耗仅为传统方案1/3
	- 支持HTTP/1-2、gRPC、TLS，兼容OpenSSL/BoringSSL（后量子加密）
	- 提供可编程过滤器（如负载均衡、请求重写），API类似OpenResty
- **适用场景**：网关、CDN、负载均衡器

## 六、WebAssembly
“Wasm” or WebAssembly is an open standard binary instruction format. It serves as a compact binary format that aims to execute at near-native speed, providing a performance-efficient compilation target for low-level languages like C, C++, and Rust. Wasm was initially developed for efficient execution in web browsers but is designed to be used in other environments as well. WebAssembly aims to maintain a safe, secure, and platform-independent runtime to perform high-performance applications on the web or on other platforms.

1. wasm-bindgen
2. wasm-pack <https://github.com/rustwasm/wasm-pack>
3. wasmer
4. xtask-wasm <https://github.com/rustminded/xtask-wasm/> 

## Awesome Librarys

1. reqwest
2. Hyper <https://hyper.rs/>


## 参考
1. rustup: <https://rustup.rs/>
2. Rust <https://www.rust-lang.org/>
3. 使用Rust编写更快的React组件: <https://mp.weixin.qq.com/s/6hWLFAN3xa9xjHeYF31y1g>
4. 编程语言新宠Rust不完全入门指南: <https://mp.weixin.qq.com/s/pY0OWjGLZWU3du45XRJbdA>
5. Rust Development Roadmap <https://serokell.io/blog/rust-development>
6. 2023 Annual Rust Survey Results <https://blog.rust-lang.org/2024/02/19/2023-Rust-Annual-Survey-2023-results.html>
7. crustaceans <https://rustacean.net/>
