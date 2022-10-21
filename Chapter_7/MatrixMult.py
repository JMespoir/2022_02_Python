# 2740 : Matrix Multiple
import sys
input = sys.stdin.readline

def solve(a,b,n,m,k):
    c = [[0]*k for _ in range(n)]
    for i in range(n):
        for j in range(k):
            c[i][j] = sum(a[i][t]*b[t][j] for t in range(m))

    return c

N,M ,K= map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
B = [list(map(int,input().split())) for _ in range(M)]

C= solve(A,B,N,M,K)

for i in range(len(C)):
    print(" ".join(map(str,C[i])))