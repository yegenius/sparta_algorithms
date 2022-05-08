input = "abcabcabcabcdededededede"


def string_compression(string):
    n = len(string)
    compressed_len_array=[]
    for split_size in range(1, n // 2 + 1):
        splited = [
            string[i:i + split_size] for i in range(0, n, split_size)
        ]
        # print(splited)
        count =1
        compressed=""
        for ii in range(1,len(splited)):
            prev,cur=splited[ii-1],splited[ii]
            if prev==cur:
                count+=1
            elif count==1:
                compressed+=prev
            else:
                compressed+=(str(count)+prev)
                count = 1

        if count>1:
            compressed+=(str(count)+splited[-1])
        else:
            compressed+=splited[-1]

        compressed_len_array.append(len(compressed))
        #print(compressed)

    return min(compressed_len_array)



print(string_compression(input))  # 14 가 출력되어야 합니다!
print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA"))
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA"))
print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))