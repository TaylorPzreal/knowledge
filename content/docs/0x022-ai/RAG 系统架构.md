

1. LangChain
2. LLM - GPT 4o
3. Embeddeds 模型：将文本转换为向量
4. 向量数据库
5. 数据处理：加载、分割、向量化

检索架构
先检索、后推理

检索要求
1. 提高召回率
2. 减少无关信息，准确率要高
3. 速度快

二级索引
1. 一级索引：关键信息
2. 二级索引：原始文本

切分 关键信息抽取
chunk_size 切分，不能满足复杂的业务场景；chunk_overloap 重叠区域

切分
1. 基于 NLP 篇章分析工具，识别段落的主从关系
2. Bert、NSP 训练任务，基于阈值 t

keyLLM
1. keyBert 基于关键字匹配训练模型，存储的是向量数据库，向量检索
2. ElasticSearch 基于关键字检索，存储的是JSON，字符串检索


## 参考
[KeyBERT](https://github.com/MaartenGr/KeyBERT) Minimal keyword extraction with BERT
