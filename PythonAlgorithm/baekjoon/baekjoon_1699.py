# # 어떤 자연수 N은 그보다 작거나 같은 제곱수들의 합으로 나타낼 수 있다. 예를 들어 11=3^2+1^2+1^2(3개 항)이다.
# # 이런 표현방법은 여러 가지가 될 수 있는데, 11의 경우 11=2^2+2^2+1^2+1^2+1^2(5개 항)도 가능하다. 
# # 이 경우, 수학자 숌크라테스는 “11은 3개 항의 제곱수 합으로 표현할 수 있다.”라고 말한다. 
# # 또한 11은 그보다 적은 항의 제곱수 합으로 표현할 수 없으므로, 11을 그 합으로써 표현할 수 있는 제곱수 항의 최소 개수는 3이다.
# # 주어진 자연수 N을 이렇게 제곱수들의 합으로 표현할 때에 그 항의 최소개수를 구하는 프로그램을 작성하시오.


# # 최단거리



# from inspect import stack
from itertools import *
import itertools


# num = int(11)
# numList = []

# # stk = {int : list}
# # key = 경로 , value = 리스트

# for i in range(num):
#     numList.append(int(0))

# print(numList)

# # def calcul(num : int , stk : dict, numList : list, temp : int):
# #     value = int(0)
# #     temp = int(0)



# #     # 경로 확인 작업
# #     for i in numList:
# #         value = value+ i**i
# #         if value > num:
# #             return None
# #         elif value == num:
# #             stk.setdefault
# #         else:
# #             calcul(num , stk , numList, temp )


dataset = ['A', 'B', 'C']
printList = list(itertools.product(dataset, 2))
print(printList)

# 결과값
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]