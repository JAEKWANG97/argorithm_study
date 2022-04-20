# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, 
# ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, 
# aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오

# 3
# happy
# new
# year

# 3



def isGroupWord(groupWord):
    groupWord = list(groupWord)
    testList = []
    for i in groupWord:
        # testList가 empty이면 
        if not testList:
           testList.append(i)
        else:   
            if i != testList[-1] and i not in testList:
                testList.append(i)
            elif i != testList[-1] and i in testList:
                return False
    return True

        

n = int(input())
isItGroupword = False 
count = int(0)
for i in range(n) :
    groupWord = input()
    if isGroupWord(groupWord):
        count = count+1
print(count)

