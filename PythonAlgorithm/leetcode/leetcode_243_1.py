# 연결 리스트가 팰린드롬 구조인지 판별하는 문제이다.

# 입력 : 1-> 2 출력 : fasle
# 입력 : 1->2->2->1 출력 : True






from ast import List


def isPalindrome(head : ListNode) -> bool:
    q: List = []
    
    # 연결리스트가 비어 있다면
    if not head:
        return True

    
    node = head

    # 리스트 변환   

    while node is not None:
        q.append(node.val)
        node = node.next


    # 팰린드롬 판별

    while len(q) > 1 :
        if q.pop(0) != q.pop():
            return False
    

    return True