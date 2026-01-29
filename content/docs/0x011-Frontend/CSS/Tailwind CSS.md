#css #Archive 

Review
1. 2023-06-03 10:23

## 一、Introduction
[Tailwind CSS](https://tailwindcss.com/) is a **utility-first** CSS framework that provides a comprehensive set of classes that can be used to style any HTML element. Unlike traditional CSS frameworks, Tailwind does not provide any pre-defined components or templates. **Instead, it allows developers to create custom styles by combining the available classes.**

This approach has a number of advantages. First, it allows developers to create highly customized designs that are not limited to the styles provided by the framework. Second, it can help to reduce the amount of CSS code that needs to be written. Third, it can make it easier to maintain and update CSS styles.

Tailwind CSS is a popular choice among web developers, and it is used by a wide range of companies, including Airbnb, Netflix, and Salesforce.

### Advantages
- **Flexibility:** Tailwind CSS is a very flexible framework, and it can be used to create a wide variety of designs.
- **Speed:** Tailwind CSS is very fast, and it can help to improve the performance of your website.
- **Simplicity:** Tailwind CSS is very easy to learn and use.
- **Community:** Tailwind CSS has a large and active community, which means that there are plenty of resources available to help you get started.

### Disadvantages
- **Learning curve:** Tailwind CSS has a bit of a learning curve, and it can take some time to get used to the way it works.
- **Overhead:** Tailwind CSS can add some overhead to your website, especially if you are not careful about how you use it.
- **Customization:** Tailwind CSS can be difficult to customize, and it can be hard to get the exact look and feel that you want.

### 相似框架
- TailwindCSS  69.1K
- UnoCSS  11.9K
- MasterCSS
- [Twind](https://github.com/tw-in-js/twind) 3.4K
- [TypeWind](https://github.com/Mokshit06/typewind) 2.1K
- [Stylify CSS](https://github.com/stylify/packages) 390

## 二、Usage for Web
其他搭配 **components** and **templates** libs
1. [Tailwind CSS UI](https://tailwindui.com/) 使用的是 [@headlessui/react](https://headlessui.dev/) [@heroicons/react](https://heroicons.com/)
2. [daisyUI](https://daisyui.com/) 
3. [Tailwind Elements](https://github.com/mdbootstrap/Tailwind-Elements) 
4. [FloatUI](https://github.com/MarsX-dev/floatui) Beautiful and responsive UI components and templates for React and Vue (soon) with Tailwind CSS.
5. [Tailwind Components](https://tailwindcomponents.com/) 
6. [prettier-plugin-tailwindcss 自动排序class名字](https://github.com/tailwindlabs/prettier-plugin-tailwindcss)

### 2.1: for Create React App
https://tailwindcss.com/docs/guides/create-react-app

```sh
npx create-react-app my-project
cd my-project

npm install -D tailwindcss
npx tailwindcss init
```

`tailwind.config.js` content
```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

`index.css` content
```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### 2.2: for Vite
```sh
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

 `tailwind.config.js` content
 ```js
 /** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

VS Code extension [Tailwind CSS IntelliSense](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss) 


## 三、Usage for React Native
1. [NativeWind](https://github.com/marklawlor/nativewind) 
2. [tailwind-react-native-classnames](https://github.com/jaredh159/tailwind-react-native-classnames) 
3. [Tailwind-rn](https://github.com/vadimdemedes/tailwind-rn) 



## Reference
1. [Tailwind CSS中文官网](https://www.tailwindcss.cn/) 
2. [Tailwind CSS Github](https://github.com/tailwindlabs/tailwindcss) 
3. [NnoCSS Github](https://github.com/unocss/unocss) 
4. [daisy UI Github](https://github.com/saadeghi/daisyui) 
5. [TailwindCSS VS UnoCSS](https://dev.to/mapleleaf/tailwindcss-vs-unocss-2a53) 
6. [PicoCSS 可直接使用，语义化HTML](https://github.com/picocss/pico)
7. [SmolCSS Minimal snippets for modern CSS layouts and components](https://smolcss.dev/)
