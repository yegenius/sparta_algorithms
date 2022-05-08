current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

''' 1. 현재 위치를 청소한다.
    2. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
        a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
        b. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
        c. 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
        d. 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
이 때 d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽을 바라보고 있는 것이다.
'''
#def switch(key):
#  telecom = {"011" : "SKT", "016": "KT", "019" : "LGU"}.get(key, "알 수 없는")
#  print(f'당신은 {telecom} 사용자입니다.')

#firstNumber = input().split("-")[0]
#switch(firstNumber)
'''
def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    cur_pos_row=r-1
    cur_pos_col=c-1
    cur_d=d
    ans=0
    prev_pos_row=r-1
    prev_pos_col=c-1
    prev_d=d
    while room_map[prev_pos_row][prev_pos_col]!=1:
        if room_map[cur_pos_row][cur_pos_col] == 0:
            room_map[cur_pos_row][cur_pos_col] = -1  # -1 means 'cleaned'
            ans += 1
            print(cur_pos_row, cur_pos_col, prev_pos_row, prev_pos_col, cur_d, prev_d)
    #(0<=cur_pos_col < len(room_map[1]) and len(room_map) > cur_pos_row >= 0) and room_map[cur_pos_row + 1][cur_pos_col]==0 or room_map[cur_pos_row][cur_pos_col + 1]==0 or room_map[cur_pos_row - 1][cur_pos_col]==0 or room_map[cur_pos_row][cur_pos_col - 1]==0 or room_map[prev_pos_row][prev_pos_col]!=1:
            while 0<=cur_pos_col-1 < len(room_map[1])-1 and len(room_map)-1 > cur_pos_row-1 >= 0 and 0<=cur_pos_col+1 < len(room_map[1])-1 and len(room_map)-1 > cur_pos_row+1 >= 0 and room_map[cur_pos_row + 1][cur_pos_col]==0 or room_map[cur_pos_row][cur_pos_col + 1]==0 or room_map[cur_pos_row - 1][cur_pos_col]==0 or room_map[cur_pos_row][cur_pos_col - 1]==0:

                if cur_d==0:
                    prev_d = 0
                    if room_map[cur_pos_row][cur_pos_col-1]==0  : #move to West
                        prev_pos_row = cur_pos_row
                        prev_pos_col = cur_pos_col
                        prev_d=cur_d
                        cur_pos_col-=1
                        cur_d=3
                        break
                    elif room_map[cur_pos_row+1][cur_pos_col]==0 : #move to South
                        prev_pos_row = cur_pos_row
                        prev_pos_col = cur_pos_col
                        prev_d = cur_d
                        cur_pos_row+=1
                        cur_d=2
                        break
                    elif room_map[cur_pos_row][cur_pos_col+1]==0: #move to East
                        prev_pos_row = cur_pos_row
                        prev_pos_col = cur_pos_col
                        prev_d = cur_d
                        cur_pos_col+=1
                        cur_d=1
                        break
                    elif room_map[cur_pos_row-1][cur_pos_col]==0: #move to North
                        prev_pos_row = cur_pos_row
                        prev_pos_col = cur_pos_col
                        prev_d = cur_d
                        cur_pos_row -= 1
                        cur_d=0
                        break
                    else :
                        cur_pos_row=prev_pos_row
                        cur_pos_col=prev_pos_col
                        cur_d=prev_d
                        continue
                elif cur_d==3:
                    prev_d=3
                    if room_map[cur_pos_row + 1][cur_pos_col] == 0:  # move to South
                        prev_pos_row = cur_pos_row
                        prev_pos_col = cur_pos_col
                        prev_d = cur_d
                        cur_pos_row += 1
                        cur_d = 2
                        break
                    elif room_map[cur_pos_row][cur_pos_col + 1] == 0:  # move to East
                        prev_pos_row = cur_pos_row
                        prev_pos_col = cur_pos_col
                        prev_d = cur_d
                        cur_pos_col += 1
                        cur_d = 1
                        break
                    elif room_map[cur_pos_row - 1][cur_pos_col] == 0:  # move to North
                        prev_pos_row = cur_pos_row
                        prev_pos_col = cur_pos_col
                        prev_d = cur_d
                        cur_pos_row -= 1
                        cur_d = 0
                        break
                    elif room_map[cur_pos_row][cur_pos_col-1]==0  : #move to West
                        prev_pos_row = cur_pos_row
                        prev_pos_col = cur_pos_col
                        prev_d = cur_d
                        cur_pos_col-=1
                        cur_d=3
                        break
                    else:
                        cur_pos_row = prev_pos_row
                        cur_pos_col = prev_pos_col
                        cur_d = prev_d
                        continue
                elif cur_d==2:
                    prev_d=2
                    if room_map[cur_pos_row][cur_pos_col + 1] == 0:  # move to East
                        prev_pos_row = cur_pos_row
                        prev_pos_col = cur_pos_col
                        prev_d = cur_d
                        cur_pos_col += 1
                        cur_d = 1
                        break
                    elif room_map[cur_pos_row - 1][cur_pos_col] == 0:  # move to North
                        prev_pos_row = cur_pos_row
                        prev_pos_col = cur_pos_col
                        prev_d = cur_d
                        cur_pos_row -= 1
                        cur_d = 0
                        break
                    elif room_map[cur_pos_row][cur_pos_col - 1] == 0:  # move to West
                        prev_pos_row = cur_pos_row
                        prev_pos_col = cur_pos_col
                        prev_d = cur_d
                        cur_pos_col -= 1
                        cur_d = 3
                        break
                    elif room_map[cur_pos_row + 1][cur_pos_col] == 0:  # move to South
                        prev_pos_row = cur_pos_row
                        prev_pos_col = cur_pos_col
                        prev_d = cur_d
                        cur_pos_row += 1
                        cur_d = 2
                        break
                    else:
                        cur_pos_row = prev_pos_row
                        cur_pos_col = prev_pos_col
                        cur_d = prev_d
                        continue
                elif cur_d==1:
                    prev_d=1
                    if room_map[cur_pos_row - 1][cur_pos_col] == 0:  # move to North
                        prev_pos_row = cur_pos_row
                        prev_pos_col = cur_pos_col
                        prev_d = cur_d
                        cur_pos_row -= 1
                        cur_d = 0
                        break
                    elif room_map[cur_pos_row][cur_pos_col - 1] == 0:  # move to West
                        prev_pos_row = cur_pos_row
                        prev_pos_col = cur_pos_col
                        prev_d = cur_d
                        cur_pos_col -= 1
                        cur_d = 3
                        break
                    elif room_map[cur_pos_row + 1][cur_pos_col] == 0:  # move to South
                        prev_pos_row = cur_pos_row
                        prev_pos_col = cur_pos_col
                        prev_d = cur_d
                        cur_pos_row += 1
                        cur_d = 2
                        break
                    elif room_map[cur_pos_row][cur_pos_col + 1] == 0:  # move to East
                        prev_pos_row = cur_pos_row
                        prev_pos_col = cur_pos_col
                        prev_d = cur_d
                        cur_pos_col += 1
                        cur_d = 1
                        break
                    else:
                        cur_pos_row = prev_pos_row
                        cur_pos_col = prev_pos_col
                        cur_d = prev_d
                        continue
        elif (room_map[prev_pos_row + 1][prev_pos_col]==0 or room_map[prev_pos_row][prev_pos_col + 1]==0 or room_map[prev_pos_row - 1][prev_pos_col]==0 or room_map[prev_pos_row][prev_pos_col - 1]==0):
            cur_pos_row = prev_pos_row
            cur_pos_col = prev_pos_col
            cur_d = prev_d
            print("dd")
            while 0<=cur_pos_col-1 < len(room_map[1])-1 and len(room_map)-1 > cur_pos_row-1 >= 0 and 0<=cur_pos_col+1 < len(room_map[1])-1 and len(room_map)-1 > cur_pos_row+1 >= 0 and room_map[cur_pos_row + 1][cur_pos_col]==0 or room_map[cur_pos_row][cur_pos_col + 1]==0 or room_map[cur_pos_row - 1][cur_pos_col]==0 or room_map[cur_pos_row][cur_pos_col - 1]==0:

                if cur_d==0:
                    prev_d = 0
                    if room_map[cur_pos_row][cur_pos_col-1]==0  : #move to West
                        prev_pos_row = cur_pos_row
                        prev_pos_col = cur_pos_col
                        prev_d=cur_d
                        cur_pos_col-=1
                        cur_d=3
                        break
                    elif room_map[cur_pos_row+1][cur_pos_col]==0 : #move to South
                        prev_pos_row = cur_pos_row
                        prev_pos_col = cur_pos_col
                        prev_d = cur_d
                        cur_pos_row+=1
                        cur_d=2
                        break
                    elif room_map[cur_pos_row][cur_pos_col+1]==0: #move to East
                        prev_pos_row = cur_pos_row
                        prev_pos_col = cur_pos_col
                        prev_d = cur_d
                        cur_pos_col+=1
                        cur_d=1
                        break
                    elif room_map[cur_pos_row-1][cur_pos_col]==0: #move to North
                        prev_pos_row = cur_pos_row
                        prev_pos_col = cur_pos_col
                        prev_d = cur_d
                        cur_pos_row -= 1
                        cur_d=0
                        break
                    else :
                        cur_pos_row=prev_pos_row
                        cur_pos_col=prev_pos_col
                        cur_d=prev_d
                        continue
                elif cur_d==3:
                    prev_d=3
                    if room_map[cur_pos_row + 1][cur_pos_col] == 0:  # move to South
                        prev_pos_row = cur_pos_row
                        prev_pos_col = cur_pos_col
                        prev_d = cur_d
                        cur_pos_row += 1
                        cur_d = 2
                        break
                    elif room_map[cur_pos_row][cur_pos_col + 1] == 0:  # move to East
                        prev_pos_row = cur_pos_row
                        prev_pos_col = cur_pos_col
                        prev_d = cur_d
                        cur_pos_col += 1
                        cur_d = 1
                        break
                    elif room_map[cur_pos_row - 1][cur_pos_col] == 0:  # move to North
                        prev_pos_row = cur_pos_row
                        prev_pos_col = cur_pos_col
                        prev_d = cur_d
                        cur_pos_row -= 1
                        cur_d = 0
                        break
                    elif room_map[cur_pos_row][cur_pos_col-1]==0  : #move to West
                        prev_pos_row = cur_pos_row
                        prev_pos_col = cur_pos_col
                        prev_d = cur_d
                        cur_pos_col-=1
                        cur_d=3
                        break
                    else:
                        cur_pos_row = prev_pos_row
                        cur_pos_col = prev_pos_col
                        cur_d = prev_d
                        continue
                elif cur_d==2:
                    prev_d=2
                    if room_map[cur_pos_row][cur_pos_col + 1] == 0:  # move to East
                        prev_pos_row = cur_pos_row
                        prev_pos_col = cur_pos_col
                        prev_d = cur_d
                        cur_pos_col += 1
                        cur_d = 1
                        break
                    elif room_map[cur_pos_row - 1][cur_pos_col] == 0:  # move to North
                        prev_pos_row = cur_pos_row
                        prev_pos_col = cur_pos_col
                        prev_d = cur_d
                        cur_pos_row -= 1
                        cur_d = 0
                        break
                    elif room_map[cur_pos_row][cur_pos_col - 1] == 0:  # move to West
                        prev_pos_row = cur_pos_row
                        prev_pos_col = cur_pos_col
                        prev_d = cur_d
                        cur_pos_col -= 1
                        cur_d = 3
                        break
                    elif room_map[cur_pos_row + 1][cur_pos_col] == 0:  # move to South
                        prev_pos_row = cur_pos_row
                        prev_pos_col = cur_pos_col
                        prev_d = cur_d
                        cur_pos_row += 1
                        cur_d = 2
                        break
                    else:
                        cur_pos_row = prev_pos_row
                        cur_pos_col = prev_pos_col
                        cur_d = prev_d
                        continue
                elif cur_d==1:
                    prev_d=1
                    if room_map[cur_pos_row - 1][cur_pos_col] == 0:  # move to North
                        prev_pos_row = cur_pos_row
                        prev_pos_col = cur_pos_col
                        prev_d = cur_d
                        cur_pos_row -= 1
                        cur_d = 0
                        break
                    elif room_map[cur_pos_row][cur_pos_col - 1] == 0:  # move to West
                        prev_pos_row = cur_pos_row
                        prev_pos_col = cur_pos_col
                        prev_d = cur_d
                        cur_pos_col -= 1
                        cur_d = 3
                        break
                    elif room_map[cur_pos_row + 1][cur_pos_col] == 0:  # move to South
                        prev_pos_row = cur_pos_row
                        prev_pos_col = cur_pos_col
                        prev_d = cur_d
                        cur_pos_row += 1
                        cur_d = 2
                        break
                    elif room_map[cur_pos_row][cur_pos_col + 1] == 0:  # move to East
                        prev_pos_row = cur_pos_row
                        prev_pos_col = cur_pos_col
                        prev_d = cur_d
                        cur_pos_col += 1
                        cur_d = 1
                        break
                    else:
                        cur_pos_row = prev_pos_row
                        cur_pos_col = prev_pos_col
                        cur_d = prev_d
                        continue
        else:
            break
    return ans
'''

''' 북쪽으로     전진: r -= 1
    동쪽으로     전진: c += 1
    남쪽으로     전진: r += 1
    서쪽으로 전진: c -= 1
'''
# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))
current_room_map2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print("정답 = 29 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(6,3,1,current_room_map2))
current_room_map3 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print("정답 = 33 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(7,4,1,current_room_map3))
current_room_map4 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print("정답 = 25 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(6,2,0,current_room_map4))