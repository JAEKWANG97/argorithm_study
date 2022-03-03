# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며, 구두점 또한 무시한다.

from ast import Pass
import collections
import re

from matplotlib.collections import Collection


paragraph = "Bob hit a ball, the hit BALL flew far after ,,it was hit"
paragraph = paragraph.lower()
banned = ["hit"]
paragraph = paragraph.split()
s = re.sub('[^a-z0-9]', ' ', str(paragraph))
s = s.split()

for value in banned:
    s.remove(value)

count = {}

for i in s:
    try: count[i] += 1
    except: count[i] = 1
max_value = max(count.values())

print(max_value)

for i in range(len(count)):
    Pass()
    










# 출력 ㅣ "ball"