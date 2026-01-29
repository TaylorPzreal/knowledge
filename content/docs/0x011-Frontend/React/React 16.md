
代码示例
```jsx
import React from 'react';
import ReactDOM from 'react-dom';

class Toggle extends React.Component {
  constructor(props) {
    super(props);
    this.state = {isToggleOn: true};

    // 为了在回调中使用 `this`，这个绑定是必不可少的
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick() {
    this.setState(state => ({
      isToggleOn: !state.isToggleOn
    }));
  }

  render() {
    return (
      <button onClick={this.handleClick}>
        {this.state.isToggleOn ? 'ON' : 'OFF'}
      </button>
    );
  }
}
ReactDOM.render(
  <Toggle />,
  document.getElementById('root')
);
```

1.  `ReactDOM.render` 函数是利用 `react-dom` 模块提供的能力将 `react` 组件渲染到 `web` 页面。
2.  点击事件通过 `setState` 修改组件的`state`，内部的机制是通过`react-reconciler`模块创建一个_更新对象_，并生成一个到期时间，然后遍历整个`fiber`树，更新每个fiber节点的到期时间，并找出最大的到期时间（优先级最高），根据这个时间判断是否是一个同步更新，如果是则直接开始调度；如果是一个异步更新，则生成一个_异步更新执行函数_丢给`scheduler`模块，该模块会根据浏览器每一帧是否有空闲时间来决定是否执行接收到的函数，并且接收到的每个函数都有一个到期时间，`scheduler`模块会根据到期时间来决定先执行哪个函数。需要注意的是_异步更新执行函数_的逻辑在`react-reconciler`模块中，`scheduler`模块是独立的不依赖 `react`,值得一提的是，`react-cache`也是基于`scheduler`模块实现的。


### 理念篇

#### 第一章 React理念

✅ React理念

✅ 老的React架构

✅ 新的React架构

✅ Fiber架构的心智模型

✅ Fiber架构的实现原理

✅ Fiber架构的工作原理

✅ 总结

#### 第二章 前置知识

✅ 源码的文件结构

✅ 调试源码

✅ 深入理解JSX

### 架构篇

#### 第三章 render阶段

✅ 流程概览

✅ beginWork

✅ completeWork

#### 第四章 commit阶段

✅ 流程概览

✅ before mutation阶段

✅ mutation阶段

✅ layout阶段

### 实现篇

#### 第五章 Diff算法

✅ 概览

✅ 单节点Diff

✅ 多节点Diff

#### 第六章 状态更新

✅ 流程概览

✅ 心智模型

✅ Update

✅ 深入理解优先级

✅ ReactDOM.render

✅ this.setState

#### 第七章 Hooks

✅ Hooks理念

✅ 极简Hooks实现

✅ Hooks数据结构

✅ useState与useReducer

✅ useEffect

✅ useRef

✅ useMemo与useCallback

#### 第八章 Concurrent Mode

✅ 概览

✅ Scheduler的原理与实现

✅ lane模型

📝 异步可中断更新

📝 高优任务打断机制

📝 batchedUpdates

📝 Suspense
