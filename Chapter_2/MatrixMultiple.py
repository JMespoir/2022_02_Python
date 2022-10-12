# 2740 : Matrix Multiple
def solve(a,b,n,m,k):
    c = [[0]*n for _ in range(k)]
    for i in range(n):
        for j in range(k):
            c[i][j] = sum(a[i][t]*b[t][j] for t in range(m))

    return c
N,M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
M,K = map(int,input().split())
B = [list(map(int,input().split())) for _ in range(M)]

C = solve(A,B,N,M,K)
for i in range(N):
    print(" ".join(map(str,C[i])))