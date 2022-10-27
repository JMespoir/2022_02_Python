#2581 : Prime Number
import sys
input = sys.stdin.readline

def primeNum():
    N = 10000
    a = [False,False] + [True]*(N-1)

    for i in range(2,N+1):
        if a[i]:
            for j in range(2*i, N+1, i):
                a[j] = False
    return a


primes = primeNum()
M = int(input())
N = int(input())
sum = 0
min = 0
for i in range(N,M-1,-1):
    if(primes[i]):
        sum += i
        min = i
if(sum == 0):
    print(-1)
else:
    print(sum)
    print(min)
