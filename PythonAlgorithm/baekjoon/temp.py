from itertools import combinations_with_replacement, product
import math

dataset = []
num =int(41)

for i in range(num):
    if int(math.pow(i,2)) < num :
        dataset.append(i)

# 개를 뽑아 일렬로 나열하는 경우의 수(단, 중복 허용)
res = list(combinations_with_replacement(dataset,num))
temp = int(0)
key = []
theShortestKey = []
for i in res:
    temp = 0 
    for j in i:
        if j != 0:
            temp = temp + int(math.pow(j,2))
    if temp == num:
        list(i).count(0)
        key.append(list(i))

temp2 = 0
for i in key:
    if i.count(0) > temp2:
        theShortestKey = i
        temp2 = i.count(0)

print(num - theShortestKey.count(0))