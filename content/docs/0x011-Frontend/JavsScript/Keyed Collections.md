

Review
1. 2019-03-09
2. 2020-03-26
3. 2024-07-24 21:32

> [!本文摘要]
> Keyed collections -- namely, `Map`, `Set`, `WeakMap`, and `WeakSet`
> 1: `Map` – is a collection of keyed values.
> 2: `Set` – is a collection of unique values.
> 3: `WeakMap` is `Map`-like collection that allows only objects as keys and removes them together with associated value once they become inaccessible by other means. `weak reference`
> 4: `WeakSet` is `Set`-like collection that stores only objects and removes them once they become inaccessible by other means. `weak reference`
> 5: `Set` 比 `Array` checkExist(has), 删除(delete)更快
>  
>  These newer keyed collections are more flexible, easier to iterate over, and higher-performing.



## 一、Introduction
Keyed collections are data collections that are ordered by key not index. They are associative in nature. `Map` and `set` objects are keyed collections and are iterable in the order of insertion.

### Map
A [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map) object is a simple key/value map and can iterate its elements in insertion order.

Features
- It only contains what is explicitly put into it
- Keys can be any value
- The keys are ordered
- A Map is an iterable, so it can be directly iterated
- Performs better in scenarios involving frequent additions and removals of key-value paris

```js
const sayings = new Map();

// const sayings = new Map([[true, 'ok']]);
// const sayings = new Map(Object.entries(obj));

sayings.set("dog", "woof");

// Every `map.set` call returns the map itself, so we can “chain” the calls:
sayings.set("cat", "meow").set("elephant", "toot");

sayings.size; // 3

sayings.get("dog"); // woof
sayings.get("fox"); // undefined

sayings.has("bird"); // false

sayings.delete("dog"); // `true` if an element in the `Map` object existed and has been removed, or `false` if the element does not exist.
sayings.has("dog"); // false

for (const [key, value] of sayings) {
  console.log(`${key} goes ${value}`);
}

// "cat goes meow"
// "elephant goes toot"

sayings.clear(); // return undefined
sayings.size; // 0
```

**Object vs Map**
- The keys of an `Object` are [strings](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String) or [symbols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol), whereas they can be of any value for a `Map`.
- You can get the `size` of a `Map` easily, while you have to manually keep track of size for an `Object`.
- The iteration of `maps` is in insertion order of the elements.
- An `Object` has a prototype, so there are default keys in the map. (This can be bypassed using `map = Object.create(null)`.)

```js
let john = { name: "John" };
let ben = { name: "Ben" };

let visitsCountObj = {}; // try to use an object

visitsCountObj[ben] = 234; // try to use ben object as the key
visitsCountObj[john] = 123; // try to use john object as the key, ben object will get replaced

// That's what got written!
alert( visitsCountObj["[object Object]"] ); // 123
```


 whether to use a `Map` or an `Object`:
 - Use `maps` over objects when keys are unknown until run time, and when all keys are the same type and all values are the same type.
- Use maps if there is a need to store primitive values as keys because object treats each key as a string whether it's a number value, boolean value or any other primitive value.
- Use objects when there is logic that operates on individual elements.

Besides that, `Map` has a built-in `forEach` method, similar to `Array`:
```js
// runs the function for each (key, value) pair
recipeMap.forEach( (value, key, map) => {
  alert(`${key}: ${value}`); // cucumber: 500 etc
});
```


There’s `Object.fromEntries` method that does the reverse: given an array of `[key, value]` pairs, it creates an object from them:
```js
let prices = Object.fromEntries([
  ['banana', 1],
  ['orange', 2],
  ['meat', 4]
]);

// now prices = { banana: 1, orange: 2, meat: 4 }

alert(prices.orange); // 2
```

```js
let map = new Map();
map.set('banana', 1);
map.set('orange', 2);
map.set('meat', 4);

let obj = Object.fromEntries(map.entries()); // make a plain object (*)

// done!
// obj = { banana: 1, orange: 2, meat: 4 }

alert(obj.orange); // 2
```

```js
const first = new Map([
  [1, "one"],
  [2, "two"],
  [3, "three"],
]);

const second = new Map([
  [1, "uno"],
  [2, "dos"],
]);

// Merge two maps. The last repeated key wins.
// Spread syntax essentially converts a Map to an Array
const merged = new Map([...first, ...second]);

console.log(merged.get(1)); // uno
console.log(merged.get(2)); // dos
console.log(merged.get(3)); // three
```

