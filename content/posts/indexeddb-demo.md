---
title: "IndexedDB Demo"
date: 2025-04-03T21:38:22+08:00
tags: 
 - Common
categories: Inbox
# bookComments: false
# bookSearchExclude: false
---

# IndexedDB Demo

```ts
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
    const openRequest = indexedDB.open('development-database', 1);

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

  // 更新所有跟 componentName 相关的数据
  public updateByComponentName(list: IData[], componentName: string): Promise<{ code: number; msg: string; }> {
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

## Reference
<https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API>
