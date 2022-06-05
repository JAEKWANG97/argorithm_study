

# 자신의 신체 정보를 입력해주세요.
# height = int(input('키를 입력하시오 : '))
# weight = int(input('몸무게를 입력하시오 : '))
# age = int(input('나이를 입력하시오: '))

height = int(170)
weight = int(80)
age = int(26)

# 기초 대사량(헤리슨 베네딕트 방정식)
value = 66+(13.7*weight)+(5*height) - 6.8*age
print("기초대사량", round(value))
# 유지
Need_value = round(value * 1.55)
print("유지 칼로리 ", Need_value)
#증량을 위한 칼로리 
purpose_value = Need_value*1.2

carbon_cal = round(purpose_value*0.5)

protein_cal = round (purpose_value*0.3)

fat_cal = round(purpose_value*0.2)

carbon_gram = carbon_cal/4

protein_gram = protein_cal/4

fat_gram = round(fat_cal/9)

diet_gram = {'탄수화물 그람' : carbon_gram, '단백질 그람' : protein_gram, '지방 그람' : fat_gram}

onece_meal = {'탄수화물 그람' : carbon_cal/5, '단백질 그람' : protein_cal/5, '지방 그람' : fat_cal/5}


print('하루 총 열량 : ', diet_gram)
print('식사 한끼 열량(5끼) : ' , onece_meal)




