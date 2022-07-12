# 파이썬 다운 방식
# 앞서 살펴본 슬라이싱을 활용하면 놀랍게도 단 한줄로도 풀이가 가능하다.

from ast import List

nums = [1,4,3,2]

def arrayPairSum(nums):
    return sum(sorted(nums)[::2])


print(arrayPairSum(nums))

