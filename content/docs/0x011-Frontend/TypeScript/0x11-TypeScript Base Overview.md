

Review
1. 2020-08-26
2. 2025-04-04 14:34

> [!Summary]
> 

## 一、Introduction
微软开发的开源编程语言。于2012年10月发布首个公开版本；
目前大型项目的标配

TS主要为了实现2个目标：
1. 为JS提供可选的类型系统；能提高代码质量、可读性和可维护性；有利于在编译时而不是运行时捕获错误；
2. 是JS的超集；兼容当前及未来的JS特性

DefinitedTyped社区定义了大多数流行的JS库的TypeScript声明模板，安装使用@types
declare关键字告诉TS，你正在试图表述一个在其他地方已经存在的代码；
对于没有声明的模块及变量的快速修复方法：`globals.d.ts`

```ts
declare var $:any; // 全局变量
declare let process: any;
declare const myPoing: { x: number; y: number; };
declare module 'foo' {}; // 模块
declare type JQuery = any; // 在某些内容上添加显示的注解，并且会在类型声明空间使用它；
declare module '*.css';
```

##### 编译上下文
`tsconfig.json`

##### 声明空间
1. 类型声明空间：用来当做类型注解；`class`, `interface`, `type`
2. 变量声明空间：用来当做变量的内容；`class`

##### 模块
1. 全局模块
2. 文件模块（外部模块）：在文件中含有import或export，那么文件中就创建了一个本地作用域。

根据 `tsconfig` 中 module 选项，把TypeScript编译成不同的JavaScript模块类型
- AMD：只能在浏览器工作
- SystemJS：这是一个好的实验，已经被ES模块代替。
- ES模块：还未准备好
- CommonJS：这个选项比较好；

##### 模块路径
- 相对模块路径
- 动态查找模块

##### 动态查找模块foo的顺序：
1. `./node_modules/foo`
2. `../node_modules/foo`
3. `../../node_modules/foo`
4. 一直查到系统的根目录

被检查的place，TS将会检查一下内容：
1. place表示一个文件，如 `foo.ts`
2. place是一个文件夹，并且存在一个文件 `foo/index.ts`
3. place是一个文件夹，存在 `foo/package.json` 文件，其中指定了 types 的文件路径
4. place是一个文件夹，存在 `foo/package.json` 文件，其中指定了 main的文件路径

##### 懒加载
require可以实现运行时加载文件。
所以应该在类型注解中使用导入的模块名称，在代码被编译成JS时，这些将会被移除；
应用场景：
1. Web App里，在特定路由上加载JS时
2. 在Node应用里，只想加载特定模块，用来加快启动速度时；

##### 命名空间

```ts
namespace Utility {
	export function log(msg){}
	export function error(msg) {}
}

Utility.log(‘test’);
Utility.error(‘test’);
```

命名空间支持嵌套。

##### 动态导入表达式

```ts
import() proposal for javascript
webpack可以通过此方法实现代码分割
require.ensure（不赞成使用了，非标准方法）
```

##### 类型系统
1. 基本类型注解：string, number, boolean
2. 数组注解：`number[]`
3. 接口注解：多个类型注解，合并成一个类型注解；`interface Name { first: string; second: string; }`
4. 内连类型注解：使用 `let；let name: {first: string; second: string;}`省去了为类型起名的麻烦；如果使用频繁，需要重构为接口或 `type alias`
5. 特殊类型：
    1. any：关闭类型检查，尽量不要使用；
    2. null，undefined：可以被赋值给任意类型的变量
    3. void：一个函数没有返回值
6. 泛型：`interface Array<T> { reverse(): T[]; }; function a<T> (items: T[]): T[]{}`
7. 联合类型注解：使用 | 作为类型注解；
8. 交叉类型：extends是一种非常常见的模式，可以根据两个对象创建一个新对象，新对象拥有两个对象所有的功能；
9. 元祖类型：`let nameNumber: [string, number]`
10. 类型别名：`type SomeName = someValidTypeAnnotation`

可以为任意类型注解提供类型别名；

##### 交叉类型：
```ts
function extend<T, U>(fiist: T, second: U): T & U {}
```

如果需要使用类型注解的层次结构，使用接口；它能使用implements和extends；类可以实现接口，接口可以自己实现继承；
当想给联合类型或交叉类型提供一个语义化的名称时，使用类型别名更好。

```ts
function a<T extends string>(o: Array<T>):{[K in T]: K}{}
```

可以使用 `keyof`, `typeof` 来生成字符串的联合类型；
```ts
const B = a(['North', 'South']);
```

