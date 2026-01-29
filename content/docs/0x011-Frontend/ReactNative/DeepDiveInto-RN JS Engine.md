

Review
1. 2024-10-02 10:00

> [!Summary]
> 1. [Hermes](https://github.com/facebook/hermes) Hermes is the default engine as of React Native 0.70.
> 2. JavaScriptCore(JSC) 早期默认JS引擎

## 一、Introduction
Hermes是Facebook专门为React Native优化的一款轻量级、高性能的JavaScript引擎


##### JSC vs Hermes
JavaScriptCore采用JIT（即时编译）方案。在初始化时，JSC 引擎需要把整个 JavaScript 代码都编译和执行一次。

Hermes 引擎是在本地先将 JavaScript 编译为*字节码*，然后再下发字节码。Hermes 引擎下发的字节码的体积和 JSC 引擎下发的 JavaScript 代码是一样大的，但 Hermes 引擎执行字节码的首屏性能，却是 JSC 引擎执行 JavaScript 首屏性能的 2 倍以上。



##### 为什么选择Hermes？
- **性能提升：** Hermes在启动速度、内存占用和执行效率方面都比JavaScriptCore有显著的提升。
- **更小的包体积:** Hermes 的二进制文件更小，可以减少应用的安装包大小。
- **更好的垃圾回收:** Hermes 的垃圾回收机制更加高效，可以减少内存抖动。
- **为React Native量身定制:** Hermes在设计之初就考虑到了React Native的特性，可以更好地与React Native框架配合。
- **更好的热更新支持：** Hermes对热更新的支持更加友好，可以更快地加载和应用热更新代码。
- 支持AOT



Hermes 引擎提供的 enablePromiseReje...  捕获全局 Promise 错误。




## Reference
[Using Hermes](https://reactnative.dev/docs/hermes) 


