seat_count = 9
vip_seat_array = [4, 7]


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    arrangeable_seats=[]
    num_of_ways=1
    for i in range(len(fixed_seat_array)):
        if i==0:
            arrangeable_seats.append(fixed_seat_array[i]-1)
        elif 0<i<len(fixed_seat_array):
            arrangeable_seats.append(fixed_seat_array[i]-fixed_seat_array[i-1]-1)
    arrangeable_seats.append(total_count-fixed_seat_array[len(fixed_seat_array)-1])
    arrangeable_seats.sort()
    dp=[0]*(arrangeable_seats[len(arrangeable_seats)-1]+1)
    dp[0]=1
    dp[1]=1
    for i in range(2, arrangeable_seats[len(arrangeable_seats)-1]+1):
        dp[i] = dp[i - 1] + dp[i - 2]
    for seat in arrangeable_seats:
        num_of_ways*=dp[seat]
    return num_of_ways


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))

print("정답 = 4 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9,[2,4,7]))
print("정답 = 26 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(11,[2,5]))
print("정답 = 6 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(10,[2,6,9]))