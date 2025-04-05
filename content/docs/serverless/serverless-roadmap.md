---
title: "Serverless Roadmap"
# weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

## 概述

Review

1. 2022/07/18
2. 2023/02/04
3. 2023/11/28
4. 2025/04/05

Serverless 是云计算发展的最新阶段，它提供了进一步的抽象，使 IT 基础设施资源在需要时动态可用。Serverless 不仅局限于计算服务，而是指一种端到端的架构，覆盖了计算、存储、网络、容器、数据库等多个方面的服务。

20 世纪 90 年代后期，Linux 受到了空前的关注，并最终成为业界领先的服务器操作系统。在 2000 年代初期，虚拟化提高了服务器利用率，为云计算铺平了道路。如今，Linux 和虚拟化作为云计算的基础已经无处不在。而现在，最热的技术话题都是围绕着容器、Kubernetes 和 Serverless 展开，它们也将成为我们日常使用的云基础设施的一部分。

Serverless 提供了进一步的抽象，使 IT 基础设施资源在需要时动态可用。实际上 Serverless 不仅局限于计算服务，而是指一种端到端的架构。除了比较常提起的 Lambda 外，还覆盖了计算、存储、网络、容器、数据库等，集成多个方面的服务，可以快速地构建现代化应用。Serverless屏蔽了服务器细节。

## 核心概念

### Serverless 定义

Serverless = FaaS (Function as a Service) + BaaS (Backend as a Service)

![FaaS演进路线](images/serverless-revolution.jpg)

![Serverless Request](images/serverless-flow.jpg)

### 主要特性

1. 无服务化（自动扩容）
2. 按需付费
3. 通过触发器事件驱动

## 技术实现

### 开源解决方案

1. Kubeless
2. Fission
3. Knative - [GitHub](https://github.com/knative/serving)
4. Midway Serverless
5. Serverless Framework - [GitHub](https://github.com/serverless/serverless)
6. Spin - [官网](https://developer.fermyon.com/spin/index)
   - 基于 WebAssembly (Wasm) 的运行时
   - 专注于构建和运行事件驱动的微服务应用

> Spin 是一个面向开发者的工具，用于引导、构建、测试和部署 Serverless功能。Spin 的核心是其基于 Wasm 运行时。它是开源的。
>
> Spin is a framework for building and running event-driven microservice applications with WebAssembly (Wasm) components. With Spin, we're trying to make it easier to get started with using WebAssembly on the server so that we can all take advantage of the security, portability, and speed WebAssembly provides when it comes to running microservices.

### 弹性伸缩实现

1. Knative Autoscaler：基于实时流量按需进行弹性伸缩
2. Kubernetes HPA（Horizontal Pod Autoscaling）

## 冷启动优化

### 冷启动定义

实例生成需要系统准备工作，包括：

- 下载镜像
- 启动容器
- 下载程序
- 加载程序
- 程序初始化

> 在容器中执行用户程序，这样的环境我们称为实例。实例的生成需要一些额外的系统准备工作，比如下载镜像、启动容器、下载程序、加载程序、程序初始化等。如果请求的调用链路里包含了上述环节，我们就称之为冷启动。实例一旦生成，会持续服务请求；当一段时间内没有请求后，系统将回收实例。因此，冷启动通常发生在函数首次调用或者负载升高需要更多的实例来处理对应的请求。
>
> 不过针对不同的实例生成方式，冷启动有些区别。
> a. 基于 Docker Image 的方式
> 冷启动指的是下载镜像、启动容器、加载程序、程序初始化这些环节。
> 可以先将基础镜像预分发到物理 Node 节点，这样冷启动时只需要下载业务镜像就可以了，能有效降低下载镜像的耗时；另外，后续还会与 Hulk 团队一道去优化 Image 的启动耗时，争取 Docker Image 的方式冷启动时间降低到 10s 以内，（业界一般是 12-13s）。
>
> b. 基于资源池的 Package 方式
> 冷启动指的是下载程序、加载程序、程序初始化这些环节。
> 业界还有一种策略是通过预先准备一批机器资源池，机器内的 Pod 预先启动好，在需要扩容时，只需要下载代码的 Package 包，然后启动起来，这种方式会节省冷启动时间，能够做到 100-200ms 以内（业界一般是 100-200ms）。

### 优化方案

1. 基于 Docker Image 的方式
   - 预分发基础镜像到物理节点
   - 目标：冷启动时间降低到 10s 以内
   - 业界标准：12-13s

2. 基于资源池的 Package 方式
   - 预先准备机器资源池
   - 目标：冷启动时间 100-200ms
   - 业界标准：100-200ms

## 业界发展历程

1. 2014年：亚马逊推出 Amazon Lambda，最早的Serverless框架产品
2. 2019年：Amazon Lambda 发布"预置并发"功能，它允许亚马逊云科技 Serverless 计算用户使其函数保持"已初始化"的状态，极大程度地减少了工作负载突然增加时的扩容时间
3. 2022年：Amazon Lambda SnapStart 发布
   - 冷启动时间降低至 200ms
   - 延迟率降低 90%
4. 2022年：Amazon OpenSearch Serverless 发布
   - 无需管理 OpenSearch 集群
   - 完成数据分析服务 Serverless 化
5. 2023年：AI 与 Serverless 的融合
   - AWS Lambda 支持 AI 模型部署
   - Azure Functions 集成 OpenAI 服务
   - Google Cloud Functions 支持 Vertex AI
6. 2024年：Serverless 架构的进一步演进
   - 边缘计算与 Serverless 的深度整合
   - 多云 Serverless 编排平台兴起
   - 基于 eBPF 的 Serverless 性能优化
7. 2025年：Serverless 新趋势
   - 量子计算与 Serverless 的初步探索
   - 基于 WebAssembly 的 Serverless 运行时成为主流
   - 智能资源调度与成本优化

## 未来趋势

1. 轻服务应用
   - 小程序后端
   - H5页面后端
2. Serverless 与低代码开发结合
3. AI 驱动的 Serverless 应用
   - 自动扩缩容
   - 智能资源调度
   - 预测性成本优化
4. 边缘计算与 Serverless 的融合
   - 更低的延迟
   - 更好的用户体验
   - 更智能的流量分发
5. 多云 Serverless 管理
   - 统一的开发体验
   - 跨云资源调度
   - 成本优化

## Reference

1. Cloud Programming Simplified: A Berkeley View on Serverless Computing <https://www2.eecs.berkeley.edu/Pubs/TechRpts/2019/EECS-2019-3.pdf>
