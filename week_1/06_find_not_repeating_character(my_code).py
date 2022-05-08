input = "aabbcdddxjdofueofpp"

def find_not_repeating_character(string):
    # 이 부분을 채워보세요!
    alpha=[0]*26
    for char in string:
        if not char.isalpha():
            continue
        alpha[ord(char)-ord('a')]+=1

    for char in string:
        if alpha[ord(char)-ord('a')]==1:
            return char
    return "_"


result = find_not_repeating_character(input)
print(result)