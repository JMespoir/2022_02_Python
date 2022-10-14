def primeNum():
    N = 5000000
    a = [False,False] + [True]*(N-1)
    primes=[]

    for i in range(2,N+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, N+1, i):
                a[j] = False
    return primes

def solve(N,primes):
    high,low = len(primes), 0
    while(high>=low):
        mid = (high+low)//2
        if(primes[mid] == N):
            return mid+1
        elif(primes[mid]<N):
            low = mid+1
        else:
            high = mid-1
    return -1

T = int(input())
primes = primeNum()
for i in range(T):
    N = int(input())
    print(solve(N,primes))