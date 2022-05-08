input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    big_ = array[0]
    for i in array:
        if big_ < i:
            big_ = i
    return big_




result = find_max_num(input)
print(result)