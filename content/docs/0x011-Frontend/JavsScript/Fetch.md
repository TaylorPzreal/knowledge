
Review
1. 2024-07-28 09:38

## 一、Introduction
The `fetch()` method is modern and versatile.

```js
let promise = fetch(url, [options])
```
- **`url`** – the URL to access.
- **`options`** – optional parameters: method, headers etc.

**First, the `promise`, returned by `fetch`, resolves with an object of the built-in Response class as soon as the server responds with headers.**

```js
let response = await fetch(url);

if (response.ok) { // if HTTP-status is 200-299
  // get the response body (the method explained below)
  let json = await response.json();
} else {
  alert("HTTP-Error: " + response.status);
}
```

Response properties:
- `response.status` – HTTP code of the response,
- `response.ok` – `true` if the status is 200-299.
- `response.headers` – Map-like object with HTTP headers.

`Response` provides multiple promise-based methods to access the body in various formats:
- **`response.text()`** – read the response and return as text,
- **`response.json()`** – parse the response as JSON,
- **`response.formData()`** – return the response as `FormData` object,
- **`response.blob()`** – return the response as [Blob](https://javascript.info/blob) (binary data with type),
- **`response.arrayBuffer()`** – return the response as [ArrayBuffer](https://javascript.info/arraybuffer-binary-arrays) (low-level representation of binary data),
- additionally, `response.body` is a [ReadableStream](https://streams.spec.whatwg.org/#rs-class) object, it allows you to read the body chunk-by-chunk.

```js
async function req() {
  let url = 'https://api.github.com/repos/javascript-tutorial/en.javascript.info/commits';
  let response = await fetch(url);
  let commits = await response.json(); // read response body and parse as JSON

  console.log(commits[0].author.login);
  console.log(response.headers.get('Content-Type'));

  for (const [key, value] of response.headers) {
    console.log(key, '--', value);
  }
}

req();

```


To make a `POST` request, or a request with another method, we need to use `fetch` options:
- **`method`** – HTTP-method, e.g. `POST`,
- **`body`** – the request body, one of:
    - a string (e.g. `JSON-encoded`),
    - `FormData` object, to submit the data as `multipart/form-data`,
    - `Blob`/`BufferSource` to send binary data,
    - `URLSearchParams`, to submit the data in `x-www-form-urlencoded` encoding, rarely used.


```js
async function req() {
  let response = await fetch('/post/url', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json;charset=utf-8'
    },
    body: JSON.stringify({ name: 'Demo' })
  });

  let result = await response.json(); // read response body and parse as JSON
}

req();
```

> Please note, if the request `body` is a string, then `Content-Type` header is set to `text/plain;charset=UTF-8` by default.



## Reference
Fetch API <https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API>
Using the Fetch API <https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch>
