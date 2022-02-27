from audioop import reverse
from gettext import npgettext
import re


s = 'a'


value = True

s = s.lower()
s = s.replace(' ','')
s = list(s)
s_del = []
# 새로운 리스트
list_s = []
# 텍스트를 가지고 있는 리스트

for i in s:
    # 영어,숫자 및 공백 제거.
    s_text = re.sub('[^a-zA-Z0-9]',' ',i)
    # 빈 리스트는 제거.
    if(s_text != ''):
        list_s.append(s_text)

#거꾸로 리스트
list_par_reverse = list(reversed(list_s))

if len(list_s) == 0:
    print(value)
else:
    if list_s == list_par_reverse:
        value = True
        print(value)
    else:
        value = False
        print(value)
        

