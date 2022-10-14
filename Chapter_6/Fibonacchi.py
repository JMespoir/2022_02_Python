# Fibonacchi
def solve(t):
    global Fibonacchi
    high , low = 50000, 0
    while(high>=low):
        mid = (high+low)//2
        if(int(Fibonacchi[mid]) == t):
            return mid
        elif(int(Fibonacchi[mid])>t):
            high = mid -1
        else:
            low = mid +1
    return -1

def fibonacchi():
    N = 50000
    F = [0, 1] + [0] *(N-1)
    for i in range(2,N+1):
        F[i] = F[i-1] + F[i-2]
    return F

T = int(input())
Fibonacchi =fibonacchi()
for i in range(T):
    N = int(input())
    print(solve(N))