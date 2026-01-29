

Review
1. 2024-09-10 22:47

> [!Summary]
> 

## 一、Introduction


小根堆实现
```ts
class MinHeap {
    private heap: number[];

    constructor() {
        this.heap = [];
    }

    private getParentIndex(index: number): number {
        return Math.floor((index - 1) / 2);
    }

    private getLeftChildIndex(index: number): number {
        return 2 * index + 1;
    }

    private getRightChildIndex(index: number): number {
        return 2 * index + 2;
    }

    private swap(index1: number, index2: number): void {
        const temp = this.heap[index1];
        this.heap[index1] = this.heap[index2];
        this.heap[index2] = temp;
    }

    private siftUp(index: number): void {
        let currentIndex = index;
        while (currentIndex > 0 && this.heap[currentIndex] < this.heap[this.getParentIndex(currentIndex)]) {
            this.swap(currentIndex, this.getParentIndex(currentIndex));
            currentIndex = this.getParentIndex(currentIndex);
        }
    }

    private siftDown(index: number): void {
        let currentIndex = index;
        let minIndex = index;
        const length = this.heap.length;

        while (true) {
            const leftChildIndex = this.getLeftChildIndex(currentIndex);
            const rightChildIndex = this.getRightChildIndex(currentIndex);

            if (leftChildIndex < length && this.heap[leftChildIndex] < this.heap[minIndex]) {
                minIndex = leftChildIndex;
            }

            if (rightChildIndex < length && this.heap[rightChildIndex] < this.heap[minIndex]) {
                minIndex = rightChildIndex;
            }

            if (minIndex === currentIndex) {
                break;
            }

            this.swap(currentIndex, minIndex);
            currentIndex = minIndex;
        }
    }

    insert(value: number): void {
        this.heap.push(value);
        this.siftUp(this.heap.length - 1);
    }

    extractMin(): number | undefined {
        if (this.heap.length === 0) {
            return undefined;
        }

        if (this.heap.length === 1) {
            return this.heap.pop();
        }

        const min = this.heap[0];
        this.heap[0] = this.heap.pop()!;
        this.siftDown(0);

        return min;
    }

    peek(): number | undefined {
        return this.heap[0];
    }

    size(): number {
        return this.heap.length;
    }

    isEmpty(): boolean {
        return this.heap.length === 0;
    }
}
```


### Leetcode习题

1. [x] 215. 数组中的第K个最大元素 ✅ 2024-10-08
2. [x] 347. 前K个高频元素 ✅ 2024-10-08


## Reference

