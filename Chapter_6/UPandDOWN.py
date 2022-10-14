#UP & DOWN
def solve(N,M,A):
    high, low = M,N
    while(high>=low):
        mid = (high+low)//2
        if(mid == A):
            print(mid ,"END")
            return
        elif(mid<A):
            low = mid+1
            print(mid, "UP")
        else:
            high = mid-1
            print(mid,"DOWN")
    print(-1)

N,M = map(int,input().split())
A = int(input())

solve(N,M,A)