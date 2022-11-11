#N번째 소수 출력
def prime(N):
    A = [False,False]+[True]*(N-1)

    primes = []

    for i in range(2,N+1):
        if(A[i]):
            primes.append(i)
            for j in range(i*2,N+1,i):
                A[j] = False

    return primes

primes = prime(1000000)

N = int(input())

print(primes[N-1])