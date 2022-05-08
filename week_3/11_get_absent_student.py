all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["나연",  "지효", "미나", "다현", "채영", "쯔위"]


def get_absent_student(all_array, present_array):
    # 구현해보세요!
    absent=[]
    #set_array=set(all_array)
    for student in all_array:
        if student not in present_array:
            absent.append(student)
    if absent ==[]:
        return "all present"
    return absent
    #return "all present"


print(get_absent_student(all_students, present_students))