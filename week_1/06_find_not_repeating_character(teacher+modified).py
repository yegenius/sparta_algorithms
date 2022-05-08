#input = "aaaaaaaa"
input="abadabac"#"aabbcddd"

def find_not_repeating_character(string):
    # 이 부분을 채워보세요!
    alpha=[0]*26
    for char in string:
        if not char.isalpha():
            continue
        alpha[ord(char)-ord('a')]+=1

    not_repeating_char_array=[]
    for char in string:
        if alpha[ord(char)-ord('a')]==1:
            not_repeating_char_array.append(char)
            #return char
    if not not_repeating_char_array:
        return "_"
    else:
        return not_repeating_char_array[0]#[len(not_repeating_char_array) - 1]


result = find_not_repeating_character(input)
print(result)
#이렇게 하면 not repeating char 중 마지막 index의 문자도 찾을 수 있다
