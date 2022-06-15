# 빗물 트래핑

# 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라.

# 입력 : [0,1,0,2,1,0,1,3,2,1,2,1]

# 출력 : 6

# max를 찾아가며 빈칸을 매꾼다면 ? 

# 스택 구조를 이용해서 풀 수 있을 것 같다.

rain = [0,1,0,2,1,0,1,3,2,1,2,1]
temp = []
water = 0

for i in rain:
    temp.append(int(i))
    # 첫 요소가 0일 경우 불필요한 자료이기때문에 pop
    if temp[0] == 0:
        temp.pop()
    # 이제 max 값을 찾으면서 그 이전의 요소들을 빼줘서 고인 물을 찾을 거임
    if len(temp) > 1:
        print(i, water)
        if max(temp) > i:
            


print(temp, water)
