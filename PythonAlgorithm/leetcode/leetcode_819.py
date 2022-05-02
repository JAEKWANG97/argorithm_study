# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 
# 대소문자 구분을 하지 않으며, 구두점 또한 무시한다.


import collections
import re
# 3107H#FBFB

paragraph = "Bob hit a ball, the hit BALL flew far after ,,it was hit"
banned = ["hit"]

words = [word for word in re.sub(r'[^\w]', ' ' , paragraph)
    .lower().split()
        if word not in banned]



print(words)

counts = collections.Counter(words)

print(counts)

print(counts.most_common(1)[0][0])
# dddddddd

# print(counts.most_common(1)[0][0])

# 출력 ㅣ "ball"