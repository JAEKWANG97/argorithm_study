from itertools import combinations_with_replacement, product
from more_itertools import flatten
dataset = [0,1,2,3,]
num =int(11)
# 2개를 뽑아 일렬로 나열하는 경우의 수(단, 중복 허용)
res = list(combinations_with_replacement(dataset, num))
temp = int(0)

# for i in res:
#     print(type(i))

# print(f"모든 경우: {res}")
# print(f"모든 경우의 수: {len(res)}") # 9

