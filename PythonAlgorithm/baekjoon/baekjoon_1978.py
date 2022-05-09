# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
n = int(input())
nList = map(int , input().split())
primeNum = 0
for num in nList:
    primeNumValue = True
    if num > 1:
        for i in range(2,num):
                if num % i == 0:
                    primeNumValue = False
        if primeNumValue == True:
            primeNum += 1
print(primeNum)