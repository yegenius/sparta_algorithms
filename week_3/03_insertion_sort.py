input =[100,56,-3,32,44]#[4, 6, 2, 9, 1]


def insertion_sort(array):
    for i in range(len(array)-1):
        cur_index = i + 1
        for j in reversed(range(0,i+1)):
            #print(i,j)
            if array[cur_index]<array[j]:
                array[cur_index],array[j]=array[j],array[cur_index]
                cur_index=j
            else:
                break
    return array


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!
print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",insertion_sort([5,8,4,7,7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",insertion_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",insertion_sort([100,56,-3,32,44]))