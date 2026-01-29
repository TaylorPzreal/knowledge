
Review
1. 2024-08-24 16:58

> [!Summary]
> 关注 FPS 流畅度（滚动性能）
> 
> 评判列表卡顿的指标是 UI 线程的帧率和 JavaScript 线程的帧率。
> 
> 推荐使用社区开源的 `RecyclerListView` 替代 `FlatList` 。`RecyclerListView` 在滚动时复用了列表项，而不是创建新的列表项，因此性能好

## 一、Introduction

1. ScrollView
2. FlatList
3. SectionList
4. VirtualizedList
5. RecyclerListView (Third-party lib) [Github](https://github.com/Flipkart/recyclerlistview) FlashList [Github](https://github.com/Shopify/flash-list) 
6. RefreshControl

> [!Error] 第一版 ListView 问题
> ListView 组件性能很差，没有内存回收机制，翻一页内存就涨一点，再翻一页内存又再涨一点。前 5 页滚动非常流畅，第 10 页开始就感觉到卡顿了，到 50 页的时候，基本就滑不动了。卡顿的原因就是无限列表太吃内存了。如果手机的可使用内存不够了，卡顿就会发生。


> [!Summary]
> 1. ScrollView 内容的布局方式是从上到下依次排列的，你给多少内容，ScrollView 就会渲染多少内容；
> 2. FlatList 内容的布局方式还是从上到下依次排列的，它通过更新第一个和最后一个列表项的索引控制渲染区域，默认渲染当前屏幕和上下 10 屏幕高度的内容，其他地方用空白视图进行占位；
> 3. RecyclerListView 性能最好，你应该优先使用它，但使用它的前提是列表项类型可枚举且高度确定或大致确定。


### 1: ScrollView
In React Native, the `ScrollView` is a generic scrolling container used to provide a scrollable view to its child components. It is useful when you need to display scrollable content larger than the screen, such as lists, images, or text. A `ScrollView` must have a bounded height in order to properly work.

> [!Abstract] 深入原理
> React Native 的 ScrollView 组件在 Android 的底层实现用的是 ScrollView 和 HorizontalScrollView，在 iOS 的底层实现用的是 UIScrollView。
> 
> ScrollView 的所有内容都会在首次刷新时进行渲染

```jsx
import React from 'react';
import { ScrollView, Text } from 'react-native';

const MyScrollView = () => {
  return (
	<SafeAreaView style={{flex: 1}}>
    <ScrollView>
      <Text>Item 1</Text>
      <Text>Item 2</Text>
      <Text>Item 3</Text>
    </ScrollView>
	</SafeAreaView>
  );
}

export default MyScrollView;
```

> [!warning] 注意
> Keep in mind that `ScrollView` is not optimized for long lists of items, and you should use the `FlatList` or `SectionList` components for better performance in those cases. However, it’s still useful for smaller content where you need a scrollable area, such as forms or when the content size is unknown.

`StickyHeaderComponent` 实现 CSS 中的 `position:sticky` 特性


### 2: FlatList
**FlatList** - It is a high-performance, scrollable list component that renders a large number of items efficiently.

> [!Summary] 总结
> 1. FlatList 列表组件是 “自动”按需渲染的
> 2. FlatList 组件底层使用的是虚拟列表 `VirtualizedList`，`VirtualizedList` 底层组件使用的是 `ScrollView` 组件。因此 VirtualizedList 和 ScrollView 组件中的大部分属性，FlatList 组件也可以使用。
> 3. FlatList 性能比 ScrollView 好的原因是， FlatList 列表组件利用按需渲染机制减少了首次渲染的视图，利用空视图的占位机制回收了原有视图的内存


```jsx
import { FlatList, Text } from 'react-native';

const data = [
  { id: 1, text: 'Item 1' },
  { id: 2, text: 'Item 2' },
  { id: 3, text: 'Item 3' },
];

const renderItem = ({ item }) => <Text>{item.text}</Text>;

const MyFlatList = () => (
  <FlatList
    data={data}
    renderItem={renderItem}
    keyExtractor={item => item.id.toString()}
  />
);
```

> 老版本的 FlatList 在 iOS 端表现很好，但在 Android 低端机还是能感觉到卡顿。社区中提供了性能更好的 RecyclerListView 

列表组件和滚动组件的关键区别是，列表组件把其内部子组件看做由一个个列表项组成的集合，每一个列表项都可以单独渲染或者卸载。而滚动组件是把其内部子组件看做一个整体，只能整体渲染。而自动按需渲染的前提就是每个列表项可以独立渲染或卸载。

> 实现 FlatList 自动按需渲染的思路具体可以分为三步：
> 1. 通过滚动事件的回调参数，计算需要按需渲染的区域；
> 2. 通过需要按需渲染的区域，计算需要按需渲染的列表项索引；
> 3. 只渲染需要按需渲染列表项，不需要渲染的列表项用空视图代替。

在 onScroll 事件中，我们可以获取到当前滚动的偏移量 offset 等信息。以当前滚动的偏移量为基础，默认向上数 10 个屏幕的高度，向下数 10 个屏幕的高度，这一共 21 个屏幕的内容就是需要按需渲染的区域，其他区域都是无需渲染的区域。

FlatList 内部实现就是通过 setState 改变按需渲染区域第一个索引和最后一个索引的值，来实现按需渲染的 。

列表项的高度是确定的，在写代码的时候，就可以通过获取列表项布局属性 `getItemLayout` 告诉 FlatList。

对于高度未知的情况，FlatList 会启用列表项的布局回调函数 `onLayout`，在 `onLayout` 中会有大量的动态测量高度的计算，包括每个列表项的准确高度和整体的平均高度。

如果不填 `getItemLayout` 属性，不把列表项的高度提前告诉 FlatList，让 FlatList 通过 `onLayout` 的布局回调动态计算，用户是可以感觉到滑动变卡的。


### 3: SectionList
**SectionList** - Similar to FlatList, but it is used when you want to display data in separate sections with *section headers*.

```jsx
import { SectionList, Text } from 'react-native';

const sections = [
  { title: 'Section 1', data: ['Item 1', 'Item 2', 'Item 3'] },
  { title: 'Section 2', data: ['Item 4', 'Item 5', 'Item 6'] },
];

const Item = ({ text }) => <Text>{text}</Text>;
const SectionHeader = ({ title }) => <Text>{title}</Text>;

const MySectionList = () => (
  <SectionList
    sections={sections}
    renderItem={({ item }) => <Item text={item} />}
    renderSectionHeader={({ section: { title } }) => (
      <SectionHeader title={title} />
    )}
    keyExtractor={(item, index) => item + index}
  />
);
```


### 4: VirtualizedList
**VirtualizedList** - A lower-level component for rendering large lists and for more fine-grained control over list rendering performance.

```jsx
import { VirtualizedList, Text } from 'react-native';

const data = [
  { id: 1, text: 'Item 1' },
  { id: 2, text: 'Item 2' },
  { id: 3, text: 'Item 3' },
];

const getItemCount = data => data.length;
const getItem = (data, index) => data[index];

const renderItem = ({ item }) => <Text>{item.text}</Text>;

const MyVirtualizedList = () => (
  <VirtualizedList
    data={data}
    renderItem={renderItem}
    keyExtractor={item => item.id.toString()}
    getItemCount={getItemCount}
    getItem={getItem}
  />
);
```


### 5: RecyclerListView
RecyclerListView 是开源社区提供的列表组件，它的底层实现和 FlatList 一样也是 ScrollView，它也要求开发者必须将内容整体分割成一个个列表项。

在首次渲染时，RecyclerListView 只会渲染首屏内容和用户即将看到的内容，所以它的首次渲染速度很快。在滚动渲染时，只会渲染屏幕内的和屏幕附近 250 像素的内容，距离屏幕太远的内容是空的。

React Native 的 `RecyclerListView` 复用灵感来源于 Native 的**可复用**列表组件。

> 在 iOS 中，表单视图 UITableView，实际就是可以上下滚动、左右滚动的可复用列表组件。它可以通过复用唯一标识符 reuseIdentifier，标记表单中的复用单元 cell，实现单元 cell 的复用。
> 
> 在 Android 上，动态列表 RecyclerView 在列表项视图滚出屏幕时，不会将其销毁，相反会把滚动到屏幕外的元素，复用到滚动到屏幕内的新的列表项上。这种复用方法可以显著提高性能，改善应用响应能力，并降低功耗。

RecyclerListView 用的是 position:absolute 的绝对定位布局，所有的列表项的宽度 width、高度 height、顶部偏移量 top、左边偏移量 left 都得在布局之前计算出来。


*Shopify 开源的 `FlashList` 也很好，比 `RecyclerListView` 使用更简单。*

### 6: Refresh Control
`RefreshControl` is a component in React Native that is used to provide pull-to-refresh functionality for scrollable components like `ScrollView`, `ListView`, and `FlatList`.

```jsx
import React, { useState } from 'react';
import { FlatList, RefreshControl, Text } from 'react-native';

const App = () => {
    const [refreshing, setRefreshing] = useState(false);

    const fetchData = () => {
        // Fetch the data and update your state accordingly
    };

    const onRefresh = () => {
        setRefreshing(true);
        fetchData().then(() => {
            setRefreshing(false);
        });
    };

    return (
        <FlatList
            data={['Item 1', 'Item 2', 'Item 3']}
            renderItem={({ item }) => <Text>{item}</Text>}
            refreshControl={
                <RefreshControl refreshing={refreshing} onRefresh={onRefresh} />
            }
        />
    );
};

export default App;
```


When `refreshing` is set to `true`, the refresh indicator is shown. It is hidden when `refreshing` is set to `false`.


## Reference
[# React Native 无限列表的优化与实践](https://mp.weixin.qq.com/s/kN4MxfEkvICq3JneUvM56w) 
[# RecyclerListView: High performance ListView for React Native and Web](https://medium.com/@naqvitalha/recyclerlistview-high-performance-listview-for-react-native-and-web-e368d6f0d7ef)

