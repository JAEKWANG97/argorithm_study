height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

def trap(height):

    volume = 0

    # 높이가 없을 때
    if not height:
        return 0
    
    # 포인터 지정 / left, right = >인덱스값
    left = 0
    right = len(height) - 1

    # 최댓값 초기화 // left_max, right_max => 인덱스 값
    left_max = height[left]
    right_max = height[right]

    while left < right :
        # 최댓값 찾기
        left_max , right_max = max(left_max , height[left]), max(right_max, height[right])
        # 더 높은 쪽을 향해 투포인터 이동
        if left_max < right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
        

    return volume

print(trap(height))
            