from msvcrt import putch
from this import d
from turtle import onscreenclick

# 자신의 신체 정보를 입력해주세요.
# height = int(input('키를 입력하시오 : '))
# weight = int(input('몸무게를 입력하시오 : '))
# age = int(input('나이를 입력하시오: '))

height = int(172)
weight = int(82)
age = int(26)

# 기초 대사량(헤리슨 베네딕트 방정식)
value = 66+(13.7*weight)+(5*height) - 6.8*age
# 유지
Need_value = value * 1.55

purpose_value = Need_value*0.8

carbon_cal = round(purpose_value*0.5/4)

protein_cal = round(purpose_value*0.3/4)

fat_cal = round(purpose_value*0.2/9)

diet_cal = {'탄수화물 그람' : carbon_cal, '단백질 그람' : protein_cal, '지방 그람' : fat_cal}

onece_meal = {'탄수화물 그람' : carbon_cal/4, '단백질 그람' : protein_cal/4, '지방 그람' : fat_cal/4}
print('하루 총 열량 : ', diet_cal)
print('식사 한끼 열량 : ' , onece_meal)



