input = "0101" #
# 0001100 #1110011 #101101 #0111011010


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 이 부분을 채워보세요!
    #bundle=[]
    plus=0
    minus=0
    for i in range(len(string)-1) :
        if string[i]=='0' and string[i+1]=='1':
            #bundle.append('+')
            plus+=1
        elif string[i]=='1' and string[i+1]=='0':
            #bundle.append('-')
            minus+=1
        else :
            continue
    return max([plus,minus])


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)