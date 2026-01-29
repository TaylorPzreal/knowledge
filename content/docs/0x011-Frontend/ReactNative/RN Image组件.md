
Review
1. 2024-10-13 16:31

> [!Summary]
> React Native 框架对图片的默认缓存处理并不是最优的方案，社区中提供了替代方案 [FastImage](https://github.com/DylanVann/react-native-fast-image)，它是基于 *SDWebImage* (iOS) 和 *Glide* (Android) 实现的性能和效果会更好一些。

## 一、Introduction
React Native 的 Image 组件一共支持 4 种加载图片的方法：
1. 静态图片资源；
2. 网络图片；
3. 宿主应用图片；
4. Base64 图片。

### 静态资源图片
静态图片资源（Static Image Resources）是一种使用内置图片的方法。静态图片资源中的“静态”指的是每次访问时都不会变化的图片资源。站在用户的视角看，App 的 logo 图片就是不会变化的静态图片资源，而每次访问新闻网站的新闻配图就是动态变化的图片。

如果图片每次都不会变化，那么你就可以把这张图片作为*静态图片资源，内置在 App 中*。首先，把图片放到 React Native 的代码仓库中，然后通过 require 的方式引入图片，最后把图片的引用值传给 source 属性。`Image.source` 属性是用来设置图片加载来源的。

```tsx
// 方案一：正确
const dianxinIcon = require('./dianxin.jpg')
log(JSON.stringify(Image.resolveAssetSource(dianxinIcon)))

<Image source={dianxinIcon}/>

// 方案二：错误
const path = './dianxin.jpg'
const dianxinIcon = require(path)
<Image source={dianxinIcon}/>
```
缓存与预加载

正是因为静态图片资源加载方式，它在"编译时"提前获取了图片宽高等信息，在"构建时"内置了静态图片资源，因此在"运行时"，程序可以提前获取图片宽高和真正的图片资源。相对于网络图片等加载方式，使*用静态图片资源加载，即使不设置图片宽高，也有一个默认宽高来进行展示*，而且加载速度更快。


### 网络图片
网络图片（Network Images）指的是使用 `http/https` 网络请求加载远程图片的方式。在使用网络图片时，*建议将宽高属性作为一个必填项来处理*。为什么呢？和前面介绍的静态图片资源不同的是，网络图片下载下来之前，React Native 是没法知道图片的宽高的，所以它只能用默认的 0 作为宽高。这个时候，如果你没有填写宽高属性，初始化默认宽高是 0，网络图片就展示不了。

```tsx
// 建议
<Image source={{uri: 'https://reactjs.org/logo-og.png'}}
       style={{width: 400, height: 400}} />

// 不建议
<Image source={{uri: 'https://reactjs.org/logo-og.png'}} />
```


### 缓存与预加载
React Native Android 用的是 *Fresco* 第三方图片加载组件的缓存机制，iOS 用的是 *NSURLCache* 系统提供的缓存机制。

Android 和 iOS 的缓存设置方式和实现原理虽然有所不同，但整体上采用了内存和磁盘的综合缓存机制。第一次访问时，网络图片是先加载到内存中，然后再落盘存在磁盘中的。

iOS 的 NSURLCache 遵循的是 HTTP 的 Cache-Control 缓存策略，同时当 CDN 图片默认都已经设置了 Cache-Control 时，iOS 图片就是有缓存的。而 NSURLCache 的默认最大内存缓存为 512kb，最大磁盘缓存为 10MB，如果缓存图片的体积超出了最大缓存的大小限制，那么一些老的缓存图片就会被删除。

React Native 也提供了非常方便的图片预加载接口 Image.prefetch：

```js
Image.prefetch(url);
```


### 宿主应用图片
宿主应用图片（Images From Hybrid App’s Resources​）指的是 React Native 使用 Android/iOS 宿主应用的图片进行加载的方式。在 React Native 和 Android/iOS *混合应用*中，也就是一部分是原生代码开发，一部分是 React Native 代码开发的情况下，可能会用到这种加载方式。

使用 Android drawable 或 iOS asset 文件目录中的图片资源时，可以直接通过统一资源名称 URN（Uniform Resource Name）进行加载。不过，使用 Android asset 文件目录中图片资源时，需要在指定它的统一资源定位符 URL（Uniform Resource Locator）。

*在 React Native 中，我们为什么要用 URI ，比如 `{ uri: 'app_icon' }`，来代表图片，而不是用更常用的 URL，比如 `{ url: 'app_icon' }`， 代表图片呢？*

这是因为，URI 代表的含义更广泛，它既包括 URN 这种用名称代表图片的方式，也包括用 URL 这种地址代表图片的方式。以 iOS 和 Android 宿主图片为例:

```tsx
// Android drawable 文件目录
// iOS asset 文件目录
<Image source={{ uri: 'app_icon' }} />

// Android asset 文件目录
<Image source={{ uri: 'asset:/app_icon.png' }} />
```


### Base64 图片
Base64 指的是一种基于 64 个可见字符表示二进制数据的方式，Base64 图片指的是使用 Base64 编码加载图片的方法，它适用于那些图片体积小或关键的场景。

```tsx
<Image
  source={{
    uri: 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADMAAAAzCAYAAAA6oTAqAAAAEXRFWHRTb2Z0d2FyZQBwbmdjcnVzaEB1SfMAAABQSURBVGje7dSxCQBACARB+2/ab8BEeQNhFi6WSYzYLYudDQYGBgYGBgYGBgYGBgYGBgZmcvDqYGBgmhivGQYGBgYGBgYGBgYGBgYGBgbmQw+P/eMrC5UTVAAAAABJRU5ErkJggg=='
  }}
/>
```

Base64 字符串的体积也要比二进制字节码的体积要大 1/3
二进制图片可以借助 Base64 进行转换。Base64 从 ASCII 256 个字符中选取了 64 个可见字符作为基础，这样就二进制就能以 Base64 的格式转换为 ASCII 字符串了，Base64 字符也是以 ASCII 码的形式存在。

> Base64 以 3 个字节作为一组，一共是 24 比特。将这 24 个比特分成 4 个单元，每个单元 6 个比特。每个单元前面加 2 个 0 作为补位，一共 8 个比特，凑整 1 个字符。原来的 24 比特，转换后就变成了 32 比特，因此转换后的体积就大了 1/3（ 1/3 = 1 - 24/32）。



### Image 组件 高级方法

1. `Image.getSize(uri, success, [failure])` 
2. `Image.queryCache(urls)` 
3. `Image.resolveAssetSource(source)` 

## Reference

