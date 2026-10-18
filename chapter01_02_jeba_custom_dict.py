# 02: 自定义词表，用于增强特定领域词汇的识别能力
import warnings

# jieba 源码里的正则用了非 raw string（"..\._"、"(\r\n|\s)"），
# Python 3.12 起会抛 SyntaxWarning。必须在 import jieba 之前过滤才有效。
warnings.filterwarnings("ignore", category=SyntaxWarning)

from pathlib import Path

import jieba

TEXT = "随着云计算技术的普及, 越来越多企业采用云原生架构部署服务，此外还有大模型能力的支持。"

# 基础模式
print(list(jieba.cut(TEXT, cut_all=False)))
# ['随着', '云', '计算技术', '的', '普及', ',', ' ', '越来越', '多', '企业',
# '采用', '云', '原生', '架构', '部署', '服务',
# '，', '此外', '还有', '大', '模型', '能力', '的', '支持', '。']

# 指定词典（用 __file__ 定位，避免工作目录不是项目根时报 FileNotFoundError）
# 词典格式：词 词频 词性，词频和词性都不能省（词性可省但词频不行），
# 分隔符必须是半角空格，Tab 不行
DICT_PATH = Path(__file__).parent / "assets" / "my_test_jieba_dict.txt"
jieba.load_userdict(str(DICT_PATH))
print(list(jieba.cut(TEXT, cut_all=False)))
# ['随着', '云计算', '技术', '的', '普及', ',', ' ', '越来越', '多', '企业',
# '采用', '云原生', '架构', '部署', '服务', '，', '此外', '还有', '大模型', '能力', '的', '支持', '。']
