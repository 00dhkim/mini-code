#2019112920 김도현
#소수 구하기, 에라토테네스의 체 사용시 가산점

MAX_VALUE = 100

prime = [i for i in range(2,MAX_VALUE)]

for i in prime:
    n=2
    while(i*n<MAX_VALUE):
        if(prime.count(i*n)):
            prime.remove(i*n)
        n+=1

print(prime)
