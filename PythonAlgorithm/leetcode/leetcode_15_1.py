# 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.





nums = [-1,0,1,2,-1,-4]

# 출력 = [ [-1,0,1] , [-1,-1,2] ]

value = []

nums.sort()

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            if nums[i] + nums[j] + nums[k] == 0:
                print(nums[i],nums[j],nums[k])
                temp = [nums[i],nums[j],nums[k]]
                if temp not in value:
                    value.append(temp)



