

import sys
sys.stdout = open('C:/argorithm_study/leetcode42_2.txt', 'w');
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(f'height = {height}')
def trap(height: list) -> int:
    stack = []
    volume = 0
    print(f"\tfor i in range({len(height)})")
    for i in range(len(height)):

        # 변곡점을 만나는 경우
        while stack and height[i] > height[stack[-1]]:
            print(f"\t\twhile stack and height[{i}] > height[{stack[-1]}]: , while stack and {height[i]} > {height[stack[-1]]}:")
            # 스택에서 꺼낸다.
            top = stack.pop()
            print(f"\t\t\ttop = stack.pop() , top = {top}")

            if not len(stack):
                print(f"\t\t\t\tif not len(stack):")
                print("\t\t\t\tbreak")
                break

            # 이전과의 차이만큼 물 높이 처리 
            distance = i - stack[-1] -1
            print(f"\t\t\tdistance = i - stack[-1] -1 , {distance} = {i} - {stack[-1]} -1")
            waters = min(height[i], height[stack[-1]]) - height[top]
            print(f"\t\t\twaters = min(height[i], height[stack[-1]]) - height[top] , {waters} = {min(height[i], height[stack[-1]])} - {height[top]}")
            print(f"\t\t\tvolume += distance * waters , {volume} += {distance} * {waters}")
            volume += distance * waters

        stack.append(i)
        print(f"\t\tstack.append(i) , {i}")
    print(f"\tvolume = {volume}")
    return volume

print(trap(height))

sys.stdout.close()