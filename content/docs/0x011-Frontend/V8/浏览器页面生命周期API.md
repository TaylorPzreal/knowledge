
Review
1. 2024-10-05 19:23

> [!Summary]
> [Page Lifecycle API](https://developer.chrome.com/docs/web-platform/page-lifecycle-api) 

## 一、Introduction

**Events**
- `DOMContentLoaded` DOM Tree构建完成
- `load` 所有资源加载完成
- `beforeunload` 正在离开，可以检查用户是否保存了更改并确认 
- `unload` 已离开
- `readystatechange` 
- `visibilitychange` 
- `pageshow` & `pagehide` 


**属性**
`document.readyState`  提供当前加载状态的信息
- `loading` —— 文档正在被加载。
- `interactive` —— 文档被全部读取。
- `complete` —— 文档被全部读取，并且所有资源（例如图片等）都已加载完成。


##### 1: `DOMContentLoaded` event
- 浏览器已经完全加载了HTML，并构建了DOM树。
- 此时，JavaScript 可以访问所有的DOM节点，初始化页面。
- **注意：** 样式表和图片等外部资源可能还没有加载完成。


> [!Caution] 不会阻塞 `DOMContentLoaded` 的脚本
> 1. 具有 `async`, `defer` 特性（attribute）的脚本不会阻塞 `DOMContentLoaded` 
> 2. 使用 `document.createElement('script')` 动态生成并添加到网页的脚本也不会阻塞 `DOMContentLoaded`。


###### `DOMContentLoaded` 和样式
外部样式表不会影响 DOM，因此 `DOMContentLoaded` 不会等待它们。

但这里有一个陷阱。如果在样式后面有一个脚本，那么该脚本必须等待样式表加载完成：

```html
<link type="text/css" rel="stylesheet" href="style.css">
<script>
  // 在样式表加载完成之前，脚本都不会执行
  alert(getComputedStyle(document.body).marginTop);
</script>
```

原因是，脚本可能想要获取元素的坐标和其他与样式相关的属性，如上例所示。因此，它必须等待样式加载完成。

##### 2: `load` event
- 浏览器不仅加载完成了HTML，还加载完成了所有外部资源（图片，样式等）。
- 此时，页面上的所有元素都已准备就绪。


##### 3: `beforeunload` event 

```js
window.onbeforeunload = function() {
  return false;
};
```

```js
window.addEventListener("beforeunload", (event) => {
  // 起作用，与在 window.onbeforeunload 中 return 值的效果是一样的
  event.returnValue = "有未保存的值。确认要离开吗？";
});
```


##### 4: `unload` event 

```js
let analyticsData = { /* 带有收集的数据的对象 */ };

window.addEventListener("unload", function() {
  navigator.sendBeacon("/analytics", JSON.stringify(analyticsData));
});
```

- 请求以 POST 方式发送。
- 我们不仅能发送字符串，还能发送表单以及其他格式的数据，但通常它是一个字符串化的对象。
- 数据大小限制在 64kb。


##### 5: `readystatechange` event 

###### document.readyState 属性
`document.readyState` 属性可以用来获取当前文档的加载状态。它有三个可能的值：
- **loading:** 文档正在被加载。
- **interactive:** 文档被全部读取，`DOMContentLoaded` 事件即将触发。
- **complete:** 文档和所有子资源已完成加载，`window.onload` 事件即将触发。


```js
document.addEventListener('readystatechange', () => {
  console.log(document.readyState);
});
```


##### 6: `visibilitychange` event
> 优先于 `pageshow` & `pagehide` 使用

This event fires with a `visibilityState` of `hidden` when a user navigates to a new page, switches tabs, closes the tab, minimizes or closes the browser, or, on mobile, switches from the browser to a different app. Transitioning to `hidden` is the last event that's reliably observable by the page, so developers should treat it as the likely end of the user's session

The transition to `hidden` is also a good point at which pages can stop making UI updates and stop any tasks that the user doesn't want to have running in the background.

```js
document.addEventListener("visibilitychange", () => {
  if (document.hidden) {
    playingOnHide = !audio.paused;
    audio.pause();
  } else {
    // Resume playing if audio was "playing on hide"
    if (playingOnHide) {
      audio.play();
    }
  }
});
```


##### 7: `pageshow` & `pagehide` event
- Initially loading the page
- Navigating to the page from another page in the same window or tab
- Restoring a frozen page on mobile OSes
- Returning to the page using the browser's forward or back buttons

> **Note:** During the initial page load, the `pageshow` event fires _after_ the `load` event.


## Reference
[页面生命周期](https://zh.javascript.info/onload-ondomcontentloaded) 

