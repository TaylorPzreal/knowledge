
#Streaming 

Review
1. 2024-08-15 07:56

> [!Summary]
> 

## 一、Introduction
> HTTP streaming, also known as HTTP-based streaming or HTTP live streaming, is a technique used to deliver real-time multimedia content, such as audio or video, over the Internet. This protocol allows continuous data transmission from a server to a client device, enabling users to consume media content without requiring complete file downloads.

HTTP streaming utilizes the *Hypertext Transfer Protocol (HTTP)* as its communication protocol. It leverages existing web infrastructure and uses HTTP servers' scalability, caching, and `load-balancing` capabilities. This makes it an efficient and flexible solution for delivering real-time content to many users.

Data is continuously sent from the server to the client without waiting for the entire response to be ready. This allows for real-time or near-real-time updates and can be more efficient for certain types of applications.


## 二、Solutions
- Server-Sent Events (SSE): [[Server Sent Events(SSE)]]
    - A simple protocol that allows the server to push data to the client over HTTP
    - Unidirectional (server to client only)
    - Supported by most modern browsers
- WebSockets:
    - Provides full-duplex, bidirectional communication
    - Allows both client and server to send messages at any time
    - More complex than SSE but offers more flexibility
- Long Polling:
    - An older technique where the client repeatedly polls the server for new information
    - Less efficient than SSE or WebSockets but works in older browsers
- HTTP/2 Server Push:
    - Allows the server to proactively send resources to the client
    - Part of the HTTP/2 protocol
- WebRTC (Web Real-Time Communication):
    - Primarily used for peer-to-peer communication
    - Can be used for streaming data between browsers without a server intermediary
- HTTP Chunked (`Transfer-Encoding: chunked`)


**Protocol**
1. HTTP Streaming(HTTP-based adaptive streaming)
2. WebSockets
3. WebRTC
4. MQTT
5. RTMP(Read-Time Messaging Protocol)
6. HLS(HTTP Live Streaming) by Apple
7. RTSP(Real-Time Streaming Protocol)


### 2.1、SSE
[[Server Sent Events(SSE)]]

### 2.2、HTTP-Chunked



## Reference
[What is HTTP Streaming?](https://www.pubnub.com/guides/http-streaming/)
[Data Streaming Technologies Overview](https://www.pubnub.com/blog/data-streaming-technologies-overview/)
