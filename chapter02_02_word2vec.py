# 安装gensim, 提供了便捷接口来加载Word2Vec格式的词向量,也支持基于自有语料训练属于自己的词向量模型.

from gensim.models import KeyedVectors

# 微博的语料库训练的词向量.
model_path = 'C:\\Users\\mzygd\\Desktop\\kvcache\\AI学习资料\\sgns.weibo.word.bz2' # 支持解压后的也支持压缩包
model = KeyedVectors.load_word2vec_format(model_path)

# 向量维度
print(model.vector_size) # 300

# 查看某个词的向量
print(model['地铁'])

# 查看2个词的余弦相似度, [-1,1]
print(model.similarity('地铁','公交')) # 0.65458214
print(model.similarity('地铁','放牛')) #

# 查看与某个词相近的词
print(model.most_similar(positive="地铁", negative=None,topn=4))
# [('二号线', 0.6998022198677063),
# ('四号线', 0.6872348785400391),
# ('北京地铁', 0.6863653659820557),
# ('一号线', 0.6666116118431091),

# 先向量运算，再查询： 男人+男孩-女孩=？
print(model.most_similar(positive=["男人", "女孩"], negative=["男孩"],topn=4))
# [('女人', 0.6578881740570068),
# ('女孩子', 0.515068531036377),
# ('女生', 0.45194485783576965),
# ('女人真', 0.4420627951622009)]