// 创建一个类型
```ts
type B = keyof typeof B;
let c: B;
c = B.North;
c = ’North’;
```

##### 类型断言
- `<string>foo`: 不推荐，跟React一起使用时，有歧义；
- as：`foo = bar as any;`
类型断言之所以不被称为“类型转换”，是因为转换通常意味着某种运行时的支持。但是类型断言纯粹是一个编译时的语法。
尽量少用断言；
双重断言：
```ts
const element = (event as any) as HTMLElement;
```

##### 枚举
枚举是组织收集相关联变量的一种方式；枚举类型的值默认都是数字类型的，也称为数字枚举；

```ts
enum Card {
	red,
	green,
	yellow,
}

enum Book {
	A = ‘a’,
	B = ‘b’,
}
```

应用场景时做标记，检查条件是否为真。配合|&~;
- |=：添加标记
- &=和~：清除标记
- |：合并标记

常量枚举会有一个性能提升：
```ts
const enum TTTT {
	TRUE,
}
```


```ts
const lie = TTTT.TRUE; // 将会被编译成 const lie = 0;
```

可以使用enum + namespace的声明方式向枚举类型添加静态方法；需要定义相同的标识符；

安装TS会顺带安装一个lib.d.ts声明文件，该文件包含JS运行时DOM中的各种常见JS环境声明，如window，document，math，Window，Document；
lib分类如下：
JavaScrpt功能
1. es5
2. es6
3. es2015
4. es2016
5. es2017
6. ES2018
7. ES2019
8. ES2020
9. ESNext

运行环境：
1. dom
2. dom.iterable
3. webworker
4. WebWorker.ImportScripts
5. ScriptHost

函数可选参数：function foo(name?: string): void {}
函数重载：需要多次声明函数头，最后一个函数头是实现函数，需要与所有重载兼容；
函数类型定义：
1）接口定义
```ts
interface Complex {
	(foo: string): stirng;
	(foo: number): number;
}
```
可实现重载；


2）箭头函数
`(foo: number) => string;`
不能实现重载；

3）可实例化
```ts
interface Test {
	new () : string;
}
```
意味着你需要使用new关键字去调用它。

Freshness
更严格的对象字面量类型检查
之所以只对对象字面量类型检查，因为实际上那些并没有被用到的属性有可能会拼写错误或被误用；
典型用例：React state；

readonly标记对象属性；可以在接口和类型别名里面使用；

变体
类型兼容性的分析；
- 协变
- 逆变
- 双向协变
- 不变

never（是底部类型）
永远不会发生的事情
- 一个从来不会有返回值的函数
- 一个总会抛出错误的函数


##### 类型移动
目的：无缝与JS高动态语言一起工作；
关键动机是，当改变了一个内容时，其他相关的内容都会自动更新；
1. 复制类型和值：`namespace importing{ export class Foo{}}; import Bar = importing.Foo;  let bar: Bar;`
2. 捕获变量类型：（变量）`let foo =123; let bar: typeof foo;`
3. 捕获类成员类型：`class Foo { foo: number }; declare let _foo: Foo; let bar: typeof _foo.foo;`
4. 捕获字符串类型：(常量) `const foo = ''; let bar: typeof foo;`
5. 捕获键的名称：`keyof typeof`

##### ThisType
可以在对象字面量中输入this；

非空断言操作符：`!`

```ts
e!.name; // 断言e是非null；
```

配合Jest测试库
```sh
jest, @types/jest, ts-jest(ts预处理器), enzyme, @types/enzyme, enzyme-to-json, enzyme-adapter-react-16
Prettier, husky, conventional-changelog, standard-version;
eslint eslint-plugin-react @typescript-eslint/parser @typescript-eslint/eslint-plugin
```

谨慎使用 — outFile
对于大部分使用者来说，命名空间可以用模块来替代。
Barrel就像一个容器，他的作用就是把分散在多个模块的导出合并到一个模块里。


##### 代码风格与代码约定
1. camelCase命名：变量，函数名，类属性方法，接口成员，
2. PascalCase命名：类名，接口，类型别名，命名空间，枚举类型
3. 单引号
4. 2空格缩紧
5. 使用分号
6. 需要联合类型或交叉类型，使用type
7. 想用extends或implements，使用interface

##### TypeScript编译原理
1. Scanner扫描器
2. Parser解析器
3. Binder绑定器
4. Checker检查器
5. Emitter发射器


## Reference
- 《深入浅出TypeScript》
- tsconfig: https://www.typescriptlang.org/tsconfig

