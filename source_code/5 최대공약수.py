#2019112920 김도현
#최대공약수 구하는 프로그램, 함수 및 재귀형태 사용시 가산점

def gcd_r(a, b):
    if(b>a): a,b=b,a
    if(not a%b): return b
    else: return gcd_r(b, a%b)
    


n = int(input('input 1st number: '))
m = int(input('input 2nd number: '))
print('gcd is', gcd_r(n, m))
