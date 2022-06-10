# def twoSum(nums: list[int], target : int) -> list[int]:
#     nums_map = {}
#     # 키와 값을 바꿔서 딕셔너리로 저장
#     for i , num in enumerate(nums):
#         nums_map[num] = i

#     # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
#     for i , num in enumerate(nums):
#         temp = target - num
#         if temp in nums_map and i != nums_map[temp]:
#             return [i, nums_map[temp]]


nums = [2,7,11,15]
target = 9
# # print(twoSum(nums, target))
# nums_map = {}
# for i , num in enumerate(nums):
        
#        nums_map[num] = i
#        print(nums_map[num])

# for i , num in enumerate(nums):
#     print(i , num)



# from typing import List


# def twoSum(nums: List[int], target: int) -> list[int]:
#     nums_map  = {}
#     # 하나의 for문으로 통합
#     for i, num in enumerate(nums):
#         if target - num in nums_map:
#             return [nums_map[target - num], i]
#         nums_map[num] = i

# nums_map  = {}
#     # 하나의 for문으로 통합
# for i, num in enumerate(nums):
#     if target - num in nums_map:
#         print ([nums_map[target - num], i])
#     nums_map[num] = i





def twoSum(nums: list[int] , target: int) -> list[int]:
    left, right =0, len(nums) -1
    while not left == right:
        #합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
        if nums[left] + nums[right] < target:
            left += 1
        # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]


