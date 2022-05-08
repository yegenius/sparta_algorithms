class Node:
    def __init__(self, data):
        self.data = data
        self.next = self

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next != self.head:
            cur = cur.next
        cur.next = Node(value)
        cur.next.next=self.head

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def delete_node(self,index):
        if index==0:
            self.head=self.head.next
            return
        node=self.get_node(index-1)
        next_node=node.next.next
        node.next=next_node
        self.head=next_node

def size(linked_list):
    j=0
    while linked_list.get_node(j).next.data !=linked_list.head.data:
        j+=1
    siz=j+1
    return siz

def josephus_problem(n, k):
   # 이 부분을 채워보세요!
    linked_list=LinkedList(1)
    for i in range (1,n):
        linked_list.append(i+1)
    #j=0
    _list=[]
    while size(linked_list)>1:
        _list.append(linked_list.get_node(k-1).data)
        linked_list.delete_node(k-1)
    _list.append(linked_list.get_node(0).data)

    for l in range(n):
        _list[l]= str(_list[l])

    print("<",",".join(_list),">")

n, k = map(int, input().split())
josephus_problem(n, k)