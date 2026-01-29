#Archive 

Review
1. 2023-02-20 23:38

## 一、Introduction
Protocol Buffers(Protobuf) are a language-neutral, platform-neutral extensible mechanism for serializing structured data. ==It's like XML/JSON, but smaller, faster, and simpler.== You define how you want your data to be structured once, then you can use special generated source code to easily write and read your structured data to and from a variety of data streams and using a variety of languages.

Protobuf是Google开源的一种混合语言数据标准。
Protobuf最大的特点是数据格式拥有极高的压缩比，这在移动互联时代是极具价值的（因为移动网络流量到目前为止仍然昂贵的），如果你的APP能比竞品更省流量，无疑这也将成为您产品的亮点之一。现在，尤其IM、消息推送这类应用中，Protobuf的应用更是非常广泛，基于它的优秀表现，微信和手机QQ这样的主流IM应用也早已在使用它。

### 为什么说使用类似protobuf的二进制协议通信更好呢？
1. 二进制协议对于电脑来说更容易解析，在解析速度上是http这样的文本协议不可比拟的；
2. 有tcp和udp两种选择，在一些场景下，udp传输的效率会更高；
3. 在后台开发中，后台与后台的通信一般就是基于二进制协议的。甚至某些native app和服务器的通信也选择了二进制协议（例如腾讯视频）。但由于web前端的存在，后台同学往往需要特地开发维护一套http接口专供我们使用，如果web也能使用二进制协议，可以节省许多后台开发的成本。

在大公司，最重要的就是优化效率、节省成本，因此二进制协议明显优于http这样的文本协议。

### 使用场景
Protocol buffers 非常适用于任何需要以语言中立、平台中立、可扩展的方式序列化结构化、类记录、类型化数据的情况。 它们最常用于定义通信协议（与 gRPC 一起）和数据存储。
1. 存储：数据存储
2. 通信：RPC数据交换格式

### 相似技术
1. XML
2. JSON
3. Protobuf
4. XMPP
5. MQTT
6. Plain text

-   _1）_ Jackson：Java 程序里用的最多的 JSON 解析器。
-   _2）_ DSL-JSON：世界上最快的 Java JSON 实现；
-   _3）_ Jsoniter：抄袭 DSL-JSON 写的实现；
-   _4）_ Fastjson：在中国很流行的 JSON 解析器；
-   _5）_ Protobuf：在 RPC （远程方法调用）里非常流行的二进制编解码格式；
-   _6）_ Thrift：另外一个很流行的 RPC 编解码格式。


### Protocol buffers props and cons
#### Advantages
1. Protocol buffers 允许在不破坏现有服务的情况下无缝支持任何协议缓冲区的更改，包括添加新字段和删除现有字段。
2. 紧凑的数据存储
3. 快速解析
4. 跨语言兼容（C++, Java, Python, Go, JS...）
5. 通过自动生成的类优化功能

#### 不适合场景
- Protocol buffers 倾向于假设整个消息可以一次加载到内存中并且不大于对象图。 对于超过几兆字节的数据，考虑不同的解决方案； 当处理更大的数据时，由于序列化副本，您可能最终会得到多个数据副本，这可能会导致内存使用量出现惊人的峰值。
- 当协议缓冲区被序列化时，相同的数据可以有许多不同的二进制序列化。 如果不完全解析它们，就不能比较两条消息是否相等。
- 消息未压缩。 虽然可以像任何其他文件一样对消息进行压缩或 gzip 压缩，但专用压缩算法（如 JPEG 和 PNG 使用的算法）将为适当类型的数据生成小得多的文件。
- 对于涉及**大型多维浮点数数组**的许多科学和工程用途，Protocol buffer 消息在大小和速度方面都达不到最大效率。 对于这些应用程序，**FITS** 和类似格式的开销较小。
- 科学计算中流行的非面向对象语言（如 Fortran 和 IDL）不能很好地支持协议缓冲区。
- Protocol buffer 消息本身并不自我描述它们的数据，但它们有一个完全反射的模式，您可以使用它来实现自我描述。 也就是说，如果不访问相应的 `.proto` 文件，您就无法完全解释一个。
- Protocol buffers 不是任何组织的正式标准。 这使得它们不适合在具有基于标准构建的法律或其他要求的环境中使用。

## 二、Node.js端开发

### Popular Node.js libraries
1. [protobuf.js](https://github.com/protobufjs/protobuf.js/) 【推荐】
2. [@apollo/protobufjs](https://www.npmjs.com/package/@apollo/protobufjs)
3. [protobuf-javascript](https://github.com/protocolbuffers/protobuf-javascript)
4. [protocol-buffers](https://github.com/mafintosh/protocol-buffers)

推荐使用第一个，如果使用了Apollo，那可以直接使用第二个。

通过 `.proto` 文件描述
```proto
message Person {
  optional string name = 1;
  optional int32 id = 2;
  optional string email = 3;
}
```

proto 编译器在构建时对 .proto 文件调用，以生成各种编程语言的代码（在本主题后面的跨语言兼容性中介绍）来操作相应的协议缓冲区。

#### Installation
```sh
npm install protobufjs --save --save-prefix=~

npm install protobufjs-cli --save --save-prefix=~
```

![](./assets/5b5570f449c6_cee08d74.svg)



### Protocol buffers workflow
![](./assets/0e597feb0224_63c46a80.png)

### Protocol Buffers Definition Syntax
When defining `.proto` files, you can specify that a field is either `optional` or `repeated` (proto2 and proto3) or `singular` (proto3). (The option to set a field to `required` is absent in proto3 and strongly discouraged in proto2. For more on this, see “Required is Forever” in [Specifying Field Rules](https://protobuf.dev/programming-guides/proto#specifying-rules).)

After setting the optionality/repeatability of a field, you specify the data type. Protocol buffers support the usual primitive data types, such as integers, booleans, and floats. For the full list, see [Scalar Value Types](https://protobuf.dev/programming-guides/proto#scalar).

A field can also be of:
-   A `message` type, so that you can nest parts of the definition, such as for repeating sets of data.
-   An `enum` type, so you can specify a set of values to choose from.
-   A `oneof` type, which you can use when a message has many optional fields and at most one field will be set at the same time.
-   A `map` type, to add key-value pairs to your definition.

In proto2, messages can allow **extensions** to define fields outside of the message, itself. For example, the protobuf library’s internal message schema allows extensions for custom, usage-specific options.

For more information about the options available, see the language guide for [proto2](https://protobuf.dev/programming-guides/proto) or [proto3](https://protobuf.dev/programming-guides/proto3).

After setting optionality and field type, you assign a field number. Field numbers cannot be repurposed or reused. If you delete a field, you should reserve its field number to prevent someone from accidentally reusing the number.


## Reference
1. [Protocol Buffers Github](https://github.com/protocolbuffers/protobuf)
2. [Protocol Buffers Doc](https://protobuf.dev/)
