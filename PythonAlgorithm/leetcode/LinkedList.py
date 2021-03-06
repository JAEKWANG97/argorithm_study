from unicodedata import name


class SLinkedList:
    #S_L_list에서 쓸 노드
    class Node:
        def __init__(self, v, n=None):
            self.value= v #저장된 데이터 
            self.next = n #다음 노드를 가르키는 변수

    def __init__(self):
        self.head = None #첫 생성시 내부에는  노드가 없으므로 


    def inserNode(self,v):
        # 만일 첫 노드일 경우 -> head값이 None임
        if self.head is None:
            # head에 새 노드를 저장
            self.head = self.Node(v)
        else: #이미 노드가 있는 경우
            # head에 새 노드를 저장
            # 기존 head에 저장된 노드는 새로 생성할 노드의 next로 저장
            self.head = self.Node(v, self.head)
    
    # 출력
    def printNode(self):
        # 데이터가 없을 때
        if self.head is None:
            print(None)
            return
        else:
            print("<현재 리스트 구조>", end='\t')
            # end로 print 마지막 개행을 변경할 수 있음
            link = self.head
            # 처음은 head를 지정. 이후부터는 현 노드의 next를 지정
            # link가 가리키는 노드가 없을 때까지 반복
            # None,0,""는 조건판단에서 False 처리, 그 외는 True로 처리됨
            while link:
                print(link.value, '->',end = ' ')
                link = link.next
            
            print()

        #삭제
    def deleteNode(self):
        #노드가 없으면 skip
        if self.head is None :
            print("삭제할 노드가 없습니다.")
            return
        else:
            #head를 현 head의 next. 즉, 다음 노드로 변경.
            self.head = self.head.next
        #조회
    def searchNode(self,v):
        # 데이터가 없을 때
        if self.head is None:
            print("저장된 데이터가 없음")
            return
        else:
            link = self.head  # 처음은 head를 지정. 이후부터는 현 노드의 next를 지정
            index  = 0 #몇 번째 노드인지 기록
            while link:
                #내가 찾는 노드인지 확인
                if v == link.value:
                    return index #위치를 반환
                else:
                    link = link.next  # link를 현 위치 노드의 next로 변경
                    index += 1 #위치값 1 증가
            #여기까지 왔다 == 해당 v값을 가진 노드가 없다.
            #print("일치되는 값이 없습니다.")
        
if __name__ == "__main__":
    sl = SLinkedList()
    sl.inserNode(1)
    sl.inserNode(2)
    sl.inserNode(3)
    sl.inserNode(4)
    sl.inserNode(5)
    sl.printNode()
    print(sl.searchNode(3))