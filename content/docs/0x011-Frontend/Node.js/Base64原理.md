#Archive 

Review
1. 2023-02-21 22:57

## 一、Introduction
Base64 编码是最常见的编码方式，基于 64 个==可打印字符==（A-Za-z0-9+/）来表示任意二进制数据的方法，是从二进制转换到可见字符的过程。


## 二、使用场景
1. 数据加密或签名通过 Base64 转换为字符串存储或传输。  
2. 不能传输文件的网络环境可以转换 Base64 进行网络传输。  
3. 在文本资源(如 HTML 和 CSS文件)中嵌入图片文件或其他二进制资源。  
4. 在 URL、网页中传输少量二进制数据等等。

## 三、Base64 编码原理
原理是把每 3 个字节（每个字节为 8 位, 3 个字节为 24 位）重新划为 4 组（每组为 6位，高位补两个 0，作为一个新字节，划分后的每个字节数值的范围是 00000000 - 00111111 即十进制的 0 - 63），然后将划分后的字节的数值作为索引查编码表，获得相应的字符，从而得到编码后的字符串。通过 64 个字符来对任意数据进行编码，因此称为 Base64。

Base64 标准编码表：
![](./assets/7a0427de4724_0a8dca1e.png)

以字符串 “NEW” 为例，对其 Base64 编码：
![[a6eabafb7f81_21c8525a.png]]

如果要编码的字节数不能被 3 整除，最后会多出 1 个或 2 有效的字节。将这样处理，将其用 0 补充至 6 的最小倍数位后，剩余的空位将使用 “=” 填充处理。例如：
![](./assets/40e6df2d2e17_e0cfae03.png)

![](./assets/07faa51f7e99_87aa3a69.png)

经过 Base64 编码后数据会增大，数据经过 Base64 处理后，由原来每 3 个字节，变为为 4 个字节，数据大小会变为原来的 4/3, 因此==数据增大 1/3==。

对于字符内容，相同字符串不同的字符编码(如 utf-8 与 gbk)的 Base64 编码结果会不一样。Base64 是一种通过查表的编码方法，不能用于加密，即使是自定义编码表也不行。

## 四、相似实现
1. Base64
2. Base128
3. LEB128
4. Base85
5. Base128 Varints


### Base 128 Varints
Base 128 Varints 是 Google 开发的序列化库 **Protocol Buffers** 所用的编码方式。  
  
以下为 Protobuf 官方文档中对于 Varints 的解释：  
> Varints are a method of serializing integers using one or more bytes. Smaller numbers take a smaller number of bytes.

即：使用一个或多个字节对整数进行序列化，小的数字占用更少的字节。

简单来说，Base 128 Varints 编码原理就是尽量只储存整数的有效位，高位的 0 尽可能抛弃。

Base 128 Varints 有两个需要注意的细节：
-   _**1）**_ 只能对一部分数据结构进行编码，不适用于所有字节流（当然你可以把任意字节流转换为 string，但不是所有语言都支持这个 trick）。否则无法识别哪部分是无效的 bits；
-   _**2）**_ 编码后的字节可以不存在于 Ascii 表中，因为和 Base 64 使用场景不同，不用考虑是否能正常打印。


## Reference
1. [Base64编码原理](https://www.cnblogs.com/newobjectcc/p/14391876.html)
2. [从Base64到Protobuf，详解Protobuf的数据编码原理](https://mp.weixin.qq.com/s/OgPnO2TEGSc2Eb8wxQTs6g)
