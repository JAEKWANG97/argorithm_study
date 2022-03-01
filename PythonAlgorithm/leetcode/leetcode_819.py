# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며, 구두점 또한 무시한다.

import collections
import re

from matplotlib.collections import Collection


paragraph = "Bob hit a ball, the hit BALL flew far after ,,it was hit"
paragraph = paragraph.lower()
banned = ["hit"]
paragraph = paragraph.split()
s = re.sub('[^a-z0-9]', ' ', str(paragraph))
s = s.split()
print(s)

count = {}

for i in s:
    try: count[i] += 1
    except: count[i] = 1

print(max(count))









# 출력 ㅣ "ball"