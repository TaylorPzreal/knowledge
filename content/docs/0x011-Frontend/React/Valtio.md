
Review
1. 2024-10-01 12:38

> [!Summary]
> 

## 一、Introduction
Valtio 是一个基于 Proxy 实现的、极简的、灵活的状态管理工具。它可以让使用者拥有类 MobX 的使用体验，但实现上更加简单直观。

**Proxy 的核心作用**
Valtio 的核心在于对数据的代理。它通过 JavaScript 的 Proxy 对象来拦截对状态对象的访问和修改。当我们对代理对象进行操作时，Proxy 会捕获这些操作，并触发相应的更新机制。

```jsx
import { proxy, useSnapshot } from 'valtio';

const state = proxy({ count: 0 });

function Counter() {
  const snap = useSnapshot(state);

  return (
    <div>
      <p>Count: {snap.count}</p>
      <button onClick={() => state.count++}>+</button>
    </div>
  );
}
```

### Valtio 的工作原理
1. **创建代理对象:**
    - 使用 `proxy` 函数创建一个代理对象。
    - 这个代理对象是对原始状态对象的代理。
2. **拦截操作:**
    - 当我们对代理对象进行读写操作时，Proxy 会拦截这些操作。
    - 对于读取操作，Proxy 直接返回原始对象对应的值。
    - 对于写入操作，Proxy 会触发状态更新，并通知订阅者。
3. **通知订阅者:**
    - Valtio 内部维护了一个订阅者列表。
    - 当状态发生变化时，Valtio 会遍历订阅者列表，并调用每个订阅者的回调函数。
4. **组件更新:**
    - React 组件通过 `useSnapshot` Hook 订阅状态。
    - 当状态发生变化时，订阅的组件会重新渲染，从而实现 UI 的更新。

Valtio 使用 `useSyncExternalStore` 实现
- Valtio 利用 Proxy 来拦截对状态对象的访问和修改，从而实现状态的追踪。
- 当状态发生变化时，Valtio 会通知 `useSyncExternalStore` 的订阅函数。
- `useSyncExternalStore` 会触发组件的重新渲染，从而将最新的状态更新到组件中。
- 组件重新渲染，执行 `useSnapshot` 获取最新的状态

```js
import { useSyncExternalStore } from 'react';
import { proxy } from 'valtio';

const state = proxy({ count: 0 });

function useSnapshot(state) {
  const getSnapshot = () => state;
  const subscribe = (callback) => {
    // Valtio 内部实现：在状态变化时调用 callback
  };

  return useSyncExternalStore(subscribe, getSnapshot);
}
```


## Reference

