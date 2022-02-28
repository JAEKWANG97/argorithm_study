a,b = input().split()

a,b = list(a) , list(b)
a.reverse()
b.reverse()
print(max("".join(a) , "".join(b)))



