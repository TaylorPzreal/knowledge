
Review
1. 2023-02-17 23:13

## 总结
#### 现状
充满活力的完整的工具生态系统

近10年左右的Web生态发展，有些偏离正轨了，使用各种框架/库（React/Vue）开发，All in JS（从JSX，到CSS-in-JS，再到随处可见的JS First。），这通常会产出更大的JS，前端的有效负载变得比较大：
1. 对于用户来讲，在“可访问性”、“功能性”上，没有带来更好的提升；
2. 对于开发者而言，平均生产力也很难突破，大量的代码级复杂性、需要通过编译才能正常运行的网页、还有一些难以理解的运行时行为；
3. 越接近前端性能瓶颈，会发现很多问题都是由工具引起的，这些强大便利的工具，目标是解决问题，但最终所制造的问题要比解决的问题还多。使用工具的复杂性，已经超出了要解决的问题本身复杂性。

Web开发的根本目标，是**提供快速，稳定，安全，用户友好的界面，提升开发者的生产力**。

那么未来新的探索，可能是基于**Web-Native**开发，文章提出了一个Web原生开发理念，归根结底，Web 原生开发更多地依赖于 Web 平台而不是各种抽象框架！当然也不可能完全重构现有实现。
主要有2条线投入：
1. 低级工具：以平台为中心的倡议，用于标准化和纳入平台通用的 Web 开发架构和范式，获得原生级别的响应式和更强大的组件模型。
2. 更高级别的工具：以社区为中心的倡议，通过“Web-Native”库和框架扩展平台的低级别功能。

详细可以关注WebQit https://github.com/webqit 


## 一、Introduction
Frontend has an engineering problem!
*前端有工程问题！*

It is one field that has **forged** about the most **enviable** tooling ecosystem by **roughly** every measure - from growth rate to technical **wizardry** - and along with that an incredible amount of thought leadership on its every move, and ==yet at its bottom line==:
-   the average website performance is only **regressing with** us!
-   the average developer productivity is only **grinding** to a halt!

*这个领域几乎从每一项指标（从增长率到技术魔法）都打造了最令人羡慕的工具生态系统，并且在其一举一动中都有令人难以置信的思想领导力，但归根结底：*
- 网站的平均性能只会随着我们而倒退！
- 开发人员的平均生产力只会停滞不前！

==So it turns out==, all of that "vibrant ecosystem" isn't really translating to more "accessible", "functional" apps on the _user_ front, and neither to more "speed" and "productivity" on the _developer_ front!

*所以事实证明，所有这些“充满活力的生态系统”并没有真正转化为在用户端具有更好的“可访问”、“功能性”的应用程序，也没有转化为开发人员端具有更快的“速度”和更大的“生产力”！*

The closer you get to Frontend's **bottlenecks** and to how much of that is **tooling-induced** the more you are wondering if we just have created more problems with our tools than we've solved!

*您越接近前端的瓶颈，尤其其中有很多是由工具引起的，您就越想知道，用我们的工具制造的问题是否比我们解决的问题还多！*

## The Counterintuitive Equations!
*违反直觉的等式*

Consider how self-defeating it gets...
*想想他是如何弄巧成拙的...*

### ...on the _user_ front

