# 연결 리스트가 팰린드롬 구조인지 판별하는 문제이다.

# 입력 : 1-> 2 출력 : fasle
# 입력 : 1->2->2->1 출력 : True







from tkinter.tix import ListNoteBook


nums = ListNoteBook()

nums.addAthead(1)
nums.addAtTail(2)
nums.addAtTail(2)
nums.addAtTail(1)

print(nums)