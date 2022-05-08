import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    answer = 0
    last_added_date_index = 0
    max_heap = []
    while stock <= k: #받아 놓은게 k에 도달하면 마친다  (5)
        while last_added_date_index<len(dates) and dates[last_added_date_index]<=stock: #바닥나기 전에    (1)      받아놓은 걸로 다시 얼마나 버틸 수 있는지 보고 (4)
            heapq.heappush(max_heap,-supplies[last_added_date_index]) #최대로 받아놓을 수 있을 만큼 받아놓고  (2)
            last_added_date_index+=1                                         #
        maximum=-heapq.heappop(max_heap)                              #받아놓은것들 중 현재의 최대값만 stock에 저장  (3)
        stock+=maximum
        answer+=1
    return answer


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
print("정답 = 2 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
print("정답 = 4 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
print("정답 = 1 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))
print("정답= 3/ 현재 풀이값=", get_minimum_count_of_overseas_supply(4,[4, 10, 24, 30, 40],[20, 14, 17, 10, 10],50))
