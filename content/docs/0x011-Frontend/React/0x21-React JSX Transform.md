
Review
1. 2024-09-30 07:58

> [!Summary]
> [Introducing the New JSX Transform](https://legacy.reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html) 
> 1. 使用 `react/jsx-runtime` 中的 `jsx()` 替代之前的 `React.createElement()` 
> 2. Babel@8 默认启用，低版本需要自行配置
> 
> 优势
> 1. 不必再手动引入 React (`import React from 'react`)
> 2. 解决了 `React.createElement` 的历史问题，详见 [RFC](https://github.com/reactjs/rfcs/blob/createlement-rfc/text/0000-create-element-changes.md) ，更好的性能，更好的静态检查和类型检查

## 一、Introduction
> JSX -> ReactElement 的转换

##### Old JSX Transform (react@<17)
将 `JSX` 转换为 `React.createElement(...)` 调用

```jsx
import React from 'react';

function App() {
  return <h1>Hello World</h1>;
}
```

=> 

```jsx
import React from 'react';

function App() {
  return React.createElement('h1', null, 'Hello world');
}
```

缺点
- Because JSX was compiled into `React.createElement`, `React` needed to be in scope if you used JSX.
- There are some [performance improvements and simplifications](https://github.com/reactjs/rfcs/blob/createlement-rfc/text/0000-create-element-changes.md#motivation) that `React.createElement` does not allow.

##### New JSX Transform (react@≥17)

```jsx
function App() {
  return <h1>Hello World</h1>;
}
```

=>

```jsx
// Inserted by a compiler (don't import it yourself!)
import {jsx as _jsx} from 'react/jsx-runtime';

function App() {
  return _jsx('h1', { children: 'Hello world' });
}
```

> Note how our original code **did not need to import React** to use JSX anymore! (But we would still need to import React in order to use Hooks or other exports that React provides.)


> [!Warning] 温馨提示
> The functions inside `react/jsx-runtime` and `react/jsx-dev-runtime` must only be used by the compiler transform. If you need to manually create elements in your code, you should keep using `React.createElement`. It will continue to work and is not going away.


###### 优势
> Advantages of the New JSX Transform (`jsx()` function)

1. **Smaller Bundle Size**
   - Eliminates the need to import React in every file that uses JSX
   - Allows for more efficient tree-shaking, potentially reducing bundle size

2. **Slightly Better Performance**
   - The new transform is more efficient at creating React elements
   - Reduces the amount of generated code, leading to faster parsing and execution

3. **Future-Proofing**
   - Provides more flexibility for future optimizations in React
   - Allows React to change the implementation of JSX without breaking existing code

4. **Simplified Code**
   - No need to import React in every file using JSX
   - Cleaner code structure, especially in large projects with many components

5. **Better Developer Experience**
   - Faster refresh times in development mode
   - Improved error messages and warnings related to JSX usage

6. **Compatibility**
   - Works with all existing JSX code
   - Can be adopted gradually, allowing for incremental migration in large codebases

7. **Reduced Learning Curve**
   - Simplifies the mental model for new React developers
   - Aligns more closely with how other frameworks handle template compilation

8. **Improved Tooling Support**
   - Enables better static analysis and type checking of JSX code
   - Facilitates the development of more advanced React-specific development tools


##### 启用新的转换方案
```js
// If you are using @babel/preset-react
{
  "presets": [
    ["@babel/preset-react", {
      "runtime": "automatic"
    }]
  ]
}
```

```js
// If you're using @babel/plugin-transform-react-jsx
{
  "plugins": [
    ["@babel/plugin-transform-react-jsx", {
      "runtime": "automatic"
    }]
  ]
}
```


## Reference


