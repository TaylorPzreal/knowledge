
Review
1. 2023-11-23 22:29

## 一、Introduction


在开发态，一个应用包含一个或者多个Module，可以在[DevEco Studio](https://developer.harmonyos.com/cn/develop/deveco-studio/)工程中[创建一个或者多个Module](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/ohos-adding-deleting-module-0000001218760594-V3)。**Module是HarmonyOS应用/服务的基本功能单元**，包含了源代码、资源文件、第三方库及应用/服务配置文件，每一个Module都可以独立进行编译和运行。Module分为“Ability”和“Library”两种类型，“Ability”类型的Module对应于编译后的HAP（Harmony Ability Package）；“Library”类型的Module对应于[HAR](https://developer.huawei.com/consumer/cn/doc/development/harmonyos-guides-V2/har-package-0000001573432125-V2)（Harmony Archive），或者[HSP](https://developer.huawei.com/consumer/cn/doc/development/harmonyos-guides-V2/in-app-hsp-0000001523312158-V2)（Harmony Shared Package）。全文中介绍到的Module默认指的是“Ability”类型的Module。
![](./assets/70081a4e0215_4181b5e7.png)

开发者通过DevEco Studio把应用程序编译为一个或者多个.hap后缀的文件，即HAP。**HAP是HarmonyOS应用安装的基本单位**，包含了编译后的代码、资源、三方库及配置文件。HAP可分为Entry和Feature两种类型。

在基于Stage模型开发的应用项目代码下，都存在一个`app.json5`及一个或多个`module.json5`这两种配置文件。

[app.json5](https://developer.huawei.com/consumer/cn/doc/development/harmonyos-guides-V2/app-configuration-file-0000001427584584-V2)主要包含以下内容：
- 应用的全局配置信息，包含应用的包名、开发厂商、版本号等基本信息。
- 特定设备类型的配置信息。

[module.json5](https://developer.huawei.com/consumer/cn/doc/development/harmonyos-guides-V2/module-configuration-file-0000001427744540-V2)主要包含以下内容：
- Module的基本配置信息，例如Module名称、类型、描述、支持的设备类型等基本信息。
- [应用组件](https://developer.huawei.com/consumer/cn/doc/development/harmonyos-guides-V2/stage-model-development-overview-0000001427744552-V2)信息，包含UIAbility组件和ExtensionAbility组件的描述信息。
- 应用运行过程中所需的权限信息。

## 二、ArkTS和ArkUI框架介绍
[浅析ArkTS的起源和演进](https://developer.huawei.com/consumer/cn/training/course/slightMooc/C101667356568959645)
ArkUI开发框架
![](./assets/bf9a72d99e92_257d06fd.png)


ArkTS声明式开发范式
![](./assets/cc5f23dd89dc_d5fae394.png)

**ArkUI 中进一步提供了多维度的状态管理机制**。和 UI 相关联的数据，不仅可以在组件内使用，还可以在不同组件层级间传递，比如父子组件之间，爷孙组件之间，也可以是全局范围内的传递，还可以是跨设备传递。另外，从数据的传递形式来看，可分为**只读的单向传递和可变更的双向传递**。开发者可以灵活的利用这些能力来实现数据和 UI 的联动。

## 三、开发基础知识

### 3.1、状态管理
装饰器@State、@Prop、@Link来管理组件状态
- [@State](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-state-0000001474017162-V3) 装饰的变量是**组件内部的状态数据**，当这些状态数据被修改时，将会调用所在组件的build方法进行UI刷新。
- [@Prop](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-prop-0000001473537702-V3) 与@State有相同的语义，但初始化方式不同。@Prop装饰的变量必须使用其父组件提供的@State变量进行初始化，允许组件内部修改@Prop变量，但更改不会通知给父组件，即@Prop属于**单向数据绑定**。
- [@Link](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-link-0000001524297305-V3) 装饰的变量可以**和父组件的@State变量建立双向**数据绑定，需要注意的是：@Link变量不能在组件内部进行初始化。
- @Watch 监听状态变化
- @Provide & @Consume
- [@Observed & @ObjectLink](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-observed-and-objectlink-0000001473697338-V3?catalogVersion=V3) 
- [@Builder](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-builder-0000001524176981-V3)装饰的方法用于定义组件的声明式UI描述，在一个自定义组件内快速生成多个布局内容。

ForEach() // 循环渲染
```ts
ForEach(
  arr: any[], // 用于迭代的数组
  itemGenerator: (item: any, index?: number) => void, // 生成子组件的lambda函数
  keyGenerator?: (item: any, index?: number) => string // 用于给定数组项生成唯一且稳定的键值
)
```


```ts
@Component
export default struct TargetList {
  @State clickIndex: number = CommonConstants.DEFAULT_CLICK_INDEX;
  ...
             TargetListItem({
               clickIndex: $clickIndex,
              ...
             })
  ...
}
```


```ts
// @Builder 引用传递参数
@Builder function ABuilder($$:{par: string}){
  Row(){
    Text( 'abs:' + $$.par)
  }
}

@Entry
@Component
struct Index {
  @State message: string = 'Hello World'

  build() {
    Row() {
      Column() {
        ABuilder({par:this.message})
      }
      .width('100%')
    }
    .height('100%')
  }
}
```


完成在父子组件中定义状态后，最关键的就是要建立父子组件的双向关联关系。在父组件中使用子组件时，将父组件的clickIndex传递给子组件的clickIndex。其中父组件的clickIndex加上 **$** 表示传递的是**引用**。

#### 跨组件层级双向同步状态：@Provide和@Consume
![](./assets/16389872ccf5_569c2cca.png)
跨组件层级双向同步状态是指@Provide修饰的状态变量自动对提供者组件的所有后代组件可用，后代组件通过使用@Consume装饰的变量来获得对提供的状态变量的访问。@Provide作为数据的提供方，可以更新其子孙节点的数据，并触发页面渲染。@Consume在感知到@Provide数据的更新后，会触发当前自定义组件的重新渲染。

使用@Provide的好处是开发者不需要多次将变量在组件间传递。@Provide和@Consume的具体使用方法请参见开发指南：[@Provide装饰器和@Consume装饰器：与后代组件双向同步](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-provide-and-consume-0000001473857338-V3?catalogVersion=V3)。


### 3.2、Column&Row组件使用
- Column表示沿垂直方向布局的容器。
- Row表示沿水平方向布局的容器。
- Flex
- Stack
- List & ListItem: List是很常用的滚动类容器组件，一般和子组件ListItem一起使用，List列表中的每一个列表项对应一个ListItem组件。
- Grid & GridItem
- Tabs & TabContent
- [Swiper](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-swiper-0000001427744844-V3?catalogVersion=V3)  
- [Flex](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-flex-0000001427902472-V3?catalogVersion=V3) 

#### 主轴和交叉轴概念
在布局容器中，默认存在两根轴，分别是主轴和交叉轴，这两个轴始终是相互垂直的。不同的容器中主轴的方向不一样的。
- **主轴**：在Column容器中的子组件是按照从上到下的垂直方向布局的，其主轴的方向是垂直方向；在Row容器中的组件是按照从左到右的水平方向布局的，其主轴的方向是水平方向。
- **交叉轴**：与主轴垂直相交的轴线，如果主轴是垂直方向，则交叉轴就是水平方向；如果主轴是水平方向，则交叉轴是垂直方向。

| 属性名称       | 描述                                     |
| -------------- | ---------------------------------------- |
| justifyContent | 设置子组件在**主轴方向**上的对齐格式。   |
| alignItems     | 设置子组件在**交叉轴**方向上的对齐格式。 |

子组件在主轴方向上的对齐使用justifyContent属性来设置，其参数类型是[FlexAlign](https://developer.harmonyos.com/cn/docs/documentation/doc-references/ts-appendix-enums-0000001281201130#ZH-CN_TOPIC_0000001281201130__flexalign)。FlexAlign定义了以下几种类型：
- Start
- Center
- End
- SpaceBetween
- SPaceAround
- SpaceEvenly

子组件在交叉轴方向上的对齐方式使用alignItems属性来设置。

Column容器的主轴是垂直方向，交叉轴是水平方向，其参数类型为 **HorizontalAlign**（水平对齐），HorizontalAlign定义了以下几种类型：
- Start：设置子组件在水平方向上按照起始端对齐。
- Center（默认值）：设置子组件在水平方向上居中对齐。
- End：设置子组件在水平方向上按照末端对齐。

Row容器的主轴是水平方向，交叉轴是垂直方向，其参数类型为 **VerticalAlign**（垂直对齐），VerticalAlign定义了以下几种类型：
- Top：设置子组件在垂直方向上居顶部对齐。
- Center（默认值）：设置子组件在竖直方向上居中对齐。
- Bottom：设置子组件在竖直方向上居底部对齐。

接下来，我们介绍Column和Row容器的接口。

| 容器组件 | 接口                                      |
| -------- | ----------------------------------------- |
| Column   | Column(value?:{space?: string \| number}) |
| Row      | Row(value?:{space?: string \| number})    |

Column和Row容器的接口都有一个可选参数space，表示子组件在主轴方向上的间距。
![](./assets/6b8c987d07d8_9776944e.png)


### 3.3、单位

1. vp
2. 无 == vp
3. fr
4. 百分比：100%
5. fp


### 3.4、List
[List组件和Grid组件的使用](https://developer.huawei.com/consumer/cn/training/course/slightMooc/C101667360160710997) 

```ts
List({ space: 10 }) {
  ForEach(this.arr, (item) => {
    ListItem() {
      Text(`${item}`)
        ...
    }
  }, item => item)
}
.onScrollIndex((firstIndex: number, lastIndex: number) => {
  console.info('first' + firstIndex)
  console.info('last' + lastIndex)
})
.onScroll((scrollOffset: number, scrollState: ScrollState) => {
  console.info('scrollOffset' + scrollOffset)
  console.info('scrollState' + scrollState)
})
.onReachStart(() => {
  console.info('onReachStart')
})
.onReachEnd(() => {
  console.info('onReachEnd')
})
.onScrollStop(() => {
  console.info('onScrollStop')
})
```


```ts
@Entry
@Component
struct GridExample {
  // 定义一个长度为16的数组
  private arr: string[] = new Array(16).fill('').map((_, index) => `item ${index}`);

  build() {
    Column() {
      Grid() {
        ForEach(this.arr, (item: string) => {
          GridItem() {
            Text(item)
              .fontSize(16)
              .fontColor(Color.White)
              .backgroundColor(0x007DFF)
              .width('100%')
              .height('100%')
              .textAlign(TextAlign.Center)
          }
        }, item => item)
      }
      .columnsTemplate('1fr 1fr 1fr 1fr')
      .rowsTemplate('1fr 1fr 1fr 1fr')
      .columnsGap(10)
      .rowsGap(10)
      .height(300)
    }
    .width('100%')
    .padding(12)
    .backgroundColor(0xF1F3F5)
  }
}
```

上面构建的网格布局使用了固定的行数和列数，所以构建出的网格是不可滚动的。然而有时候因为内容较多，我们通过滚动的方式来显示更多的内容，就需要一个可以滚动的网格布局。我们只需要设置rowsTemplate和columnsTemplate中的一个即可。

#### 列表性能优化
开发者在使用长列表时，如果直接采用循环渲染方式，会一次性加载所有的列表元素，从而导致页面启动时间过长，影响用户体验，推荐通过以下方式来进行列表性能优化：
[使用数据懒加载](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/ui-ts-performance-improvement-recommendation-0000001477981001-V3#ZH-CN_TOPIC_0000001477981001__%E6%8E%A8%E8%8D%90%E4%BD%BF%E7%94%A8%E6%95%B0%E6%8D%AE%E6%87%92%E5%8A%A0%E8%BD%BD)
[设置list组件的宽高](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/ui-ts-performance-improvement-recommendation-0000001477981001-V3#ZH-CN_TOPIC_0000001477981001__%E8%AE%BE%E7%BD%AElist%E7%BB%84%E4%BB%B6%E7%9A%84%E5%AE%BD%E9%AB%98)


### 3.5、Video
[Video组件使用](https://developer.huawei.com/consumer/cn/training/course/slightMooc/C101680765314766141)


### 3.6、弹窗

确认类型
- AlertDialog

选择类
- TextPickerDialog
- DatePickerDialog
- TimePickerDialog

自定义弹窗
- @CustomDialog

### 3.7、动画
[属性动画的使用](https://developer.huawei.com/consumer/cn/training/course/slightMooc/C101667368091091005)

属性动画，是最为基础的动画，其功能强大、使用场景多，应用范围较广。常用于如下场景中：
- 一、页面布局发生变化。例如添加、删除部分组件元素。
- 二、页面元素的可见性和位置发生变化。例如显示或者隐藏部分元素，或者将部分元素从一端移动到另外一端。
- 三、页面中图形图片元素动起来。例如使页面中的静态图片动起来。

```ts
Image(iconItem.imgRes)
  .width(this.iconWidth)
  .position({ x: iconItem.posX })
  .objectFit(ImageFit.Contain)
  .animation({
    duration: 2000,
    tempo: 3.0,
    delay: iconItem.delay,
    curve: Curve.Linear,
    playMode: PlayMode.Normal,
    iterations: 1, // 当iterations设置为-1时，表示无限次播放，则onFinish回调函数不会被调用。
    onFinish: () => {      
      prompt.showToast({ message:"动画播放结束！！！" })
    }
  })
```

**注意**
1、animation属性作用域。animation自身也是组件的一个属性，其作用域为animation之前。即产生属性动画的属性须在animation之前声明，其后声明的将不会产生属性动画。以示例中的五个图标动画为例，我们期望产生动画的属性为Image组件的width属性，故该属性width需在animation属性之前声明。如果将该属性width在animation之后声明，则不会产生动画效果。

2、产生属性动画的属性变化时需触发UI状态更新。在本示例中，产生动画的属性width，其值是通过变量iconWidth从30变为100，故该变量iconWidth的改变需触发UI状态更新。

3、产生属性动画的属性本身需满足一定的要求，并非任何属性都可以产生属性动画。目前支持的属性包括**width、height、position、opacity、backgroundColor、scale、rotate、translate**等

- 关闭属性动画页面，是指将动画的组件删除或者隐藏起来

### 3.8、首选项（Preference）
首选项为应用提供Key-Value键值型的数据存储能力，支持应用持久化轻量级数据，并对其进行增删除改查等。该存储对象中的数据会被缓存在内存中，因此它可以获得更快的存取速度。

常用接口有：保存数据（put）、获取数据（get）、是否包含指定的key（has）、删除数据（delete）、数据持久化（flush）等，后面依次详细介绍接口使用。


### 3.9、三方库
三方库是开发者在系统能力的基础上进行了一层具体功能的封装，对其能力进行拓展，提供更加方便的接口，提升开发效率的工具。如果是发布到开源社区，称为开源三方库，开发者可以通过访问开源社区获取。而一些团队内部开发使用的三方库，没有发布到开源社区的称为内部三方库。

[开源三方库资源汇总](https://gitee.com/openharmony-tpc/tpc_resource)
[三方库](https://repo.harmonyos.com/#/cn/application/atomService?sort=downloads&page=1) 


## 相关资源
[Common Components](https://developer.harmonyos.com/en/docs/documentation/doc-guides-V3/ui-ts-components-intro-0000001544575561-V3)


## Reference
1. [HarmonyOS应用开发者基础认证](https://developer.huawei.com/consumer/cn/training/dev-cert-detail/101666948302721398)
2. [Gitee OpenHarmony codelabs](https://gitee.com/openharmony/codelabs)
3. [TypeScript](https://www.typescriptlang.org/)
