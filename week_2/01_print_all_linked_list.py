class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)  # head 에 시작하는 Node 를 연결합니다.

    def append(self, value):     # LinkedList 가장 끝에 있는 노드에 새로운 노드를 연결합니다.
        cur = self.head
        while cur.next is not None: # cur의 다음이 끝에 갈 때까지 이동합니다.
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur=self.head
        while cur is not None:
            print(cur.data)
            cur=cur.next



linked_list = LinkedList(5)
linked_list.append(12)
# 이렇게 되면 5 -> 12 형태로 노드를 연결한 겁니다!
linked_list.append(8)
linked_list.print_all()
#print(linked_list.head.next.next.data)