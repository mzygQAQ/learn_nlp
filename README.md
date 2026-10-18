# learn_nlp

NLP 学习笔记与代码实践，按章节编号组织，每个脚本对应一个知识点，可以单独运行。

## 环境准备

项目用 [uv](https://docs.astral.sh/uv/) 管理依赖（Python >= 3.12）：

```bash
uv sync                                          # 安装依赖（gensim / jieba）
uv run python chapter01_01_jieba_basic_usage.py   # 运行任意脚本
```

## 文件索引

| 文件 | 对应内容 | 链接 |
| --- | --- | --- |
| `chapter01_01_jieba_basic_usage.py` | **jieba 分词基础**：精确模式 / 全模式 / 搜索引擎模式三种切分方式的效果对比，附带中英文混排切分测试 | [查看源码](chapter01_01_jieba_basic_usage.py) |
| `chapter01_02_jieba_custom_dict.py` | **自定义词典**：`jieba.load_userdict` 加载领域词表，让「云计算 / 云原生 / 大模型」这类词不再被拆散，并对比加载前后的切分差异 | [查看源码](chapter01_02_jieba_custom_dict.py) |
| `chapter02_01_word_representation.py` | **词表示的演进**：One-Hot 编码的局限（无语义、维度膨胀）→ Word2Vec 稠密语义向量 → 静态向量与上下文相关向量的区别 | [查看源码](chapter02_01_word_representation.py) |
| `chapter02_02_word2vec.py` | **使用预训练词向量**：用 gensim 加载中文词向量，实操向量维度、词向量查看、余弦相似度、`most_similar` 近义词检索，以及向量算术 `男人 + 女孩 - 男孩` | [查看源码](chapter02_02_word2vec.py) |
| `chapter02_03_train_word_vector.py` | **自己训练词向量**：基于自有语料训练（待补充） | [查看源码](chapter02_03_train_word_vector.py) |
| `chapter02_04_train_word_vector_from_dataset.py` | **从数据集训练词向量**：改用 `LineSentence` 读取外部语料文件训练，摆脱硬编码语料的规模限制（待补充） | [查看源码](chapter02_04_train_word_vector_from_dataset.py) |

配套资源：[`assets/my_test_jieba_dict.txt`](assets/my_test_jieba_dict.txt) —— `chapter01_02` 用到的 jieba 自定义词典，格式为 `词 词频 词性`（半角空格分隔）。

## 目录结构

```
learn_nlp/
├── assets/
│   └── my_test_jieba_dict.txt      # jieba 自定义词典
├── chapter01_01_jieba_basic_usage.py
├── chapter01_02_jieba_custom_dict.py
├── chapter02_01_word_representation.py
├── chapter02_02_word2vec.py
├── chapter02_03_train_word_vector.py
├── chapter02_04_train_word_vector_from_dataset.py
├── pyproject.toml                  # 依赖声明
└── uv.lock                         # 依赖版本锁定
```

## 运行说明

- `chapter01_02` 通过 `Path(__file__).parent` 定位词典文件，因此在任意工作目录下运行都不会报 `FileNotFoundError`。
- `chapter02_02` 需要先下载中文预训练词向量（如 `sgns.weibo.word.bz2`），脚本中的 `model_path` 目前是本机绝对路径，换机器运行时需要改成自己的路径。`.gitignore` 已排除 `*.bz2` 等大文件，不会误提交。
- jieba 源码中的正则使用了非 raw string，在 Python 3.12+ 下会触发 `SyntaxWarning`，脚本已在 `import jieba` 前过滤该警告。

## 作业

### 用 PyTorch 实现 Skip-Gram

> 对应 `chapter02_03` 中的 TODO：`# TODO: 使用pytorch自己实现一个skip gram模型`

不依赖 gensim，自己完整实现一遍 Word2Vec 的 Skip-Gram 训练流程：

- [ ] **语料预处理**：读入分好词的文本，构建词表与词 → 索引映射
- [ ] **滑动窗口采样**：按窗口大小生成 `(中心词, 上下文词)` 训练样本对
- [ ] **负采样**：按词频的 `3/4` 次幂分布为每个正样本采样若干负样本
- [ ] **模型定义**：`nn.Embedding` + 点积 + `sigmoid` 二分类
- [ ] **训练循环**：negative sampling 目标函数、反向传播、学习率衰减
- [ ] **效果验证**：用 `most_similar` 看近义词是否成组，并与 gensim 训练结果对比差异来源

前置条件：PyTorch 尚未列入项目依赖，完成前先执行

```bash
uv add torch
```

> 语料请用**真实文本**（几万不同词量级）。手写的小句子训不出可用的向量——词太少会全挤在 ±0.1 的噪声区，词表太小则会全部塌缩到 0.99+ 的饱和区，两种情况下相似度都不可解释。
