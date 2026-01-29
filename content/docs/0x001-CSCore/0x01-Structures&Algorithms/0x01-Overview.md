
#Algorithm #Structure 

Review
1. 2019/01/29
2. 2021/02/13
3. 2022/11/20
4. 2024-09-07 21:35

> [!Summary]
> ***程序 = 数据结构 + 算法***
> 数据结构是工具，算法是通过合适的数据结构解决特定问题的方法。
> 
> 书籍📚
> - 啊哈算法
> - 漫画算法
> - 算法图解
> - 算法（第四版）
> - 计算机程序设计艺术
> - Algorithm Design `JON KLEINBERG EVA TRADOS`
> - Introduction to Algorithms (Third Edition)
> - 《50 Algorithms Every Programmer Should Know》Second Edition, 2023/09
> 
> Websites
> - [Runoob 数据结构与算法](https://www.runoob.com/data-structures/data-structures-tutorial.html) 
> 
> 更多信息查看
> [[0a01-Interview Overview]]


> [!Summary] 优化策略
> 空间换时间：对于执行较慢的程序，可以通过消耗更多的内存（空间换时间）来进行优化
> 时间换空间：而消耗过多内存的程序，可以通过消耗更多的时间（时间换空间）来降低内存的消耗


## 一、Data Structures
数据结构的存储方式：
1. 顺序存储
2. 链式存储
3. 索引存储
4. 散列存储

数据结构的基本存储方式可以理解为只有**顺序**和**链式**两种，其他数据结构都是基于这两种的封装，基本操作就是增删查改，遍历方式无非迭代和递归。

**分类**
- Array
- Hash Table
- Singly Linked List
- Doubly Linked List
- 跳舞链？
- 跳表？
- Queue
- Priority Queue
- 双端队列
- Stack
- Tree
	- Binary Search Tree(BST)
	- AVL Tree(Balanced Binary Tree)
	- Red Black Tree
	- Segment Tree
	- Fenwick Tree
	- 递归树
	- Huffman tree
- Heap: Binary Heap，大/小根堆、可并堆，加强堆
- Trie
- Graph
- Disjoint Set
- Bloom Filter
- String: 字典树、后缀书
- 并查集

## 二、Algorithms
- Sorting
- Searching
- Tree traversal
- Graph traversal
- Breadth First Search (BFS)
- Depth First Search (DFS)
- Encoding
- String manipulation: 字符串匹配, BF, RK, BM, KMP
- Cryptography
- Compilers
- Interpreters
- 哈希算法
- 贪心算法
- 分治算法
- 递归
- 动态规划
- AC自动机
- 概率统计
- 向量空间
- 索引
- 并行算法
- 割点与割边
- 二分图的最大匹配
- 位运算
- 对数器
- 比较器


### 排序算法
[[0x04-排序算法]] 
1. 冒泡排序
2. 快速排序
3. 选择排序
4. 插入排序
5. 希尔排序
6. 归并排序
7. 桶排序
8. 计数排序
9. 基数排序
10. 快排优化
11. 堆排序
12. 拓扑排序

Gale-Shapley Algorithm(盖尔-沙普利算法)，简称GS算法

### 搜索算法 - Searching
1. 回溯算法
2. Recursion
3. 剪枝技巧
4. 二分查找
5. 

### Tree
1. B+树

### 图论
1. 最短路径
2. 最小生成树
3. 网络流建模
4. 位图

### 动态规划
1. 背包问题
2. 最常子序列
3. 计数问题


## Reference
1. <https://github.com/sudheerj/datastructures-algorithms> 
2. 基于LeetCode题目讲解：[https://github.com/labuladong/fucking-algorithm](https://github.com/labuladong/fucking-algorithm)
3. Data Structure Visualizations: [https://www.cs.usfca.edu/~galles/visualization/Algorithms.html](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html)
4. visuAlgo: [https://visualgo.net/zh](https://visualgo.net/zh)
5. Algorithm Visualizer: [https://algorithm-visualizer.org/](https://algorithm-visualizer.org/)
6. Online Judge: [https://onlinejudge.org/](https://onlinejudge.org/)
7. hello algorithm: [https://github.com/geekxh/hello-algorithm](https://github.com/geekxh/hello-algorithm)
8. algorithm-pattern(Base GoLang): [https://github.com/greyireland/algorithm-pattern](https://github.com/greyireland/algorithm-pattern)
9. javascript-algorithm: [https://github.com/trekhleb/javascript-algorithms](https://github.com/trekhleb/javascript-algorithms)
10. GitHub 地址：https://github.com/halfrost/LeetCode-Go
11. 电子书在线阅读地址：https://books.halfrost.com/leetcode/
12. 王争《算法与数据结构之美》笔记：[https://blog.csdn.net/ityqing/article/details/82838524](https://blog.csdn.net/ityqing/article/details/82838524)
13. 408统考笔记：[https://zhuanlan.zhihu.com/p/32440622](https://zhuanlan.zhihu.com/p/32440622)
14. 汇总图表展示：[https://www.bigocheatsheet.com/](https://www.bigocheatsheet.com/)
15. AlgoMonster(**Master the Coding Interview** Without the Endless Grind): [https://algo.monster/](https://algo.monster/)
16. Grokking the Coding Interview: Patterns for Coding Questions [https://designgurus.org/course/grokking-the-coding-interview](https://designgurus.org/course/grokking-the-coding-interview)  
17. Master the Coding Interview: Data Structures + Algorithms [https://www.udemy.com/course/master-the-coding-interview-data-structures-algorithms](https://www.udemy.com/course/master-the-coding-interview-data-structures-algorithms)
