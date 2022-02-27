a , b = map(int,input().split())
if b < 45 :
    b = (60+b) - 45
    a = a-1
    if a < 0 :
        a = 23
    print (a,b)
elif b>= 45 :
    b = b-45
    print (a,b)