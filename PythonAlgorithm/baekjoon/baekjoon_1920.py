import sys


N = int(sys.stdin.readline())
a = sys.stdin.readline().split()


M = int(sys.stdin.readline())
b = sys.stdin.readline().split()



for i in range(0,len(b)):
    if b[i] in a:
        print(1)
    else:
        print(0)