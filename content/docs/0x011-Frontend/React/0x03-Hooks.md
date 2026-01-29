
Review
1. 2021/01/04
2. 2023/02/04
3. 2023/06/03
4. 2024-07-29 10:07

> [!Summary]
> Hooks are functions that let you “hook into” React state and lifecycle features from function components. Hooks don't work inside classes.


> [!Summary] Awesome Third Hooks
> - awesome react hooks <https://github.com/rehooks/awesome-react-hooks> 
> - useHooks https://github.com/uidotdev/usehooks
> - **react-use** https://github.com/streamich/react-use
> - **react-hook-form** https://github.com/react-hook-form/react-hook-form
> - **query(For fetching)** https://github.com/TanStack/query
> - usehooks-ts https://github.com/juliencrn/usehooks-ts
> - ahooks https://github.com/alibaba/hooks
> - use-http https://github.com/ava/use-http
> - react-hanger <https://github.com/kitze/react-hanger>
> - react-hooks-lib <https://github.com/beizhedenglong/react-hooks-lib> 
> - react-recipes(hooks utility libs) <https://github.com/craig1123/react-recipes> 
> - scriptkavi-hooks <https://github.com/scriptkavi/hooks> 
> - use-immer(`useImmer`, `useImmerReducer`) <https://github.com/immerjs/use-immer>


> [!Important] Best Pratices
> 1. **Use Hooks at the Top Level**: Always call Hooks at the top level of your React function, before any early returns. This ensures that Hooks are called in the same order each time a component renders.
> 2. **Only Call Hooks from React Functions**: Hooks should only be called from React function components or custom Hooks, not from regular JavaScript functions.
> 3. **Keep Hooks Pure**: Hooks should not cause side effects. Use useEffect for side effects like data fetching or subscriptions.
> 4. Optimize Performance: Use useMemo and useCallback to memoize expensive calculations and functions to avoid unnecessary re-renders.
> 5. Encapsulate Logic in Custom Hooks: If you find yourself using the same logic in multiple components, consider creating a custom Hook to encapsulate that logic.
> 6. Use Dependency Arrays in useEffect: Always specify dependencies in useEffect to avoid unnecessary re-runs of the effect.
> 7. Avoid Overusing State: Use state sparingly and only when necessary. Too many state variables can make your component complex and hard to manage.

## 一、Introduction
Functions starting with `use` are called _Hooks_
_Hook_ 是 **React 16.8** 的新增特性，它可以在不编写 class 的情况下使用 state 以及其他的 React 特性。

1. useState
2. useEffect
3. useContext
4. useReducer
5. useMemo
6. useCallback
7. useRef
8. useImperativeHandle
9. useDebugValue
10. useDeferredValue
11. useId
12. useLayoutEffect
13. useInsertionEffect
14. useSyncExternalStore
15. useTransition
16. CustomHooks


### 1: useState
**useState**：定义变量，可以理解为他是类组件中的this.state
```jsx
const [state, setState] = useState(initialState);
```

```jsx
// 惰性初始化state
const [state, setState] = useState(() => {
  const initialState = someExpensiveComputation(props);
  return initialState;
});
```

### 2: useEffect
useEffect：副作用，你可以理解为是类组件的生命周期，也是我们最常用的钩子

**副作用（Side Effect）**：是指 function 做了和本身运算返回值无关的事，如请求数据、修改全局变量，打印、数据获取、设置订阅以及手动更改 React 组件中的 DOM 都属于副作用操作都算是副作用

```jsx
useEffect(() => {
  console.log('挂载');
  return () => {
    console.log('卸载');
  };
}, []);

useEffect(() => {
  console.log('count改变才会执行');
}, [count]);
```

### 3: useContext
**useContext**：上下文，类似于Context：其本意就是设置全局共享数据，使所有组件可跨层级实现共享。

useContext的参数一般是由**createContext**的创建，通过 **CountContext.Provider** 包裹的组件，才能通过 useContext 获取对应的值

