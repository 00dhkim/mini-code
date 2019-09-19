import random as r
import sys

def big_sum(a, b):
    A = a; B = b

    a = list(a)
    b = list(b)

    for i in range(len(a)):
        a[i] = int(a[i])
        
    for i in range(len(b)):
        b[i] = int(b[i])

    sumli = list()
    c = s = 0
    while(a and b): #a, b둘다 값이 있을때
        s = a.pop() + b.pop() + c
        c = 0
        if(s >= 10):
            c = 1
            s %= 10
        sumli.append(s)
        s = 0

    # 이때 또다시 캐리가 발생할수이따 (반례: 9999+1)
    if(a):  #a에만 값이 있다면
        while(a):
            s = a.pop() + c
            c = 0
            if(s >= 10):
                c = 1
                s %= 10        
            sumli.append(s)
            s = 0
    elif(b):   #b에만 값이 있다면
        while(b):
            s = b.pop() + c
            c = 0
            if(s >= 10):
                c = 1
                s %= 10        
            sumli.append(s)
            s = 0
    if(c):
        sumli.append(c)
        c = 0

    ans_sumli = list()

    answer = str()
    while(sumli):
        answer += str(sumli.pop())

    if(int(A) + int(B) == int(answer)): # correct answer
        return 0,answer
#        print('correct')
    else:                               # error
        return -1,answer
#        print('*'*30,'\nERROR\n','*'*30,sep='')

while(True):
    a = input('Input the First Number\n')
    b = input('Input the second Number\n')
    print(big_sum(a,b)[1])


'''
for i in range(10**4):
    a = str(r.randint(sys.maxsize, sys.maxsize**sys.maxsize))
    b = str(r.randint(sys.maxsize, sys.maxsize**sys.maxsize))
    if(big_sum(a, b)[0] == -1): #error
        print(a,b,'Find ERROR', sep='\n')
        break
        
print('END')
'''
