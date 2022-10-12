# 2738: Matrix Plus
def solve(a,b,n,m):
    c= [[0]*m for _ in range (n)]
    for i in range(n):
        for j in range(m):
            c[i][j] = a[i][j] + b[i][j]
    return c



N,M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range (N)]
B = [list(map(int,input().split())) for _ in range (N)]

C = solve(A,B,N,M)
for i in range(N):
    print(" ".join(map(str,C[i])))