
网页性能瓶颈
- CPU: 当遇到大计算量的操作或者设备性能不足使页面掉帧，导致卡顿
- IO: 发送网络请求后，由于需要等待数据返回才能进一步操作导致不能快速响应


Review
1. 2024-08-25 09:44

> [!Summary]
> 

## 一、Introduction

##### React Fiber:
- **Core algorithm:** It's the heart of React's rendering mechanism, designed to be more efficient and interruptible than the previous stack reconciliation.
- **Data structure:** It represents the React component tree as a linked list of fiber nodes, each containing information about the component's type, props, and state.
- **Work in progress:** React creates a work in progress fiber tree during reconciliation, allowing for incremental updates and prioritizing high-priority tasks.
- **Scheduler integration:** It works closely with the Scheduler API to prioritize and schedule rendering work based on user interactions and application priorities.

##### Reconciliation:
- **Process:** It's the process of comparing the current state of the React component tree with the desired state and updating the DOM accordingly.
- **Efficiency:** Fiber's incremental updates and prioritization make reconciliation more efficient, especially for large and complex applications.
- **Virtual DOM:** It uses a virtual DOM representation of the UI to minimize direct DOM manipulations, improving performance.

##### Virtual DOM
> 根据自变量变化，计算出UI变化的技术
- **Representation:** It's a lightweight, in-memory copy of the actual DOM.
- **Comparison:** React compares the virtual DOM with the previous state to identify changes.
- **Minimal updates:** Only the necessary DOM updates are applied, reducing overhead and improving performance.

##### Render:
- **Phase:** It's the initial phase of reconciliation where React creates a work in progress fiber tree and updates the state of components.
- **Prioritization:** React prioritizes rendering based on user interactions and application priorities.
- **Interruptibility:** Fiber allows rendering to be interrupted and resumed, ensuring responsiveness and preventing UI freezes.

##### Commit:
- **Phase:** It's the final phase of reconciliation where React applies the necessary DOM updates to the actual DOM.
- **Layout effects:** React executes layout effects, such as component mounting or updating, during the commit phase.
- **User interactions:** React synchronizes with the browser's event loop to ensure that user interactions are handled promptly.

##### Lanes:
- **Prioritization:** They are a mechanism for prioritizing different types of updates based on their importance.
- **Work units:** Each lane represents a different priority level, allowing React to focus on high-priority updates while deferring lower-priority ones.
- **Scheduling:** The Scheduler uses lanes to schedule rendering work based on the priority of updates.

##### Scheduler:
- **Prioritization:** It's a browser API that allows developers to prioritize tasks and schedule them for execution.
- **Integration:** React integrates with the Scheduler to prioritize rendering work based on user interactions and application priorities.
- **Interruptibility:** It allows rendering to be interrupted and resumed, ensuring responsiveness and preventing UI freezes.

##### ReactElement
`createElement` 返回值
```jsx
const element = <App />;
```

**ReactComponent**
函数或类组件，是**一种概念或形式**

**FiberNode**
Fiber架构的工作单元，一般情况下与 **ReactElement** 对应，上方 `element` 有对应的 `FiberNode` 


##### 受控组件
“如果一个表单元素的值是由React来管理的，那么它就是一个受控组件”

##### 非受控组件
使用受控组件虽然保证了表单元素的状态也由React统一管理，但需要为每个表单元素定义onChange事件的处理函数，然后把表单状态的更改同步到React组件的state，这一过程是比较烦琐的，一种可替代的解决方案是使用非受控组件。非受控组件指表单元素的状态依然由表单元素自己管理，而不是交给React组件管理。使用非受控组件需要有一种方式可以获取到表单元素的值，React中提供了一个特殊的属性ref，用来引用React组件或DOM元素的实例，因此我们可以通过为表单元素定义ref属性获取元素的值。使用defaultValue属性指定默认值。

```jsx
<input defaultValue="something" type="text" ref={(input) => this.input = input} />
```

##### Render Props
Render prop是指组件的使用者通过组件暴露的函数属性来参与定制渲染相关的逻辑。
```js

import React from "react";
class Loader extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      loading: true,
      data: {},
    };
  }
  componentDidMount() {
    fetch(url)
      .then((res) => res.json())
      .then(({ data }) => this.setState({ data }))
      .finally(() => this.setState({ loading: false }));
  }
  render() {
    if (this.state.loading) {
      return <div>Loading...</div>;
    }
    return this.props.renderData(this.state.data);
  }
}

function Container() {
  return (
    <Loader
      renderData={(data) => <div>{JSON.stringify(data)}</div>}
    />
  )
}
```

##### HOC


##### Compound components
Compound components是指通过多个组件的组合来完成特定任务，这些组件通过共享的状态、逻辑进行关联。典型的例子是Select和Select.Option组件。

```jsx
import React from 'react';
const SelectContext = React.createContext({});

export function Select({ value, onChange, children }) {
  const [open, setOpen] = React.useState(false);
  const [val, setValue] = React.useState(value);

  return (
    <div className={`select`}>
      <div
        className='select-value'
        onClick={() => {
          setOpen(true);
        }}
      >
        {val}
      </div>
      <SelectContext.Provider
        value={{
          value: val,
          setOpen,
          setValue: (newValue) => {
            setValue(newValue);
            if (value !== newValue) {
              onChange(newValue);
            }
          },
        }}
      >
        {open && children}
      </SelectContext.Provider>
    </div>
  );
}

function Option({ children, value }) {
  const {
    setOpen,
    setValue,
    value: selectedValue,
  } = React.useContext(SelectContext);
  return (
    <div
      className={`select-option ${value === selectedValue ? 'selected' : ''}`}
      onClick={() => {
        setValue(value);
        setOpen(false);
      }}
    >
      {children}
    </div>
  );
}

function OptionGroup({ children, label }) {
  return (
    <div className='select-option-group'>
      <div className='select-option-group-label'>{label}</div>
      {children}
    </div>
  );
}

Select.Option = Option;
Select.OptionGroup = OptionGroup;

function Demo() {
  const [city, setCity] = React.useState('北京市');
  return (
    <Select value={city} onChange={setCity}>
      <Select.Option value='北京市'>北京市</Select.Option>
      <Select.OptionGroup label='河北省'>
        <Select.Option value='石家庄市'>石家庄市</Select.Option>
        <Select.Option value='保定市'>保定市</Select.Option>
      </Select.OptionGroup>
    </Select>
  );
}

```

## Reference

