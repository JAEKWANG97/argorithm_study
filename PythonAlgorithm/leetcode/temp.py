

s = 'ffddapplppaeerr'

def longestPalindrome(s:str) -> str:
    print('************************************************************팰린드롬 식별 시작************************************************************')
    print('************************************************************팰린드롬 식별 시작************************************************************')
    print('************************************************************팰린드롬 식별 시작************************************************************')
    print('************************************************************팰린드롬 식별 시작************************************************************')
    print('************************************************************팰린드롬 식별 시작************************************************************')
    #팰린드롬 판별 및 투 포인터 확장
    def expand(left : int, right : int) -> str:
        print('left >= 0 and right < len(s) and s[left] == s[right] 일때')
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            print('left -= 1, left = ', left)
            right += 1
            print('right += 1, right = ', right)
        return s[left+1 : right]

    if len(s) < 2 or s == s[::-1]:
        return s
    
    result = ''

    for i in range(len(s)-1):
        print(i)
        result = max(result, expand(i,i+1), expand(i,i+2),key=len)
        print(result)
    return result



print(longestPalindrome(s))