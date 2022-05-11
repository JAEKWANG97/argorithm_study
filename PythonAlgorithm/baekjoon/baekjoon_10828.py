# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 다섯 가지이다.

# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.


import collections
import re
import sys


class Stack:
    def push(self, stackList : list, x ):
        stackList.append(int(x))
        return stackList


    def pop(self, stackList : list):
        if len(stackList) == 0:
            print('-1')
            return stackList
        else:
            print(stackList[-1])
            del stackList[-1]
            return stackList


    def size(self, stackList : list):
        print(len(stackList))
        return stackList


    def empty(self, stackList : list):
        if len(stackList) == 0:
            print('1')
        else:
            print('0')
        return stackList


    def top(self, stackList : list):
        if len(stackList) == 0 :
            print('-1')
        else:
            print(stackList[-1])
        return stackList


main = Stack()
N = int(sys.stdin.readline())
stackList = []


for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        main.push(stackList, command[1])
    if command[0] == 'pop':
        main.pop(stackList)
    if command[0] == 'size':
        main.size(stackList)
    if command[0] == 'empty':
        main.empty(stackList)
    if command[0] == 'top':
        main.top(stackList)