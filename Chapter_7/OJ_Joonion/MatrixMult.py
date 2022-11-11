# 행렬곱셈
def solve(A,B,N,M,K):
    C=[[0]*K for _ in range(N)]
    for i in range(N):
        for j in range(K):
            C[i][j] = sum(A[i][t] * B[t][j] for t in range(M))
    return C

N,M,K = map(int,input().split())
A=[list(map(int,input().split()))for _ in range(N)]
B=[list(map(int,input().split()))for _ in range(M)]

C = solve(A,B,N,M,K)
for i in range(N):
    print(" ".join(map(str,C[i])))