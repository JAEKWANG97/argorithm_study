from operator import le


s = "hello world"
s = list(s)
s.reverse()

print(s)

###################################

s = "hello world"
s= list(s)
left , right = 0 , len(s)-1

while left < right : 
    s[left] , s[right] = s[right] , s[left]
    left += 1
    right -= 1

print(s)

