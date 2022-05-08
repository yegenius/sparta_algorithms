class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, value):
        if index-1<0:
            temp_node=self.head
            self.head=Node(value)
            self.head.next=temp_node
        else:
            node= self.get_node(index-1)
            temp=node.next
            node.next=Node(value)
            node.next.next=temp
    def delete_node(self,index):
        if index==0:
            self.head=self.head.next
            return
        node=self.get_node(index-1)
        next_node=node.next.next
        node.next=next_node



linked_list = LinkedList(5)
linked_list.append(12)
linked_list.add_node(1, 3)
linked_list.print_all()
linked_list.delete_node(0)
linked_list.print_all()