### WeakMap
A [`WeakMap`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap) is a collection of key/value pairs whose keys must be objects or [non-registered symbols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol#shared_symbols_in_the_global_symbol_registry), with values of any arbitrary [JavaScript type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures), and which does not create strong references to its keys. That is, an object's presence as a key in a `WeakMap` does not prevent the object from being garbage collected.

**Use case**
1. additional data storage
2. caching
3. Store private data for an object, or to hide implementation details.

```js
let visitsCountMap = new WeakMap(); // weakmap: user => visits count

// increase the visits count
function countUser(user) {
  let count = visitsCountMap.get(user) || 0;
  visitsCountMap.set(user, count + 1);
}

let john = { name: "John" };
countUser(john); // count his visits

// later john leaves us
john = null;
```

```js
// 📁 cache.js
let cache = new WeakMap();

// calculate and remember the result
function process(obj) {
  if (!cache.has(obj)) {
    let result = /* calculate the result for */ obj;

    cache.set(obj, result);
    return result;
  }

  return cache.get(obj);
}

// 📁 main.js
let obj = {/* some object */};

let result1 = process(obj);
let result2 = process(obj);

// ...later, when the object is not needed any more:
obj = null;

// Can't get cache.size, as it's a WeakMap,
// but it's 0 or soon be 0
// When obj gets garbage collected, cached data will be removed as well
```

```js
const privates = new WeakMap();

function Public() {
  const me = {
    // Private data goes here
  };
  privates.set(this, me);
}

Public.prototype.method = function () {
  const me = privates.get(this);
  // Do stuff with private data in `me`
  // …
};

module.exports = Public;

```

Now, if we use an object as the key in it, and there are no other references to that object – it will be removed from memory (and from the map) automatically.
```js
let john = { name: "John" };

let weakMap = new WeakMap();
weakMap.set(john, "...");

john = null; // overwrite the reference

// john is removed from memory!
```

`WeakMap` has only the following methods:
- `weakMap.set(key, value)`
- `weakMap.get(key)`
- `weakMap.delete(key)`
- `weakMap.has(key)`

### Set
[`Set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set) objects are collections of unique values. You can iterate its elements in insertion order. A value in a `Set` may only occur once; it is unique in the `Set`'s collection.

```js
const mySet = new Set();
mySet.add(1);
mySet.add("some text");
mySet.add("foo"); // adds a value, returns the set itself.

mySet.has(1); // true
mySet.delete("foo"); // removes the value, returns `true` if `value` existed at the moment of the call, otherwise `false`.
mySet.size; // 2

for (const item of mySet) {
  console.log(item);
}
// 1
// "some text"

mySet.clear(); // removes everything from the set.

```

```js
Array.from(mySet);
[...mySet2];


mySet2 = new Set([1, 2, 3, 4]);
```

**Array vs Set**
- Deleting `Array` elements by value (`arr.splice(arr.indexOf(val), 1)`) is very slow.
- `Set` objects let you delete elements by their value. With an array, you would have to `splice` based on an element's index.
- The value [`NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN) cannot be found with `indexOf` in an array.
- `Set` objects store unique values. You don't have to manually keep track of duplicates.

> The alternative to `Set` could be an `array` of users, and the code to check for duplicates on every insertion using [arr.find](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find). But the performance would be much worse, because this method walks through the whole array checking every element. `Set` is much better optimized internally for uniqueness checks.

```js
let set = new Set(["oranges", "apples", "bananas"]);

for (let value of set) alert(value);

// the same with forEach:
set.forEach((value, valueAgain, set) => {
  alert(value);
});
```


### WeakSet
[`WeakSet`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakSet) objects are collections of garbage-collectable values, including objects and [non-registered symbols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol#shared_symbols_in_the_global_symbol_registry). A value in the `WeakSet` may only occur once. It is unique in the `WeakSet`'s collection.

**Set vs WeakSet**
- In contrast to `Sets`, `WeakSets` are **collections of _objects or symbols only_**, and not of arbitrary values of any type.
- The `WeakSet` is _weak_: References to objects in the collection are held weakly. If there is no other reference to an object stored in the `WeakSet`, they can be garbage collected. That also means that there is no list of current objects stored in the collection.
- `WeakSets` are not enumerable.

> The use cases of `WeakSet` objects are limited. They will not leak memory, so it can be safe to use DOM elements as a key and mark them for tracking purposes.

methods
1. `add`
2. `has`
3. `delete`

## Reference
[Keyed collections](<https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Keyed_collections>)
[ES6 keyed collections: Maps and sets](<https://blog.logrocket.com/es6-keyed-collections-maps-and-sets/>)
[How to Use JavaScript Collections – Map and Set](https://www.freecodecamp.org/news/how-to-use-javascript-collections-map-and-set/)
[Map and Set](https://javascript.info/map-set)
[WeakMap and WeakSet](https://javascript.info/weakmap-weakset)
