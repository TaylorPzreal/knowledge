
Review
1. 2024-07-29 23:16

> [!Summary]
> - Context 使组件向其下方的整个树提供信息。
> - 传递 Context 的方法:
>     1. 通过 `export const MyContext = createContext(defaultValue)` 创建并导出 context。
>     2. 在无论层级多深的任何子组件中，把 context 传递给 `useContext(MyContext)` Hook 来读取它。
>     3. 在父组件中把 children 包在 `<MyContext.Provider value={...}>` 中来提供 context。
> - Context 会穿过中间的任何组件。
> - Context 可以让你写出 “较为通用” 的组件。
> - 在使用 context 之前，先试试传递 props 或者将 JSX 作为 `children` 传递。
> 
> Libs
> [constate](https://github.com/diegohaz/constate) React Context + State


> [!Summary] 使用场景
> 替代 passing props
> Global state

## 一、Introduction
Usually, you will pass information from a parent component to a child component via props. But passing props can become verbose and inconvenient if you have to pass them through many components in the middle, or if many components in your app need the same information. _Context_ lets the parent component make some information available to any component in the tree below it—no matter how deep—without passing it explicitly through props.


```jsx
import { createContext } from 'react';

export const LevelContext = createContext(1);
```


```jsx
import { useContext } from 'react';
import { LevelContext } from './LevelContext.js';

export default function Section({ children }) {
  const level = useContext(LevelContext);
  return (
    <section className="section">
      <LevelContext.Provider value={level + 1}>
        {children}
      </LevelContext.Provider>
    </section>
  );
}
```

```jsx
import { useContext } from 'react';
import { LevelContext } from './LevelContext.js';

export default function Heading({ children }) {
  const level = useContext(LevelContext);
  switch (level) {
    case 0:
      throw Error('Heading 必须在 Section 内部！');
    case 1:
      return <h1>{children}</h1>;
    case 2:
      return <h2>{children}</h2>;
    case 3:
      return <h3>{children}</h3>;
    case 4:
      return <h4>{children}</h4>;
    case 5:
      return <h5>{children}</h5>;
    case 6:
      return <h6>{children}</h6>;
    default:
      throw Error('未知的 level：' + level);
  }
}
```


## Reference
https://react.dev/learn/passing-data-deeply-with-context
https://www.robinwieruch.de/react-state-usereducer-usestate-usecontext/

