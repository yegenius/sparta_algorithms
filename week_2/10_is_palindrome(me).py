input = "abcbaabcbaabcba"


def is_palindrome(string):
    print(string)
    start=0
    end=len(string)-1
    if string[start]==string[end] and len(string)>=3:
        string=string[start + 1:end]
        return is_palindrome(string)
    elif string[start]==string[end] and len(string)==2:
        return True
    elif string[start]==string[end] and len(string)==1:
        return True
    else:
        return False
    return True


# elif  and start<end:

        #return False















#    n = len(string) - 1
#    if n==-1:
#        return True
#    #print(n)
#    if string[0]==string[n]:
#        string=string[1:n]
#        print(string)
#        is_palindrome(string)
#    elif string[0]!=string[n] :
#        return False


#    elif string[0]!=string[n]:
 #       return False


print(is_palindrome(input))