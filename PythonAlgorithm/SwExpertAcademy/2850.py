# 입력
# 1
# 5
# 14054
# 44250
# 02032
# 51204
# 52212
 

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    garden = [input() for _ in range(N)]
    print(garden[0][0])
    sum_garden = 0
    mid = N // 2
    print(mid)
    for i in range(N):
        list_for_sum = []
        for g in garden[i]:
            list_for_sum.append(int(g))
        if i < mid:
            sum_garden += sum(list_for_sum[mid-i: -mid+i])
        elif i == mid:
            sum_garden += sum(list_for_sum[:])
        else:
            sum_garden += sum(list_for_sum[i-mid:mid-i])
    print(f'#{test_case} {sum_garden}')
