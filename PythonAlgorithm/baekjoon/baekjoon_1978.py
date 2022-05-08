# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
import collections


N = [i for i in range(2,int(10)+1)]
# int(input())



primeNum = []
nonPrimeNum = []
primeNum = list(collections.defaultdict(int))
nonprimeNum = list(collections.defaultdict(int))
for i in range(2,len(N)):
    for j in range(1,i+1):
        if i*j in N:
            
            print(N)
            N[N.index(i*j)] = 0
            if i not in primeNum:
                primeNum.append(i)


print(N)
print(primeNum)
