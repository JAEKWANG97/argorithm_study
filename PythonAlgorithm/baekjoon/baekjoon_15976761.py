#str = input()
#list_str = []
#str = str.upper()
#for i in range(0, len(str)):
#    list_str.append(str[i:i+1])
#
#list_str.sort()
#top_char_num = 0
#compare_char_num = 0
#value = 0
#
#list_str.sort()
#
#topchar = ''
#cmpchar = ''
#
#while True:
#
#    if len(list_str) == 0:
#        break
#    compare_char_num = 0
#    temp = list_str.pop()
#    compare_char_num += 1
#    temp2 = list_str.count(temp)+1
#
#    for i in range(0, temp2-1):
#        list_str.pop()
#        compare_char_num += 1
#    if compare_char_num > top_char_num:
#        top_char_num = compare_char_num
#        topchar = temp
#        continue
#    elif compare_char_num < top_char_num:
#        continue
#    else:
#        value = top_char_num
#        continue
#    
#if value == top_char_num:
#    print("?")
#else:
#    print(topchar)




import collections


str = input()

str = str.upper()

list_str = []

for i in range(0, len(str)):
    list_str.append(str[i:i+1])

str_dict = collections.Counter(list_str)

if len(list_str) > 1:
    if str_dict.most_common(2)[0][1] == str_dict.most_common(2)[1][1]:
        print("?")
    else:
        print(str_dict.most_common(2)[0][0])
else:
        print(str_dict.most_common(1)[0][0])
        
