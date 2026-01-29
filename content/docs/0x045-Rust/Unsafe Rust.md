
Review
1. 2025-06-14 23:00


虽然 Rust 强调安全性，但 `unsafe` 关键字允许你绕过一些编译时检查，从而执行以下操作：
- 解引用裸指针 (dereference a raw pointer)
- 调用不安全的函数或方法 (call an `unsafe` function or method)
- 访问或修改可变静态变量 (access or modify a mutable static variable)
- 实现不安全的 trait (implement an `unsafe` trait)
- 访问联合体中的字段 (access fields of a `union`)

使用 `unsafe` 意味着你需要手动保证代码的内存安全。
