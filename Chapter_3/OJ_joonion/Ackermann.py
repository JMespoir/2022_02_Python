# 아커만 함수
import sys
sys.setrecursionlimit(10**6)

def solve(N,M):
    if(N==0):
        return M+1
    elif(N>0 and M==0):
        return solve(N-1,1)
    elif(N>0 and M>0):
        return solve(N-1,solve(N,M-1))


N,M = map(int,input().split())

print(solve(N,M))