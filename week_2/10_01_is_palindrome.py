input = "tomato"


def is_palindrome(string):
    n= len(string)
    for i in range( len(string)):
        if string[i]==string[n-1-i]:
            continue
        else:
            return False
    return True


print(is_palindrome(input))