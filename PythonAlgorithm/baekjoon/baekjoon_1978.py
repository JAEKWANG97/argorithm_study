# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
import collections

n = int(input())

nList = input().split()


print(nList)


# int(input())



primeNum = []

primeNum = list(collections.defaultdict(int))

for i in range(2,len(nList)):
    for j in range(1,len(nList)):
        if i*j in nList: 
            nList[nList.index(i*j)] = 0
            if i not in primeNum:
                primeNum.append(i)



print(primeNum)
