#css #Archive 

Review
1. 2023-06-03 12:31

## 一、Introduction
[UnoCSS](https://github.com/unocss/unocss) is an atomic CSS engine that provides an instant on-demand experience. It is inspired by `Windi CSS`, `Tailwind CSS`, and `Twind`. UnoCSS has a number of features that make it a powerful tool for web development, including:

- **Fully customizable:** No core utilities are provided, so all functionalities are provided via presets. This allows you to create a custom CSS system that meets your specific needs.
- **Instant:** UnoCSS is instant, which means that it does not require any parsing, AST, or scanning. This makes it much faster than other CSS engines.
- **Small:** UnoCSS is only about 6kb min+brotli, which makes it very lightweight.
- **Shortcuts:** UnoCSS provides a number of shortcuts that allow you to alias or group utilities dynamically. This can save you a lot of time and effort.
- **Attribuify mode:** UnoCSS allows you to group utilities in attributes. This can make your code more readable and maintainable.
- **Pure CSS Icons:** UnoCSS allows you to use any icon as a single class. This can make it easy to add icons to your websites and applications.
- **Variant Groups:** UnoCSS allows you to create shorthand for group utilities with common prefixes. This can make your code more concise and easier to read.
- **CSS Directives:** UnoCSS allows you to reuse utils in CSS with @apply directive. This can make your code more reusable and maintainable.
- **Compilation mode:** UnoCSS allows you to synthesize multiple classes into one at build time. This can make your CSS files smaller and faster.
- **Inspector:** UnoCSS provides an inspector that allows you to inspect and debug your CSS. This can be helpful for troubleshooting problems.
- **CSS-in-JS Runtime build:** UnoCSS can be used with CSS-in-JS frameworks like Vue.js and React. This can make it easy to use UnoCSS with your favorite framework.

### The difference between Tailwind CSS and UnoCSS
Tailwind CSS and UnoCSS are both utility-first CSS frameworks, but they have some key differences.

- **Tailwind CSS** is a more established framework with a larger community and more documentation. It is also more customizable, as you can create your own custom classes using Tailwind's syntax.
- **UnoCSS** is a newer framework that is designed to be more performant and easier to learn. ***Uno supports all of Tailwind*** and it also has a few features that Tailwind CSS does not, such as fluid columns and dynamic utilities.
- **Tailwind CSS** was created by Adam Wathan in 2016. It is a popular framework used by many developers, including those at companies like Airbnb and Netflix. Tailwind CSS is known for its small bundle size and its ability to be customized to fit any project.
- **UnoCSS** was created by Max Stoiber in 2021. It is a newer framework that is designed to be more performant and easier to learn than Tailwind CSS. UnoCSS uses a different syntax than Tailwind CSS, which some developers find easier to use.


|Feature|Tailwind CSS|UnoCSS|
|---|---|---|
|Performance|Good|Excellent|
|Learning curve|Steeper|Less steep|
|Customization|High|Low|
|Community|Large|Small|
|Features|Basic|Advanced|


## 二、Usage

### 2.1: for Vite

```sh
yarn add -D unocss
```

```ts
// vite.config.ts
import UnoCSS from 'unocss/vite'
import { defineConfig } from 'vite'

export default defineConfig({
  plugins: [
    UnoCSS(),
  ],
})
```

```ts
// uno.config.ts
import { defineConfig } from 'unocss'

export default defineConfig({
  // ...UnoCSS options
})
```

```ts
// main.ts
import 'virtual:uno.css'
```



## Reference
1. [Why UnoCSS](https://unocss.dev/guide/why) 
