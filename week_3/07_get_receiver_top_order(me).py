top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    orders_rev=[]
    for j in range(len(heights)-1,0,-1):
        top=heights[j]
        i=j-1
        while top>=heights[i] and i>=0:
            i-=1
        if i==-1:
            orders_rev.append(0)
        else:
            orders_rev.append(i+1)
               # break
        #orders_rev.append(0)
    orders_rev.append(0)
    orders_rev.reverse()

    return orders_rev


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ",get_receiver_top_orders([6,9,5,7,4]))
print("정답 = [0, 0, 0, 3, 3, 3, 6] / 현재 풀이 값 = ",get_receiver_top_orders([3,9,9,3,5,7,2]))
print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ",get_receiver_top_orders([1,5,3,6,7,6,5]))