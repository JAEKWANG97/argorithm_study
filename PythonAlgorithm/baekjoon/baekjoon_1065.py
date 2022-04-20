# # 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 
# # 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
# # N이 주어졌을 때, 1보다 크거나 같고,
# # N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

# 110   99

def hansu(n : int, value : int):
   
    temp = []
    if n < 100:
        value = value + n
        return value
    else:
        for i in str(n):
            temp.append(int(i))
        if (temp[0]+temp[2])//2 == temp[1]:
            return hansu(n-1 , value+1)
        else:
            return hansu(n-1 , value)

# 입력된 정수
n = int(input())
# 한수의 개수
value = 0

print(hansu(n,value))

