import math
import queue


def solution(progresses, speeds):
    stack=[]
    stack_list=[]
    for i in range(len(progresses)):
       print(progresses[i])
       stack.append(math.ceil((100-progresses[i])/speeds[i]))

    temp=stack[0]
    i=0
    count=0
    while True:
        acc=0
        if i>len(stack)-1:
            break
        temp = stack[i]
        while i<len(stack) and temp>=stack[i]:
            i+=1
            acc+=1
        stack_list.append(acc)
           # print(i)




    #temp=stack[-1]
    #temp_1=-1
#    q = queue.Queue()
#    temp=stack[0]
#    for j in range(len(stack)):
#        q.put(stack[j])
#    count=0
#    while not q.empty() and count<len(stack):
#        acc=0
#        while temp>=q.get() and count<len(stack):
#            acc+=1
#            count+=1
 #       stack_list.append(acc)
  #      temp = stack[count]
   #     for s in range(len(stack)-count):
    #        q.put(stack[count+s])
     #   count+=1
      #  print(count)
        #print(q.get())
       # print(temp)

    #q.put(stack[0])
    #q.put(stack[1])
    #q.put(stack[2])
    #print(q.get())
    #print(q.get())
    #print(q.get())
    #print(q.empty())


    #print(stack)
    #answer = stack_list
    return stack_list

print(solution([93,30,55],[1,30,5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
#    stack_list=[]
#    temp=stack[0]
#    j=0
#    i=0
#    while j<len(stack)-1 and i< len(stack) :
 #       acc=0

  #      while j<len(stack)-1 and temp>=stack[j] :
   #         acc+=1
    #        j+=1
     #       i+=1
      #      print(j)
       # temp=stack[j]
       # stack_list.append(acc)
   # acc=0
    #print(temp)

#    while stack:
 #       acc=0
  #      while temp>=temp_1 and temp_1 is not None and temp is not None:
   #         temp_1=stack.pop()
    #        acc+=1
     #       if len(stack)==1:
      #          temp=stack[0]
       #     else: #len(stack)>1:

        #        temp=stack[-1]


       # stack_list.append(acc)


#    while stack:
 #       acc=0
  #      if len(stack)>=2:
   #         while temp>=stack[-1] and len(stack)>1:  #temp_1:
    #            stack.pop()
     #           acc+=1
      #      temp = stack[-1]
       #     stack_list.append(acc)
        #elif len(stack)==1:
         #   stack_list.append(1)
          #  break
 #           break

import math
def solution(brown, yellow):
    multip=brown+yellow
    for i in range(int(math.sqrt(multip))):
        if multip%(i+1)==0 and yellow==(multip/(i+1)-2)*(i-1): #i+1-2
            return [multip/(i+1),i+1]