Given [real world network and device-capability factors](https://infrequently.org/2017/10/can-you-afford-it-real-world-web-performance-budgets/#js-is-your-most-expensive-asset), performance starts with _**shipping less bytes**_, especially when it coms to JavaScript - [your most expensive asset](https://infrequently.org/2017/10/can-you-afford-it-real-world-web-performance-budgets/#js-is-your-most-expensive-asset). (Truth is, all of the extra things like **instant** navigations and transitions that will **delight** your users need your app to _first be accessible_!)

考虑到现实世界的网络和设备能力因素，性能从传输更少的字节开始，尤其是当涉及到 JavaScript——你最昂贵的资产时。 （事实上 ，所有额外的东西，如即时导航和过渡，想让您的用户满意，首先需要您的应用程序能够立刻可访问！）

Unfortunately, SPA frameworks, who have this as their primary call, have their engineering model going the _opposite_ way: **towards more JavaScript**! These may follow different programming paradigms... but ==all have got the same _JavaScript_ bottom-line==!
-   `[HTML, CSS, JS]` > `Build_Step` > `[JS, JS, JS]` e.g. Svelte, Vue
-   `[JS, JS, JS]` > `Build_Step` > `[JS, JS, JS]` e.g. React

不幸的是，将此作为主要调用的 SPA 框架，其工程模型正朝着相反的方向发展：转向更多 JavaScript！ 它们可能遵循不同的编程范式……但它们都具有相同的 JavaScript 底线！


> Your final bundle here is the sum of your _framework_ bundle, plus your **_essential_** JS, plus the _induced_ (usually larger) JS from page structure, content, and styling - the obvious math to Frontend's [terrifying payloads](https://httparchive.org/reports/page-weight#bytesJs)!

这里的最终包是框架包的总和，加上基本的 JS，再加上从页面结构、内容和样式中引入的（通常更大的）JS——前端可怕的有效负载是显而易见的！

With your application's entire weight now **culminating** in JavaScript... and its non-JS aspects - page structure, content, and styling - now being accounted for in JS, you're now wrongly set up for the real world! It soon becomes clear how much of a knife edge you're on as your application becomes a real thing and starts to **regress** with every weight gained!

*现在你的应用程序的全部重量在 JavaScript 中达到顶峰……及其非 JS 方面——页面结构、内容和样式——现在也被考虑在 JS 中，你现在错误地为现实世界做了准备！ 随着您的应用程序成为真实的东西并随着每增加一次体重而开始倒退，您很快就会清楚自己处于多大的刀刃上！*

Not surprising... the idea of a "highly-optimized", "accessible", "functional" application ==quickly falls apart==!

*不足为奇……“高度优化”、“可访问”、“功能性”应用程序的想法很快就会土崩瓦解！*

Reporting on this in the 2017 Real-world Web Performance Budgets ([here](https://dev.to/oxharris/rethinking-the-modern-web-5cn1#:~:text=real%20world%20network%20and%20device-capability%20factors)), Alex Russell [relates](https://infrequently.org/2017/10/can-you-afford-it-real-world-web-performance-budgets/#:~:text=i%27ve%20seen%20teams%20that%20have,%20faster%22%20experiences%20under%20real-world%20conditions.):

> _"I've seen teams that have just finished re-building on a modern tech stack **cringe** for an hour as we walk them through the experience of using their 'better', 'faster' experiences under real-world conditions."_

*在 2017 年真实世界Web性能预算（此处）中对此进行了报告，Alex Russell 提到：
“我见过一些团队，他们在现代技术堆栈上完成了重建，但他们畏缩了一个小时，因为我们引导他们体验了在真实条件下，使用他们‘更好’、‘更快’的体验。”*

Tim Kadlec also [notes from field experience](https://timkadlec.com/remembers/2020-04-21-the-cost-of-javascript-frameworks/#:~:text=what%20is%20clear%3A%20right%20now%2C%20if%20you%E2%80%99re%20using%20a%20framework,in%20the%20best%20of%20scenarios.&text=if%20you%20are%20going%20to%20use%20one%20of%20these%20frameworks,meantime.):

> _"What is clear: right now, if you’re using a framework to build your site, you’re making a trade-off in terms of initial performance—even in the best of scenarios. If you are going to use one of these frameworks, then you have to take extra steps to make sure you don’t negatively impact performance in the meantime."_


*Tim Kadlec 还根据现场经验指出：*
> “很明显：现在，如果您使用框架来构建您的网站，那么您将在初始性能方面做出权衡——即使是在最好的情况下。要使用这些框架之一，则必须采取额外的步骤以确保同时不会对性能产生负面影响。”

It is often excluded in the **conversation**, but many are **winding up** with more tooling-induced performance problems than they ever would otherwise! How entirely **counterproductive**!

*它经常被排除在谈话中，但很多人最终都遇到了比以往任何时候都多的由工具引起的性能问题！ 多么的适得其反！*

### ...on the _developer_ front

Performance is all about being able to **tame** complexity with the least amount of overhead. This calls for the abstractions/tools for managing complexity to hold to "a '**first do no harm**' principle... make sure you are at least no less productive with overhead than you were without it." ([Swyx](https://dev.to/swyx/what-drives-optimal-overhead-2p3a#:~:text=a%20%22first%20do%20no%20harm%22,without%20it.))

*性能就是能够以最少的开销来控制复杂性。 这要求用于管理复杂性的抽象/工具坚持“‘首先不要伤害’的原则……确保你的工作效率至少不低于没有开销的情况。”* 

Question is: are we really improving at managing complexity? Not when it feels like we're drowning in **more complexity than ever**, with an entire **curriculum** of [deep programming concepts](https://auth0.com/blog/glossary-of-modern-javascript-concepts/) ==taking the place of== what used to be the "HTML" kind of problems, and along with that ==a doze of== [compilers](https://dev.to/this-is-learning/a-look-at-compilation-in-javascript-frameworks-3caj) - that themselves have to **cater** to a number of new paradigms, magic syntaxes and dialects!

*问题是：我们在管理复杂性方面真的有所改进吗？ 不是当我们感觉自己被淹没在比以往任何时候都更加复杂的时候，一整套深度编程概念课程取代了过去的“HTML”类问题，以及一大堆编译器——他们自己必须迎合一些新的范例、神奇的语法和方言！*

We must now **rigor** through the surprisingly ==high amount of== _code-level complexity_, and pay the price of a _compile-step_ (with [Webpack](https://webpack.js.org/) and [babel](https://babeljs.io/) (or similar beast) and **a barrage of** configurations, plugins and extensions) to have a working web page! ==But that's not all==, we must also **bend along with** mind-bending _runtime behaviours_ (of hooks and friends), and _debug_ through **difficult-to-grok** transforms of our code!

*我们现在必须严格执行令人惊讶的大量代码级复杂性，并付出编译步骤的代价（使用 Webpack 和 babel（或类似的野兽）以及大量的配置、插件和扩展）以获得一个可以运行的网页 ！ 但这还不是全部，我们还必须适应（钩子和朋友的）令人费解的运行时行为，并通过难以理解的代码转换进行调试*！

At this point... you're now entirely cracking a different grade of nut! Everything easy is hard again[1](https://dev.to/oxharris/rethinking-the-modern-web-5cn1#fn1)!

*在这一点上......你现在完全破解了不同等级的困难！ 一切容易的又变得困难* 

Jelan [shares her frustration](https://news.ycombinator.com/item?id=33134021#:~:text=I%20have%20a,this%20space%20now.):

> _"I'm getting more and more **frustrated** with all the added layers of complexity needed to work with most common frontend frameworks. **I’ve hit a point** where it just doesn’t seem like the end **justifies** the means ==in the vast majority of cases anymore.=="_

*“我对使用最常见的前端框架所需的所有额外的复杂层感到越来越沮丧。我已经达到了这样一个地步，即在绝大多数情况下，最终似乎并不能证明手段是合理的 了。”*

And Chris Coyer [puts a fitting analogy to that](https://css-tricks.com/the-great-divide/#:~:text=ironically,cougar%20problem.):

> _"**Ironically**, while heaps of tooling add complexity, the reason they are used is for battling complexity. Sometimes it feels like releasing **cougars** into the forest to handle your snake problem. Now you have a cougar problem."_

*“具有讽刺意味的是，虽然成堆的工具增加了复杂性，但使用它们的原因是为了对抗复杂性。有时感觉就像将美洲狮释放到森林中来解决你的蛇问题。现在你遇到了美洲狮问题。”*

Look what was going to land you in the **pit** of success[2](https://dev.to/oxharris/rethinking-the-modern-web-5cn1#fn2) **winding you up with** **more complexity than you had at first**! (On the [essential/accidental](https://en.wikipedia.org/wiki/No_Silver_Bullet)[3](https://dev.to/oxharris/rethinking-the-modern-web-5cn1#fn3) scale, that's you having your "accidental" (tooling-induced) complexity trump your "essential" (real problem-space) complexity!) And again, that's **utterly** counterproductive!

*看看是什么让你陷入成功的深渊，让你陷入比最初更复杂的境地！ （在本质/偶然尺度上，这就是你的“偶然”（工具引起的）复杂性胜过你的“本质”（真正的问题空间）复杂性！）再一次，这完全适得其反！*

---

If there's anything that's obvious, it is the one thing that **ruins** the experience each time: **that "JavaScript"**; this time, not the "JS" in the conventional "HTML, CSS, JS" approach, but the "JS" in our new "all-JS" equations:

-   the "_all-JS_ bottom-line" engineering model - which brings all of page structure, content, and styling to JS (`Build_Step => [JS, JS, JS]`)!
-   the "_all-JS_ front-line" engineering model - which defaults to JS for authoring page structure, content, and styling (`[JS, JS, JS] => Build_Step`)!

如果有什么是显而易见的，那就是每次都会破坏体验的一件事：那个“JavaScript”； 这一次，不是传统的“HTML、CSS、JS”方法中的“JS”，而是我们新的“一切JS”范式中的“JS”：
“一切 JS 底线”工程模型——将所有页面结构、内容和样式都引入 JS (Build_Step => [JS, JS, JS])！
“一切 JS 前线”工程模型——默认使用 JS 来编写页面结构、内容和样式（[JS, JS, JS] => Build_Step）！

## Looking Back: The Paradigm Shift!
Signaled by React's [Rethinking Best Practices](https://www.youtube.com/watch?v=x7cQ3mrcKaY) pitch back in March 2013, frontend's new era has for the most part sat on what seems to be ==a universal axiom==: ==**the traditional web is awful; abstract it**==! Everything "traditional" about the web application story - from **authoring** to runtime - has since been **doomed** for _an abstraction_ or _a re-engineering_ - with the conventional "HTML, CSS, JS" and the DOM being the first casualty of war, and JavaScript being the new default **instinct**!

*早在 2013 年 3 月，React 的 Rethinking Best Practices 活动就标志着前端的新时代在很大程度上建立在一个看似普遍的公理之上：传统网络很糟糕； 抽象它！ 关于 Web 应用程序故事的一切“传统”——从编写到运行时——都注定要进行抽象或重新设计——传统的“HTML、CSS、JS”和 DOM 是战争的第一个牺牲品，而 JavaScript 成为新的默认本能！*

Whole new ecosystems of breakaway technologies have **spun**, each staying at a false **dichotomy** with web fundamentals and staying defensive about that! Here's for an insight into the thought process...

全新的分离技术生态系统已经旋转，每一个都与web基础知识保持错误的二分法，并对此保持防御！ 这是对思维过程的洞察......

from HTML to JavaScript:
-   Mike Turley (on JSX): [Why JavaScript is Eating HTML](https://css-tricks.com/why-javascript-is-eating-html/)
-   Mark Dalgleish (on CSS-in-JS): [A Unified Styling Language](https://medium.com/seek-blog/a-unified-styling-language-d0c208de2660)

from the web platform to abstractions:
-   Rich Harris: [Why I don't use web components](https://dev.to/richharris/why-i-don-t-use-web-components-2cia)
-   Ryan Carniato: [Maybe Web Components are not the Future?](https://dev.to/ryansolid/maybe-web-components-are-not-the-future-hfh)

### ...from HTML to JavaScript

A surprising **exodus** ensues!
*一场出人意料的大逃亡接踵而至！*

"HTML has been the running **punchline** in the web development community lately. [...] We are in the midst of a very large problem in the web development field, where HTML is being left in the **rearview** mirror in place of JavaScript", [writes Mark Steadman](https://www.deque.com/blog/javascript-frameworks-the-lost-art-of-html/#:~:text=HTML%20has%20been%20the%20running%20punchline%20in%20the%20web%20development%20community%20lately.&text=We%20are%20in%20the%20midst%20of%20a%20very%20large%20problem,JavaScript.)

“最近 HTML 一直是 Web 开发社区的热门话题。[...] 我们正处于 Web 开发领域的一个非常大的问题之中，HTML 被留在后视镜中代替 JavaScript”， 马克斯蒂德曼写道

React's [infamous movement](https://dev.to/oxharris/rethinking-the-modern-web-5cn1#:~:text=Rethinking%20Best%20Practices) may have had an initial context of just [JSX](https://en.wikipedia.org/wiki/JSX_(JavaScript)) and, later, [CSS-in-JS](https://en.wikipedia.org/wiki/CSS-in-JS)! But unfortunately, this has swept and overturned how a broader share of the frontend tooling space thinks! There's now multiple JS-first agendas everywhere you look - even on web platform proposal boards!

*React 臭名昭著的运动最初可能只是 JSX 的上下文，后来是 CSS-in-JS！ 但不幸的是，这已经席卷并颠覆了更广泛的前端工具领域的想法！ 现在到处都有多个 JS-first 议程——甚至在网络平台提案板上！*

Consider as honorable mentions:
-   [HTML Modules](https://github.com/WICG/webcomponents/blob/gh-pages/proposals/html-modules-explainer.md) - a proposed "JS-first" _import_ mechanism for "HTML".
-   [CSS Modules](https://github.com/css-modules/css-modules) - a "JS-first" _import_ mechanism for "CSS".

Slowly, some of what belongs in the HTML problem space are now beginning to land as JavaScript feature proposals - sometimes downright namesquatting HTML!

*慢慢地，一些属于 HTML 问题空间的内容现在开始作为 JavaScript 功能提案落地——有时是彻头彻尾的域名抢注 HTML！*

> But lest you asked how "HTML Modules" and friends don't solve a problem: maybe they do! But those would certainly not be the "HTML" kind of problems, but the "accidental limitation" type of problem in the JS-first world! Proposals like this are only symptomatic of having gone the "unconventional" way; you must endlessly build JS-first bridges, seek a JavaScript metaphor for every other HTML/CSS thing, and wish the rest of the web were colored [yellow](https://en.wikipedia.org/wiki/File:Unofficial_JavaScript_logo_2.svg)! (You can tell clearly how these aren't a feature, but a means to an end!) And notice how this comes even at the risk of _tight-coupling_ a supposed _general-purpose_, _DOM-agnostic_ programming language with the DOM! (See how HTML Modules in principle tortures the JavaScript language to produce DOM primitives!)

但唯恐你问“HTML 模块”和朋友们是如何解决问题的：也许他们能解决！ 但那些肯定不是“HTML”类型的问题，而是 JS-first 世界中的“意外限制”类型的问题！ 像这样的提议只是走“非常规”道路的征兆； 您必须无休止地构建 JS 优先的桥梁，为所有其他 HTML/CSS 事物寻找 JavaScript 隐喻，并希望网络的其余部分被涂成黄色！ （您可以清楚地看出这些不是功能，而是达到目的的手段！）请注意，即使冒着将假定的通用、与 DOM 无关的编程语言与 DOM 紧密耦合的风险，这也是如何实现的！ （看看 HTML 模块原则上是如何折磨 JavaScript 语言来生成 DOM 基元的！）

It has turned out to be not just more JavaScript being smuggled in through the back door, but also more HTML and CSS being thrown out the window! (Probably the greater harm!) Think the case regarding the removal - rather than improvement - of [HTML Imports](https://web.dev/imports/) from the spec in favour of [ES6 Modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules) - or possibly now the name-squatting [HTML Modules](https://dev.to/oxharris/rethinking-the-modern-web-5cn1#:~:text=HTML%20Modules) above! It just happened that "the JS-centric zeitgeist won" this over - to put it in [Brad Frost's words](https://bradfrost.com/blog/link/why-were-breaking-up-with-css-in-js/#:~:text=the%20js-centric%20zeitgeist%20version%20won%2C%20which%20is%20why%20we%20don%E2%80%99t%20have%20html%20imports)!

事实证明，不仅有更多的 JavaScript 通过后门走私，还有更多的 HTML 和 CSS 被扔出窗外！ （可能危害更大！）想想从规范中移除（而不是改进）HTML 导入以支持 ES6 模块的情况——或者现在可能是上面的域名抢注 HTML 模块！ 碰巧“以 JS 为中心的时代精神赢得了”这一胜利——用 Brad Frost 的话来说！

> And is someone pointing to the removal of Scoped CSS in favour of Shadow DOM based CSS? We'll come to that!

有人指出移除 Scoped CSS 以支持基于 Shadow DOM 的 CSS 吗？ 我们会做到这一点！

JS-first has this way led to setting fire on many good thinking around HTML just to have them reborn in JavaScript! An irreversible, all-in proposition!

JS-first 以这种方式点燃了许多围绕 HTML 的好想法，只是为了让它们在 JavaScript 中重生！ 一个不可逆转的，all-in 的命题！

Needles to say is how therefore many highly-missing features in HTML aren't even in the radar on proposal boards! When you look around, really, how much "developer mind-share" does HTML have anymore to push those?

不用说，HTML 中许多高度缺失的功能甚至都没有出现在提案板上！ 当你环顾四周时，真的，HTML 有多少“开发人员的思想共享”来推动这些？

This has been so deep that if you dared to contend with the status quo and build a specialised career on real UI development skills that means less engineering, you'd find yourself in the marginalised half of the [Great Divide](https://css-tricks.com/the-great-divide/) and [risk not having a career](https://news.ycombinator.com/item?id=33134021#:~:text=the%20one%20redeeming%20quality%20of%20doing%20this%20kind%20of%20work%20is%20that%20it%20is%20in%20very%20high%20demand%2C%20and%20i%20worry%20that%20the%20price%20of%20becoming%20more%20specialized%20or%20doing%20something%20more%20enjoyable%20with%20less%20bloat%20is%20that%20it%20becomes%20much%20harder%20to%20find%20jobs.)! (So then, [many devs have had to acquiesce against their own will](https://bradfrost.com/blog/link/why-were-breaking-up-with-css-in-js/#:~:text=Again%20we%E2%80%99re%20all,and%20learned%20React.) considering that there are bills to pay!)

这已经很深了，如果你敢于与现状抗衡，并在真正的 UI 开发技能上建立一个专业的职业生涯，这意味着更少的工程，你会发现自己处于 Great Divide 的边缘化一半，并且有可能没有职业！ （因此，考虑到要支付账单，许多开发者不得不违背自己的意愿默许！）

### ...from the web platform to abstractions

Suddenly, the platform is abandoned!
突然，平台被废弃了！

Born out of contempt and mischaracterization of the web platform, the focus of modern abstractions has come to seem somewhat like _re-engineering_ web languages, _replicating_ platform features and APIs, and _duplicating_ the browser's efforts! The whole idea of using the web platform has remained an unattractive option for breakaway technologies. To put it in [Alex Russell's words](https://infrequently.org/2017/10/web-components-the-long-game/#:~:text=the%20incentives%20of%20framework%20authors%20are%20not%20aligned%20with%20compatibility), "The incentives of framework authors are not aligned with compatibility". I often see "web standards" being touted only where it makes a big news or where the performance gains are the incentive!

Looking back at how React and its ecosystem has stayed detached over the years, Mikeal Rogers relates:

> _"I remember when React was launched, the whole thing was about DOM diffing. The value of it is this virtual DOM thing. Then we made the DOM fast, and who gives a shit now. But we’re still using React because of – I don’t know. [...] And then now we have Web Components and they can’t adopt it, because they’re on their own pattern, so we can’t take this feature upgrade from the platform. [And] I think there's a ton of other examples of this where the platform starts to catch up, and then the frameworks can’t."_ - [JS Party – Episode #89 | Changelog](https://changelog.com/jsparty/89#:~:text=i%20remember%20when%20react%20was%20launched%2C%20the%20whole%20thing%20was%20about%20dom%20diffing,we%E2%80%99re%20still%20using%20react%20because%20of%20%E2%80%93%20i%20don%E2%80%99t%20know&text=and%20then%20now%20we%20have%20web%20components%20and%20they%20can%E2%80%99t%20adopt%20it,platform%20starts%20to%20catch%20up%2C%20and%20then%20the%20frameworks%20can%E2%80%99t.)

We just seem to be disposed to trading the "norm" and yet searching for the "kind" in the _abstract_ world!

==And what has been a particularly sad implication of the framework-first culture? The more we've invested in breakaway technologies and side ecosystems, _the less we've learned about our real problem space and all the opportunities to actually move the web forward_!== It turns out, HTML and its ecosystem remains _undertooled_ to date, whereas the framework web continues to flourish! You're now almost guaranteed to get stranded as being in a desert land building anything in vanilla HTML and the DOM:

> _"It’s really depressing that most useful tools these day are made for React projects and/or require React knowledge to set up and use. This locks out many of us who are not using React for everything & who still prefer the **vanilla** route for their projects."_ - [Sara Soueidan](https://twitter.com/sarasoueidan/status/1098960689455075330?s=21)

You just realise how much everyone seems to have disconnected from the real "problem-space" type of problems and gotten buried in "abstract" problems, leaving us with framework-specific solutions to very common problems!

It turns out, undertooling remains a real deterrent for everyone who has craved the simplicity of the vanilla web. (And this should also be one valid challenge to the _challenge_ thrown here by Remy Sharp when he asked: [what's stopping you from using _exactly_ [that] method today?](https://remysharp.com/2021/02/11/the-web-didnt-change-you-did#:~:text=dear%20reader%20-%20let%20me%20ask%20you%20this%2C%20and%20i%20hope%20you%20ask%20your%20colleagues%20the%20same%3A%20what%27s%20stopping%20you%20from%20using%20exactly%20method%20today%3F))

---

With so much having gone wrong in the tooling space, what follows is only expected: a community at large suffering a terrible blind spot for web fundamentals! Ground truths are now debated everywhere, =="best practices" are literally going numb== ([hi Pete](https://dev.to/oxharris/rethinking-the-modern-web-5cn1#:~:text=%20Rethinking%20Best%20Practices)), and ==standards are increasingly losing their place among developers==! (Consider a survey: [What do you know about Web Standards?](https://www.smashingmagazine.com/2019/01/web-standards-guide/#why-am-i-telling-you-this).)

Go see a typical framework-speaking dev - even in their seniors of roles; go check the typical learning path of the coming generation; and go see what the modern Frontend job descriptions on job boards are saying! Surprisingly, the modern developer career is now little about web technologies themselves and all "about [the] intricacies of the most popular frameworks", to put it in [Frédéric Bonnet's words](https://dev.to/fredericbonnet/the-third-age-of-web-development-kgj#:~:text=about%20mastering%20the%20intricacies%20of%20the%20most%20popular%20frameworks)! See that?

There's a destructive _information gap_ and a _culture erosion_[4](https://dev.to/oxharris/rethinking-the-modern-web-5cn1#fn4) now also overtaking us!

Suffice to say, the past decade has been **a life of alienation** from conventional wisdom, almost entirely spent _trading_ HTML - and burning our ships on the go - in an irreversible bet on _JavaScript_; turning our backs and throwing dirt on the web platform to bank futures on abstractions! Yet, only a few are really talking about the almost irreversible proposition of this decade-long shift...

> _"In elevating frontend to the land of Serious Code we have not just made things incredibly over-engineered but we have also set fire to all the ladders that we used to get up here in the first place."_ - [Laura Buns](https://dev.to/walaura/the-web-without-the-web-aeo#:~:text=In%20elevating%20frontend,here%20in%20the%20first%20place.)

*“在将前端提升到  Serious Code 领域的过程中，我们不仅让事情变得令人难以置信的过度设计，而且还烧毁了我们最初用来爬上这里的所有梯子。” - 劳拉包子*


## Towards a Faster Web: A New Quest!
新的探索

As the ills of the Framework era become more and more palpable, the [bells and whistles of the decade](https://blog.daftcode.pl/hype-driven-development-3469fc2e9b22) are losing their charms on people! Folks are now coming around on our lived reality, and many are actively going back on their life's bets in search of sanity, at the risk of bringing people with torches and pitchforks to their door!
-   Hajime Yamasaki Vukelic: [What Got Me Writing Vanilla JavaScript again](https://javascript.plainenglish.io/what-got-me-writing-vanilla-js-again-2c53756c8a4c)
-   Sam Magura: [Why We're Breaking Up with CSS-in-JS](https://dev.to/srmagura/why-were-breaking-up-wiht-css-in-js-4g9b)

==But what about the philosophy at the tooling layer: is it now time for a rethink? It depends on how much of a rethink you are asking of!==

On the one hand, folks have been hard at work with identifying and addressing inherent overheads in the current system. (But of course, not with a view to rethinking the overall JS-first philosophy!)

For example, realising that the idea of shipping applications as just JavaScript wasn't working anything good on the user front, React and friends have since slid back to the idea of being able to send HTML over the network. This has called for major architectural rework (think [React 18's Streaming SSR architecture](https://reactjs.org/blog/2022/03/29/react-v18.html#new-suspense-features)); this being in addition to the existing idea of static site generation with build tools like [Gatsby](https://www.gatsbyjs.com/). Server-Side Rendering ([SSR](https://web.dev/rendering-on-the-web/)) and Static Site Generation ([SSG](https://web.dev/rendering-on-the-web/)) have been such a feat for the status quo!

*例如，意识到将应用程序作为 JavaScript 发布的想法在用户方面没有任何好处，React 和朋友们已经退回到能够通过网络发送 HTML 的想法。 这需要进行重大的架构改造（想想 React 18 的 Streaming SSR 架构）； 这是对使用 Gatsby 等构建工具生成静态站点的现有想法的补充。 服务器端呈现 (SSR) 和静态站点生成 (SSG) 已经成为现状的壮举！*

So, right now, HTML and progressive enhancement have again become an attractive option to what has been the "all-JS or nothing" camp. (In fact, [Remix](https://remix.run/) has this as a new bragging right! In its own words: who knew?) Put together, all of the new takes here just represent a new game plan: a long walk back to the basics; a bit of a _compromise_ on its [initial takes](https://dev.to/oxharris/rethinking-the-modern-web-5cn1#:~:text=Rethinking%20Best%20Practices), but a bit of some greater good: ==towards a faster, functional Frontend!==

On the other hand, a new wave of innovation is taking center stage with a more ambitious take than the ongoing long, painful walk back to the basics: this time, the idea of an outright ==HTML-first==, "progressive enhancement" architecture from start! (SitePen Engineering gives the perfect [Intro to HTML-first Frontend Frameworks](https://www.sitepen.com/blog/intro-to-html-first-frontend-frameworks) featuring [Qwik](https://qwik.builder.io/), [Marko](https://markojs.com/), [Astro](https://astro.build/), [11ty](https://www.11ty.dev/), [Fresh](https://fresh.deno.dev/), and [Enhance](https://enhance.dev/); and ==this is absolutely worth your time!==)

I find this especially interesting because, finally, everyone can see that the idea of a faster web didn't have to be the hard, compute-intensive, and yet elusive thing we've had for years! It is now clearer than ever how much of an absolute illusion we've been on... in staying _fixated to JS_ and yet _subscribed to HTML_, albeit cleverly! You'd also realise: HTML over the network didn't have to be any "modern" wisdom or such a big deal of an innovation, or any feat! Not when this is something the web has had from genesis! (Streaming SSR from day 1 of PHP, anyone?)

Sad that we seem to only live after the fact when it comes to tooling, but thanks to the new wave of frameworks for shedding the light that openly challenges the status quo! Finally, we've come to a point that we can be hopeful about: the prospect of having "accessible", "functional" applications at half the price! (Hopefully related is how we've now for the first time - since the JS-making epoch - [recorded a less steep increase](https://almanac.httparchive.org/en/2022/javascript#:~:text=from%202021%20to%202022%2C%20an%20increase%20of%208%25%20for%20mobile%20devices%20was%20observed%2C%20whereas%20desktop%20devices%20saw%20an%20increase%20of%2010%25.&text=is%20less%20steep%20than%20in%20previous%20years) in the amount of JavaScript shipped to users!)

---

So are we good now? Well, not just yet!

Not when it seems that we've come only halfway with the idea: sending pages as HTML but authoring them as JS; addressing the tradeoff problem and its overheads on the _user_ front but leaving it unchanged on the _developer_ front! Clear yet? **_Much_ of the "HTML" in our new HTML-first equations is still the _tooling-yielded HTML_, not the _hand-authored HTML_**; same as before where HTML is treated as a _compile target_, an _implementation detail_... something you'd abstract to have a good DX! =="Tooling" still remains Frontend's primary means to its "HTML" end!==

This sheer idea of getting "HTML" behind a compile wall in favor of an abstraction is also where it begins to tell that we might yet be suffering the decade-long blindspot for the platform in a new way - **embracing HTML for just the performance incentives and not for the whole idea of _using the platform_**! Let's just throw it out there: Frontend still isn't aligned with _using the platform_ to [give legacy tooling their well-earned rest](https://developer.chrome.com/blog/modulepreload/#:~:text=giving%20bundlers%20their%20well-earned%20rest) and [take a correction back to simplicity](https://world.hey.com/dhh/modern-web-apps-without-javascript-bundling-or-transpiling-a20f2755#:~:text=we're%20way%20overdue%20a%20correction%20back%20to%20simplicity%20for%20the%20frontend.)!

[Chad Fowler notes](https://twitter.com/chadfowler/status/646624348028190720) how deep-seated this is:

> _"The older I get, the more I realize the biggest problem to solve in tech is to get people to stop making things harder than they have to be."_

“我年纪越大，就越意识到科技领域要解决的最大问题是让人们停止让事情变得比他们必须做的更难。”

So, how about just taking the plunge... and embracing the whole web platform thing? Now, we would not only be unlocking performance on both the _user_ front and the _developer_ front, we would be doing more: **==unleashing the web's full potential==**! (And what could be a more ambitious goal?)

Actually, **this is why we're here**! Can we skip to the good parts?

## Introducing: Web-Native Development!
介绍：Web原生开发！

==Take this as not the name of a new framework or some anti-framework movement, but as a playbook to unleashing the web's full potential.==

Web-native development[5] is an approach to web development that sees the web platform as an enabler in the whole application story, and in fact, a fundamental key to succeeding at each phase of that story - from authoring to runtime! This comes as a hard reset to the decade-long cultural shift and its pessimistic take on the web platform!

This is really about embracing and leveraging native web technologies, APIs, languages and conventions, etc, and minimizing tooling! ==For a fact, there comes a time in life when this is all you really want... get things done with less of the drama==! "I've been in enough teams in my 20 years of programming to value this part almost more than anything else", [writes Andrea Giammarchi](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#:~:text=i've%20been%20in%20enough%20teams%20in%20my%2020%20years%20of%20programming%20to%20value%20this%20part%20almost%20more%20than%20anything%20else.)!

As the platform and its technologies and languages advance, we often can find multiple opportunities "to shed a lot of this tooling" and defer to native approaches. ([JS Party - Episode #89 | Changelog](https://changelog.com/jsparty/89#:~:text=and%20as%20the%20platform%20improves,%20we%20need%20to%20be%20able%20to%20shed%20a%20lot%20of%20this%20tooling.)) ==Good to know is that tools are only as good as being solutions to _unsolved_ problems, not _solved_ problems!== Anything in exception soon begins to change the narrative to something counterproductive! Thus, for all we've bet on custom tooling, we must now beat that Sunk Cost fallacy[6](https://dev.to/oxharris/rethinking-the-modern-web-5cn1#fn6) to explore what's natively available!

==At the end of the day, web-native development **gets you banking more on the web platform and less on abstractions**!== You're now on the _winning_ side - rather than on the _contending_ side - of the web's "moving" story! You're now winning as the platform unfolds!

归根结底，Web 原生开发让您更多地依赖于 Web 平台而不是抽象！

[George Katsanos explains](https://dev.to/richharris/why-i-don-t-use-web-components-2cia#:~:text=It%20should%20be,user-friendly%20interfaces.) how this allows us take back more brain cycles to finally go make something:

> _"It should be obvious to all of us that if we would focus all our efforts in the Platform and stop reinventing the wheel... ==we would have a lot more free time to focus on the real reason we are in this job which is to deliver fast, stable, secure, user-friendly interfaces.=="_

So, where's a good place to get well-rounded with the web platform? **Chrome's [web.dev](https://web.dev/) developer centre is a treasure trove of resources on key web design and development subjects, maintained by the Chrome team and other industry experts!** ([Here's the learning centre](https://web.dev/learn/).) And for when you need to take the web platform by its individual technologies, here is [MDN](https://developer.mozilla.org/)! (And [here's the learning centre](https://developer.mozilla.org/en-US/docs/Learn).) For showcases, here is one: [Using the platform](https://elisehe.in/2021/08/22/using-the-platform) - a delightful piece of a story on going buildless with ES6 modules and going framework-free with Web components, written by Elise Hein!

Up next is: **how far does this go in real life**? Build a twitter clone with zero tooling? Uhh, that has never been the idea, and we may never get there! The web platform is anything but a framework of its own! _At some point_, we are going to have to need higher-level abstractions over native lower-level features! Where there seems to be a bit of a bad news is that **the current state of HTML and the DOM makes that happen _sooner_**; it isn't long into the journey before gaps and dips in the platform gets you into forced labour! But we can easily turn this around by investing along two lines:

1.  **Low-level tooling**: platform-focused initiative to _standardise_ and _factor into the platform_ common web development architectures and paradigms. (We're overdue for native-level reactivity and a more empowering component model - just to mention a few!)
2.  **Higher-level tooling**: community-focused initiative to _extend_ the platform's low-level capabilities with "web-native" libraries and frameworks. (We need a new wave of modest abstractions that draw on the web platform and let us do the same!)

低级工具：以平台为中心的倡议，用于标准化和纳入平台通用的 Web 开发架构和范式。 （我们早该获得 native-level 响应式和更强大的组件模型）

更高级别的工具：以社区为中心的倡议，通过“web-native”库和框架扩展平台的低级别功能。 （我们需要在网络平台上绘制新一波适度的抽象，让我们也这样做！）

**This is where I _put my money where my mouth is_!** I'd like to take you on a few ideas I've been working on along these lines!

Open to some tooling ideas?

### Explore with Me...

Our journey spans a series of posts! We begin with the underlying equations and move on to a showcase of the proposals and polyfils, the userland libraries and framework!

> For the curious, [here's a sneak peak](https://github.com/webqit/webqit) into this project on github.



## Reference
- <https://dev.to/oxharris/rethinking-the-modern-web-5cn1>
- [Can You Afford It?: Real-world Web Performance Budgets](https://infrequently.org/2017/10/can-you-afford-it-real-world-web-performance-budgets/) (Alex Russell)
-   [2022 Page Weight Report: JavaScript Bytes](https://httparchive.org/reports/page-weight#bytesJs) (HTTP Archive)
-   [The Cost of JavaScript Frameworks](https://timkadlec.com/remembers/2020-04-21-the-cost-of-javascript-frameworks/) (Tim Kadlec)
-   [What drives Optimal Overhead?](https://dev.to/swyx/what-drives-optimal-overhead-2p3a) (Shawn Wang)
-   [Glossary of Modern JavaScript Concepts: Part 1](https://auth0.com/blog/glossary-of-modern-javascript-concepts/) (Kim Maida)
-   [Rethinking Best Practices](https://www.youtube.com/watch?v=x7cQ3mrcKaY) (Pete Hunt)
-   [Why JavaScript is Eating HTML](https://css-tricks.com/why-javascript-is-eating-html/) (Mike Turley)
-   [A Unified Styling Language](https://medium.com/seek-blog/a-unified-styling-language-d0c208de2660) (Mark Dalgleish)
-   [Why I don't use web components](https://dev.to/richharris/why-i-don-t-use-web-components-2cia) (Rich Harris)
-   [Maybe Web Components are not the Future?](https://dev.to/ryansolid/maybe-web-components-are-not-the-future-hfh) (Ryan Carniato)
-   [JavaScript Frameworks & The Lost Art of HTML](https://www.deque.com/blog/javascript-frameworks-the-lost-art-of-html/) (Mark Steadman)
-   [why we’re breaking up with css-in-js](https://bradfrost.com/blog/link/why-were-breaking-up-with-css-in-js/) (Brad Frost)
-   [The Great Divide](https://css-tricks.com/the-great-divide/) (Chris Coyer)
-   [Web Components: The Long Game](https://infrequently.org/2017/10/web-components-the-long-game/) (Alex Russell)
-   [Is modern JS tooling too complicated?](https://changelog.com/jsparty/89) (JS Party – Episode #89 | Changelog)
-   [The web didn't change; you did](https://remysharp.com/2021/02/11/the-web-didnt-change-you-did) (Remy Sharp)
-   [Web Standards: The What, The Why, And The How](https://www.smashingmagazine.com/2019/01/web-standards-guide/) (Amy Dickens)
-   [From Classicism to Metamodernism — A Short History of Web Development Series' Articles](https://dev.to/fredericbonnet/series/10459) (Frédéric Bonnet)
-   [Hype Driven Development](https://blog.daftcode.pl/hype-driven-development-3469fc2e9b22) (Marek Kirejczyk)
-   [What Got Me Writing Vanilla JavaScript again](https://javascript.plainenglish.io/what-got-me-writing-vanilla-js-again-2c53756c8a4c) (Hajime Yamasaki Vukelic)
-   [Why We're Breaking Up with CSS-in-JS](https://dev.to/srmagura/why-were-breaking-up-wiht-css-in-js-4g9b) (Sam Magura)
-   [Intro to HTML-first Frontend Frameworks](https://www.sitepen.com/blog/intro-to-html-first-frontend-frameworks) (SitePen Engineering)
-   [Modern web apps without JavaScript bundling or transpiling](https://world.hey.com/dhh/modern-web-apps-without-javascript-bundling-or-transpiling-a20f2755) (David Heinemeier Hansson)

---

1.  Borrowing Frank Chimero's title: [Everything Easy is Hard Again](https://frankchimero.com/blog/2018/everything-easy/) [↩](https://dev.to/oxharris/rethinking-the-modern-web-5cn1#fnref1)
    
2.  Defining [The Pit of Success](https://english.stackexchange.com/questions/77535/what-does-falling-into-the-pit-of-success-mean) [↩](https://dev.to/oxharris/rethinking-the-modern-web-5cn1#fnref2)
    
3.  See [Fred Brooks: No Silver Bullet (PDF)](http://worrydream.com/refs/Brooks-NoSilverBullet.pdf) [↩](https://dev.to/oxharris/rethinking-the-modern-web-5cn1#fnref3)
    
4.  See [Cultural Erosion](https://geographyrevisionalevel.weebly.com/6b-cultural-erosion.html) [↩](https://dev.to/oxharris/rethinking-the-modern-web-5cn1#fnref4)
    
5.  "Web-native" is a recurring theme across multiple initiatives and paradigms: [↩](https://dev.to/oxharris/rethinking-the-modern-web-5cn1#fnref5)
    
    -   [Web Native](https://webnative.tech/) - Ionic Team's presentation of the idea, but scoped to its [Capacitor](https://capacitorjs.com/) runtime.
    -   [Web-Native](https://dev.to/fredericbonnet/the-third-age-of-web-development-kgj#:~:text=web-native) - Frédéric Bonnet's presentation of the idea in [The Postmodernist Period](https://dev.to/fredericbonnet/the-third-age-of-web-development-kgj#:~:text=market%20(2012-today).-,the%20postmodernist%20period%20,-and%20the%20Second) of [The Third Age of Web Development](https://dev.to/fredericbonnet/the-third-age-of-web-development-kgj).
    -   [Modern Web](https://modern-web.dev/) - Guides, tools and libraries for modern web development built on web standards.
    -   [The Stackless Way](https://tutorials.yax.com/articles/the-yax-way/index.html) - Daniel Kehoe's optimistic take on web development that proposes we “use the platform” instead of frameworks and build tools.
    -   [Buildless](https://buildless.site/) - Pascal Schilp's paradigm for creating production websites without a build process.
    
    Some related tags:
    
    -   buildless - [DEV](https://dev.to/t/buildless)
    -   vanilla - [DEV](https://dev.to/t/vanilla)
    -   useThePlatform - [twitter](https://twitter.com/hashtag/justUseThePlatform?src=hashtag_click)
6.  See [Sunk Cost Fallacy](https://en.wikipedia.org/wiki/Sunk_cost) [↩](https://dev.to/oxharris/rethinking-the-modern-web-5cn1#fnref6)

