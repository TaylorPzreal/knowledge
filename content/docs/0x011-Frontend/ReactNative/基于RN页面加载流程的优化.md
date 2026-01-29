
Review
1. 2024-10-13 08:00

> [!Summary]
> 

## 一、Introduction

### RN页面加载流程
1. 容器创建
2. 包下载与解压
3. 初始化JS引擎
4. 加载业务包
5. 初始化React布局计算
6. 渲染
7. 加载异步资源
8. 页面可交互

#### 容器创建
- 启动原生应用
- 创建RN的宿主容器(iOS上是 `RCTRootView`, Android上是 `ReactRootView`)

#### 包下载与解压
- 检查是否有新的JavaScript业务包，如果有，下载新包，解压JavaScript包到本地存储

#### 初始化引擎
- 创建JavaScript运行时环境（通常是Hermes或JavaScriptCore）
- 初始化桥接层(Bridge)或新架构中的JavaScript Interface (JSI)


#### 加载业务包
- 读取解压后的JavaScript代码
- 通过JavaScript引擎执行代码
- 加载React Native核心库和应用代码


#### 初始化React
- 执行应用的入口点(通常是 `index.js` )
- 创建React组件树
- 设置应用的根组件


#### 布局计算

- 使用Yoga布局引擎计算组件的尺寸和位置
- 生成布局信息


#### 渲染

- 创建Shadow Tree(虚拟视图层级)
- 将React组件映射到对应的原生UI组件
- 在主线程上渲染原生UI元素


#### 加载异步资源

- 加载图片、字体等静态资源
- 发起网络请求获取数据


#### 页面可交互

- 完成首屏渲染
- 注册事件监听器,处理用户输入


#### 持续更新

- 响应状态变化,触发重新渲染
- 执行增量更新以优化性能


## Reference

