---
tags:
  - Rust
  - Async
  - Concurrency
---

# Async Rust

Review: 2025-02

## 一、与「线程并发」的区别

- **0x16 Concurrency** 讲的是 **std::thread**：多线程 + channel + Mutex/Arc，适合 CPU 密集或少量 OS 线程。
- **Async Rust** 是 **协作式多任务**：在少量 OS 线程上跑大量异步任务，适合 I/O 密集（网络、文件、定时器）。不替代线程，而是另一种并发模型。

## 二、核心概念

- **Future**：表示“将来会产出某个值”的 trait。异步函数返回 `impl Future`，需要被 **poll** 才会推进。
- **async / await**：`async fn` 返回一个 Future；`.await` 在 Future 上等待完成而不阻塞线程。
- **Executor / Runtime**：负责 poll 多个 Future、在 I/O 就绪时唤醒。Rust 标准库**只提供** Future trait，**不提供**运行时；常用 [Tokio](https://tokio.rs/)、[async-std](https://async.rs/)。
- **Pin**：保证 Future 在内存中不移动，以便自引用结构能安全存在。多数写业务代码时由 `async fn`/`async move` 自动处理。

## 三、简单示例

```rust
use std::time::Duration;

// 需要运行时，例如 tokio
// #[tokio::main]
// async fn main() {
//     let out = fetch_and_print().await;
// }

async fn fetch_and_print() -> String {
    tokio::time::sleep(Duration::from_secs(1)).await;
    "done".to_string()
}
```

## 四、Send 与 Sync 在异步中的意义

- 若 Future 需要跨 await 点被其他任务在不同线程里 poll，则该 Future 必须实现 **Send**。
- 在 `async` 块或 `async fn` 里持有的数据若跨 `.await`，通常也需要是 `Send`（取决于运行时是否多线程）。
- **Sync**：若 `&T` 能安全跨线程共享，则 `T: Sync`。多线程运行时里共享状态常用 `Arc<Mutex<T>>` 等，其要求内部 `T` 满足 `Send`（有时还有 `Sync`）。

## 五、学习与参考

- [Asynchronous Programming in Rust](https://rust-lang.github.io/async-book/)（官方 async book）
- [Tokio Tutorial](https://tokio.rs/tokio/tutorial)
- [Rust Book 多线程章节](https://doc.rust-lang.org/book/ch16-00-concurrency.html) 与 本目录 **0x16-Concurrency.md** 对应「线程 + channel + Mutex」

## Reference

1. <https://rust-lang.github.io/async-book/>
2. <https://tokio.rs/>
