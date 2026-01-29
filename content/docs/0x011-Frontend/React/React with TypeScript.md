
Review
1. 2024-09-07 16:10

> [!Summary]
> 

## 一、Introduction

#####  1、Use `ReactNode` instead of `JSX.Element | null | undefined | ...` to keep your code more compact

```tsx
 type ReactElement = JSX.Element | null | undefined;
```

```tsx
type ReactElement = ReactNode;
```

##### 2、Simplify the typing of components expecting children props with `PropsWithChildren`

```tsx
// 🟠 Ok
const HeaderPage = ({ children,...pageProps }: { children: ReactNode } & PageProps) => {
  //   …
};

// ✅ Better
const HeaderPage = ({ children, ...pageProps } : PropsWithChildren<PageProps>) => {
//   …
};
```


##### 3、Access element props efficiently with `ComponentProps`, `ComponentPropsWithoutRef`,…

```tsx
const ButtonWithLogging = (props: ComponentProps<"button">) => {
  const handleClick: MouseEventHandler<HTMLButtonElement> = (e) => {
    console.log("Button clicked"); //TODO: Better logging
    props.onClick?.(e);
  };
  return <button {...props} onClick={handleClick} />;
};
```

This trick also works with custom components.
```tsx
const MyComponent = (props: { name: string }) => {
  //   …
};

const MyComponentWithLogging = (props: ComponentProps<typeof MyComponent>) => {
  //   …
};
```

##### 4、Leverage types like `MouseEventHandler`, `FocusEventHandler` and others for concise typings

Rather than typing the event handlers manually, you can use types like `MouseEventHandler` to keep the code more concise and readable.

```tsx
// 🟠 Ok
const MyComponent = ({ onClick, onFocus, onChange }: {
  onClick: (e: MouseEvent<HTMLButtonElement>) => void;
  onFocus: (e: FocusEvent<HTMLButtonElement>) => void;
  onChange: (e: ChangeEvent<HTMLInputElement>) => void;
}) => {
  //   …
};

// ✅ Better
const MyComponent = ({ onClick, onFocus, onChange }: {
  onClick: MouseEventHandler<HTMLButtonElement>;
  onFocus: FocusEventHandler<HTMLButtonElement>;
  onChange: ChangeEventHandler<HTMLInputElement>;
}) => {
  //   …
};
```

##### 5、Simplify your types with `ComponentType`
```ts
interface Size {
  width: number;
  height: number
};

interface Widget {
  title: string;
  Component: ComponentType<{ size: Size }>;
}
```

```tsx
const WidgetWrapper = ({ widget }: { widget: Widget }) => {
  const { Component, title } = widget;
  const { onClose, size, onResize } = useGetProps();

  return (
    <Wrapper onClose={onClose} onResize={onResize}>
      <Title>{title}</Title>
      {/* We can render the component below with the size */}
      <Component size={size} />
    </Wrapper>
  );
};
```

##### 6、Effortlessly type refs with the `ElementRef` type helper

There is a hard and easy way to type refs.
The hard way is to remember the element's type name and use it directly 🤣.

```tsx
const ref = useRef<HTMLDivElement>(null);
```

The easy way is to use the `ElementRef` type helper. This method is more straightforward since you should already know the element's name.
```tsx
const ref = useRef<ElementRef<"div">>(null);
```


## Reference

