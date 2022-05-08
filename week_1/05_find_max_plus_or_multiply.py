#result([0, 3, 5, 6, 1, 2, 4]) [3, 5, 6, 1, 2, 4]

def find_max_plus_or_multiply(array):
    # 이 부분을 채워보세요!
    temp_result = 0
    # temp_result_1=1
    for num in array:
        if num <=1 or temp_result<=1:

            temp_result += num
        else:
            temp_result *= num

    return temp_result


result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0, 3, 5, 6, 1, 2, 4]))
print("정답 = 8820 현재 풀이 값 =", result([3, 2, 1, 5, 9, 7, 4]))
print("정답 = 270 현재 풀이 값 =", result([1, 1, 1, 3, 3, 2, 5]))
print("정답 = 3 현재 풀이 값 =", result([0,0,0, 0, 0, 0, 0,1,2]))
