
Review
1. 2024-08-24 21:10

> [!Summary]
> 
> 1. [React Navigation](https://github.com/react-navigation/react-navigation) 
> 2. [React Native Navigation](https://github.com/wix/react-native-navigation) 
> 3. use **Linking** 

## 一、Introduction
*Deep linking is a technique used in mobile applications that allows you to open a specific screen, content, or functionality within the application using a URL or a custom URL scheme.* This is useful for providing seamless user experiences by navigating the user directly to the desired part of the app. Deep linking can be triggered by clicking on a link in an email, scanning a QR code, or through a push notification.

There are two types of deep links:

1. **Universal Links** (iOS) / **App Links** (Android): These are HTTPS URLs that allow the user to navigate to a specific screen when the app is installed and fallback to a specified website when the app is not installed.
2. **Custom URL Schemes**: Unique URLs, like `myapp://my-screen`, that can open the app directly to a specific screen when clicked.

In React Native, you can handle deep links using the `Linking` module which provides the necessary methods to work with deep links.

First, you have to import `Linking` from `"react-native"`:

```jsx
import React from 'react';
import { Linking, Text, View } from 'react-native';

class App extends React.Component {
  componentDidMount() {
    Linking.addEventListener('url', this.handleOpenURL);
  }

  componentWillUnmount() {
    Linking.removeEventListener('url', this.handleOpenURL);
  }

  handleOpenURL(event) {
    // Handle your deep link logic
    console.log('Received deep link: ', event.url);
  }

  render() {
    return (
      <View>
        <Text>Hello from React Native!</Text>
      </View>
    );
  }
}

export default App;
```


### Linking
1. `Linking.canOpenURL('')` 
2. `Linking.getInitialURL()` 
3. `Linking.openSettings()` 
4. `Linking.openURL('')` 
5. `Linking.addEventListener('url', callback)` 


Built-in URL Schemes

| scheme           | description                                 | iOS | Android |
| ---------------- | ------------------------------------------- | --- | ------- |
| `mailto`         | Open mail app, eg: `mailto:support@expo.io` | ✅   | ✅       |
| `tel`            | Open phone app, eg: `tel:+123456789`        | ✅   | ✅       |
| `sms`            | Open SMS app, eg: `sms:+123456789`          | ✅   | ✅       |
| `https` / `http` | Open web browser app, eg: `https://expo.io` | ✅   | ✅       |


## Reference

