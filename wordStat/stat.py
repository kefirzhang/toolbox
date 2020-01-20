import jieba
import jieba.analyse
from collections import Counter
from pprint import pprint

jieba.enable_paddle()  # 启动paddle模式。 0.40版之后开始支持，早期版本不支持
file_object = open('jd.txt')
file_context = file_object.read()
file_object.close()
for word, weight in jieba.analyse.extract_tags(file_context, topK=50, withWeight=True):
    print('%s %s' % (word, weight))
print('-' * 20)
for word, weight in jieba.analyse.textrank(file_context, withWeight=True):
    print('%s %s' % (word, weight))
exit()
seg_list = jieba.cut(file_context, use_paddle=False)  # 使用paddle模式
counter = Counter(seg_list)
pprint(counter.most_common(100))
'''

for i in seg_list:
    print(i)
'''
