class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail= None


    def append(self, value):
        cur = self.head
        while cur.next is not None :
            temp = cur
            cur = cur.next
            cur.prev = temp

        cur.next = Node(value)
        cur.next.prev = cur
        self.tail=cur.next



    def get_kth_node_from_last(self, k):
        current=self.tail
        count=1
        while count<k:
            current=current.prev
            count+=1
        return current


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
#linked_list.append(10)
#linked_list.append(15)
#print(linked_list.tail.data)
print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!