# 1. 로그의 가장 앞 부분은 식별자다.
# 2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
# 3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
# 4. 숫자 로그는 입력 순서대로 한다.
from unicodedata import digit
logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
# 출력 ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]

digits = []
letters = []

for log in logs:
    if log.split()[1].isdigit():
        digits.append(log)
    else:
        letters.append(log)

print(digits)
print(letters)

letters.sort(key = lambda x : (x.split()[1:], x.split()[0]))
print(letters  + digits)