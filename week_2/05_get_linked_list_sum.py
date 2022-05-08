class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_size(self):
        count = 0
        cur = self.head

        while cur is not None:
            cur = cur.next
            count += 1
        return count


def get_linked_list_sum(linked_list_1, linked_list_2):
    size_1=linked_list_1.get_size()
    size_2=linked_list_2.get_size()
    num_1=0
    num_2=0
    for i in range(0,size_1):
        num_1+=(linked_list_1.get_node(i).data)*(pow(10,size_1-i-1))
        #
    for j in range(0,size_2):
        num_2+=(linked_list_2.get_node(j).data)*(pow(10,size_2-j-1))
    #print(num_1)
    return num_1+num_2


    # 구현해보세요!
#        return 1


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)
linked_list_1.append(9)
print(linked_list_1.get_size())

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))
