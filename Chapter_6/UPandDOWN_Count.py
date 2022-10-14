#UP & DOWN _Count

def solve(N,M,A):
    high, low = M,N
    cnt = 1
    while(high>=low):
        mid = (high+low)//2
        if(mid == A):
            return cnt
        elif(mid<A):
            low = mid+1
            cnt+= 1
        else:
            high = mid-1
            cnt+=1
    return -1

N,M = map(int,input().split())
A = int(input())
S = list(map(int,input().split()))
cnt = 0
for i in range(len(S)):
    cnt += solve(N,M,S[i])
print(cnt)