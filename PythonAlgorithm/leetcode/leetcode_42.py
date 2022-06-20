# 빗물 트래핑

# 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라.

# 입력 : [0,1,0,2,1,0,1,3,2,1,2,1]

# 출력 : 6

# max를 찾아가며 빈칸을 매꾼다면 ? 

# 스택 구조를 이용해서 풀 수 있을 것 같다.

import sys
sys.stdout = open('C:/argorithm_study/leetcode_42.txt','a')



rain = [0,1,0,2,1,0,1,3,2,1,2,1]
print(len(rain))

def trap(height: list ) -> int:
    if not height:
        return 0
    
    volume = 0
    left, right = 0, len(height) -1
    
    left_max,right_max =height[left], height[right]

    while left < right:
        left_max, right_max = max(height[left],left_max),max(height[right],right_max)
        print(f"left_max, right_max = {left_max}, {right_max}")
        print("left, right 높이", height[left], height[right])
    # 더 높은 쪽을 향해 투 포인터 이동
        if left_max <= right_max:
            print("\t left_max <= right_max")
            print(f"\t{volume} += {left_max} - {height[left]}")
            volume += left_max - height[left]
            print(f"\tvolume = {volume} ")
            left += 1
            print(f"\tleft += 1 , left = {left}")
        else:
            print("\tleft_max > right_max")
            print(f"\t{volume} += {right_max} - {height[right]}")
            volume += right_max - height[right]
            print(f"\tvolume = {volume} ")
            right -= 1
            print(f"\tleft += 1 , left = {left}")
    return volume

print(trap(rain))
sys.stdout.close()