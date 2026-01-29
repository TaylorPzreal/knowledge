
#IndexedDB 

Review
1. 2023-08-25 23:21

## 一、Introduction
> [!Info] 简介
> IndexedDB is a low-level API for client-side storage of significant amounts of structured data, including files/blobs. This API uses indexes to enable high performance searches of this data. While DOM Storage is useful for storing smaller amounts of data, it is less useful for storing larger amounts of structured data. IndexedDB provides a solution.

IndexedDB is a large-scale, NoSQL storage system. It lets you store just about anything in the user's browser. In addition to the usual search, get, and put actions, IndexedDB also supports transactions.

Each IndexedDB database is unique to an [origin](https://developer.mozilla.org/docs/Glossary/Origin) (typically, this is the site domain or subdomain), meaning it cannot access or be accessed by any other origin. [Data storage limits](https://web.dev/storage-for-the-web/) are usually quite large, if they exist at all, but different browsers handle limits and data eviction differently.

## 二、IndexedDB terms

### [Database](https://developer.mozilla.org/docs/Web/API/IDBDatabase)

The highest level of IndexedDB. It contains the object stores, which in turn contain the data you would like to persist. You can create multiple databases with whatever names you choose. The **second parameter** to the open method is the version of the database. The version of the database determines the database schema — the object stores in the database and their structure.

```js
// Let us open our database
const request = window.indexedDB.open("MyTestDatabase", 3);

request.onerror = (event) => {
  // Do something with request.errorCode!
};
request.onsuccess = (event) => {
  // Do something with request.result!
};
```

### [Object store](https://developer.mozilla.org/docs/Web/API/IDBObjectStore)

An individual bucket to store data. You can think of object stores as being similar to **tables** in traditional relational databases. Typically, there is one object store for each _type_ (not JavaScript data type) of data you are storing. For example, given an app that persists blog posts and user profiles, you could imagine two object stores. Unlike tables in traditional databases, the actual JavaScript data types of data within the store do not need to be consistent (for example, if there are three people in the `people` object store, their age properties could be `53`, `'twenty-five'`, and `unknown` ).

```js
// Check for support.
if (!('indexedDB' in window)) {
  console.log("This browser doesn't support IndexedDB.");
  return;
}

const dbPromise = idb.open('test-db3', 1, function (upgradeDb) {
  if (!upgradeDb.objectStoreNames.contains('people')) {
    upgradeDb.createObjectStore('people', { keyPath: 'email' });
  }

  if (!upgradeDb.objectStoreNames.contains('notes')) {
    upgradeDb.createObjectStore('notes', { autoIncrement: true });
  }

  if (!upgradeDb.objectStoreNames.contains('logs')) {
    upgradeDb.createObjectStore('logs', { keyPath: 'id', autoIncrement: true });
  }
});
```

### [Index](https://developer.mozilla.org/docs/Web/API/IDBIndex)

A kind of object store for organizing data in another object store (called the reference object store) by an individual property of the data. **The index is used to retrieve records in the object store by this property**. For example, if you're storing people, you may want to fetch them later by their name, age, or favorite animal.

```js
objectStore.createIndex('indexName', 'property', options);
```

### Operation

An interaction with the database.

### [Transaction](https://developer.mozilla.org/docs/Web/API/IDBTransaction)

**A wrapper around an operation, or group of operations, that ensures database integrity.** If one of the actions within a transaction fails, none of them are applied and the database returns to the state it was in before the transaction began. All read or write operations in IndexedDB must be part of a transaction. This allows for atomic read-modify-write operations without having to worry about other threads acting on the database at the same time.

All data operations in IndexedDB are carried out inside a transaction. Each operation has this form:
1. Get database object
2. Open transaction on database
3. Open object store on transaction
4. Perform operation on object store

### [Cursor](https://developer.mozilla.org/docs/Web/API/IDBCursor)

A mechanism for **iterating over multiple records** in a database.

## 三、Usage

add
```js
someObjectStore.add(data, optionalKey);
```

The `data` parameter can be data of any type: a string, number, object, array, and so forth.

The `add()` method has an optional second argument that lets you define the primary key for the individual object on creation, but it should only be used if you have not specified the key path in `createObjectStore()`.

get(only return first match)
```js
someObjectStore.get(primaryKey);
```


update
```js
someObjectStore.put(data, optionalKey);
```


delete
```js
someObjectStore.delete(primaryKey);
```

Getting all the data
```js
someObjectStore.getAll(optionalConstraint);
```

```js
someObjectStore.openCursor(optionalKeyRange, optionalDirection);
```


### A Demo
```js
interface IData {
  componentName: string;
  propName: string;
  voId: number;
  renterKey: string;
  componentName_voId: string;
}

class Database {
  private static _instance: Database;

  private connection;

  constructor() {
    const openRequest = indexedDB.open('mcp-development-database', 1);

    openRequest.onupgradeneeded = (e: any) => {
      const db = e.target.result;
      console.log('Database upgradeneeded');

      if (!db.objectStoreNames.contains('voStore')) {
        const store = db.createObjectStore('voStore', { keyPath: 'componentName_voId' });
        store.createIndex('componentName_voId', 'componentName_voId', { unique: true });
        store.createIndex('componentName', 'componentName', { unique: false });
        store.createIndex('voId', 'voId', { unique: false });
      }
    };

    openRequest.onsuccess = (e: any) => {
      const db = e.target.result;
      this.connection = db;
    };

    openRequest.onerror = (e: any) => {
      console.log('Database init error', e.target.error.name);
    };
  }

  static getDB() {
    if (!Database._instance) {
      Database._instance = new Database();
    }
    return Database._instance;
  }

  // 更新所有跟物料 componentName 相关的数据
  public updateByComponentName(list: IData[], componentName: string): Promise<{code: number; msg: string;}> {
    return new Promise((resolve) => {
      const tx = this.connection.transaction('voStore', 'readwrite');
      const store = tx.objectStore('voStore');

      this._searchByComponentName(componentName, store).then((data) => {
        const listByName: IData[] = data;

        list.forEach((item) => {
          if (listByName.some((l) => item.componentName_voId === l.componentName_voId)) {
            // update
            const putRequest = store.put(item);
            putRequest.onsuccess = () => {
              console.log('update');
            };
          } else {
            // new add
            const addRequest = store.add(item);

            addRequest.onsuccess = () => {
              console.log('add');
            };
          }
        });

        // remove not found
        const removeList = listByName.filter((l) => list.every((i) => i.componentName_voId !== l.componentName_voId));
        removeList.forEach((l) => {
          const deleteRequest = store.delete(l.componentName_voId);
          deleteRequest.onsuccess = () => {
            console.log('delete');
          };
        });
      });

      tx.oncomplete = () => {
        resolve({
          code: 200,
          msg: '更新成功',
        });
      };
    });
  }

  private _searchByComponentName(componentName: string, store: any): Promise<IData[]> {
    return new Promise((resolve) => {
      const index = store.index('componentName');
      const getRequest = index.openCursor(IDBKeyRange.only(componentName));
      const result: IData[] = [];

      getRequest.onsuccess = (e) => {
        const cursor = e.target.result;

        if (cursor) {
          result.push(cursor.value);
          cursor.continue();
        } else {
          // 没有更多数据
          resolve(result);
        }
      };
    });
  }

  public searchByComponentName(componentName: string): Promise<IData[]> {
    const tx = this.connection.transaction('voStore', 'readwrite');
    const store = tx.objectStore('voStore');

    return new Promise((resolve) => {
      const index = store.index('componentName');
      const getRequest = index.openCursor(IDBKeyRange.only(componentName));
      const result: IData[] = [];

      getRequest.onsuccess = (e) => {
        const cursor = e.target.result;

        if (cursor) {
          result.push(cursor.value);
          cursor.continue();
        } else {
          // 没有更多数据
          resolve(result);
        }
      };
    });
  }
}

export default Database;
```


## 四、生态

开源库
1. [idb](https://github.com/jakearchibald/idb)
2. [localForage](https://github.com/localForage/localForage)
3. [idb-keyval](https://github.com/jakearchibald/idb-keyval)
4. [Dexie.js](https://dexie.org/)
5. [JsStore](https://jsstore.net/)


## Reference
1. [MDN IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API)
2. [Working with IndexedDB](https://web.dev/indexeddb/)
3. [IndexedDB](https://javascript.info/indexeddb)
