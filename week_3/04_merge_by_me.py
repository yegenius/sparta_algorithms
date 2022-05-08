array_a = [1, 2, 3, 6, 9, 12, 14]
array_b = [4, 5, 7, 8, 10, 11, 13]


def merge(array1, array2):
    merged=[]
    pointer_1 = 0
    pointer_2 = 0
    for element in array1:
        for element_2 in array2:
            while element not in merged and element_2 not in merged :
                if array1[pointer_1]<array2[pointer_2]:
                    merged.append(array1[pointer_1])
                    if pointer_1<len(array1):
                        pointer_1+=1
                else:
                    merged.append(array2[pointer_2])
                    if pointer_2<len(array2):
                        pointer_2+=1
    if pointer_1==len(array1):
        merged=merged+array2[pointer_2:]
    elif pointer_2==len(array2):
        merged=merged+array1[pointer_1:]
    return merged


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!
print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge([-7, -1, 9, 40], [5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge([-1,2,3,5,40], [10,78,100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge([-1,-1,0], [1, 6, 9, 10]))