
Review
1. 2024-08-22 22:47

> [!Summary]
> 

## 一、Introduction
Core components are the essential building blocks provided by React Native to create a user interface for mobile applications.

1. Text
2. View
3. TextInput
4. Button
5. Image
6. ImageBackground
7. Switch
8. StatusBar
9. ActivityIndicator
10. Modal
11. Pressable
12. SectionList
13. FlatList
14. VirtualizedList
15. ScrollView
16. RefreshControl
17. SafeAreaView
18. KeyboardAvoidingView
19. TouchableOpacity
20. Alert
21. Linking

`ImageBackground` is a React Native core component that allows you to display an image as a background while still being able to place content inside the component. This helps in creating beautiful layouts with images and text or other content on top.

The `StatusBar` component is used to control the appearance of the status bar on the top of the screen. It may strike as a bit unusual since, unlike other React Native components, it doesn’t render any visible content. Instead, it sets some native properties that can help customize the look of status bars on Android, iOS, or other platforms.

`TouchableOpacity` is a wrapper for making elements like `View` and `Text` respond properly to touch events. It provides feedback by reducing the opacity of the wrapped component when pressed.

```jsx
<TouchableOpacity onPress={this.onButtonPress}>
  <Text style={styles.buttonText}>Press me!</Text>
</TouchableOpacity>
```


`Linking` 
`Linking.openURL('tel:1234567')` 

|Scheme|Description|iOS|Android|
|---|---|---|---|
|`mailto`|Open mail app, eg: mailto: [support@expo.io](mailto:support@expo.io)|✅|✅|
|`tel`|Open phone app, eg: tel:+123456789|✅|✅|
|`sms`|Open SMS app, eg: sms:+123456789|✅|✅|
|`https` / `http`|Open web browser app, eg: [https://expo.io](https://expo.io/)|✅|✅|

## 二、扩展
1. Swipe *react-native-gesture-handler* -> `Swipeable` 
2. Marquee

**Marquee libs**
<https://github.com/justin-chu/react-fast-marquee> 
<https://github.com/wuyunqiang/react-native-marquee-easy> 
<https://github.com/animate-react-native/marquee> 


## Reference

