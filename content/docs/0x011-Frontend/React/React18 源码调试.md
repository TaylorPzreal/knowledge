
Review
1. 2024-09-14 15:06

> [!Summary]
> 

## 一、Introduction



### Prerequisites
```sh
brew install autoconf
```

`node@18.20.1`
`yarn@1.22.22`

### Clone and build
```sh
git clone --depth 1 --branch v18.3.1 git@github.com:facebook/react.git react18
cd react18
yarn install
```

```sh
yarn run build-for-devtools-dev
```

output `build/node_modules` 

```sh
cd build/node_modules/react
yarn link

cd build/node_modules/react-dom
yarn link
```


### Create React App

```sh
npm create vite@latest react-debug -- --template react

cd react-debug
yarn install

yarn link react react-dom
yarn dev
```




## Reference
<https://dev.to/arnabchat90/debugging-react-source-code-with-a-react-client-app-1l7> 

