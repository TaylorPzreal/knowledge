

Review
1. 2024-07-28 19:53

> [!Summary]
> - Garbage collection is performed automatically. We cannot force or prevent it.
> - Objects are retained in memory while they are reachable.
> - Being referenced is not the same as being reachable (from a root): a pack of interlinked objects can become unreachable as a whole, as we’ve seen in the example above.

## 一、Introduction
Low-level languages like C, have manual memory management primitives such as `malloc()` and `free()`. In contrast, JavaScript automatically allocates memory when objects are created and frees it when they are not used anymore (garbage collection). This automaticity is a potential source of confusion: it can give developers the false impression that they don’t need to worry about memory management.

Regardless of the programming language, the memory life cycle is pretty much always the same:

- Allocate the memory you need
- Use the allocated memory (read, write)
- Release the allocated memory when it is not needed anymore


The following “garbage collection” steps are regularly performed:

- The garbage collector takes roots and “marks” (remembers) them.
- Then it visits and “marks” all references from them.
- Then it visits marked objects and marks _their_ references. All visited objects are remembered, so as not to visit the same object twice in the future.
- …And so on until every reachable (from the roots) references are visited.
- All objects except marked ones are removed.



## Reference
Garbage collection <https://javascript.info/garbage-collection>
Memory management <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Memory_management>
[The lifecycle of Memory in JavaScript](https://medium.com/swlh/the-lifecycle-of-memory-in-javascript-5b5bffc5ff4c)

