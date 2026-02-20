---
tags:
  - Rust
  - Review
---

# Rust 知识复习与校准

> 本文档用于复习知识结构、校准内容准确性、并标记待补充知识点。  
> 最后更新：2025-02

## 一、知识结构总览

当前 `0x045-Rust` 目录覆盖了 **The Rust Book** 主线 + 部分进阶与生态，结构如下。

### 1. 基础 (Fundamentals)

| 文档 | 内容概要 |
|------|----------|
| 0x01 Rust overview | 环境、Cargo、生态（CLI/GUI/后端/WASM）、国内源、文档注释 |
| 0x03a Data Types | 标量（整型/浮点/bool/char）、复合（tuple/array）、字面量 |
| 0x03b Functions | 函数定义、语句与表达式、返回值 |
| 0x03c Control Flow | `if`、`loop`/`while`/`for` |
| 0x05 Struct | 结构体定义、字段、方法、关联函数 |
| 0x06 Enums and Pattern Matching | 枚举变体、`match`、`if let`、模式 |

### 2. 所有权与类型系统 (Core)

| 文档 | 内容概要 |
|------|----------|
| 0x04 Ownership | 三规则、move、Copy、drop、函数传参 |
| 0x04 References and Borrowing | 引用、借用规则、可变/不可变、切片、data race |
| 0x10a Generic Types, Traits, and Lifetimes | 泛型 struct/enum/impl、泛型函数 |
| 0x10b Traits | trait 定义与实现、trait bounds、多态 |
| 0x10c Lifetimes | 显式生命周期注解、struct/impl、`'static`、与泛型组合 |

### 3. 工程与错误 (Project & Error)

| 文档 | 内容概要 |
|------|----------|
| 0x07 Packages, Crates, and Modules | package/crate/mod、路径、`use`、workspace |
| 0x08a Common Collections | Vec 等 |
| 0x08b String | String 与 str、UTF-8 |
| 0x08c Hash Map | HashMap |
| 0x09 Error Handling | `Result`/`Option`、`?`、`unwrap`/`expect`、`main` 返回 Result |

### 4. 进阶 (Advanced)

| 文档 | 内容概要 |
|------|----------|
| 0x11 Automated Tests | 测试（未在本次逐字审阅） |
| 0x13a Iterators and Closures | 闭包、捕获、Fn/FnMut/FnOnce、move |
| 0x13b Iterators | 惰性、iter/into_iter/iter_mut、map/filter/collect/sum |
| 0x15 Smart Pointers | Box、Deref、Drop、Rc、RefCell、内部可变性 |
| 0x16 Concurrency | 线程、JoinHandle、move、mpsc、Mutex、Arc |
| 0x10c Lifetimes | 见上 |
| Macros | 声明宏 vs 过程宏（简述） |
| Unsafe Rust | 五类 unsafe 操作列举 |

### 5. 生态与工具 (Overview 中)

- CLI：clap、structopt、termion、serde 等  
- GUI：Tauri、Iced、Dioxus、Slint、egui 等  
- 后端：Rocket、Actix、Axum、Pingora 等  
- WASM：wasm-bindgen、wasm-pack  

---

## 二、校准项（已修正与建议）

### 已修正

1. **0x01-Rust overview.md**  
   - 标题：`#Rust` → `# Rust`（格式统一）。

2. **0x10a-Generic Types, Traits, and Lifetimes.md**  
   - 示例：`String::from('ok')` → `String::from("ok")`（字符串字面量用双引号）。

### 建议注意

- **0x09 文件名**：当前为 `0x09-Error Handing.md`，应为 “Handling”。若重命名，需检查站内/站外链接。
- **structopt**：官方已进入维护模式，新项目推荐使用 **clap v4 的 derive**；Overview 中可加一句说明。
- **Concurrency 文档**：开头提到 Futures / Async/Await，但正文只讲了**标准库线程 + channel + Mutex/Arc**，没有 async/await 与 Future。建议在文档内注明“异步并发见补充或单独章节”。

---

## 三、建议补充的知识点

### 高优先级

1. **异步 Rust (Async Rust)**  
   - 当前缺失。建议补充：`Future`、`async`/`await` 语法、`Pin` 概念、常见运行时（如 Tokio）、以及 `Send`/`Sync` 在异步中的意义。  
   - 可新建 `0x17-Async Rust.md` 或类似。

2. **生命周期省略规则 (Lifetime elision)**  
   - 三条规则已写入本文「补充说明」；0x10c 文件中因含特殊 Unicode 空格未自动插入，需要时可手动粘贴到 0x10c 中「One lifetime annotation」与「The longest function」之间。  
   - **三条规则**：① 每个引用参数各自一个生命周期；② 若只有一个引用参数，其生命周期赋给所有输出；③ 若有 `&self`/`&mut self`，其生命周期赋给所有输出。

3. **常用 Trait 小结**  
   - 在 0x10b 或单独小节补充：`Clone` vs `Copy`、`Send`/`Sync`、`Default`、`From`/`Into`、`Debug`/`Display`，便于查阅和面试复习。

### 中优先级

4. **Unsafe Rust**  
   - 当前仅列举五类操作。可补充：何时使用 unsafe、典型用法（FFI、实现 unsafe trait）、“用 safe API 封装 unsafe 实现”的原则。

5. **宏 (Macros)**  
   - 补充：声明宏简单示例（如 `vec!`）、过程宏三种（derive、attribute、function-like）的用途与示例链接；可配合 Rust Book / Rust by Example。

6. **迭代器 (0x13b)**  
   - 已有 iter/into_iter/iter_mut、map/filter/collect/sum。可补充：`Iterator` trait、适配器与消费者区分、常用链式写法（如 `filter_map`、`fold`）。

### 低优先级

7. **测试 (0x11)**  
   - 若尚未展开，可补充：单元测试、`#[cfg(test)]`、集成测试目录、`assert!`/`assert_eq!`。

8. **Edition 与近期语法**  
   - 可选：2024 edition、let chains 等，在 Overview 或单独“语言版本”小节提一句即可。

---

## 四、复习检查清单（自测用）

- [ ] 能默写所有权三规则并解释 move/copy/drop。  
- [ ] 能说明借用规则及为何能避免 data race。  
- [ ] 能写出带生命周期参数的函数、struct 及 impl。  
- [ ] 能区分 `Result`/`Option` 及 `?` 的用法与限制。  
- [ ] 能区分 `Box`/`Rc`/`RefCell` 的 ownership 与借用检查时机。  
- [ ] 能写出多线程下用 channel 或 Mutex+Arc 共享状态的示例。  
- [ ] 知道闭包 Fn/FnMut/FnOnce 与捕获方式的关系。  
- [ ] 知道何时需要 `unsafe` 及五类允许的操作。  

---

## 五、参考

- [The Rust Programming Language](https://doc.rust-lang.org/stable/book/)  
- [Rust Reference](https://doc.rust-lang.org/reference/index.html)  
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/)  
