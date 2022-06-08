# leetcode 5.longest Palindrome Substring
# 가장 긴 팰린드롬 부분 문자열을 출력하라
# 입력 : "babad"
# 출력 : "bab"

# 설명 : bab 외에도 aba도 정답이다.

# 입력 : cbbd
# 출력 : bb

s = 'cbbd'


def longestPalindrome(s:str) -> str:
    def expand(left: int, right : int)-> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 :right]
    if len(s) < 2 or s == s[::-1]:
        return s
    result = ''
    for i in range(0, len(s)-1):
        result = max(result, expand(i, i+1), expand(i, i+2), key = len)
    return result

print(longestPalindrome(s))


d