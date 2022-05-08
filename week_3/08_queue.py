class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        # 어떻게 하면 될까요?
        new_Node = Node(value)
        if self.is_empty():
            self.tail=new_Node
            self.head=new_Node
            return
        self.tail.next=new_Node
        self.tail=new_Node


#[4] ->[2]-> [3]


  #  None
    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
            return
        temp=self.head
        self.head=temp.next
        # 어떻게 하면 될까요?
        return temp.data

    def peek(self):
        if self.is_empty():
            print("Queue is Empty")
            return
        return self.head.data
        # 어떻게 하면 될까요?

    def is_empty(self):
        return self.head==None
        # 어떻게 하면 될까요?
queue=Queue()
queue.enqueue(3)
print(queue.peek())
queue.enqueue(4)
print(queue.peek())
queue.enqueue(5)
print(queue.peek())
print(queue.dequeue())
print(queue.peek())
print(queue.is_empty())
print(queue.dequeue())
print(queue.dequeue())

print(queue.dequeue())
print(queue.is_empty())