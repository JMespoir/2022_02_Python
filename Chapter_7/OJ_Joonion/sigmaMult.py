#정방행렬의 거듭제곱
def solve(N,A,M,T):
    if(T==1):
        return A
    tem = solve(N,A,M,T//2)
    if(T%2 == 0):
        return mult(N,tem,tem,M)
    else:
        return mult(N,A,mult(N,tem,tem,M),M)
    
def mult(N,A,B,M):
    C = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][j] += A[i][k] * B[k][j]
            C[i][j] %= M
    return C


N = int(input())
A = [list(map(int,input().split()))for _ in range(N)]
M, T = map(int,input().split())
B= solve(N,A,M,T)
for i in range(N):
    print(" ".join(map(str,B[i])))