```jsx
import React, { useState, createContext, useContext } from 'react';
import { Button } from 'antd-mobile';

const CountContext = createContext(-1);

const Child = () => {
  const count = useContext(CountContext);

  return (
    <div style={{ marginTop: 20 }}>
      子组件获取到的count:{count}
      <Son />
    </div>
  );
};

const Son = () => {
  // !Important
  const count = useContext(CountContext);
  return <div style={{ marginTop: 20 }}>孙组件获取到的count:{count}</div>;
};

const Index = () => {
  const [count, setCount] = useState(0);

  return (
    <div style={{ padding: 20 }}>
      <div>父组件：{count}</div>

      <Button color='primary' onClick={() => setCount((v) => v + 1)}>
        点击加1
      </Button>

      <CountContext.Provider value={count}>
        <Child />
      </CountContext.Provider>
    </div>
  );
};

export default Index;
```

### 4: useReducer
**useReducer**：它类似于redux功能的api

> - [`useReducer`](https://react.dev/reference/react/useReducer) declares a state variable with the update logic inside a reducer function.

```jsx
const [state, dispatch] = useReducer(reducer, initialArg, init);
```

- state：更新后的state值
- dispatch：可以理解为和useState的setState一样的效果
- reducer：可以理解为redux的reducer
- initialArg：初始值
- init：惰性初始化

```jsx
import React, { useReducer } from 'react';
import { Button } from 'antd-mobile';

const Index = () => {
  const [count, dispatch] = useReducer((state, action) => {
    switch (action?.type) {
      case 'add':
        return state + action?.payload;
      case 'sub':
        return state - action?.payload;
      default:
        return state;
    }
  }, 0);

  return (
    <div style={{ padding: 20 }}>
      <div>count：{count}</div>

      <Button
        color='primary'
        onClick={() => dispatch({ type: 'add', payload: 1 })}
      >
        加1
      </Button>

      <Button
        color='primary'
        style={{ marginLeft: 8 }}
        onClick={() => dispatch({ type: 'sub', payload: 1 })}
      >
        减1
      </Button>
    </div>
  );
};
export default Index;
```

### 5: useMemo
**useMemo**: 与**memo**的理念上差不多，都是判断是否满足当前的限定条件来决定是否执行callback函数，而useMemo的第二个参数是一个数组，通过这个数组来判定是否更新回调函数。

> **useMemo** is used to memoize values, React **memo** is used to wrap React components to prevent re-renderings.
> **useMemo** is used to memoize values, **useCallback** is used to memoize functions.

当一个父组件中调用了一个子组件的时候，父组件的 state 发生变化，会导致父组件更新，而子组件虽然没有发生改变，但也会进行更新。

简单的理解下，当一个页面内容非常复杂，模块非常多的时候，函数式组件会**从头更新到尾**，只要一处改变，所有的模块都会进行刷新，这种情况显然是没有必要的。

我们理想的状态是各个模块只进行自己的更新，不要相互去影响，那么此时用useMemo是最佳的解决方案。这里要尤其注意一点，**只要父组件的状态更新，无论有没有对子组件进行操作，子组件都会进行更新**，useMemo就是为了防止这点而出现的。

```jsx
import { useMemo } from 'react';

const Index = (list) => {
  return useMemo(
    () =>
      list.map((item) => {
        console.log(1);
        return Math.pow(item, 2);
      }),
    []
  );
};
export default Index;
```

### 6: useCallback
useCallback与useMemo极其类似,可以说是一模一样，唯一不同的是useMemo返回的是函数运行的**结果**，而useCallback返回的是**函数**

注意：这个函数是父组件传递子组件的一个函数，防止做无关的刷新，其次，这个组件必须配合memo,否则**不但不会提升性能，还有可能降低性能**。

```jsx
import React, { useState, useCallback } from 'react';
import { Button } from 'antd-mobile';

const MockMemo = () => {
  const [count, setCount] = useState(0);
  const [show, setShow] = useState(true);

  const add = useCallback(() => {
    setCount(count + 1);
  }, [count]);

  return (
    <div>
      <div style={{ display: 'flex', justifyContent: 'flex-start' }}>
        <TestButton title='普通点击' onClick={() => setCount(count + 1)} />
        <TestButton title='useCallback点击' onClick={add} />
      </div>
      <div style={{ marginTop: 20 }}>count:{count}</div>
      <Button
        onClick={() => {
          setShow(!show);
        }}
      >
        切换
      </Button>
    </div>
  );
};

const TestButton = React.memo((props) => {
  console.log(props.title);
  return (
    <Button
      color='primary'
      onClick={props.onClick}
      style={
        props.title === 'useCallback点击'
          ? {
              marginLeft: 20,
            }
          : undefined
      }
    >
      {props.title}
    </Button>
  );
});

export default MockMemo;
```

可以单独使用useCallback，但只用useCallback起不到优化的作用，反而会增加性能消耗。像之前讲的，React.memo会通过浅比较里面的props，如果没有memo，那么使用的useCallback也就毫无意义，因为useCallback本身是需要开销的，所以反而会增加性能的消耗。

### 7: useRef
**useRef**：可以获取当前元素的所有属性，并且返回一个可变的ref对象，并且这个对象只有current属性，可设置initialValue。

> useRef is a React hook that provides a way to create a **mutable reference** that persists across component re-renders. It stores a value that doesn’t cause re-renders when it changes.
> It can be used to access a DOM element directly.
> **Changing a ref does not trigger a re-render.**
> - You can **store information** between re-renders (unlike regular variables, which reset on every render).
> - Changing it **does not trigger a re-render** (unlike state variables, which trigger a re-render).
> - The **information is local** to each copy of your component (unlike the variables outside, which are shared).

```jsx
const refContainer = useRef(initialValue);
```

useRef可以获取对应元素的属性，但useRef还具备一个功能，就是缓存数据。

> 不能在函数组件中使用 createRef，因为每次函数组件渲染都是一次新的函数执行，每次执行 createRef 得到的都是一个新的对象，无法保留其原来的引用。

所以在函数组件中，我们会使用 useRef 创建 Ref 对象，React 会将 useRef 和函数组件对应的 fiber 对象关联，将 useRef 创建的 ref 对象挂载到对应的 fiber 对象上，这样一来每次函数组件执行，只要函数组件不被销毁，那么对应的 fiber 对象实例也会一直存在，所以 ref 也能够被保留下来。

callback ref
ref 属性传递函数时，会在 commit 阶段创建真实 DOM 时执行 ref 指定的函数，并将元素作为第一个参数传入，此时我们就可以利用它进行赋值以获取 DOM 元素或组件实例。

forwardRef
```jsx
import { forwardRef } from 'react';

const MyInput = forwardRef(function MyInput(props, ref) {
  const { label, ...otherProps } = props;
  return (
    <label>
      {label}
      <input {...otherProps} ref={ref} />
    </label>
  );
});

function Form() {
  const ref = useRef(null);

  function handleClick() {
    ref.current.focus();
  }

  return (
    <form>
      <MyInput label="Enter your name:" ref={ref} />
      <button type="button" onClick={handleClick}>
        Edit
      </button>
    </form>
  );
}
```


### 8: useImperativeHandle
**useImperativeHandle**：可以让你在使用 ref 时自定义暴露给父组件的实例值。

> `useImperativeHandle` is a React Hook that lets you customize the handle exposed as a ref.

**使用场景**
在一个页面很复杂的时候，我们会将这个页面进行模块化，这样会分成很多个模块，有的时候我们需要在最外层的组件上控制其他组件的方法，希望最外层的点击事件，同时执行子组件的事件，这时就需要useImperativeHandle 的帮助。

```jsx
useImperativeHandle(ref, createHandle, [deps])
```

- ref：useRef所创建的ref
- createHandle：处理的函数，返回值作为暴露给父组件的 ref 对象。
- deps：依赖项，依赖项更改形成新的 ref 对象。

```jsx
import React, { useState, useImperativeHandle, useRef } from 'react';
import { Button } from 'antd-mobile';

const Child = ({ cRef }) => {
  const [count, setCount] = useState(0);

  useImperativeHandle(cRef, () => ({
    add,
  }));

  const add = () => {
    setCount((v) => v + 1);
  };

  return (
    <div style={{ marginBottom: 20 }}>
      <p>点击次数：{count}</p>

      <Button color='primary' onClick={() => add()}>
        加1
      </Button>
    </div>
  );
};

const Index = () => {
  const ref = useRef(null);

  return (
    <div style={{ padding: 20 }}>
      <div>注意:是在父组件上的按钮，控制子组件的加1哦～</div>
      <Button color='primary' onClick={() => ref.current.add()}>
        父节点上的加1
      </Button>
      <Child cRef={ref} />
    </div>
  );
};
export default Index;
```


### 9: useDebugValue
`useDebugValue` is a React Hook that lets you add a label to a custom Hook in React DevTools.

> Don’t add debug values to every custom Hook. It’s most valuable for custom Hooks that are part of shared libraries and that have a complex internal data structure that’s difficult to inspect.

```jsx
useDebugValue(value, format?)
```

```jsx
import { useDebugValue } from 'react';

function useOnlineStatus() {
  // ...
  useDebugValue(isOnline ? 'Online' : 'Offline');
  // ...
}
```


### 10: useDeferredValue
`useDeferredValue` is a React Hook that lets you defer updating a part of the UI.

```jsx
const deferredValue = useDeferredValue(value)
```

Usage
1. Showing stale content while fresh content is loading
2. Indicating that the content is stale
3. Deferring re-rendering for a part of the UI

> Use the `useDeferredValue` hook to display the previous query results until the new results become available

### 11: useId
`useId` is a React Hook for generating unique IDs that can be passed to accessibility attributes.

```jsx
const id = useId()
```

However, hardcoding IDs like this is not a good practice in React. A component may be rendered more than once on the page—but IDs have to be unique! Instead of hardcoding an ID, generate a unique ID with `useId`:

```jsx
import { useId } from 'react';

function PasswordField() {
  const passwordHintId = useId();
  return (
    <>
      <label>
        Password:
        <input type='password' aria-describedby={passwordHintId} />
      </label>
      <p id={passwordHintId}>
        The password should contain at least 18 characters
      </p>
    </>
  );
}

```



### 12: useLayoutEffect
**useLayoutEffect**：与useEffect基本一致，不同的地方时，**useLayoutEffect**是**同步**

要注意的是useLayoutEffect在 DOM 更新之后，浏览器绘制之前，这样做的好处是可以更加方便的修改 DOM，获取 DOM 信息，这样浏览器只会绘制一次，所以useLayoutEffect在useEffect之前执行。

如果是useEffect的话 ，useEffect 执行在浏览器绘制视图之后，如果在此时改变DOM，有可能会导致浏览器再次回流和重绘。

除此之外**useLayoutEffect**的 callback 中代码执行会阻塞浏览器绘制。

> `useLayoutEffect` can hurt performance. Prefer [`useEffect`](https://react.dev/reference/react/useEffect) when possible.

```jsx
useLayoutEffect(setup, dependencies?)
```

When an effect isn't caused by a user interaction, the user will see the UI before the effect runs (often briefly).

As a result, if the effect modifies the UI, the user will see the initial UI version very quickly before seeing the updated one, creating a visual glitch.

Using `useLayoutEffect` ensures the effect runs synchronously after all DOM mutations, preventing the initial render glitch.

### 13: useInsertionEffect


### 14: useSyncExternalStore
`useSyncExternalStore` is a React Hook that lets you subscribe to an external store.

`zustand` 基于此实现。

```js
const snapshot = useSyncExternalStore(subscribe, getSnapshot, getServerSnapshot?)
```

- **外部数据源:** `useSyncExternalStore` 允许我们从外部数据源（例如，自定义的状态管理库、WebSocket、GraphQL 客户端等）读取数据，并将这些数据同步到 React 组件中。
- **订阅机制:** 它提供了一种订阅外部数据源变化的机制。当外部数据源发生变化时，React 会自动重新渲染订阅了该数据源的组件。

优势
1. **性能优化:** `useSyncExternalStore` 提供了更细粒度的控制，可以避免不必要的重新渲染。
2. **灵活的订阅机制:** 可以自定义订阅函数，实现更复杂的订阅逻辑。


### 15: useTransition
`useTransition` hook allows you to mark certain updates as **transitions** so they can be deprioritized, allowing other, more urgent updates to be processed first. This ensures that the UI remains responsive during updates that might take some time.

```jsx
export default function App() {
  const [isPending, startTransition] = useTransition();
  const [page, setPage] = useState('home');

  function changePage(newPage: string) {
    startTransition(() => {
      setPage(newPage);
    });
  }

  return (
    <>
      <button onClick={() => changePage('home')}>Home</button>
      <button onClick={() => changePage('posts')}>Posts</button>
      <button onClick={() => changePage('contact')}>Contact</button>
      <hr />
      {isPending && <div>Loading...</div>}
      {page === 'home' && <Home />}
      {page === 'posts' && <Posts />}
      {page === 'contact' && <Contact />}
    </>
  );
}
```

### 16: customHooks
[[0x04-customHooks]]


## Reference

