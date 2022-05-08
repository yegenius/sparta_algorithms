# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}
#1. start 노드가

def dfs_stack(adjacent_graph, start_node):
    visited=[]
    stack=[]
    stack.append(start_node)
    while stack:
        cur=stack.pop()
        visited.append(cur)
        for adjacent_node in adjacent_graph[cur]:
            if adjacent_node not in visited:
                stack.append(adjacent_node)
    return visited



    # 구현해보세요!



print(dfs_stack(graph, 1))  # 1 이 시작노드입니다!
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!