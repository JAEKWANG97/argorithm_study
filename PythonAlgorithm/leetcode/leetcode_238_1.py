# 배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라



# 출력 [24,12,8,6]

# 나눗셈을 하지 않고 O(n)에 풀이하라

nums = [1,2,3,4]
values = []

for i in range(0,len(nums)):
    tmp = nums.copy()
    tmp[i] = 1
    tmp = '*'.join(list(map(str,tmp)))
    values.append(eval(tmp))

print(values)

    