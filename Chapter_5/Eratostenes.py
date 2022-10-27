#2960 : Eratostenes
def solve(N,K):
    cnt = 0
    a = [False,False] + [True]*(N-1)
    for i in range(2,N+1):
        if(a[i]):
            a[i]= False
            cnt+=1
            if(cnt == K):
                return i
            for j in range(i*2, N+1,i):
                if(a[j]):
                    a[j]= False
                    cnt += 1
                    if(cnt == K):
                        return j

N,K = map(int,input().split())

print(solve(N,K))