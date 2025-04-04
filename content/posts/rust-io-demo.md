---
title: "Rust IO Demo"
date: 2024-06-17
tags: 
 - Rust
categories: Fullstack
# bookComments: false
# bookSearchExclude: false
---

# A Rust IO Operation Demo

```rust
use colored::Colorize;
use csv::ReaderBuilder;
use csv::WriterBuilder;
use serde::Deserialize;
use serde::Serialize;
use std::error::Error;
use std::fs::File;
use std::path::Path;
use std::time::{SystemTime, UNIX_EPOCH};
use std::{env, process};

#[derive(Debug, Deserialize, Serialize)]
struct Row {
    name: String,
    age: u32,
    city: String,
}

fn file_check(args: &Vec<String>) {
    if args.len() < 2 {
        println!("{}", "请输入CSV文件路径".yellow());
        process::exit(1);
    }

    let file_path = Path::new(&args[1]);

    if file_path.exists() && file_path.is_file() {
        println!("{}", "文件存在".green());
    } else {
        println!("{}", "文件不存在，请输入正确的文件路径".red());
        process::exit(1);
    }
}

fn main() -> Result<(), Box<dyn Error>> {
    println!("{} \n", "正在处理...".green());

    let args: Vec<String> = env::args().collect();
    file_check(&args);

    // 读取 CSV 文件
    let file = File::open(&args[1])?;
    let mut reader = ReaderBuilder::new().has_headers(true).from_reader(file);
    let mut rows: Vec<Row> = reader.deserialize().collect::<Result<_, _>>()?;

    let mut rows_output_ok: Vec<Row> = vec![];
    let mut rows_output_warn: Vec<Row> = vec![];

    for row in &mut rows {
        println!("Current Row: {} {} {}", row.name, row.age, row.city);

        if row.city.len() > 5 {
            println!("超过限定 {}", row.city);
            rows_output_ok.push(Row {
                name: row.name.to_string(),
                age: row.age,
                city: row.city.to_string(),
            });
        } else {
            println!("低于限定 {}", row.city);
            rows_output_warn.push(Row {
                name: row.name.to_string(),
                age: row.age,
                city: row.city.to_string(),
            });
        }
    }

    let now = SystemTime::now();
    let duration_since_epoch = now
        .duration_since(UNIX_EPOCH)
        .expect("Failed to get duration since epoch");
    let milliseconds = duration_since_epoch.as_millis() as u64;
    let output_ok = format!("output_ok_{}.csv", milliseconds);
    let output_warn = format!("output_warn_{}.csv", milliseconds);

    // 写入新的 CSV 文件
    let mut ok_writer = WriterBuilder::new()
        .has_headers(true)
        .from_path(&output_ok)?;

    for row in &rows_output_ok {
        ok_writer.serialize(row)?;
    }

    ok_writer.flush()?;
    println!("写入文件 {} 完成", &output_ok.red());

    let mut warn_writer = WriterBuilder::new()
        .has_headers(true)
        .from_path(&output_warn)?;

    for row in &rows_output_warn {
        warn_writer.serialize(row)?;
    }

    warn_writer.flush()?;
    println!("写入文件 {} 完成", &output_warn.red());

    Ok(())
}
```
