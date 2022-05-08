input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    # 이 부분을 채워보세요!
    for i in array:
        if number == i:
            return True
        else:
            continue
    return False


result = is_number_exist(6, input)
print(result)
