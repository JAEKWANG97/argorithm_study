from msvcrt import putch
from this import d
from turtle import onscreenclick


height = int(input('키를 입력하시오'))
weight = int(input('몸무게를 입력하시오'))


value = 66+(13.7*weight)+(5*height) - 6.8*26

Need_value = value * 1.55

print(Need_value)

purpose_value = Need_value*0.8

print(purpose_value)

carbon_cal = round(purpose_value*0.5/4)

protein_cal = round(purpose_value*0.3/4)

fat_cal = round(purpose_value*0.2/9)

diet_cal = {'탄수화물 그람' : carbon_cal, '단백질 그람' : protein_cal, '지방 그람' : fat_cal}

onece_meal = {'탄수화물 그람' : carbon_cal/4, '단백질 그람' : protein_cal/4, '지방 그람' : fat_cal/4}
print(diet_cal)
print(onece_meal)

