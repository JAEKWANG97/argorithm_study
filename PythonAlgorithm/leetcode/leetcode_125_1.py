# s = 'A man, a plan, a canal : Panama'

class Solution:

    def isPalindrome(self, s: str) -> bool:
        value = True

        s = s.lower()
        s = s.replace(' ','')
        s = list(s)

        s_del = []


        if len(s) == 0:
            print(value)
            return value
        else:
            for i in range(0 ,len(s) - 1):
                if ord(s[i]) > 122 or ord(s[i]) < 97:
                    s_del.append(s[i])

            i = 0
            while True:
                if i > len(s_del) - 1:
                    break
                s.remove(s_del[i])
                i += 1
                
                
            for i in range(0 ,len(s)-1):
                if s[i] != s[len(s)-1 - i]:
                    value = False
                else:
                    value = True

            return value


def main():
    s = 'A man, a plan, a canal : Panama'
    sol  = Solution()
    print(s)
    print(sol.isPalindrome(s))

if __name__ == "__main__":
    main()
