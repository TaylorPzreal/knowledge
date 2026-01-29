
Review
1. 2024-08-01 08:02

> [!Summary] 
> - 自定义 Hook 让你可以在组件间**共享逻辑**。
> - 自定义 Hook 命名必须以 `use` 开头，后面跟一个大写字母。
> - 自定义 Hook 共享的只是状态逻辑，不是状态本身。
> - 你可以将响应值从一个 Hook 传到另一个，并且他们会保持最新。
> - 每次组件重新渲染时，所有的 Hook 会重新运行。
> - 自定义 Hook 的代码应该和组件代码一样保持纯粹。
> - 把自定义 Hook 收到的事件处理函数包裹到 Effect Event。
> - 不要创建像 `useMount` 这样的自定义 Hook。保持目标具体化。

## 一、Introduction
> 1. **Hook 的名称必须以 `use` 开头，然后紧跟一个大写字母**，就像内置的 [`useState`](https://zh-hans.react.dev/reference/react/useState) 或者本文早前的自定义 `useOnlineStatus` 一样。Hook 可以返回任意值。
> 2. 自定义 Hook 共享的是**状态逻辑**，而不是状态本身，**对 Hook 的每个调用完全独立于对同一个 Hook 的其他调用**。

```jsx
function useOnlineStatus() {
  const [isOnline, setIsOnline] = useState(true);
  useEffect(() => {
    function handleOnline() {
      setIsOnline(true);
    }
    function handleOffline() {
      setIsOnline(false);
    }
    window.addEventListener('online', handleOnline);
    window.addEventListener('offline', handleOffline);
    return () => {
      window.removeEventListener('online', handleOnline);
      window.removeEventListener('offline', handleOffline);
    };
  }, []);
  return isOnline;
}
```


```jsx
function NetworkStatus() {
  const isOnline = useNetworkStatus();

  return (
    <div>
      <p>You are {isOnline ? 'online' : 'offline'}.</p>
    </div>
  );
}
```

## Reference
<https://react.dev/learn/reusing-logic-with-custom-hooks>
<https://www.robinwieruch.de/react-custom-hook/>
<https://utopia-insights.dev/react-custom-hooks-best-practices-and-examples/>

