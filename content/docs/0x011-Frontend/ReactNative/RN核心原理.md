
Review
1. 2024-10-11 21:37

> [!Summary]
> 

## 一、Introduction

React Native Skia 自绘引擎
React Native SSR 服务端渲染
React Native WishList 原生高性能列表


### 1. 核心原理
- **虚拟 DOM (Virtual DOM):**
    - React Native 借鉴了 React 的虚拟 DOM 概念，在 JavaScript 中创建了一个虚拟的 UI 树。
    - 当数据发生变化时，React Native 会重新渲染整个虚拟 DOM，然后通过 diff 算法计算出哪些部分真正发生了变化。
    - 只有发生变化的部分才会被更新到真实的原生视图上，从而提高了性能。
- **双线程模型:**
    - JavaScript 线程：负责执行 JavaScript 代码，包括 UI 逻辑和业务逻辑。
    - 主线程：负责 UI 渲染和原生模块的调用。
    - JavaScript 线程和主线程通过一个异步的桥接器 (Bridge) 进行通信。
- **桥接器 (Bridge):**
    - 桥接器是 JavaScript 线程和主线程之间的通信桥梁。
    - JavaScript 线程通过桥接器向主线程发送指令，例如创建视图、更新属性、调用原生模块等。
    - 主线程接收到指令后，执行相应的操作，并将结果返回给 JavaScript 线程。
- **原生组件:**
    - React Native 提供了一套封装好的原生 UI 组件，如 View、Text、Image 等。
    - 这些组件在 JavaScript 中使用，但实际渲染的是原生平台的组件，从而保证了应用的原生性能。


### 2. 渲染流程
1. **JavaScript 线程:**
    - 开发者使用 JavaScript 和 React 语法编写 UI 组件。
    - React Native 将这些组件渲染成一个虚拟 DOM 树。
    - 当数据发生变化时，虚拟 DOM 会重新渲染，并计算出需要更新的节点。
2. **桥接器:**
    - JavaScript 线程通过桥接器将需要更新的 UI 信息序列化，发送给主线程。
3. **主线程:**
    - 主线程接收到消息后，将序列化数据反序列化，并更新对应的原生视图。
    - 更新后的视图会立即呈现在屏幕上。


原生线程（主线程）：创建和更新原生视图
- **UIManager：** 原生线程中的 UIManager 模块负责创建、更新和销毁原生视图。
- **ShadowView：** 为了提高性能，React Native 在原生线程中维护了一棵 ShadowView 树，它与虚拟 DOM 树一一对应。
- **视图更新：** 根据从 JavaScript 线程传来的更新指令，UIManager 会更新 ShadowView 树，然后将更新同步到真实的原生视图上。

**原生渲染管线：** 更新后的原生视图会被提交给原生平台的渲染管线，最终呈现在设备屏幕上。



### 优势
- **跨平台开发:** 使用一套代码库，开发 iOS 和 Android 两个平台的应用。
- **高性能:** 虚拟 DOM 和原生组件的结合，保证了应用的流畅性。
- **热更新:** 可以直接在设备上更新 JavaScript 代码，无需重新发布应用。
- **大社区和生态:** 拥有庞大的开发者社区和丰富的第三方库。




useEffect 在RN和Web有什么区别？

## Reference

