finding_target = 39
finding_numbers = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    current_max=len(array)-1
    current_min=0
    current_try= (current_min+current_max)//2
    while current_min<=current_max:
        if array[current_try]<target:
            current_min= current_try+1
        elif array[current_try]==target:
            return True
        else:
            current_max= current_try-1
        current_try = (current_min + current_max) // 2
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)