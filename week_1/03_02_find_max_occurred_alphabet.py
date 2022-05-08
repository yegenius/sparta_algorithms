input = "best of best sparta"

def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!
    alphas_occurrence = [0] * 26
    for a in string:
        if a.isalpha():
            alphas_occurrence[ord(a) - ord('a')] += 1
    max_occurrence = alphas_occurrence[0]
    max_index = 0
    for i in range(len(alphas_occurrence)):
        if max_occurrence < alphas_occurrence[i]:
            max_occurrence = alphas_occurrence[i]
            max_index = i
    return chr(max_index + ord('a'))
    # for i in alphas:
    #   if max_num < i:
    #      max_num = i
    # return chr(alphas.index(max_num)+ord('a'))


result = find_max_occurred_alphabet(input)
print(result)
