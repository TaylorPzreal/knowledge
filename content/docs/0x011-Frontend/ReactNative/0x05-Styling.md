
Review
1. 2024-08-23 08:24

> [!Summary]
> RN 默认不支持className，即不支持 CSS/SASS，仅支持 **Inline Styles** 和 **StyleSheet**. 
> 常用功能
> 1. Platform: Platform.OS (ios/android)

## 一、Introduction
Styling in React Native is accomplished through JavaScript and uses a subset of CSS properties. Unlike CSS in web development, React Native has its own set of components and styling rules.

1. StyleSheet
2. Inline styles
3. 手动配置 SASS

`StyleSheet` is a module provided by React Native to manage and optimize styles. It is similar to a CSS stylesheet and helps in creating and working with multiple styles efficiently.

**StyleSheet 优势**
1. 元素结构和样式分离，可维护性更好；
2. 样式对象可以复用，能减少重复代码；
3. 样式对象只创建一次，也减少性能的损耗。


```jsx
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

const App = () => {
  return (
    <View style={[styles.container, styles.backgroundRed]}>
      <Text style={styles.text}>Hello, React Native!</Text>
      <Text style={{flex: 1}}>Inline text style</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5FCFF',
  },
  text: {
    fontSize: 20,
    textAlign: 'center',
    margin: 10,
  },
  backgroundRed: {
    backgroundColor: 'red',
  },
});

export default App;
```


### 支持SASS
sass-transformer <https://github.com/kristerkari/react-native-sass-transformer> 
css module <https://github.com/kristerkari/react-native-css-modules> 

```sh
yarn add --dev react-native-sass-transformer sass
```


## Layout
<https://reactnative.dev/docs/flexbox>

In React Native, layouts are primarily managed using the Flexbox styling system. Flexbox is a powerful and flexible layout system that allows you to create responsive and complex UIs using a set of simple rules.

==Flexbox== consists of three key elements: the `container`, `main axis`, and `cross axis`.
- The `container` is the parent flex container that holds and distributes all the child elements.
- The `main axis` is the primary direction of the layout (horizontal or vertical).
- The `cross axis` is the perpendicular direction, opposite of the main axis.
- **`flexDirection`**: This style specifies the primary axis using four possible values: `row`, `row-reverse`, `column`, or `column-reverse`.
- **`alignItems`**: This style is used to align the child items along the ==cross-axis==. It uses the values `flex-start`, `flex-end`, `center`, `stretch`, or `baseline`.
- **`justifyContent`**: This style is used to align the child items along the ==main axis==. It accepts the values `flex-start`, `flex-end`, `center`, `space-between`, or `space-around`.
- **`flexWrap`**: Set to either `wrap` or `nowrap` to specify if child items should wrap around to the next line when there’s not enough space on the current line.
- **`flex`**: This style determines how the child items grow or shrink when there’s remaining space in the container. It’s a shorthand for `flex-grow`, `flex-shrink`, and `flex-basis`.



## Reference

