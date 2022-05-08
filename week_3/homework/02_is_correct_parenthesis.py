# import stack
s = "(())()"


def is_correct_parenthesis(string):
    temp_list = []
    sums = 0
    for char in string:
        if char == '(':
            temp_list.append('+')
        elif char == ')' and len(temp_list) == 0: # )으로 시작
            return False
        elif char == ')' and len(temp_list) != 0:
            temp_list.pop()
    return len(temp_list) == 0


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!

print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("(()))("))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")()("))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("(()("))
print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(((())(())))"))

