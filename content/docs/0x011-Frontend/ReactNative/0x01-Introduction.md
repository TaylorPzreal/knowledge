---
Created: 2024-07-21T23:19:00
Last updated: 2026-01-28T06:19:00
aliases:
  - React Native Introduction
tags:
  - ReactNative
---

Review
1. 2024-07-21 23:19
2. 2024-09-07


> [!Summary]
> 1. React Native <https://reactnative.dev/> [🥷Github](https://github.com/facebook/react-native) 
> 2. [Github: React Native New Architecture Working Group](https://github.com/reactwg/react-native-new-architecture) 
> 3. [About the New Architecture](https://reactnative.dev/docs/the-new-architecture/landing-page) 
> 
> [React Native 新架构实战课 -- 蒋宏伟](https://time.geekbang.org/column/intro/100110101?tab=catalog) 


## 一、Introduction
[React Native](https://reactnative.dev/) **Written in JavaScript, rendered with native code.** React primitives render to native platform UI, meaning your app uses the same native platform APIs other apps do.

React Native is an open-source framework developed by Facebook that allows developers to build mobile applications using JavaScript and React. It enables building apps for both iOS and Android platforms by offering a shared codebase, which significantly reduces development time and effort.

*Features*
1. Code Reusability
2. Familiar React Concepts
3. Native Performance
4. Vast Ecosystem
5. Hot Reloading


*Alternatives*
1. Flutter <https://flutter.dev/> 
2. Ionic <https://ionicframework.com/>
3. MAUI(.NET Multi-platform App UI) <https://dotnet.microsoft.com/en-us/apps/maui> 
4. 小程序
5. Weex


***News***


## 二、Development

### 环境配置
#### 安装 `Watchman`

```sh
# 监听环境变更，自动重新运行项目
brew install watchman
```

#### 安装 JDK (Java Development Kit)
Zulu 是一款 Java 运行时环境，基于 OpenJDK 构建。
推荐 `sdkman` 类似于 NodeJS NVM，便捷管理多个Java版本

```sh
brew tap homebrew/cask-versions
brew install --cask zulu11
```

```sh
java --version
javac --version
```

#### 安装 Android Studio
Android Studio 是 Android 开发的官方集成开发环境（IDE）。你需要安装 Android Studio 才能在本机构建 React Native 应用程序，并运行在真机或模拟器上。

```txt
腾讯： https://mirrors.cloud.tencent.com/AndroidSDK/

阿里： https://mirrors.aliyun.com/android.googlesource.com/
```

#### 安装 Android SDK
- Android SDK Platform 33
- `Intel x86 Atom_64 System Image` 或 `Google APIs Intel x86 Atom System Image`(Inter CPU)  或 `Google APIs ARM 64 v8a System Image` (Apple CPU)
- `Android SDK Build-Tools` 33.0.0 版本

配置 `.zshrc`

```txt
export ANDROID_HOME=$HOME/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/emulator
export PATH=$PATH:$ANDROID_HOME/platform-tools
```

```sh
echo $ANDROID_HOME
/Users/jianghongwei/Library/Android/sdk

echo $PATH
/Users/local/bin...
```

#### 安装 Android 模拟器


#### 安装 Ruby
iOS环境会用到。Ruby 有两种常用包管理工具，Gem 和 Bundler。

```sh
sudo gem install cocoapods
```


#### 初始化脚手架
1. `npx react-native init` 
2. Expo
3. Ignite


### 2.1: Expo
**Expo** is a framework and a platform that allows you to develop, build, and deploy React Native applications easily and quickly. It simplifies the development process and provides a set of useful tools and services, including its own CLI (Command Line Interface), a managed workflow, and an SDK (Software Development Kit) with pre-built modules for common features.

Create a project <https://docs.expo.dev/get-started/create-a-project/> 
```sh
npx create-expo-app@latest
```

> `create-expo-app` is a command line tool that generates a React Native project that works out of the box with Expo. It is the easiest way to get started building a new React Native application.

### 2.2: Expo Snack
https://snack.expo.dev/
在线开发、测试


### 2.3: React Native CLI
React Native CLI is the official command-line interface for building native mobile apps using React Native. This method requires you to manually set up the native development environment and tools needed for iOS and Android app development.
<https://reactnative.dev/docs/environment-setup?guide=native> 

```sh
npx react-native@latest init RNDemo
```

```sh
npx react-native start
```

```sh
# build development
$ npx react-native run-ios

# build production
npx react-native run-ios --configuration Release
```

#### Metro
<https://metrobundler.dev/>
> The JavaScript bundler for React Native

Metro Bundler is the default bundler for React Native applications. It’s a JavaScript module bundler that takes all your application code and dependencies, and bundles them together into a single JavaScript file or multiple files (based on platform).


### 2.4: Platform-specific
> 1. Platform module
> 2. File extensions

1. By appending `.android.js` or `.ios.js` to your file’s name, React Native will load the file corresponding to the platform you are running your app on.
2. `Platform.select({ios:'', android: ''})` 
3. Create separate stylesheets for each platform, like `styles.native.js` and `styles.web.js`. 

```jsx
import { Platform, StyleSheet } from 'react-native';

const styles = StyleSheet.create({
  container: {
    ...Platform.select({
      ios: {
        backgroundColor: 'red',
      },
      android: {
        backgroundColor: 'blue',
      },
    }),
  },
});
```


## 三、Third party libraries

1. `webview` 
2. `async-storage` 
3. `react-native-svg` 
4. `react-native-camera` 
5. `react-native-blur` [Github](https://github.com/Kureev/react-native-blur) 
6. `react-native-drop-shadow` [Github](https://github.com/hoanglam10499/react-native-drop-shadow) 
7. `react-native-linear-gradient` [Github](https://github.com/react-native-linear-gradient/react-native-linear-gradient) 
8. `react-native-view-shot` [Github](https://github.com/gre/react-native-view-shot) 生成海报图
9. `gl-react` [Github](https://github.com/gre/gl-react) WebGL shaders
10. `react-native-fast-image` [Github](https://github.com/DylanVann/react-native-fast-image) 


## Reference
[React Native New Architecture Working Group](https://github.com/reactwg/react-native-new-architecture) 
[About the New Architecture](https://reactnative.dev/docs/the-new-architecture/landing-page) 
