import warnings

# jieba 源码里的正则用了非 raw string（"..\._"、"(\r\n|\s)"），
# Python 3.12 起会抛 SyntaxWarning。必须在 import jieba 之前过滤才有效。
warnings.filterwarnings("ignore", category=SyntaxWarning)

import jieba

TEXT = "小明毕业于北京大学计算机系"

def show(title, words):
    print(f"{title}: {'/'.join(words)}")


# 1) 精确模式（LLM / 传统分词默认用这个）
#    jieba.cut 返回的是生成器，必须遍历或转成列表才能看到词，直接 print 只会打印生成器对象
show("精确模式", jieba.cut(TEXT, cut_all=False))

# 2) 全模式：把句子拆成所有可能的词，粒度最细
show("全模式", jieba.cut(TEXT, cut_all=True))

# 3) 搜索引擎模式：在精确模式基础上，再补出更短的词，适合用于关键词检索
show("搜索引擎模式", jieba.cut_for_search(TEXT))

# 精确模式: 小明/毕业/于/北京大学/计算机系
# 全模式: 小/明/毕业/于/北京/北京大学/大学/计算/计算机/计算机系/算机/系
# 搜索引擎模式: 小明/毕业/于/北京/大学/北京大学/计算/算机/计算机/计算机系



# 测试下混合中英文
print(list(jieba.cut("我是一个chinese, but他更喜欢吃汉堡", cut_all=False)))
# ['我', '是', '一个', 'chinese', ',', ' ', 'but', '他', '更', '喜欢', '吃', '汉堡']