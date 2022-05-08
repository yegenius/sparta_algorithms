class MaxHeap:
    def __init__(self):
        self.items = [None]

'''     1.새 노드를 맨 끝에 추가한다
        2.지금 넣은 새 노드를 부모노드와 비교하여 크면 교체한다
        3.이 과정을 꼭대기까지 반복한다
'''
    def insert(self, value):
        self.items.append(value)
        cur_index=len(self.items)-1
        while cur_index>1:
            parent_node=cur_index//2
            if items[parent_node]<items[cur_index]:
                items[parent_node],items[cur_index]=items[cur_index],items[parent_node]
                cur_index=parent_node
            else:
                break
        # 구현해보세요!
        return


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!