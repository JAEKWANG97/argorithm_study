# 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.





nums = [0,0,0]

# 출력 = [ [-1,0,1] , [-1,-1,2] ]

value = []

nums.sort()

sum_zero = []

for i in range(len(nums)-2):
    
    for j in range(i+1,len(nums)-1):
        if i == 0 and j == 0 and 0 in nums:
            temp2=[0,0,0]
            sum_zero.append(temp2)
        
        first_value = nums[i]
        second_value = nums[j]
        if -(first_value + second_value) in nums[j+1:] :
            
            temp2 = [first_value,second_value,-(first_value + second_value)]
            if temp2 not in sum_zero:
                sum_zero.append(temp2)


print(sum_zero)


# for k in range(j+1,len(nums)):
#             if nums[i] + nums[j] + nums[k] == 0:
#                 print(nums[i],nums[j],nums[k])
#                 temp = [nums[i],nums[j],nums[k]]
#                 if temp not in value:
#                     value.append(temp)
