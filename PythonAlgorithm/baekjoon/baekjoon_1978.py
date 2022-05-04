# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

import collections


n = 10
num = int(2)
PrimeNum = int(2)
count = 0
while True:
    if num > n:
        break
    temp = 0
    for i in range(2, num):
        if temp == 1:
            count += 1
        if num % i == 0:
            temp += 1
            if temp > 1:
                break
    
    num += 1

print(count)

    




