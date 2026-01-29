
Review
1. 2024-08-24 21:25

> [!Summary]
> [React Native 性能优化指南 - 渲染篇](https://supercodepower.com/react_native_performance_optimization_guides) 
> [React Native 启动速度优化 - Native](https://supercodepower.com/react-native-performance-native) 
> [React Native 启动速度优化 - JS](https://supercodepower.com/react-native-performance-js) 

## 一、Introduction
iOS devices display 60 frames per second, which gives you and the UI system about 16.67ms to do all of the work needed to generate the static image (frame) that the user will see on the screen for that interval. If you are unable to do the work necessary to generate that frame within the allotted 16.67ms, then you will "drop a frame" and the UI will appear unresponsive.




## Common Problem Sources
1、Console Logs
Excessive console logs can lead to decreased performance in React Native, especially in debug mode. In order to avoid this, keep the usage of console logging to a minimum, and clean up unnecessary logs before releasing the app.

2、Images
Heavy and unoptimized images can lead to performance issues in React Native. To avoid this, use the following techniques:

- Optimize image size and resolution before bundling them in the application.
- Use `resizeMode` prop on the `Image` component to cache images for better rendering.

3、Inline Functions and Styles

Using inline functions and styles within components can lead to unnecessary re-rendering and performance issues. Instead, define functions and styles outside of the component render method.

4、PureComponent、React.memo() 
Components that extend `React.PureComponent` or are wrapped in `React.memo()` can lead to performance issues in case they’re updating frequently and causing unnecessary re-renders. Make sure to only use them when appropriate to avoid performance bottlenecks.

5、FlatList
When working with large lists in React Native, using `ListView` instead of `FlatList` can cause performance issues. Replace `ListView` with the more performant `FlatList` or `SectionList` components.



## Reference

