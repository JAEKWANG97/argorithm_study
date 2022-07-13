# 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈 한 풀이

nums = [1,2,3,4]

def productExceptSelf(nums : list) -> list:
    # p가 1이여야 왼쪽 첫번째 오른쪽 마지막, 오른쪽 첫 번째 왼쪽 마지막 곱이 가능
    p = 1
    out = []
    # 왼쪽값 곱하기
    for i in range(0,len(nums)):
        # 한번 쭉 거치고 난 뒤 배열에 넣기
        out.append(p)
        p = p *nums[i]
    # 왼쪽 값 곱 한 것에 오른쪽 값 곱하기
    p = 1
    for i in range(len(nums)-1 , -1 , -1):
        out[i] = out[i] * p
        p = p*nums[i]

    return out

print(productExceptSelf(nums))
