# 배열파티션

# n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라

n = [1,4,3,2]

# 출력 4

#min(a,b)를 이용해서 최대합을 구해야한다. ex) min(a,b) + min(c,d) ......

# 조건 1 최대한 작은 것 끼리 모아야 한다.
# 조건 2 제일 큰수와 그 다음 큰 수를 차례로 묶는다.

# 그냥 오름차순으로 정렬한 뒤 앞 2개씩 묶으면 안되나?


# 우선 오름차순으로 정렬
n.sort()

print(n)
value = 0
for i in range(0,len(n)-1):
    value = value + min(n[i] ,n[i+1])
    if i == n[-2]:
        break

print(value)

