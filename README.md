# learn_nlp

NLP 学习笔记与代码实践，按章节编号组织，每个脚本对应一个知识点，可以单独运行。

## 环境准备

项目用 [uv](https://docs.astral.sh/uv/) 管理依赖（Python >= 3.12）：

```bash
uv sync                                          # 安装依赖（gensim / jieba）
uv run python chapter01_01_jeba_basic_usage.py   # 运行任意脚本
```

## 文件索引

| 文件 | 对应内容 | 链接 |
| --- | --- | --- |
| `chapter01_01_jeba_basic_usage.py` | **jieba 分词基础**：精确模式 / 全模式 / 搜索引擎模式三种切分方式的效果对比，附带中英文混排切分测试 | [查看源码](chapter01_01_jeba_basic_usage.py) |
| `chapter01_02_jeba_custom_dict.py` | **自定义词典**：`jieba.load_userdict` 加载领域词表，让「云计算 / 云原生 / 大模型」这类词不再被拆散，并对比加载前后的切分差异 | [查看源码](chapter01_02_jeba_custom_dict.py) |
| `assets/my_test_jieba_dict.txt` | 上一节用到的自定义词典文件，格式为 `词 词频 词性`（半角空格分隔） | [查看文件](assets/my_test_jieba_dict.txt) |
| `chapter02_01_word_representation.py` | **词表示的演进**：One-Hot 编码的局限（无语义、维度膨胀）→ Word2Vec 稠密语义向量 → 静态向量与上下文相关向量的区别 | [查看源码](chapter02_01_word_representation.py) |
| `chapter02_02_word2vec.py` | **使用预训练词向量**：用 gensim 加载中文词向量，实操向量维度、词向量查看、余弦相似度、`most_similar` 近义词检索，以及向量算术 `男人 + 女孩 - 男孩` | [查看源码](chapter02_02_word2vec.py) |
| `chapter02_03_train_word_vector.py` | **自己训练词向量**：基于自有语料训练（待补充） | [查看源码](chapter02_03_train_word_vector.py) |

## 目录结构

```
learn_nlp/
├── assets/
│   └── my_test_jieba_dict.txt      # jieba 自定义词典
├── chapter01_01_jeba_basic_usage.py
├── chapter01_02_jeba_custom_dict.py
├── chapter02_01_word_representation.py
├── chapter02_02_word2vec.py
├── chapter02_03_train_word_vector.py
├── pyproject.toml                  # 依赖声明
└── uv.lock                         # 依赖版本锁定
```

## 运行说明

- `chapter01_02` 通过 `Path(__file__).parent` 定位词典文件，因此在任意工作目录下运行都不会报 `FileNotFoundError`。
- `chapter02_02` 需要先下载中文预训练词向量（如 `sgns.weibo.word.bz2`），脚本中的 `model_path` 目前是本机绝对路径，换机器运行时需要改成自己的路径。`.gitignore` 已排除 `*.bz2` 等大文件，不会误提交。
- jieba 源码中的正则使用了非 raw string，在 Python 3.12+ 下会触发 `SyntaxWarning`，脚本已在 `import jieba` 前过滤该警告。
