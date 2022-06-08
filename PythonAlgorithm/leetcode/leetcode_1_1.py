


from itertools import combinations


class Solution:
    def twoSum(self,nums : list,target:int)->int:
        # print(list(combinations(nums,2)))
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        
        
        
if __name__ == "__main__":
    nums = [3,2,4]
    target = 6
    solve = Solution()
    print(solve.twoSum(nums,target))