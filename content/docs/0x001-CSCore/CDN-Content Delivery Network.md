#CDN 

Review
1. 2024-10-06 14:21

> [!Summary]
> CDN(Content Delivery Network)：内容分发网络

## 一、Introduction
**CDN的6大能力**
1. 静态加速能力
2. 卸载源站能力
3. 防攻击能力
4. 动态加速能力
5. 用户访问序列优化能力
6. 定制化模块开发能力


**相关术语**
1. 边缘服务器（Edge Server）：提供给用户就近连接、访问的服务器
2. CDN命中率：CDN服务器有该资源的缓存存在
3. 回源：CDN没有命中缓存，需要到源站去获取资源
4. 中间层服务器（`Midgress Server`）：将多个CDN结点的访问进行收敛，从而大幅提高命中率
5. L2 Cache：CDN的中间层服务器


**核心**
CDN全局调度器：本质是一个智能的*DNS解析工具*

CDN全局调度器：
1. F5的GTM设备
2. 其他智能DNS软件

全局调度器主要有3个元素：
1. Region（区域）
2. POOL（CDN节点池）
3. Member（CDN节点VIP）


**CDN基本调度方式**
1. 基于Local DNS的静态调度
2. 基于RTT的调度
3. 基于成本和带宽的调度
4. 基于服务等级的调度


##### CDN 厂商
1. Fastly
2. Google
3. Cloudflare
4. MaxCDN
5. Akamai


## Reference
1. [一文搞懂CDN的技术架构和原理](https://cloud.tencent.com/developer/article/1644270) 
