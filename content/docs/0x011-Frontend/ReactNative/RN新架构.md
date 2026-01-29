
Review
1. 2024-10-13 10:02

> [!Summary]
> 2022年跟随 0.68 版本发布

## 一、Introduction

1. 新的JS引擎 - Hermes引擎，支持AOT预编译（原引擎是JSC）
2. 新的通信方式 - JSI (JavaScript Interface) ，JSI把很多底层的 C++ 接口都暴露给了 JavaScript，不用在发送消息，而是直接调用，没有序列化和反序列化。（原通信通过JS Bridge，通信方式是发送序列化消息）
3. 支持同步渲染（原来仅支持异步渲染，容易造成布局抖动）可以在原生页面中嵌套 React Native 视图，另一方面 React Native 应用也能更方便地引入一些需要同步 API 的原生组件






##### 优化方向
RN SSR

## Reference

