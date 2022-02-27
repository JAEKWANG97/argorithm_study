#주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
import collections
from typing import Deque
def isPalindrome(s:str) -> bool:
    str:Deque = collections.deque()
    for char in s:
        if char.isalnum():
            str.append(char.lower())
    while len(str)>1:
        if str.popleft()!=str.pop():
            return False
    return True
if __name__=="__main__":
    s='A man, A plan, A canal : Panama'
    print(isPalindrome(s))

#주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
 
import re

class Solution:
    def isPalindrome(self, s:str)->bool:
        print(type(s))
        s = s.lower()
        print(s)
        s = re.sub('[^a-z0-9]', '', str(s))
        return s == s[::-1]


s ='A man, A plan, A canal : Panama'
sol = Solution()

print(sol.isPalindrome(s))