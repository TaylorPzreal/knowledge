
Review
1. 2024-08-04 15:05


> [!Summary] 核心仓库
> history <https://github.com/remix-run/history>
> react-router <https://github.com/remix-run/react-router>  仓库包括了 `router`, `react-router`, `react-router-dom`, `react-router-native` 等


## 一、Introduction
React Router is the most popular and fully-featured routing library for React-based SPAs. It comes with a lightweight size, easy-to-learn API, and well-written documentation so that every React developer can implement routing productively in any React app.

The `react-router-dom` package offers three higher-level, ready-to-use router components, as explained below:
- `BrowserRouter`: The `BrowserRouter` component handles routing by storing the routing context in the browser URL and implements backward/forward navigation with the inbuilt history stack
- `HashRouter`: Unlike `BrowserRouter`, the `HashRouter` component doesn’t send the current URL to the server by storing the routing context in the location hash (i.e., `index.html#/profile`)
- `MemoryRouter`: This is an invisible router implementation that doesn’t connect to an external location, such as the URL path or URL hash. The `MemoryRouter` stores the routing stack in memory but handles routing features like any other router


## 底层实现
- 历史管理(History API): React Router利用浏览器的History API来管理URL的变化。主要使用 `pushState()` 和 `replaceState()` 方法来更新URL,而不会触发页面刷新。
- 路由匹配: React Router使用一个路由匹配算法来决定哪个组件应该被渲染。它会比较当前URL路径与定义的路由规则,找出最佳匹配。
- 上下文(Context): React的 *Context API* 被用来在组件树中传递路由相关的信息,如当前location、history对象等。
- 组件渲染: 基于路由匹配的结果,React Router会渲染对应的组件。这通常通过条件渲染或者高阶组件来实现。
- 动态路由: React Router支持动态路由,允许在运行时添加或修改路由配置。
- 路由嵌套 通过组件组合的方式实现路由的嵌套,使得复杂的应用结构更容易管理。
- 编程式导航 提供API如 `history.push()` 或 `useNavigate()` hook来实现编程式导航。
- 路由参数和查询字符串解析 React Router能解析URL中的参数和查询字符串,并通过props或hooks提供给组件使用。

**核心流程简述：**
1. **URL 变化：** 用户点击链接或手动输入 URL。
2. **History API 更新：** React Router 拦截 URL 变化，通过 History API 更新浏览器历史记录。
3. **组件重新渲染：** React Router 根据新的 URL，重新渲染对应的组件。
4. **虚拟 DOM Diff：** React 对新的虚拟 DOM 和旧的虚拟 DOM 进行 Diff 比较。
5. **更新真实 DOM：** 根据 Diff 结果，高效地更新真实的 DOM。

### BrowserHistory

#### Navigation
To change the current location, you'll want to use one of the following:
- `history.push` - Pushes a new location onto the history stack
- `history.replace` - Replaces the current location with another
- `history.go` - Changes the current index in the history stack by a given delta
- `history.back` - Navigates one entry back in the history stack
- `history.forward` - Navigates one entry forward in the history stack






### HashHistory

**window.location.hash**
`hashchange` event


## Reference

