import math
input = 50


def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!
    non_prime=[]
    prime=[]
    for i in range(2,number+1):
        for j in range(2,int(math.sqrt(i))+1):
            if i%j==0:
                non_prime.append(i)
    for k in range(2,number+1):
        if k not in non_prime:
            prime.append(k)


    return prime


result = find_prime_list_under_number(input)
print(result)