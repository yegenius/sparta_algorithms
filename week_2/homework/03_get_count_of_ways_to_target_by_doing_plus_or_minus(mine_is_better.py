numbers = [2,3,1] #[2,4,4,5] [2,3,4] [2,3,4,5] [1,2,3,4,5]
target_number = 0


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    if len(array)==1 and (array[0]!=target and array[0]!=-target):
        return 0
    elif len(array)==1 and (array[0]==-target or array[0]==target) :
        return 1
    return get_count_of_ways_to_target_by_doing_plus_or_minus(array[1:],target-array[0])+get_count_of_ways_to_target_by_doing_plus_or_minus(array[1:],target+array[0])

    # 구현해보세요!



print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!
