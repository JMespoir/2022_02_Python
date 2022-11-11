#소수 순서 찾기
def prime():
    A = [False,False] + [True] * (49999)
    primes = []
    for i in range(50001):
        if(A[i]):
            primes.append(i)
            for j in range(i*2, 50001, i):
                A[j] = False
    return primes
def solve(primes, num):
    high = len(primes)-1
    low = 0
    while(high>=low):
        mid = (high+low)//2
        if(primes[mid] == num):
            return mid+1
        elif(primes[mid]> num):
            high = mid-1
        else:
            low = mid+1
    return -1

primes = prime()
T = int(input())
res = []
for i in range(T):
    res.append(int(input()))

for i in range(T):
    print(solve(primes,res[i]))