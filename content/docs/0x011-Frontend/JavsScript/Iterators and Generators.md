
Review
1. 2024-07-28 13:29

> [!Summary]
> - **Iterable**: Any object with a `[Symbol.iterator]` method, allowing it to be iterated over.
> - **Iterator**: An object with a `next()` method that returns `{ value, done }` for each iteration step.
> - **Generator**: A special type of iterator defined using `function*` and `yield`, allowing for more readable and maintainable iterative code, especially useful for asynchronous operations.

## 一、Introduction
Iterators and generators, introduced into JavaScript with ECMAScript 6, represent an extremely useful concept related to iteration in the language. Iterators are objects, abiding by the iterator protocol, that allows us to easily iterate over a given sequence in various ways, such as using the `for...of` loop. Generators, on the other hand, allow us to use functions and the `yield` keyword to easily define iterable sequences that are iterators as well.

1. `iterable`
2. `iterator`
3. `generator`
4. `Async Iterator`
5. `Async Iterable`
6. Spread Operator `...`
7. Destructuring


> **_Iteration_** has always been a common concern of computer programming.
> An **_`iterable`_** is anything that can be iterated over. 
> An **_iterator_** is an object that performs iteration over a sequence.


> An **iterable** is any object that implements the `[Symbol.iterator]` method, which returns an **iterator**.
> An **_iterator_** is a JavaScript object that implements the **iterator protocol**.

The **`for...of`** loop makes iteration over a _sequence_ superbly easy.
```js
for (var _someVar_ of _sequence_) {
	// loop body 
}
```

Essentially, anything that is a sequence/collection of values where some attribute of the sequence is changing continuously, can be used inside `for...of`.

As such we can iterate over `strings`, `arrays` (as we've just seen), `sets`, `maps`, `DOMTokenList`, `HTMLCollection` objects, typed arrays and so on and so forth.

Now being iterable doesn't always has to do with the default setup in JavaScript - one can also make a non-iterable data type iterable by implementing the **_iterable protocol_**.

### Iterator protocol
The iterator protocol is simply a set of rules which must be obeyed by an object in order for it to be called an iterator.

The protocol states that the object must have a **`next()` method**. This method shall return an object with the following two properties:

1. **`done`** - a Boolean value indicating whether the iterator has reached its last value.
2. **`value`** - holds the next value in a given sequence.

### Iterable


### Iterator
An **iterator** is an object that provides a `next()` method, which returns the next item in the sequence. It keeps track of its current position within the sequence and returns an object with two properties: `value` (the current item) and `done` (a boolean indicating whether there are more items to iterate over).

```js
// Creating a custom iterator
const iterableObj = {
    [Symbol.iterator]() {
        let step = 0;
        return {
            next() {
                step++;
                if (step === 1) {
                    return { value: 'This', done: false };
                } else if (step === 2) {
                    return { value: 'is', done: false };
                } else if (step === 3) {
                    return { value: 'iterator', done: false };
                }
                return { value: undefined, done: true };
            }
        };
    }
};

for (const item of iterableObj) {
    console.log(item); // 'This', 'is', 'iterator'
}
```

### Generator
A generator is a special type of function that can be paused and resumed, and it automatically creates an **iterator** when called.

A **generator** is a special type of iterator that allows you to define an iterative algorithm by writing a single function whose execution is suspended across multiple calls, potentially indefinitely. It uses the `function*` syntax and `yield` statements to control the iteration process. Generators are particularly useful for asynchronous programming and can simplify the creation of iterators.

```js
function* numberGenerator() {
  yield 1;
  yield 2;
  yield 3;
}
const gen = numberGenerator();
console.log(gen.next().value); // 1
```

Generators maintain their internal state automatically, making it easier to write iterators compared to using plain iterator objects. They also support two-way communication where values can be sent back into the generator using the `generator.next(value)` method.

```js
function* fibonacci() {
    let current = 0;
    let next = 1;
    while (true) {
        yield current;
        [current, next] = [next, current + next];
    }
}

// Using the fibonacci generator
const fib = fibonacci();
for (let i = 0; i < 10; i++) {
    console.log(fib.next().value); // Outputs the first 10 Fibonacci numbers
}

```


### `Async Iterator`
Similar to regular iterators, but the next() method returns a Promise that resolves to the `{value, done}` object.


### `Async Iterable`
An object that implements the `Symbol.asyncIterator` method, allowing it to be used with `for-await...of` loops.

```js
const asyncIterable = {
  async *[Symbol.asyncIterator]() {
    yield 'Hello';
    yield 'Async';
    yield 'World';
  }
};

(async () => {
  for await (const item of asyncIterable) {
    console.log(item);
  }
})();
```




## Reference
JavaScript Iterators <https://www.codeguage.com/courses/advanced-js/iteration-introduction>

