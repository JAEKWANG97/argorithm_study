# 07. 두 수의 합
# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.

nums = [3,2,4]
target = 6
value =[]

# 출력 : [0,1]

def sum(target : int ,nums : list)-> list:
    
    for i in range(len(nums)):
        temp = target
        print('타겟에서 첫 요소를 뺍니다.')
        temp = temp - nums[i]
        print('타겟의 값은 ', temp)
        for j in nums[i+1:]:
            print('타겟에서 둘째 요소를 뺍니다.')
            if temp - j == 0:
                value.append(i)
                nums[i] = None
                value.append(nums.index(j))
                return value



print(sum(target, nums))