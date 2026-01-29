
## 简介


## 特点
1. 程序逻辑与用户界面解耦
2. 为复杂应用设计
3. 开放的扩展能力点

## 设计思想
Stage模型之所以成为主推模型，源于其设计思想。Stage模型的设计基于如下出发点。
1. **为复杂应用而设计**
	- ==多个应用组件共享同一个ArkTS引擎（运行ArkTS语言的虚拟机）实例==，应用组件之间可以方便的共享对象和状态，同时减少复杂应用运行对内存的占用。
	- 采用面向对象的开发方式，使得复杂应用代码可读性高、易维护性好、可扩展性强。
2. **支持多设备和多窗口形态**
	应用组件管理和窗口管理在架构层面解耦：
	- 便于系统对应用组件进行裁剪（无屏设备可裁剪窗口）。
	- 便于系统扩展窗口形态。
	- 在多设备（如桌面设备和移动设备）上，应用组件可使用同一套生命周期。
3. **平衡应用能力和系统管控成本**
	Stage模型重新定义应用能力的边界，平衡应用能力和系统管控成本。    
	- 提供特定场景（如卡片、输入法）的应用组件，以便满足更多的使用场景。
	- 规范化后台进程管理：为保障用户体验，Stage模型对后台应用进程进行了有序治理，应用程序不能随意驻留在后台，同时应用后台行为受到严格管理，防止恶意应用行为。


## 组件分类
1. UIAbility组件
2. ExtensionAbility组件

UIAbility组件是一种包含UI界面的应用组件，主要用于和用户交互。
UIAbility组件是系统调度的基本单元，为应用提供绘制界面的窗口；一个UIAbility组件中可以通过多个页面来实现一个功能模块。每一个UIAbility组件实例，都对应于一个最近任务列表中的任务。


ExtensionAbility组件是基于特定场景提供的应用组件，以便满足更多的使用场景。
每一个具体场景对应一个[ExtensionAbilityType](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-bundlemanager-0000001427585060-V3#ZH-CN_TOPIC_0000001573928977__extensionabilitytype)，各类型的ExtensionAbility组件均由相应的系统服务统一管理，例如InputMethodExtensionAbility组件由输入法管理服务统一管理。


## 进程模型
1. 主进程
2. ExtensionAbility进程
3. 渲染进程

HarmonyOS的进程模型：
- 应用中（同一包名）的所有UIAbility运行在同一个独立进程中。
- WebView拥有独立的渲染进程。


## 线程模型
1. ArkTS引擎实例的创建：一个进程可以运行多个应用组件实例，所有应用组件实例共享一个ArkTS引擎实例。
2. 线程模型：ArkTS引擎实例在主线程上创建。
3. 进程内对象共享：支持。

HarmonyOS应用中每个进程都会有一个主线程，主线程有如下职责：
1. 执行UI绘制；
2. 管理主线程的ArkTS引擎实例，使多个UIAbility组件能够运行在其之上；
3. 管理其他线程（例如Worker线程）的ArkTS引擎实例，例如启动和终止其他线程；
4. 分发交互事件；
5. 处理应用代码的回调，包括事件处理和生命周期管理；
6. 接收Worker线程发送的消息；

除主线程外，还有一类与主线程并行的独立线程Worker，主要用于执行耗时操作，但不可以直接操作UI。Worker线程在主线程中创建，与主线程相互独立。最多可以创建8个Worker

线程间通信方式
- [Emitter](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/itc-with-emitter-0000001427584616-V3)
- [Worker](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/itc-with-worker-0000001427744572-V3)

