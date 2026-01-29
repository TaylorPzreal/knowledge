
Review
1. 2024-07-28 08:12

## 一、Introduction
All modern browsers have a built-in XMLHttpRequest object to request data from a server.

The XMLHttpRequest object is **a developers dream**, because you can:

- Update a web page without reloading the page
- Request data from a server - after the page has loaded
- Receive data from a server  - after the page has loaded
- Send data to a server - in the background


```js
function reqListener() {
  console.log(this.responseText);
}

const req = new XMLHttpRequest();
req.addEventListener("load", reqListener);
req.open("GET", "https://www.example.org/example.txt", true);
req.send();
```

```js
xhr.open(method, URL, [async, user, password]);
```

This method specifies the main parameters of the request:
- `method` – HTTP-method. Usually `"GET"` or `"POST"`.
- `URL` – the URL to request, a string, can be [URL](https://javascript.info/url) object.
- `async` – if explicitly set to `false`, then the request is synchronous.
- `user`, `password` – login and password for basic HTTP auth (if required).

> Please note that `open` call, contrary to its name, does not open the connection. It only configures the request, but the network activity only starts with the call of `send`.

```js
xhr.send([body])
```

This method opens the connection and sends the request to server. The optional `body` parameter contains the request body.

Some request methods like `GET` do not have a body. And some of them like `POST` use `body` to send the data to the server.

events
1. `load`  - when the request is complete (even if HTTP status is like 400 or 500), and the response is fully downloaded.
2. `error` - when the request couldn’t be made, e.g. network down or invalid URL.
3. `progress` - triggers periodically while the response is being downloaded, reports how much has been downloaded.
4. `timeout` - the request does not succeed within the given time.
5. `abort` – the request was canceled by the call `xhr.abort()`.
6. `loadend` -  triggers after `load`, `error`, `timeout` or `abort`.
7. `readystatechange` - **@deprecated** please use `load/error/progress`


### Response Type
We can use `xhr.responseType` property to set the response format:
- `""` (default) – get as string,
- `"text"` – get as string,
- `"arraybuffer"` – get as `ArrayBuffer` (for binary data, see chapter [ArrayBuffer, binary arrays](https://javascript.info/arraybuffer-binary-arrays)),
- `"blob"` – get as `Blob` (for binary data, see chapter [Blob](https://javascript.info/blob)),
- `"document"` – get as XML document (can use XPath and other XML methods) or HTML document (based on the MIME type of the received data),
- `"json"` – get as JSON (parsed automatically).

```js
let xhr = new XMLHttpRequest();

xhr.open('GET', '/article/xmlhttprequest/example/json');

xhr.responseType = 'json';

xhr.send();

// the response is {"message": "Hello, world!"}
xhr.onload = function() {
  let responseObj = xhr.response;
  alert(responseObj.message); // Hello, world!
};
```

> [!Info]
> Please note:
> 
> In the old scripts you may also find `xhr.responseText` and even `xhr.responseXML` properties.
> 
> They exist for historical reasons, to get either a string or XML document. Nowadays, we should set the format in `xhr.responseType` and get `xhr.response` as demonstrated above.

`xhr.readyState`
```js
UNSENT = 0; // initial state
OPENED = 1; // open called
HEADERS_RECEIVED = 2; // response headers received
LOADING = 3; // response is loading (a data packet is received)
DONE = 4; // request complete
```

An `XMLHttpRequest` object travels them in the order `0` → `1` → `2` → `3` → … → `3` → `4`. State `3` repeats every time a data packet is received over the network.


```js
xhr.abort(); // terminate the request
```

That triggers `abort` event, and `xhr.status` becomes `0`.

## Reference
[Using XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest_API/Using_XMLHttpRequest)
[XMLHttpRequest](https://javascript.info/xmlhttprequest)

