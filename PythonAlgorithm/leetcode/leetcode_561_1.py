# 배열파티션
# n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라
n = [1,4,3,2]
# 출력 4
#min(a,b)를 이용해서 최대합을 구해야한다. ex) min(a,b) + min(c,d) ......
# 조건 1 비슷한 숫자들끼리 묶어야한다.
# 그냥 오름차순으로 정렬한 뒤 앞 2개씩 묶으면 안되나?
# 우선 오름차순으로 정렬
def sum(n : list):
    n.sort()

    value = 0

    for i in range(0,len(n),2):
        value = value + n[i]

    return value

print(sum(n))