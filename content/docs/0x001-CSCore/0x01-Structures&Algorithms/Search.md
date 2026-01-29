
Review
1. 2024-11-15 08:02

> [!IMPORTANT] 
>
> 总结

## 一、Introduction

1、有序数组，查找某一个数是否存在

> 二分查找

2、有序数组，找到小于等于某一个数最左侧的位置



3、局部最小

- `arr[0]` < `arr[1]` -> 0
- i-1 ≤ i ≤ i+1 -> i
- `arr[n-2]` > `arr[n-1]` -> n-1

4、对数器


5、未排序数组，查找最大值，递归实现

```js
function getMaxValue(arr) {
  if (arr.length === 0) {
    return arr[0]
  };

  process(arr, 0, arr.length - 1);
}

function process(arr, l, r) {
  if (l === r) {
    return arr[l];
  }

  let mid = l + ((r - l) >> 1);
  const leftMax = process(arr, l, mid);
  const rightMax = process(arr, mid + 1, r);
  return Math.max(leftMax, rightMax);
}

const arr = [3, 2, 5, 6, 7, 4];
getMaxValue(arr);
```


6、Master 公式
Master公式，又称为Master定理或主定理，是分析递归算法时间复杂度的一种重要工具，尤其适用于具有分治结构的递归算法。

$$
T(n)=a∗T(\frac{n}{b})+O(n^d)
$$

Master公式本身就是递归的形式，是递归方法时间复杂度的一种表示法。$T(n)$ 代表递归方法处理规模为n的数据量的时间复杂度，$T(n/b)$ 代表调用子递归方法的总体时间复杂度，$O(n^d)$ 代表调用子递归方法这行代码外其他代码（下面简称递归外代码）的时间复杂度。


###### Master公式中的变量
- **a**: 每次递归调用子问题的数量。即在一个递归方法，需要调用几次子递归方法
- **b**: 子问题的规模缩小的比例。例如二分法递归搜索时，每次需要查找的数据都缩小了一半，那么 **b=2**
- **d**: 每次递归调用之外的代码时间复杂度的参数。例如二分法递归搜索时，每次递归时除了调用递归的方法，没有什么for循环代码，时间复杂度是 $O(1)$，即 $n^d=1$，因此 `d=0`

###### 推导时间复杂度  
$log_b^a$ = $log_2^1$ = 0 = d，因此满足 $d=log_b^a$，那么时间复杂度为：$O(nd * logn) = O(n0 * logn) = O(logn)$。

1: $log_b^a < d$ -> $O(n^d)$ 
2: $log_b^a > d$ -> $O(n^{log_b^a})$ 
3: $log_b^a == d$ -> $O(n^d * logn)$ 


7、归并排序



8、小和




## Reference
[带你彻底搞懂递归时间复杂度的Master公式](https://www.cnblogs.com/wind-wound/p/18206958) 
