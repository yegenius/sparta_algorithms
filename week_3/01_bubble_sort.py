input =  [9,6,4,2,1] #[4, 6, 2, 9, 1]


def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]

    # 이 부분을 채워보세요!
    return


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!